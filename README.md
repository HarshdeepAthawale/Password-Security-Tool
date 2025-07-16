# Password Security Tool

A web-based educational tool to help you understand password security, test password strength, and simulate password cracking techniques in a safe environment.

## Features

- **Password Strength Tester**
  - Instantly checks password strength based on length, character variety, common patterns, and more.
  - Provides suggestions for improving password security.
  - Color-coded strength meter and detailed feedback.

- **Ethical Password Cracker**
  - Hashes your input password using SHA-256.
  - Simulates password cracking using:
    - A built-in or custom dictionary attack (upload your own .txt file).
    - A limited brute-force attack (up to 4 characters, a-z, 0-9).
  - Shows progress, live attempts, and timing information.

- **Educational Focus**
  - Includes a clear disclaimer: for educational purposes only.
  - Demonstrates why strong, unique passwords are important.

## Local Setup & Usage

### 1. Prerequisites
- **Python 3.8+** must be installed. [Download Python here](https://www.python.org/downloads/).

### 2. Clone or Download the Repository
If you have Git:
```bash
git clone <repository-url>
cd "Password Security  Tool"
```
Or download and extract the ZIP, then open a terminal in the project folder.

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

### 5. Open in Your Browser
- The app will open automatically, or visit [http://localhost:8501](http://localhost:8501)

### Troubleshooting
- If you get a `pip` or `python` not found error, ensure Python is added to your PATH.
- If Streamlit does not launch, try `python -m streamlit run app.py`.
- For permission errors, try running your terminal as administrator.

## How It Works

- **Password Strength Tester**: Enter a password (and optionally a username). The tool analyzes your password for length, character types, repeated characters, keyboard patterns, common substitutions, and inclusion of your username. It provides a strength rating and suggestions.

- **Ethical Password Cracker**: Enter a password to see its SHA-256 hash. Try to "crack" the hash using a dictionary or brute-force attack. You can upload your own dictionary file for testing. The tool shows progress, attempts, and how long the attack takes.

## Disclaimer

> **This tool is for educational purposes only.** Do not use it for unauthorized password cracking or malicious activities.

## License

MIT License 