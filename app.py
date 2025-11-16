from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route to display the login form
@app.route('/login', methods=['GET'])
def login_form():
    form_html = '''
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        #input type="text" id="username" name="username">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        <input type="submit" value="Login">
    </form>
    '''
    return render_template_string(form_html)

# Route to handle the submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['passoword']
    # Handle the login logic here
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)
