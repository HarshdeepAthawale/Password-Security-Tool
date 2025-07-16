# Password Security Tool

A web-based educational tool to help you understand password security, test password strength, and learn about good password practices.

## Features

- **Password Strength Tester**
  - Instantly checks password strength based on length, character variety, common patterns, and more.
  - Provides suggestions for improving password security.
  - Color-coded strength meter and detailed feedback.
  - **Displays the SHA-256 hash of your entered password** so you can see how your password is represented as a secure, irreversible cryptographic hash.

- **Educational Focus**
  - Includes a clear disclaimer: for educational purposes only.
  - Demonstrates why strong, unique passwords are important.

## Project Structure

- `app.py` — Main application code (Streamlit app).
- `requirements.txt` — Python dependencies needed to run the app.
- `README.md` — Project documentation and usage instructions.
- `.git/` — Git version control directory (hidden, used for tracking changes).

## How to Run Locally

### 1. Prerequisites
- **Python 3.8+** must be installed. [Download Python here](https://www.python.org/downloads/)
- **pip** (Python’s package installer) should be available.

### 2. Get the Project
- If you have Git:
  ```sh
  git clone <repository-url>
  cd "Password Security  Tool"
  ```
- Or download and extract the ZIP, then open a terminal in the project folder.

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the App
```sh
streamlit run app.py
```
If you get an error that `streamlit` is not recognized, try:
```sh
python -m streamlit run app.py
```

### 5. Open in Your Browser
- The app should open automatically.
- If not, open your browser and go to: [http://localhost:8501](http://localhost:8501)

### Troubleshooting
- If you get a `pip` or `python` not found error, ensure Python is added to your PATH.
- For permission errors, try running your terminal as administrator.
- If you see errors during installation or running, copy the error message and seek help.

## How It Works

- **Password Strength Tester**: Enter a password (and optionally a username). The tool analyzes your password for length, character types, repeated characters, keyboard patterns, common substitutions, and inclusion of your username. It provides a strength rating, suggestions, and **shows the SHA-256 hash** of your password.  
_SHA-256 is a cryptographic hash function commonly used to securely store passwords. This feature helps you understand how your password is transformed into a hash, which is what websites typically store instead of your actual password._

## Disclaimer

> **This tool is for educational purposes only.** Do not use it for unauthorized password cracking or malicious activities.

## License

MIT License 