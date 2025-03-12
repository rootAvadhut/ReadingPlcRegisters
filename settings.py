import os
import pandas as pd
import re
from flask import jsonify
from flask import Blueprint, render_template, request

# Define the configuration directory
CONFIG_DIR = "config"
PLC_DATA_FILE = os.path.join(CONFIG_DIR, "plc_data.xlsx")

# Ensure the config directory exists
os.makedirs(CONFIG_DIR, exist_ok=True)

# Create a Blueprint
settings_bp = Blueprint("settings", __name__)


def initialize_plc_data():
    """Create or load PLC data file."""
    if not os.path.exists(PLC_DATA_FILE):
        df = pd.DataFrame({
            'PLC': [f"PLC{i}" for i in range(1, 21)],
            'IP Address': [''] * 20,
            'Port': [0] * 20,
            'Sampling Frequency': [100] * 20,
            'Change in Data': [1] * 20
        })
        df.to_excel(PLC_DATA_FILE, index=False)
        print("PLC data file created successfully.")
    else:
        print("PLC data file already exists.")


def validate_ip(ip):
    """Validate IP address format."""
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(ip_pattern, ip):
        return all(0 <= int(num) <= 255 for num in ip.split('.'))
    return False


def validate_port(port):
    """Validate that the port is an integer and within range 1-65535."""
    return port.isdigit() and 1 <= int(port) <= 65535


def validate_sampling_freq(freq):
    """Ensure it's between 100ms and 180000ms (3 minutes)."""
    return freq.isdigit() and 100 <= int(freq) <= 180000


def validate_change_data(change):
    """Ensure it's between 1% and 100%."""
    return change.isdigit() and 1 <= int(change) <= 100


def update_plc_data(plc, ip_address, port, sampling_freq, change_data):
    """Ensure the PLC exists in the Excel file and update it."""

    try:
        # If the file doesn't exist, create a new one
        if not os.path.exists(PLC_DATA_FILE):
            initialize_plc_data()

        # Load the data
        df = pd.read_excel(PLC_DATA_FILE)

        # Ensure 'PLC' column is string type
        df['PLC'] = df['PLC'].astype(str)

        # If PLC is not found, add a new entry
        if plc not in df['PLC'].values:
            print(f"ℹ️ {plc} not found. Adding it to plc_data.xlsx.")
            new_row = pd.DataFrame({
                'PLC': [plc],
                'IP Address': [ip_address],
                'Port': [int(port)],
                'Sampling Frequency': [int(sampling_freq)],
                'Change in Data': [int(change_data)]
            })
            df = pd.concat([df, new_row], ignore_index=True)
        else:
            # Update existing PLC entry
            df.loc[df['PLC'] == plc, ['IP Address', 'Port', 'Sampling Frequency', 'Change in Data']] = [
                ip_address, int(port), int(sampling_freq), int(change_data)
            ]

        # Save back to Excel
        df.to_excel(PLC_DATA_FILE, index=False)
        print(f"✅ Data for {plc} updated successfully!")
        return True  # Success flag

    except Exception as e:
        print(f"❌ Error saving PLC data: {e}")
        return False  # Failure flag


@settings_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    initialize_plc_data()
    df = pd.read_excel(PLC_DATA_FILE)
    plc_data = df.to_dict(orient='records')

    if request.method == "POST":
        try:
            plc = request.form['plc']
            ip_address = request.form['ip_address']
            port = request.form['port']
            sampling_freq = request.form['sampling_freq']
            change_data = request.form['change_data']

            if not validate_ip(ip_address):
                return jsonify({"error": "Invalid IP Address"}), 400
            if not validate_port(port):
                return jsonify({"error": "Invalid Port Number"}), 400
            if not validate_sampling_freq(sampling_freq):
                return jsonify({"error": "Invalid Sampling Frequency"}), 400
            if not validate_change_data(change_data):
                return jsonify({"error": "Invalid Change in Data"}), 400

            success = update_plc_data(plc, ip_address, port, sampling_freq, change_data)

            if success:
                return jsonify({"message": "PLC data updated successfully!"}), 200
            else:
                return jsonify({"error": "Error saving data"}), 500

        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    return render_template("settings.html", plc_data=plc_data)
