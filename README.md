# 🔐 Password Strength Analyzer

🚀 **Project built for the Google Tools Hackathon**

Password Strength Analyzer is a **cybersecurity web application** that analyzes password security and helps users create stronger passwords.

The system checks common password security rules and classifies passwords as **Weak, Moderate, or Strong**.

The application also generates strong passwords and stores password analysis data using **Firebase Firestore**, enabling **cloud-based password security analytics**.

---

## 🌐 Live Demo

🔗 https://password-analyzer-4kwd.onrender.com

---

## ✨ Features

- 🔍 Password strength analysis
- 🔑 Secure password generator
- 💡 Security suggestions for weak passwords
- ☁️ Firebase Firestore cloud database storage
- 📊 Password security analytics collection
- 🖥 Cybersecurity-themed interface
- 🧠 Matrix-style animated background
- 📋 Copy generated password feature
- 🆔 Unique EntryID and Timestamp for each password analysis

---

## 🧠 How It Works

1. The user enters a password into the system.
2. The system analyzes the password based on security rules:
   - Minimum length **(8 characters)**
   - Presence of **uppercase letters**
   - Presence of **lowercase letters**
   - Presence of **numbers**
   - Presence of **special characters**
3. Each rule adds **1 point to the security score**.
4. Based on the score, the password strength is classified.

| Score | Strength |
|------|--------|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

5. If the password is weak, suggestions are shown to improve security.
6. The system can generate a **secure random password**.
7. Password analysis results are stored in **Firebase Firestore**.

---

## ☁️ Firebase Data Storage

Each password analysis creates a document inside the **Firestore database**.

Example stored document:

```text
EntryID: PASS_1710058901234
Strength: Moderate
Length: 10
Score: 4
Uppercase: true
Numbers: true
SpecialChar: false
Timestamp: 1710058901234
Device: Chrome
Platform: Windows
```

### Why Firebase?

Firebase Firestore was used because it provides:

- Real-time cloud database
- Easy integration with web applications
- Automatic scalability
- No server management required

This allows the system to demonstrate **security analytics using cloud databases**.

---

## 🎨 User Interface

The interface is designed with a **cybersecurity theme**.

UI components include:

- Glassmorphism card design
- Matrix-style animated background
- Password strength progress bar
- Password improvement suggestions
- Secure password generator
- Copy-to-clipboard functionality

The UI is built using **HTML, CSS, and JavaScript**.

---

## ⚙️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Cloud & Tools
- Firebase Firestore
- Render (Deployment)
- GitHub (Version Control)

---

## 📂 Project Structure

```text
password-analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhavesh979/password-analyzer.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd password-analyzer
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Your Browser

```
http://127.0.0.1:5000
```

---

## 🔥 Firebase Integration

Firebase Firestore stores password analysis data for **security analytics**.

Stored fields include:

- Password strength
- Password length
- Security score
- Uppercase presence
- Number presence
- Special character presence
- Device information
- Platform information
- Timestamp of analysis

This data can be used to analyze **password security trends**.

---

## 🛡️ Cybersecurity Concept

Weak passwords are one of the most common causes of cybersecurity breaches.

Common attack techniques include:

- Brute-force attacks
- Dictionary attacks
- Credential stuffing
- Password spraying

This project helps users understand password security and encourages **strong password practices**.

---

## 🚀 Future Improvements

Possible future enhancements include:

- AI-based password analysis
- Password breach detection
- Password entropy calculation
- Security analytics dashboard
- Multi-factor authentication simulation

---

## 👨‍💻 Author

**Bhavesh Chaudhari**  
Cybersecurity Project — Password Strength Analyzer