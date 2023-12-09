from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

PORT = 5000


@app.route("/", methods=["POST", "GET"])
def home():
    MAX_PWD_LENGTH = 500

    pwd = ""
    letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation

    if request.method == "POST":
        special_characters = request.form.get("specialCharacters")
        letter = request.form.get("letters")
        digits = request.form.get("numbers")
        length = int(request.form.get("length"))

        if special_characters == "y":
            pwd += special_chars
        elif special_characters != "n" or "y":
            return render_template("invalid-option.html")

        if letter == "y":
            pwd += letters
        elif letter != "n" or "y":
            return render_template("invalid-option.html")

        if digits == "y":
            pwd += numbers
        elif digits != "n" or "y":
            return render_template("invalid-option.html")

        times = range(length)

        if length > MAX_PWD_LENGTH:
            return render_template("over-length-page.html", maxLength=MAX_PWD_LENGTH)

        generated_password = ""
        for i in times:
            finished_password = random.choice(pwd)
            generated_password += finished_password

        return render_template("finished-password.html", password=generated_password)

    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True, port=PORT)
