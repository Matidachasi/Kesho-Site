# Kesho-Site
My ICT171 Azure server project
# ICT171 Cloud Server Project – Kesho&Co Website

This project demonstrates the deployment of a static website and Python-based visitor logging script on an Azure virtual machine (VM) running Ubuntu 20.04 and Nginx.

## 🌐 Live Website

Accessible at: [www.keshoco.site](http://www.keshoco.site)

## 📁 Files Included

- `index.html`: Homepage for the Kesho&Co organization
- `log_visit.py`: Python script that logs each visitor to `visit_log.txt`
- `visit_log.txt`: Stores timestamped logs of visitor access
- `README.md`: Project overview and usage info

## ⚙️ Server Setup Summary

- **Platform:** Microsoft Azure (Ubuntu 20.04 LTS VM)
- **Web Server:** Nginx
- **File Transfer:** FileZilla (SFTP)
- **Logging:** Python script run via manual or CGI trigger
- **Domain Setup:** DNS A record points domain to Azure VM IP

## 🚀 How It Works

1. User visits the homepage
2. Python script is triggered (via meta-refresh or test run)
3. Visitor's timestamp is logged in `visit_log.txt`

## 👤 Author

Matida Chasi  
Student ID: 0712237295  
ICT171 – Introduction to Web Programming
