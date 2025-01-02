from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/send_notification/", methods=["POST"])
def send_notification():
    # Hardcoded notification data
    patient_email = "patient@example.com"
    subject = "Upcoming Appointment Reminder"
    message = "Dear Patient, this is a reminder for your upcoming appointment."

    # Simulating sending email (no actual sending here)
    return jsonify({
        "status": "Notification sent",
        "to": patient_email,
        "subject": subject,
        "message": message
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8002)
