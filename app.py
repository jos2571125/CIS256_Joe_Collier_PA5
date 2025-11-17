from flask import Flask, request, render_template_string
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Form template
form_html = '''
<form method="POST" action="/login">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username">
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
    <input type="submit" value="Login">
</form>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}

    {% if result %}
        <h3>Login Successful!</h3>
        <p><strong>Username:</strong> {{ result.username }}</p>
        <p><strong>Password:</strong> {{ result.password }}</p>
        <p><strong>Hashed Password:</strong> {{ result.password_hash }}</p>
    {% endif %}
'''

# Route to display the login form
@app.route('/login', methods=['GET'])
def login_form():
    return render_template_string(form_html)

# Route to handle the submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check username for only letters, numbers, and underscores
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for char in username:
        if char not in allowed_chars:
            error = "Only letters, numbers, and underscores are allowed."
            return render_template_string(form_html, error=error)
        
    # Check for password length (8 characters)
    if len(password) < 8:
        error = "Password must be at least 8 characters long."
        return render_template_string(form_html, error=error)
    
    # Variables for letter and number checks
    has_letter = False
    has_number = False

    # Loop to check each character for letters and numbers
    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True
    
    # Check and error handling when no letters or number is found
    if not has_letter or not has_number:
        error = "Password must contain both letters and numbers."
        return render_template_string(form_html, error=error)

    # Hash inputed password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Provide result of username, password, and password hash
    result = {
        "username": username,
        "password": password,
        "password_hash": hashed_password
    }

    return render_template_string(form_html, result=result)

if __name__ == '__main__':
    app.run(debug=True)
