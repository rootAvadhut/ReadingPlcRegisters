import os
import pandas as pd
from flask import Blueprint, render_template, request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Register")

register_bp = Blueprint("register", __name__, template_folder="templates")

PLC_DATA_FILE = "config/plc_data.xlsx"
SAVE_ADDRESS_FILE = "config/saveAddress.xlsx"


def get_plc_list():
    try:
        df = pd.read_excel(PLC_DATA_FILE)
        return df['PLC'].tolist()
    except Exception as e:
        logger.error(f"Error loading PLC data: {e}")
        return []


def validate_numbers(coils, bits, registers):
    try:
        coils = int(coils)
        bits = int(bits)
        registers = int(registers)

        if not (1 <= coils <= 9999 and 1 <= bits <= 9999 and 1 <= registers <= 9999):
            return False, "Numbers must be between 1-9999"

        if coils != bits or bits != registers:
            return False, "All values must be equal"

        return True, ""
    except ValueError:
        return False, "Invalid numbers"


# @register_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         plc = request.form['plc']
#         num_coils = request.form['num_coils']
#         num_bits = request.form['num_bits']
#         num_registers = request.form['num_registers']
#
#         # Validate input
#         valid, msg = validate_numbers(num_coils, num_bits, num_registers)
#         if not valid:
#             return jsonify({"error": msg}), 400
#
#         # Process dynamic entries
#         entries = []
#         try:
#             for i in range(1, int(num_coils) + 1):
#                 entries.append({
#                     'PLC OUTPUT NO': f"OUTPUT{i}",
#                     'MODBUS ADDRESS (Coils)': request.form.get(f'coil_{i}', '').zfill(5),
#                     'States (Coils)': 0,
#                     'INPUT BIT NO': f"INPUT BIT{i}",
#                     'MODBUS ADDRESS (Input Bits)': request.form.get(f'bit_{i}', '').zfill(5),
#                     'States (Input Bits)': 0,
#                     'PLC ANALOG INPUT SLOT': f"ANALOG INPUT{i}",
#                     'MODBUS ADDRESS (Analog Inputs)': request.form.get(f'register_{i}', '').zfill(5),
#                     'Values': 0
#                 })
#
#             # Create DataFrame with explicit column order
#             columns = [
#                 'PLC OUTPUT NO', 'MODBUS ADDRESS (Coils)', 'States (Coils)',
#                 'INPUT BIT NO', 'MODBUS ADDRESS (Input Bits)', 'States (Input Bits)',
#                 'PLC ANALOG INPUT SLOT', 'MODBUS ADDRESS (Analog Inputs)', 'Values'
#             ]
#             df = pd.DataFrame(entries, columns=columns)
#
#             # Save to Excel
#             if os.path.exists(SAVE_ADDRESS_FILE):
#                 with pd.ExcelWriter(SAVE_ADDRESS_FILE, mode='a', if_sheet_exists='replace') as writer:
#                     df.to_excel(writer, sheet_name=plc, index=False)
#             else:
#                 df.to_excel(SAVE_ADDRESS_FILE, sheet_name=plc, index=False)
#
#             return jsonify({"message": "Data saved successfully!"})
#
#         except Exception as e:
#             logger.error(f"Save error: {e}")
#             return jsonify({"error": str(e)}), 500
#
#     # GET request - show form
#     plcs = get_plc_list()
#     return render_template("register.html", plcs=plcs)





# # register.py
# import os
# import pandas as pd
# from flask import Blueprint, render_template, request, jsonify, redirect, url_for
# import logging
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("Register")
#
# register_bp = Blueprint("register", __name__, template_folder="templates")
#
# PLC_DATA_FILE = "config/plc_data.xlsx"
# SAVE_ADDRESS_FILE = "config/saveAddress.xlsx"
#
#
# def get_plc_list():
#     try:
#         df = pd.read_excel(PLC_DATA_FILE)
#         return df['PLC'].tolist()
#     except Exception as e:
#         logger.error(f"Error loading PLC data: {e}")
#         return []
#
#
# def validate_numbers(coils, bits, registers):
#     try:
#         coils = int(coils)
#         bits = int(bits)
#         registers = int(registers)
#
#         if not (1 <= coils <= 9999 and 1 <= bits <= 9999 and 1 <= registers <= 9999):
#             return False, "Numbers must be between 1-9999"
#
#         if coils != bits or bits != registers:
#             return False, "All values must be equal"
#
#         return True, ""
#     except ValueError:
#         return False, "Invalid numbers"
#
#
# @register_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         plc = request.form['plc']
#         num_coils = request.form['num_coils']
#         num_bits = request.form['num_bits']
#         num_registers = request.form['num_registers']
#
#         # Validate input
#         valid, msg = validate_numbers(num_coils, num_bits, num_registers)
#         if not valid:
#             return jsonify({"error": msg}), 400
#
#         # Process dynamic entries
#         entries = []
#         # for i in range(1, int(num_coils) + 1):
#         #     entries.append({
#         #         'coil': request.form.get(f'coil_{i}', ''),
#         #         'bit': request.form.get(f'bit_{i}', ''),
#         #         'register': request.form.get(f'register_{i}', '')
#         #     })
#     try:
#         for i in range(1, int(num_coils) + 1):
#             entries.append({
#                 'PLC OUTPUT NO': f"OUTPUT{i}",
#                 'MODBUS ADDRESS (Coils)': request.form.get(f'coil_{i}', '').zfill(5),
#                 'States (Coils)': 0,
#                 'INPUT BIT NO': f"INPUT BIT{i}",
#                 'MODBUS ADDRESS (Input Bits)': request.form.get(f'bit_{i}', '').zfill(5),
#                 'States (Input Bits)': 0,
#                 'PLC ANALOG INPUT SLOT': f"ANALOG INPUT{i}",
#                 'MODBUS ADDRESS (Analog Inputs)': request.form.get(f'register_{i}', '').zfill(5),
#                 'Values': 0
#             })
#             # Create DataFrame with explicit column order
#             columns = [
#                 'PLC OUTPUT NO', 'MODBUS ADDRESS (Coils)', 'States (Coils)',
#                 'INPUT BIT NO', 'MODBUS ADDRESS (Input Bits)', 'States (Input Bits)',
#                 'PLC ANALOG INPUT SLOT', 'MODBUS ADDRESS (Analog Inputs)', 'Values'
#             ]
#
#             df = pd.DataFrame(entries, columns=columns)
#
#             # # Save to Excel (similar to original save_data logic)
#             #
#             #     df = pd.DataFrame([{
#             #         'PLC OUTPUT NO': f"OUTPUT{i + 1}",
#             #         'MODBUS ADDRESS (Coils)': entry['coil'],
#             #         'INPUT BIT NO': f"INPUT BIT{i + 1}",
#             #         'MODBUS ADDRESS (Input Bits)': entry['bit'],
#             #         'PLC ANALOG INPUT SLOT': f"ANALOG INPUT{i + 1}",
#             #         'MODBUS ADDRESS (Analog Inputs)': entry['register']
#             #     } for i, entry in enumerate(entries)])
#
#     if os.path.exists(SAVE_ADDRESS_FILE):
#         with pd.ExcelWriter(SAVE_ADDRESS_FILE, mode='a', if_sheet_exists='replace') as writer:
#             df.to_excel(writer, sheet_name=plc, index=False)
#     else:
#         df.to_excel(SAVE_ADDRESS_FILE, sheet_name=plc, index=False)
#
#         return jsonify({"message": "Data saved successfully!"})
#
#     except Exception as e:
#     logger.error(f"Save error: {e}")
#     return jsonify({"error": str(e)}), 500
#
#
# # GET request - show form
# plcs = get_plc_list()
# return render_template("register.html", plcs=plcs)
@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        plc = request.form['plc']
        num_coils = request.form['num_coils']
        num_bits = request.form['num_bits']
        num_registers = request.form['num_registers']

        # Validate input
        valid, msg = validate_numbers(num_coils, num_bits, num_registers)
        if not valid:
            return jsonify({"error": msg}), 400

        # Process dynamic entries with holding registers
        entries = []
        for i in range(1, int(num_coils) + 1):
            entries.append({
                'PLC OUTPUT NO': f"OUTPUT{i}",
                'MODBUS ADDRESS (Coils)': request.form.get(f'coil_{i}', '').zfill(5),
                'States (Coils)': 0,
                'INPUT BIT NO': f"INPUT BIT{i}",
                'MODBUS ADDRESS (Input Bits)': request.form.get(f'bit_{i}', '').zfill(5),
                'States (Input Bits)': 0,
                'PLC ANALOG INPUT SLOT': f"ANALOG INPUT{i}",
                'MODBUS ADDRESS (Analog Inputs)': request.form.get(f'register_{i}', '').zfill(5),
                'Values': 0,
                'HOLDING REGISTER NO': f"HOLDING REGISTER{i}",
                'MODBUS ADDRESS (Holding Registers)': request.form.get(f'holding_{i}', '').zfill(5),
                'Holding Values': 0
            })

        # Create DataFrame with explicit column order
        columns = [
            'PLC OUTPUT NO', 'MODBUS ADDRESS (Coils)', 'States (Coils)',
            'INPUT BIT NO', 'MODBUS ADDRESS (Input Bits)', 'States (Input Bits)',
            'PLC ANALOG INPUT SLOT', 'MODBUS ADDRESS (Analog Inputs)', 'Values',
            'HOLDING REGISTER NO', 'MODBUS ADDRESS (Holding Registers)', 'Holding Values'
        ]

        try:
            df = pd.DataFrame(entries, columns=columns)

            # Save to Excel
            if os.path.exists(SAVE_ADDRESS_FILE):
                with pd.ExcelWriter(SAVE_ADDRESS_FILE, mode='a', engine='openpyxl',
                                    if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name=plc, index=False)
            else:
                df.to_excel(SAVE_ADDRESS_FILE, sheet_name=plc, index=False)

            return jsonify({"message": "Data saved successfully!"})

        except PermissionError:
            return jsonify({"error": "Please close the Excel file before saving"}), 500
        except Exception as e:
            logger.error(f"Save error: {e}")
            return jsonify({"error": str(e)}), 500

    # GET request - show form
    plcs = get_plc_list()
    return render_template("register.html", plcs=plcs)
