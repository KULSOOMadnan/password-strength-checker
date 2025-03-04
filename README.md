# 🔐 Password Strength Meter

## 📌 Overview
This is a **Password Strength Meter** built using **Python** and **Streamlit**. The application allows users to check the strength of their password based on several security criteria and suggests improvements for weak passwords. Additionally, it provides a **password generator** to create strong passwords.

## 🚀 Features
### ✅ Password Strength Checker
- **Analyzes passwords** based on length, character types, and patterns.
- **Assigns a strength score** (Weak, Moderate, Strong) using a **custom scoring system**.
- **Displays feedback** to improve weak passwords.
- **Uses a progress bar** to visually indicate password strength.
- **Rejects common weak passwords** (e.g., "password123", "12345678").

### 🔑 Password Generator
- Generates **random strong passwords** containing uppercase, lowercase, digits, and special characters.
- Displays the generated password in an input field for easy copying.

### 🎨 User Interface
- Built with **Streamlit** for an interactive experience.
- Uses **Streamlit progress bar** to show password strength visually.
- Buttons for **checking password strength** and **generating strong passwords**.

## ⚙️ Installation & Usage
### 1️⃣ Install Dependencies
This project uses **uv** as a package manager. To install dependencies, run:
```sh
uv pip install -r requirements.txt
```
Or if using pip directly:
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Application
Start the Streamlit app by running:
```sh
streamlit run app.py
```

## 📜 Password Strength Criteria
| Criteria                         | Score Weight |
|----------------------------------|-------------|
| Minimum 8 characters            | 2           |
| Upper & Lowercase letters       | 1.5         |
| At least one number (0-9)       | 1.5         |
| At least one special character  | 2           |

## 📌 Technologies Used
- **Python** 🐍
- **Streamlit** 🎨
- **Regular Expressions (re)** 🔍
- **Random & String Modules** 🔢

## 💡 Future Enhancements
- Improve UI with **better styling**.
- Allow users to **customize password length** when generating passwords.
- Store password strength history.

---
Developed by **Kulsoom** 🚀
