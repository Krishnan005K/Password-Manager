from cryptography.fernet import Fernet

# Function to generate and save the key
def generate_key():
    key = Fernet.generate_key()  # Generate the key
    with open("secret.key", "wb") as key_file:
        key_file.write(key)  # Save the key to a file

# Call the function to generate the key
generate_key()
