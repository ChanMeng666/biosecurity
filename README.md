# Biosecurity Guide for Agricultural Pests and Weeds 🌱

<div align="center">
<a href="https://github.com/ChanMeng666/biosecurity"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://1160210.pythonanywhere.com"><img src="https://img.shields.io/badge/pythonanywhere-1160210.pythonanywhere.com-green.svg?style=for-the-badge"/></a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/>
</div>

<br/>

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ChanMeng666/biosecurity)

[![👉Try It Now!👈](https://gradient-svg-generator.vercel.app/api/svg?text=%F0%9F%91%89Try%20It%20Now!%F0%9F%91%88&color=000000&height=60&gradientType=radial&duration=6s&color0=ffffff&template=pride-rainbow)](https://1160210.pythonanywhere.com/)

<br/>

https://github.com/user-attachments/assets/02908422-5bc5-40df-b3ed-6fe9e1e049e5


![screencapture-1160210-pythonanywhere-2024-12-08-13_07_57](https://github.com/user-attachments/assets/9f8960f2-e101-4faa-8e4f-041dd64923da)

![screencapture-1160210-pythonanywhere-auth-login-2024-12-08-13_08_37](https://github.com/user-attachments/assets/3a6b6675-4b95-41e2-b893-b2c865da6563)

![screencapture-1160210-pythonanywhere-admin-home-2024-12-08-13_08_57](https://github.com/user-attachments/assets/729a65b7-b711-424c-b4d2-2ae153eeed3a)

![screencapture-1160210-pythonanywhere-admin-admin-manage-staff-2024-12-08-13_09_12](https://github.com/user-attachments/assets/720678e8-4bbc-4247-9cfb-582dc2345b3e)

![屏幕截图 2024-12-08 131000](https://github.com/user-attachments/assets/9cb56746-a8aa-4ee4-8fe9-521e6ff2bb6d)

![screencapture-1160210-pythonanywhere-admin-admin-manage-guide-add-2024-12-08-13_10_20](https://github.com/user-attachments/assets/e35aa016-1a49-4fe0-8e43-e7090a19f636)

![screencapture-1160210-pythonanywhere-agronomist-agronomist-view-guide-2024-12-08-13_10_49](https://github.com/user-attachments/assets/b6994684-3a55-4772-ba0c-bf3fc51bbca3)

## Overview
A Flask-based web application that serves as a comprehensive biosecurity guide for agricultural pests and weeds. This platform provides targeted information and management capabilities for different user roles including Agronomists, Staff, and Administrators.

### Project Features:
- **User Role Management**: Distinct interfaces and capabilities for Agronomists, Staff, and Administrators
- **Comprehensive Guide**: Detailed information about agricultural pests and weeds
- **Responsive Design**: Mobile-friendly interface with Bootstrap CSS
- **Image Management**: Support for pest and weed image uploads and management
- **Secure Authentication**: Role-based access control and secure password handling

## Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server
- Modern web browser

### Dependencies
```
Flask==3.0.2
mysql-connector-python==8.3.0
Werkzeug==3.0.1
WTForms==3.1.2
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ChanMeng666/biosecurity.git
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure MySQL database:
   ```python
   # config.py
   class Config(object):
       SECRET_KEY = '123456'
       DATABASE_URI = 'mysql://root:123456@localhost/biosecurity'
   ```

## Features

### User Roles
- **Agronomists**: View and access detailed pest and weed information
- **Staff**: Manage guide content and agronomist profiles
- **Administrators**: Full system access including user management

### Database Design
- Role differentiation with specific permissions
- User management with role associations
- Efficient data handling and storage
- Support for image management

## Deployment
The application is deployed on PythonAnywhere and can be accessed at [1160210.pythonanywhere.com](https://1160210.pythonanywhere.com)

### Testing Accounts

#### Local Environment
| Role       | Username | Password   |
| ---------- | -------- | ---------- |
| Agronomist | agro1    | 123qweASD@ |
| Staff      | staff1   | 123qweASD@ |
| Admin      | admin1   | 123qweASD@ |

#### PythonAnywhere Environment
| Role       | Username | Password    |
| ---------- | -------- | ----------- |
| Admin      | hello777 | 1234qweASD@ |
| Admin      | admin0   | 123qweASD@  |
| Staff      | staff1   | 123qweASD@  |
| Agronomist | agro1    | 123qweASD@  |

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
PythonAnywhere: [1160210.pythonanywhere.com](https://1160210.pythonanywhere.com)

## 🙋‍♀ Author

Created and maintained by [Chan Meng](https://github.com/ChanMeng666).
