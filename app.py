import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define your email configuration
SMTP_SERVER = 'your-smtp-server.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@example.com'
SMTP_PASSWORD = 'your-email-password'
EMAIL_RECEIVER = 'your-receiver@example.com'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def handle_contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Compose the email message
        email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"

        try:
            # Connect to the SMTP server and send the email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            msg = MIMEText(email_message)
            msg['Subject'] = subject
            msg['From'] = SMTP_USERNAME
            msg['To'] = EMAIL_RECEIVER

            server.sendmail(SMTP_USERNAME, [EMAIL_RECEIVER], msg.as_string())

            server.quit()

            # Redirect to a "Thank You" page or display a success message
            return render_template('thank_you.html')
        except Exception as e:
            # Handle email sending errors (e.g., SMTP authentication failed)
            print(str(e))
            return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
