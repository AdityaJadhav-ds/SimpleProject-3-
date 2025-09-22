# Password Strength Checker

## 📌 Project Overview
This is a simple **Python program** that simulates a basic login system with password strength validation.  
The program ensures that the user creates a **strong password** by enforcing these rules:
- Minimum **8 characters** long
- Contains at least **one uppercase letter**
- Contains at least **one lowercase letter**
- Contains at least **one digit**

If the entered password does not meet the requirements, the program provides specific feedback and prompts the user to try again.

---

## 🚀 Features
- User-friendly login system.
- Validates password strength based on common security rules.
- Gives clear feedback on why a password is weak.
- Runs continuously until a strong password is entered.

---

## 🛠️ How It Works
1. The program asks the user to **enter a username**.
2. Then it prompts for a **password**.
3. It checks the password against strength criteria:
   - ✅ At least 8 characters
   - ✅ Contains uppercase, lowercase, and a digit
4. If valid → Prints `"strong password"`.
5. If invalid → Shows hints (e.g., "add at least one digit").
6. Repeats until a strong password is provided.

---

```bash
python password_checker.py
