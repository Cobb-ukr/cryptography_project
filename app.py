from flask import Flask, render_template, request
from converter import encrypt, decrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        password = request.form.get("password", "")
        action = request.form.get("action", "")

        if text and password:
            if action == "encrypt":
                result = encrypt(text, password)
            elif action == "decrypt":
                try:
                    result = decrypt(text, password)
                except Exception:
                    result = "Error: Decryption failed. Check your input and password."

    return render_template("index.html", result=result)
    
if __name__ == "__main__":
    app.run(debug=True)
