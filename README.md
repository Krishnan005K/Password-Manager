# Password Manager

## Overview
This Password Manager is a secure web application built with Flask that allows users to store, retrieve, and manage their passwords efficiently. The application encrypts sensitive password information using the `cryptography` library to ensure data privacy and security. Users can add new passwords and retrieve existing ones for various applications while keeping their credentials safe.

## Features
- **Secure Password Storage**: Utilizes encryption to protect passwords.
- **Add New Passwords**: Easily add credentials for different applications.
- **Retrieve Passwords**: Fetch stored passwords securely using application names.
- **User-Friendly Interface**: Intuitive web interface for seamless navigation.

## Technology Stack
- **Frontend**: HTML, CSS
- **Backend**: Flask
- **Database**: MySQL
- **Encryption**: Cryptography (Fernet)

## Installation

1. **Clone the repository:**
   
       git clone https://github.com/Krishnan005K/Password-Manager.git
   
2. **Navigate to the project directory:**
 
       cd password-manager
   
3. **Install the required packages:**
 
       pip install -r requirements.txt
   
Set up your MySQL database and configure the connection settings in the code.

## Generate a secret key:**

 from your_flask_app import generate_key
 generate_key()

## Run the Flask application:**


   python password_manager.py
   Access the application at http://127.0.0.1:5000/.

## Usage

 Visit the home page to navigate to the add or retrieve password sections.
 
 Follow the prompts to store and access your passwords securely.
 
## Contributing
 Contributions are welcome! Feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
