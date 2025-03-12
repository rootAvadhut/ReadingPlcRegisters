document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("settings-form");
    const plcDropdown = document.getElementById("plc");
    const ipInput = document.getElementById("ip_address");
    const portInput = document.getElementById("port");
    const samplingFreqInput = document.getElementById("sampling_freq");
    const changeDataInput = document.getElementById("change_data");

    // Create validation error messages
    function createErrorMessage(input, message) {
        let errorElement = input.nextElementSibling;
        if (!errorElement || !errorElement.classList.contains("error-message")) {
            errorElement = document.createElement("div");
            errorElement.classList.add("error-message");
            input.parentNode.insertBefore(errorElement, input.nextSibling);
        }
        errorElement.textContent = message;
    }

    // Remove error messages
    function removeErrorMessage(input) {
        const errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains("error-message")) {
            errorElement.remove();
        }
    }

    // Validate IP Address
    function validateIp() {
        const ipPattern = /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/;
        const isValid = ipPattern.test(ipInput.value) && ipInput.value.split('.').every(num => num >= 0 && num <= 255);
        if (!isValid) {
            createErrorMessage(ipInput, "Invalid IP format (e.g., 192.168.1.1)");
        } else {
            removeErrorMessage(ipInput);
        }
        return isValid;
    }

    // Validate Port Number (1-65535)
    function validatePort() {
        const port = parseInt(portInput.value);
        const isValid = !isNaN(port) && port >= 1 && port <= 65535;
        if (!isValid) {
            createErrorMessage(portInput, "Port must be between 1 and 65535");
        } else {
            removeErrorMessage(portInput);
        }
        return isValid;
    }

    // Validate Sampling Frequency (100-180000 ms)
    function validateSamplingFreq() {
        const freq = parseInt(samplingFreqInput.value);
        const isValid = !isNaN(freq) && freq >= 100 && freq <= 180000;
        if (!isValid) {
            createErrorMessage(samplingFreqInput, "Sampling frequency must be between 100ms and 180000ms");
        } else {
            removeErrorMessage(samplingFreqInput);
        }
        return isValid;
    }

    // Validate Change in Data (1-100%)
    function validateChangeData() {
        const change = parseInt(changeDataInput.value);
        const isValid = !isNaN(change) && change >= 1 && change <= 100;
        if (!isValid) {
            createErrorMessage(changeDataInput, "Change in Data must be between 1% and 100%");
        } else {
            removeErrorMessage(changeDataInput);
        }
        return isValid;
    }

    // Validate PLC Selection
    function validatePlcSelection() {
        if (plcDropdown.value === "") {
            createErrorMessage(plcDropdown, "Please select a PLC");
            return false;
        } else {
            removeErrorMessage(plcDropdown);
            return true;
        }
    }

    // Add event listeners for live validation
    plcDropdown.addEventListener("change", validatePlcSelection);
    ipInput.addEventListener("input", validateIp);
    portInput.addEventListener("input", validatePort);
    samplingFreqInput.addEventListener("input", validateSamplingFreq);
    changeDataInput.addEventListener("input", validateChangeData);


    // ✅ Form submission validation (ONLY ONE EVENT LISTENER)
    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        if (
            validatePlcSelection() &&
            validateIp() &&
            validatePort() &&
            validateSamplingFreq() &&
            validateChangeData()
        ) {
            const formData = new FormData(form);
            try {
                const response = await fetch("/settings", {
                    method: "POST",
                    body: formData
                });

                if (response.ok) {
                    alert("✅ Settings saved successfully!");
                    location.reload();
                } else {
                    const errorMessage = await response.text();
                    alert(`❌ Error: ${errorMessage}`);
                }
            } catch (error) {
                alert("❌ Network error. Please try again.");
            }
        } else {
            alert("❌ Please correct the errors before submitting.");
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("settings-form");
    const plcSelect = document.getElementById('plcSelect');

    // Function to check if pywebview API is available
    function isPyWebViewApiReady() {
        return window.pywebview && window.pywebview.api;
    }


    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        try {
            const response = await fetch("/settings", {
                method: "POST",
                body: formData
            });

            if (response.ok) {
                alert("✅ PLC Settings Saved!");

                // ✅ Notify the main window to refresh the PLC dropdown
                localStorage.setItem("refreshPlcList", "true");
                // Call loadPlcList after saving data

            alert("✅ Settings saved successfully!");
                    window.location.reload();
            } else {
                const errorMessage = await response.json();
                alert(`❌ Error: ${errorMessage.error}`);
            }
        } catch (error) {
            alert("❌ Network error. Please try again.");
        }
    });
});



