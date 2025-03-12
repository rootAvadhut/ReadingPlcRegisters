document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('register-form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const response = await fetch('/register', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message);
            window.location.href = '/settings';
        } else {
            alert(`Error: ${result.error}`);
        }
    });
});

// function generateEntries() {
//     const numCoils = parseInt(document.getElementById('num_coils').value, 10);
//     const numBits = parseInt(document.getElementById('num_bits').value, 10);
//     const numRegisters = parseInt(document.getElementById('num_registers').value, 10);
//     const container = document.getElementById('dynamic-entries');
//
//     container.innerHTML = '';
//
//     // 🛑 **Validation: Ensure values do not exceed 128**
//     if (numCoils > 128 || numBits > 128 || numRegisters > 128) {
//         alert('Maximum allowed entries for Coils, Input Bits, and Registers is 128.');
//         return;
//     }
//
//     // 🛑 **Validation: Ensure all three numbers are the same**
//     if (numCoils !== numBits || numBits !== numRegisters) {
//         alert('All values (Coils, Input Bits, Registers) must be equal!');
//         return;
//     }
//
//     for (let i = 1; i <= numCoils; i++) {
//         const row = document.createElement('div');
//         row.className = 'entry-row';
//
//         row.innerHTML = `
//             <div class="static-field">OUTPUT${i}</div>
//             <div class="entry-field">
//                 <input type="text" name="coil_${i}" placeholder="00001" pattern="0[0-9]{4}" title="Enter a value between 00001 and 09999" required>
//             </div>
//             <div class="static-field">0</div>
//
//             <div class="static-field">INPUT BIT${i}</div>
//             <div class="entry-field">
//                 <input type="text" name="bit_${i}" placeholder="10001" pattern="1[0-9]{4}" title="Enter a value between 10001 and 19999" required>
//             </div>
//             <div class="static-field">0</div>
//
//             <div class="static-field">ANALOG INPUT${i}</div>
//             <div class="entry-field">
//                 <input type="text" name="register_${i}" placeholder="30001" pattern="3[0-9]{4}" title="Enter a value between 30001 and 39999" required>
//             </div>
//             <div class="static-field">0</div>
//         `;
//
//         container.appendChild(row);
//     }
//
//     document.getElementById('save-button').disabled = false;
// }
function generateEntries() {
    const numEntries = document.getElementById('num_coils').value;
    const container = document.getElementById('dynamic-entries');
    container.innerHTML = '';

    // Validation
    const bits = document.getElementById('num_bits').value;
    const registers = document.getElementById('num_registers').value;

    if (numEntries !== bits || bits !== registers) {
        alert('All values must be equal!');
        return;
    }

    for (let i = 1; i <= numEntries; i++) {
        const row = document.createElement('div');
        row.className = 'entry-row';

        row.innerHTML = `
            <div class="static-field">OUTPUT${i}</div>
            <div class="entry-field">
                <input type="text" name="coil_${i}" placeholder="00001" pattern="\\d{5}">
            </div>
            <div class="static-field">0</div>
            
            <div class="static-field">INPUT BIT${i}</div>
            <div class="entry-field">
                <input type="text" name="bit_${i}" placeholder="10001" pattern="\\d{5}">
            </div>
            <div class="static-field">0</div>
            
            <div class="static-field">ANALOG INPUT${i}</div>
            <div class="entry-field">
                <input type="text" name="register_${i}" placeholder="30001" pattern="\\d{5}">
            </div>
            <div class="static-field">0</div>
            
            <div class="static-field">HOLDING REG${i}</div>
            <div class="entry-field">
                <input type="text" name="holding_${i}" placeholder="40001" pattern="\\d{5}">
            </div>
            <div class="static-field">0</div>
        `;

        container.appendChild(row);
    }

    document.getElementById('save-button').disabled = false;
}













// document.addEventListener("DOMContentLoaded", () => {
//     const form = document.getElementById('register-form');
//
//     form.addEventListener('submit', async (e) => {
//         e.preventDefault();
//
//         const formData = new FormData(form);
//         const response = await fetch('/register', {
//             method: 'POST',
//             body: formData
//         });
//
//         const result = await response.json();
//         if (response.ok) {
//             alert(result.message);
//             window.location.href = '/settings';
//         } else {
//             alert(`Error: ${result.error}`);
//         }
//     });
// });
//
// function generateEntries() {
//     const numEntries = document.getElementById('num_coils').value;
//     const container = document.getElementById('dynamic-entries');
//     container.innerHTML = '';
//
//     // Validation
//     const bits = document.getElementById('num_bits').value;
//     const registers = document.getElementById('num_registers').value;
//
//     if (numEntries !== bits || bits !== registers) {
//         alert('All values must be equal!');
//         return;
//     }
//
//     for (let i = 1; i <= numEntries; i++) {
//         const row = document.createElement('div');
//         row.className = 'entry-row';
//
//         row.innerHTML = `
//             <div class="static-field">OUTPUT${i}</div>
//             <div class="entry-field">
//                 <input type="text" name="coil_${i}" placeholder="00001" pattern="\\d{5}">
//             </div>
//             <div class="static-field">0</div>
//
//             <div class="static-field">INPUT BIT${i}</div>
//             <div class="entry-field">
//                 <input type="text" name="bit_${i}" placeholder="10001" pattern="\\d{5}">
//             </div>
//             <div class="static-field">0</div>
//
//             <div class="static-field">ANALOG INPUT${i}</div>
//             <div class="entry-field">
//                 <input type="text" name="register_${i}" placeholder="30001" pattern="\\d{5}">
//             </div>
//             <div class="static-field">0</div>
//         `;
//
//         container.appendChild(row);
//     }
//
//     document.getElementById('save-button').disabled = false;
// }