# PLC Monitoring Application

## Overview
This application is built using **PyWebview, Flask, HTML, CSS, and JavaScript** to read and display PLC registers. It allows users to configure PLC settings, manage registers, and visualize real-time data.

---

## Features

### 1. **Main Window**
- **PLC Drop-down Menu**: Users can select a PLC from the list and click on the **"Show"** button.
- **Show Button**: Opens a new window displaying **reading registers** and **maximum PLC values**.

### 2. **Settings Panel**
- Accessible via the **Settings Button** on the left side of the main window.
- Users can:
  - Select a **PLC** from the drop-down menu.
  - Configure **IP address, Port Number, and Sample Frequency**.
  - Save settings, which will be displayed below.

### 3. **Register Management**
- The **Register Button** allows users to define the **number of registers** they want to display.

---

## Technologies Used
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Desktop Integration**: PyWebview

---

## Installation & Setup

### 1. **Clone the Repository**
   ```
   git clone <repository-url>

   cd <project-folder>

   pip install -r requirements.txt

   python app.py```
