<div align="center"><a name="readme-top"></a>

[![Project Banner](https://github.com/user-attachments/assets/02908422-5bc5-40df-b3ed-6fe9e1e049e5)](#)

# 🌱 Biosecurity Guide for Agricultural Pests and Weeds<br/><h3>Comprehensive Digital Platform for Agricultural Risk Management</h3>

An innovative web-based biosecurity platform that leverages modern Flask technology to provide comprehensive agricultural pest and weed management capabilities.<br/>
Supports role-based access control, detailed species information management, and visual identification tools with image galleries.<br/>
One-click **FREE** deployment of your agricultural biosecurity system.

[Live Application][live-site] · [Screenshots](#-project-screenshots) · [Documentation](#-usage-guide) · [Database Schema](#️-architecture) · [Issues][github-issues-link]

<br/>

[![🚀 Try Live Demo 🚀](https://gradient-svg-generator.vercel.app/api/svg?text=%F0%9F%9A%80Try%20Live%20Demo%F0%9F%9A%80&color=000000&height=60&gradientType=radial&duration=6s&color0=ffffff&template=pride-rainbow)][live-site]

<br/>

<!-- SHIELD GROUP -->

[![][python-shield]][python-link]
[![][flask-shield]][flask-link]
[![][mysql-shield]][mysql-link]
[![][bootstrap-shield]][bootstrap-link]<br/>
[![][live-site-shield]][live-site]
[![][github-license-shield]][github-license-link]
[![][github-stars-shield]][github-stars-link]
[![][github-forks-shield]][github-forks-link]<br/>
[![][github-issues-shield]][github-issues-link]
[![][github-contributors-shield]][github-contributors-link]

**Share Biosecurity Guide Repository**

[![][share-x-shield]][share-x-link]
[![][share-linkedin-shield]][share-linkedin-link]
[![][share-reddit-shield]][share-reddit-link]
[![][share-telegram-shield]][share-telegram-link]

<sup>🌱 Pioneering the future of agricultural biosecurity. Built for the next generation of farmers, agronomists, and agricultural professionals.</sup>

## 📸 Project Screenshots

> [!TIP]
> Explore the intuitive user interface designed for agricultural professionals across different user roles.

<div align="center">
  <img src="https://github.com/user-attachments/assets/9f8960f2-e101-4faa-8e4f-041dd64923da" alt="Home Dashboard" width="800"/>
  <p><em>Home Dashboard - Welcome interface with easy navigation</em></p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/3a6b6675-4b95-41e2-b893-b2c865da6563" alt="Authentication System" width="400"/>
  <img src="https://github.com/user-attachments/assets/729a65b7-b711-424c-b4d2-2ae153eeed3a" alt="Admin Dashboard" width="400"/>
  <p><em>User Authentication and Administrator Dashboard</em></p>
</div>

<details>
<summary><kbd>📱 More Screenshots</kbd></summary>

<div align="center">
  <img src="https://github.com/user-attachments/assets/720678e8-4bbc-4247-9cfb-582dc2345b3e" alt="Staff Management" width="600"/>
  <p><em>Staff Management Interface</em></p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/e35aa016-1a49-4fe0-8e43-e7090a19f636" alt="Guide Management" width="600"/>
  <p><em>Agricultural Guide Content Management</em></p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/b6994684-3a55-4772-ba0c-bf3fc51bbca3" alt="Agronomist View" width="600"/>
  <p><em>Agronomist's Guide Viewing Interface</em></p>
</div>

</details>

## 🎬 Demo Video

> [!NOTE]
> Experience the comprehensive biosecurity management system in action through our demo.

<div align="center">

[![Demo Video](https://github.com/user-attachments/assets/02908422-5bc5-40df-b3ed-6fe9e1e049e5)](https://1160210.pythonanywhere.com/)

*Click the image above to access the live application*

</div>

**Tech Stack Badges:**

<div align="center">

 <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
 <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
 <img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white"/>
 <img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/>
 <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
 <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>

</div>

</div>

> [!IMPORTANT]
> This project demonstrates modern agricultural technology integration with web development best practices. It combines Flask backend with MySQL database to provide comprehensive biosecurity management. Features include role-based access control, visual species identification, and comprehensive agricultural data management.

<details>
<summary><kbd>📑 Table of Contents</kbd></summary>

#### TOC

- [🌱 Biosecurity Guide for Agricultural Pests and Weeds](#-biosecurity-guide-for-agricultural-pests-and-weeds)
      - [TOC](#toc)
      - [](#)
  - [🌟 Introduction](#-introduction)
  - [✨ Key Features](#-key-features)
    - [`1` Role-Based Access Control](#1-role-based-access-control)
    - [`2` Comprehensive Species Database](#2-comprehensive-species-database)
    - [`*` Additional Features](#-additional-features)
  - [🛠️ Tech Stack](#️-tech-stack)
  - [🏗️ Architecture](#️-architecture)
    - [System Architecture](#system-architecture)
    - [Database Schema](#database-schema)
    - [User Role Structure](#user-role-structure)
  - [⚡️ Performance](#️-performance)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Quick Installation](#quick-installation)
    - [Environment Setup](#environment-setup)
    - [Development Mode](#development-mode)
  - [🛳 Deployment](#-deployment)
    - [`A` PythonAnywhere Deployment](#a-pythonanywhere-deployment)
    - [`B` Local Deployment](#b-local-deployment)
    - [`C` Environment Variables](#c-environment-variables)
  - [📖 Usage Guide](#-usage-guide)
    - [Basic Usage](#basic-usage)
    - [User Roles](#user-roles)
    - [Testing Accounts](#testing-accounts)
  - [🔌 Integrations](#-integrations)
  - [📦 Database Schema](#-database-schema)
  - [⌨️ Development](#️-development)
    - [Local Development](#local-development)
    - [Adding Features](#adding-features)
    - [Testing](#testing)
  - [🤝 Contributing](#-contributing)
    - [Development Process](#development-process)
    - [Contribution Guidelines](#contribution-guidelines)
  - [📄 License](#-license)
  - [👥 Team](#-team)

####

<br/>

</details>

## 🌟 Introduction

We are passionate developers creating next-generation agricultural biosecurity solutions. By adopting modern web development practices and comprehensive database design, we aim to provide agricultural professionals with powerful, scalable, and user-friendly biosecurity management tools.

Whether you're an agronomist seeking species identification resources, staff managing agricultural content, or administrators overseeing system operations, this platform will be your comprehensive biosecurity playground. Please note that this project is under active development, and we welcome feedback for any [issues][github-issues-link] encountered.

> [!NOTE]
> - Python 3.8+ required
> - MySQL database required for data storage
> - Web browser with JavaScript enabled
> - Internet connection for image resources

| [![][demo-shield-badge]][live-site]   | No installation required! Visit our live demo to experience it firsthand.                           |
| :------------------------------------ | :--------------------------------------------------------------------------------------------- |

> [!TIP]
> **⭐ Star us** to receive all release notifications from GitHub without delay!

[![][image-star]][github-stars-link]

<details>
  <summary><kbd>⭐ Star History</kbd></summary>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ChanMeng666%2Fbiosecurity&theme=dark&type=Date">
    <img width="100%" src="https://api.star-history.com/svg?repos=ChanMeng666%2Fbiosecurity&type=Date">
  </picture>
</details>

## ✨ Key Features

### `1` Role-Based Access Control

Experience comprehensive user management with distinct role-based interfaces. Our innovative approach provides specialized access levels for different agricultural professionals through advanced authentication and authorization systems.

<div align="center">
  <img src="https://github.com/user-attachments/assets/3a6b6675-4b95-41e2-b893-b2c865da6563" alt="Authentication System" width="600"/>
  <p><em>Secure role-based authentication system</em></p>
</div>

Key capabilities include:
- 👥 **Multi-Role Support**: Administrators, Staff, and Agronomists
- 🔒 **Secure Authentication**: Password hashing with Werkzeug
- 📋 **Profile Management**: Individual user profile customization
- 🛡️ **Session Security**: Secure session management

[![][back-to-top]](#readme-top)

### `2` Comprehensive Species Database

Revolutionary agricultural species management that transforms how users access pest and weed information. With our comprehensive database and intuitive design, users can efficiently identify and manage agricultural threats while maintaining detailed records.

<div align="center">
  <img src="https://github.com/user-attachments/assets/e35aa016-1a49-4fe0-8e43-e7090a19f636" alt="Species Management" width="300"/>
  <img src="https://github.com/user-attachments/assets/b6994684-3a55-4772-ba0c-bf3fc51bbca3" alt="Species Viewing" width="300"/>
  <p><em>Species Management (left) and Viewing Interface (right)</em></p>
</div>

**Database Features:**
- **Pest Management**: Comprehensive pest identification and control information
- **Weed Database**: Detailed weed species with biological characteristics
- **Image Galleries**: Multiple images per species for accurate identification
- **Scientific Data**: Biology, impacts, and control methods for each species

[![][back-to-top]](#readme-top)

### `*` Additional Features

Beyond the core features, this biosecurity platform includes:

- [x] 🌐 **Multi-User System**: Support for multiple concurrent users with role separation
- [x] 🔍 **Advanced Search**: Search and filter capabilities across all species data
- [x] 📊 **Data Management**: CRUD operations for agricultural species information
- [x] 🖼️ **Image Management**: Multiple image support with primary image designation
- [x] 📱 **Responsive Design**: Mobile-friendly interface with Bootstrap CSS
- [x] 🔐 **Secure Password**: Complex password requirements and secure storage
- [x] 📋 **Content Management**: Easy-to-use forms for species data entry
- [x] 🏠 **Dashboard Interface**: Role-specific home pages and navigation

> ✨ More features are continuously being added as agricultural needs evolve.

<div align="right">

[![][back-to-top]](#readme-top)

</div>

## 🛠️ Tech Stack

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/flask" width="48" height="48" alt="Flask" />
        <br>Flask 3.0.2
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/python" width="48" height="48" alt="Python" />
        <br>Python 3.8+
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/mysql" width="48" height="48" alt="MySQL" />
        <br>MySQL 8.0
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/bootstrap" width="48" height="48" alt="Bootstrap" />
        <br>Bootstrap 5
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/html5" width="48" height="48" alt="HTML5" />
        <br>HTML5
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/javascript" width="48" height="48" alt="JavaScript" />
        <br>JavaScript
      </td>
    </tr>
  </table>
</div>

**Backend Stack:**
- **Framework**: Flask 3.0.2 with Blueprint architecture
- **Language**: Python 3.8+ for robust server-side logic
- **Database**: MySQL with mysql-connector-python driver
- **Authentication**: Werkzeug for password hashing and security
- **Forms**: WTForms for form validation and processing

**Frontend Stack:**
- **Styling**: Bootstrap 5 for responsive design
- **Templates**: Jinja2 templating engine
- **JavaScript**: Vanilla JS for interactive features
- **UI Components**: Custom agricultural-focused design system

**Development & Operations:**
- **Deployment**: PythonAnywhere cloud hosting
- **Database Tools**: MySQL Workbench compatible schema
- **Version Control**: Git with structured branching
- **Documentation**: Comprehensive README and code comments

> [!TIP]
> Each technology was carefully selected for agricultural application needs, ease of deployment, and long-term maintainability in educational and professional environments.

## 🏗️ Architecture

### System Architecture

> [!TIP]
> This architecture supports multi-user agricultural environments and role-based data access patterns, making it suitable for educational institutions and agricultural organizations.

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[Flask Templates] --> B[Bootstrap UI]
        B --> C[JavaScript Interactions]
        C --> D[Form Handling]
    end
    
    subgraph "Application Layer"
        E[Flask Blueprints] --> F[Route Handlers]
        F --> G[Authentication Logic]
        G --> H[Business Logic]
    end
    
    subgraph "Data Layer"
        I[MySQL Database]
        J[User Management]
        K[Species Database]
        L[Image Storage]
    end
    
    D --> E
    H --> I
    I --> J
    I --> K
    I --> L
    
    subgraph "Security"
        M[Session Management]
        N[Password Hashing]
        O[Role-based Access]
    end
    
    G --> M
    G --> N
    G --> O
```

### Database Schema

The database follows a normalized structure optimized for agricultural data management:

```mermaid
erDiagram
    users ||--o{ agronomists : "has profile"
    users ||--o{ staff_and_administrators : "has profile"
    agriculture_items ||--o{ images : "has images"
    
    users {
        int user_id PK
        varchar username
        varchar password_hash
        enum role_name
        enum status
    }
    
    agriculture_items {
        int agriculture_id PK
        enum item_type
        varchar common_name
        varchar scientific_name
        text key_characteristics
        text biology
        text impacts
        text control
    }
    
    images {
        int image_id PK
        int agriculture_id FK
        varchar image_path
        boolean is_primary
    }
    
    agronomists {
        int agronomist_id PK
        int user_id FK
        varchar first_name
        varchar last_name
        varchar email
        varchar phone_number
        varchar address
        date date_joined
    }
    
    staff_and_administrators {
        int staff_id PK
        int user_id FK
        varchar first_name
        varchar last_name
        varchar email
        varchar work_phone_number
        date hire_date
        varchar position
        varchar department
    }
```

### User Role Structure

The system implements a three-tier role-based access control:

- **Administrators**: Full system access, user management, complete CRUD operations
- **Staff**: Content management, species data entry, user viewing capabilities  
- **Agronomists**: Read-only access to species database, identification tools

## ⚡️ Performance

### Key Metrics

**Application Performance:**
- ⚡ **Fast Load Times**: Optimized database queries with proper indexing
- 🚀 **Responsive UI**: Bootstrap-based responsive design for all devices
- 💾 **Efficient Queries**: Prepared statements preventing SQL injection
- 📊 **Pagination Support**: Efficient data loading with configurable page sizes

**Database Optimization:**
- 🔄 **Connection Pooling**: Efficient database connection management
- 📋 **Indexed Searches**: Optimized search across species characteristics
- 🖼️ **Image Management**: External image hosting for optimal performance
- 🔍 **Query Optimization**: Efficient JOIN operations for related data

> [!NOTE]
> Performance metrics are continuously monitored and optimized for agricultural workflow requirements.

## 🚀 Getting Started

### Prerequisites

> [!IMPORTANT]
> Ensure you have the following installed:

- Python 3.8+ ([Download](https://python.org/))
- MySQL Server 8.0+ ([Download](https://mysql.com/))
- pip package manager
- Git ([Download](https://git-scm.com/))

### Quick Installation

**1. Clone Repository**

```bash
git clone https://github.com/ChanMeng666/biosecurity.git
cd biosecurity
```

**2. Install Dependencies**

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

**3. Database Setup**

```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE biosecurity;

# Import database structure
mysql -u root -p biosecurity < app/database/biosecurity(structure_only).sql

# Optional: Import sample data
mysql -u root -p biosecurity < app/database/biosecurity(structure_and_data).sql
```

**4. Configuration**

```python
# Edit config.py
class Config(object):
    SECRET_KEY = 'your-secret-key-here'
    DATABASE_URI = 'mysql://username:password@localhost/biosecurity'
```

**5. Start Application**

```bash
python app.py
```

🎉 **Success!** Open [http://localhost:5000](http://localhost:5000) to view the application.

### Environment Setup

Configure your local environment:

```bash
# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=biosecurity

# Application Configuration
SECRET_KEY=your-secret-key
DEBUG=True
```

> [!TIP]
> Use a strong secret key for production deployments. Generate one using Python's secrets module.

### Development Mode

```bash
# Start with debug mode
python app.py

# Check database connection
python -c "from app.database import check_db_connection; check_db_connection()"
```

## 🛳 Deployment

> [!IMPORTANT]
> Choose the deployment strategy that best fits your agricultural organization's needs.

### `A` PythonAnywhere Deployment

**Live Application**: [1160210.pythonanywhere.com][live-site]

**Steps for PythonAnywhere:**

1. Upload your code to PythonAnywhere
2. Configure MySQL database in the Databases tab
3. Set up the WSGI configuration file
4. Configure environment variables
5. Reload the web application

### `B` Local Deployment

```bash
# Production configuration
export FLASK_ENV=production
export SECRET_KEY=your-production-secret

# Start with production settings
python app.py
```

### `C` Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Flask secret key | ✅ | `your-secret-key` |
| `DATABASE_URI` | MySQL connection string | ✅ | `mysql://user:pass@localhost/biosecurity` |
| `DEBUG` | Debug mode | 🔶 | `False` |

> [!WARNING]
> Never commit database credentials to version control. Use environment variables or secure configuration files in production.

## 📖 Usage Guide

### Basic Usage

**Getting Started:**

1. **Access Application** via the live demo or local installation
2. **Login/Register** with appropriate role credentials
3. **Navigate Dashboard** based on your user role
4. **Explore Features** through role-specific interfaces

### User Roles

**Administrator Functions:**
- User management (create, edit, delete users)
- Complete species database management
- System configuration and oversight
- Access to all application features

**Staff Functions:**
- Species database content management
- Image uploads and management
- View agronomist profiles
- Content creation and editing

**Agronomist Functions:**
- Browse species database
- View detailed species information
- Access image galleries for identification
- Read-only access to comprehensive guides

### Testing Accounts

#### PythonAnywhere Environment
| Role       | Username | Password    |
| ---------- | -------- | ----------- |
| Admin      | hello777 | 1234qweASD@ |
| Admin      | admin0   | 123qweASD@  |
| Staff      | staff1   | 123qweASD@  |
| Agronomist | agro1    | 123qweASD@  |

#### Local Environment
| Role       | Username | Password   |
| ---------- | -------- | ---------- |
| Agronomist | agro1    | 123qweASD@ |
| Staff      | staff1   | 123qweASD@ |
| Admin      | admin1   | 123qweASD@ |

> [!NOTE]
> These are demonstration accounts. Change passwords for production use.

## 🔌 Integrations

Current and planned integrations for enhanced agricultural functionality:

| Feature | Status | Description |
|---------|--------|-------------|
| **External Image APIs** | ✅ Active | Support for external agricultural image databases |
| **Email Notifications** | 🔶 Planned | User registration and system notifications |
| **Export Functions** | 🔶 Planned | PDF and Excel export of species data |
| **Mobile App** | 🔶 Future | Native mobile application for field use |
| **API Endpoints** | 🔶 Future | RESTful API for third-party integrations |

## 📦 Database Schema

The biosecurity database contains comprehensive agricultural data:

- **80+ Species Records**: Detailed pest and weed information
- **400+ Images**: Visual identification resources
- **Multi-User Support**: Role-based data access
- **Relationship Management**: Normalized database structure

**Key Tables:**
- `agriculture_items`: Core species data (pests and weeds)
- `images`: Associated identification images  
- `users`: Authentication and authorization
- `agronomists`: Agricultural professional profiles
- `staff_and_administrators`: Staff member information

## ⌨️ Development

### Local Development

**Setup Development Environment:**

```bash
# Clone and setup
git clone https://github.com/ChanMeng666/biosecurity.git
cd biosecurity

# Virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Database setup
mysql -u root -p < app/database/biosecurity(structure_and_data).sql

# Start development server
python app.py
```

### Adding Features

**Development Workflow:**

1. Create feature branch
2. Implement functionality in appropriate blueprint
3. Add templates and styling
4. Test with different user roles
5. Update documentation
6. Submit pull request

**Project Structure:**
```
app/
├── routes/           # Flask blueprints for different features
├── templates/        # Jinja2 templates organized by role
├── static/          # CSS, JavaScript, and assets
├── database/        # Database schemas and connection
└── utils.py         # Utility functions
```

### Testing

**Manual Testing:**
- Test all user roles and permissions
- Verify database operations
- Check responsive design
- Validate form submissions

**Database Testing:**
```bash
# Test database connection
python -c "from app.database.db_connection import get_db_connection; conn = get_db_connection(); print('Connected!' if conn else 'Failed')"
```

## 🤝 Contributing

We welcome contributions to improve agricultural biosecurity management! Here's how you can help:

### Development Process

**1. Fork & Clone:**
```bash
git clone https://github.com/your-username/biosecurity.git
cd biosecurity
```

**2. Create Branch:**
```bash
git checkout -b feature/your-feature-name
```

**3. Make Changes:**
- Follow Python PEP 8 style guidelines
- Add comprehensive comments
- Test across different user roles
- Update documentation as needed

**4. Submit PR:**
- Provide clear description
- Include screenshots for UI changes
- Reference related issues
- Ensure all features work correctly

### Contribution Guidelines

**Code Style:**
- Use Python 3.8+ features appropriately
- Follow Flask best practices
- Write clear, agricultural-domain-specific comments
- Ensure cross-role compatibility

**Agricultural Focus:**
- Consider real-world agricultural workflows
- Maintain scientific accuracy in species data
- Ensure accessibility for field use
- Support various agricultural environments

[![][pr-welcome-shield]][pr-welcome-link]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Open Source Benefits:**
- ✅ Educational use encouraged
- ✅ Commercial use allowed
- ✅ Modification and distribution permitted
- ✅ Agricultural research applications supported

## 👥 Team

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/ChanMeng666">
          <img src="https://github.com/ChanMeng666.png?size=100" width="100px;" alt="Chan Meng"/>
          <br />
          <sub><b>Chan Meng</b></sub>
        </a>
        <br />
        <small>Creator & Lead Developer</small>
      </td>
    </tr>
  </table>
</div>

## 🙋‍♀️ Author

**Chan Meng**
- <img src="https://cdn.simpleicons.org/linkedin/0A66C2" width="16" height="16"> LinkedIn: [chanmeng666](https://www.linkedin.com/in/chanmeng666/)
- <img src="https://cdn.simpleicons.org/github/181717" width="16" height="16"> GitHub: [ChanMeng666](https://github.com/ChanMeng666)
- <img src="https://cdn.simpleicons.org/gmail/EA4335" width="16" height="16"> Email: [chanmeng.dev@gmail.com](mailto:chanmeng.dev@gmail.com)
- <img src="https://cdn.simpleicons.org/internetexplorer/0078D4" width="16" height="16"> Website: [chanmeng.live](https://2d-portfolio-eta.vercel.app/)

---

<div align="center">
<strong>🌱 Building the Future of Agricultural Biosecurity 🚀</strong>
<br/>
<em>Empowering agricultural professionals with modern digital tools</em>
<br/><br/>

⭐ **Star us on GitHub** • 📖 **Read the Documentation** • 🐛 **Report Issues** • 💡 **Request Features** • 🤝 **Contribute**

<br/><br/>

**Made with ❤️ for the agricultural community**

<img src="https://img.shields.io/github/stars/ChanMeng666/biosecurity?style=social" alt="GitHub stars">
<img src="https://img.shields.io/github/forks/ChanMeng666/biosecurity?style=social" alt="GitHub forks">
<img src="https://img.shields.io/github/watchers/ChanMeng666/biosecurity?style=social" alt="GitHub watchers">

</div>

---

<!-- LINK DEFINITIONS -->

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square

<!-- Project Links -->
[live-site]: https://1160210.pythonanywhere.com
[github-issues-link]: https://github.com/ChanMeng666/biosecurity/issues
[github-stars-link]: https://github.com/ChanMeng666/biosecurity/stargazers
[github-forks-link]: https://github.com/ChanMeng666/biosecurity/forks
[github-contributors-link]: https://github.com/ChanMeng666/biosecurity/contributors
[github-license-link]: https://github.com/ChanMeng666/biosecurity/blob/main/LICENSE
[pr-welcome-link]: https://github.com/ChanMeng666/biosecurity/pulls

<!-- Technology Links -->
[python-link]: https://python.org
[flask-link]: https://flask.palletsprojects.com
[mysql-link]: https://mysql.com
[bootstrap-link]: https://getbootstrap.com

<!-- Shield Badges -->
[python-shield]: https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white
[flask-shield]: https://img.shields.io/badge/flask-3.0.2-black.svg?style=flat-square&logo=flask&logoColor=white
[mysql-shield]: https://img.shields.io/badge/mysql-8.0-blue.svg?style=flat-square&logo=mysql&logoColor=white
[bootstrap-shield]: https://img.shields.io/badge/bootstrap-5.0-purple.svg?style=flat-square&logo=bootstrap&logoColor=white
[live-site-shield]: https://img.shields.io/badge/live%20demo-online-green?style=flat-square&logo=pythonanywhere&logoColor=white
[github-license-shield]: https://img.shields.io/badge/license-MIT-white?labelColor=black&style=flat-square
[github-stars-shield]: https://img.shields.io/github/stars/ChanMeng666/biosecurity?color=ffcb47&labelColor=black&style=flat-square
[github-forks-shield]: https://img.shields.io/github/forks/ChanMeng666/biosecurity?color=8ae8ff&labelColor=black&style=flat-square
[github-issues-shield]: https://img.shields.io/github/issues/ChanMeng666/biosecurity?color=ff80eb&labelColor=black&style=flat-square
[github-contributors-shield]: https://img.shields.io/github/contributors/ChanMeng666/biosecurity?color=c4f042&labelColor=black&style=flat-square
[pr-welcome-shield]: https://img.shields.io/badge/🤝_PRs_welcome-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge

<!-- Badge Variants -->
[demo-shield-badge]: https://img.shields.io/badge/TRY%20DEMO-ONLINE-55b467?labelColor=black&logo=pythonanywhere&style=for-the-badge

<!-- Social Share Links -->
[share-x-link]: https://x.com/intent/tweet?hashtags=agriculture,biosecurity,flask&text=Check%20out%20this%20amazing%20agricultural%20biosecurity%20platform&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-linkedin-link]: https://linkedin.com/sharing/share-offsite/?url=https://github.com/ChanMeng666/biosecurity
[share-reddit-link]: https://www.reddit.com/submit?title=Agricultural%20Biosecurity%20Platform&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-telegram-link]: https://t.me/share/url?text=Check%20out%20this%20biosecurity%20platform&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity

[share-x-shield]: https://img.shields.io/badge/-share%20on%20x-black?labelColor=black&logo=x&logoColor=white&style=flat-square
[share-linkedin-shield]: https://img.shields.io/badge/-share%20on%20linkedin-black?labelColor=black&logo=linkedin&logoColor=white&style=flat-square
[share-reddit-shield]: https://img.shields.io/badge/-share%20on%20reddit-black?labelColor=black&logo=reddit&logoColor=white&style=flat-square
[share-telegram-shield]: https://img.shields.io/badge/-share%20on%20telegram-black?labelColor=black&logo=telegram&logoColor=white&style=flat-square

<!-- Images -->
[image-star]: https://via.placeholder.com/800x200/FFD700/000000?text=Star+Us+on+GitHub