# Flask_Application_2-Tier_Deployment
# 🏗️ Deploying a 2-Tier Architecture: Flask + MySQL on Ubuntu

This guide helps you deploy a 2-tier architecture with a **Flask backend** connected to a **MySQL database** on an Ubuntu server.

## 🧰 Prerequisites

- Ubuntu 24.04 server (e.g., AWS EC2)
- SSH access to the server
- `requirements.txt` available in your Flask app directory

---

## 🛠️ Step-by-Step Deployment

### 1️⃣ Install Python and MySQL

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv mysql-server
```

### 2️⃣ Verify Python Installation
```bash
python3 --version
```

### 3️⃣ Secure MySQL and Login
```bash
sudo systemctl start mysql
sudo mysql -u root
```

### 4️⃣ Create Database and User
Once inside the MySQL shell, run:
sql

#### CREATE DATABASE flask_app_db;
```
CREATE USER 'default_user'@'localhost' IDENTIFIED BY 'user@123!';
GRANT ALL PRIVILEGES ON flask_app_db.* TO 'default_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5️⃣ Set Up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 6️⃣ Install Flask App Dependencies
Make sure you're inside your Flask project directory with requirements.txt:
```bash
pip install -r requirements.txt
```

### 7️⃣ Run Your Flask App
```bash
python3 app.py
```
## Application Screenshots

<img width="956" height="500" alt="image" src="https://github.com/user-attachments/assets/fa48af7b-fa44-4d5e-aefb-f6b98dbc07b2" />

