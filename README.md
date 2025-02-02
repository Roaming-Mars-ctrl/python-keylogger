# python-keylogger

# This is a simple Python Keylogger using Pynput, made for logging keys to a txt file.
⚠️ **WARNING: EDUCATIONAL PURPOSES ONLY** ⚠️  

This project is intended for learning and research on security concepts. It may contain code that could be harmful if misused. Always run in a safe, isolated environment. Use responsibly and ethically. By using this software, you acknowledge the risks involved and take full responsibility for your actions.  

### **Limitations**
- **Unreliable Logging of Special Characters**:  
  The current implementation uses the `key.char` attribute to log keystrokes, which may fail for certain special characters, such as `Shift`, `Ctrl`, or other non-character keys. When this occurs, it throws an exception, which is not properly documented in the log file.

### **Suggested Improvements**
- Handle special characters more gracefully by checking for key types that don’t have a `char` value (e.g., function keys, modifiers like `Shift`, `Ctrl`, etc.).
- Add more detailed logging to capture key events like these, so they are better documented.
- **Background Upload of Logs**:  
  Implement a mechanism to upload the captured log file to a remote server in the background, ensuring continuous data collection without manual intervention.
- **Encryption of Uploaded Logs**:  
  To improve security, consider encrypting the log file before uploading it, protecting sensitive data from unauthorized access.


# Usage
## Setting Up
1.	Clone the repository
```bash
git clone https://github.com/Roaming-Mars-ctrl/Hidden-Keylogger.git
cd python-keylogger
```
2.	Clone the repository
```bash
git clone https://github.com/Roaming-Mars-ctrl/Hidden-Keylogger.git
cd python-keylogger
```
3.	Install the required packages
```bash
pip install -r requirements.txt
```
## Running the Main Script
1.	Start the main script
```bash
py keylogger.py
```
