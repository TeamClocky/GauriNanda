from flask import Flask, render_template, url_for, request
from flask_mail import Mail, Message
# from config import email_username, email_pw

app = Flask(__name__)

# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": email_username,
#     "MAIL_PASSWORD": email_pw
# }

# app.config.update(mail_settings)
# mail = Mail(app)

# app.config


@app.route('/')
@app.route('/work')
def work():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/work/clocky', methods=['GET', 'POST'])
def clocky():
    return render_template("clocky.html")


@app.route('/work/toymail', methods=['GET', 'POST'])
def toymail():
    return render_template("toymail.html")


@app.route('/press', methods=['GET', 'POST'])
def press():
    return render_template("press.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        msg = Message(subject=f"Website form message from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender="gaurinandacontactform@gmail.com", recipients=["gauri@gaurinanda.com"])
        # mail.send(msg)
        return render_template("contact.html", success=True)
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
