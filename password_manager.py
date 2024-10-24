from cryptography.fernet import Fernet
from flask import Flask, request, render_template
import mysql.connector

# Generate a key (run this only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Krish@2005",  #Update with your MySQL password
        database="password_manager" #update with your MySQL database
    )

# Flask App
app = Flask(__name__)

key = load_key()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new password
@app.route('/add', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':
        print(request.form)  # Debugging statement to check form data

        if 'application' in request.form:
            application = request.form['application']
            username = request.form['username']
            password = request.form['password']

            encrypted_password = encrypt_password(password, key)

            # Store password in MySQL
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("INSERT INTO passwords (application, username, password) VALUES (%s, %s, %s)",
                           (application, username, encrypted_password))
            db.commit()
            cursor.close()
            db.close()

            return render_template('add.html', message="Password stored successfully!")
        else:
            return "Form fields missing!"
    
    return render_template('add.html')

# Route to retrieve a password
@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve_password():
    if request.method == 'POST':
        application = request.form['application']

        # Fetch the encrypted password from MySQL
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT username, password FROM passwords WHERE application = %s", (application,))
        data = cursor.fetchone()
        cursor.close()
        db.close()

        if data:
            username, encrypted_password = data
            decrypted_password = decrypt_password(encrypted_password, key)
            return render_template('retrieve.html', username=username, password=decrypted_password)
        else:
            return render_template('retrieve.html', error="No password found for this application.")

    return render_template('retrieve.html')

if __name__ == '__main__':
    app.run(debug=True)




