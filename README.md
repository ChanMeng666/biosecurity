# Biosecurity Guide for Agricultural Pests and Weeds

## Overview
This project develops a Flask-based web application serving as a biosecurity guide. It details agricultural pests and weeds prevalent in New Zealand, offering targeted information for different user roles, including Agronomists, Staff, and Administrators.

### Project Features:
- **Responsive Web Design**: Tailored to fit an agricultural theme.
- **Role-Based Access**: Distinct dashboards and functionalities for different user roles.
- **Data-Driven**: Utilises a robust database schema to store and manage biosecurity information.

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- MySQL
- Bootstrap CSS
- JavaScript

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ChanMeng666/biosecurity.git
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
- Configure the database using MySQL scripts provided in the `database` folder.
- Set up your environment variables as outlined in the `env.sample` file.

## Usage

Launch the application by running:
```bash
python app.py
```

Navigate to `localhost:5000` in your browser to access the web application.

## Features

### User Roles
- Agronomists: Can view and manage their profile and access detailed pest and weed information.
- Staff: Have the capabilities to edit and update biosecurity guide details and manage Agronomist profiles.
- Administrators: Full system access, including user management and content moderation.

### Database Design
- Role Differentiation: Roles defined with specific permissions.
- User Management: Users are linked to roles, enhancing security and functional access.
- Data Integrity & Normalization: Ensures accurate and efficient data handling.
- Scalability: Designed to accommodate future expansions seamlessly.

### Data Insertion
- Utilises Navicat for efficient data handling and updates.
- Data sourced responsibly from [AgPest](https://agpest.co.nz/pest-directory/.

## Deployment
Hosted on PythonAnywhere, accessible at [1160210.pythonanywhere.com](https://1160210.pythonanywhere.com/).

### Testing Accounts

| Role       | Username | Password   |
|------------|----------|------------|
| **Admin**  | admin0   | 123qweASD@ |
|            | admin    | 123qweASD@ |
| **Agronomist** | agro0  | 123qweASD@ |
|            | agro1    | 123qweASD@ |
|            | agro2    | 123qweASD@ |
|            | agro3    | 123qweASD@ |
|            | agro4    | 123qweASD@ |
| **Staff**  | staff0   | 123qweASD@ |
|            | staff1   | 123qweASD@ |
|            | staff2   | 123qweASD@ |

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
