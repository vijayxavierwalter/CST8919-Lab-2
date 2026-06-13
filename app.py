from flask import Flask, request, render_template_string
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

VALID_USERNAME = "admin"
VALID_PASSWORD = "Password123"

login_page = """
<h2>Login Page</h2>
<form method="POST" action="/login">
    <label>Username:</label><br>
    <input type="text" name="username"><br><br>

    <label>Password:</label><br>
    <input type="password" name="password"><br><br>

    <button type="submit">Login</button>
</form>

<p>{{ message }}</p>
"""

@app.route("/")
def home():
    return "Flask Security Logging App is running."

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
        timestamp = datetime.utcnow().isoformat()

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            logging.info(
                f"LOGIN_SUCCESS username={username} ip={client_ip} time={timestamp}"
            )
            message = "Login successful"
        else:
            logging.warning(
                f"LOGIN_FAILED username={username} ip={client_ip} time={timestamp}"
            )
            message = "Invalid username or password"

    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run()