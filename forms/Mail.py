from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'havish7728@gmail.com'
app.config['MAIL_PASSWORD'] = 'opxo gqsb kbeu gqse'
app.config['MAIL_DEFAULT_SENDER'] = ('Havish', 'havish7728@gmail.com')

mail = Mail(app)

@app.route('/contact', methods=['POST'])
def contact():
    try:
        # Extract form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message_body = request.form['message']

        # Create email message
        msg = Message(subject=subject, recipients=['havish7728@gmail.com'])
        msg.body = f"From: {name} <{email}>\n\n{message_body}"

        # Send email
        mail.send(msg)

        return jsonify({'status': 'success', 'message': 'Email sent successfully!'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)