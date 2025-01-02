from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded appointment data
appointments = [
    {
        "patient_id": 1,
        "doctor_id": 101,
        "appointment_time": "2024-12-30T10:00:00"
    },
    {
        "patient_id": 2,
        "doctor_id": 102,
        "appointment_time": "2024-12-31T11:00:00"
    }
]

@app.route("/appointments/", methods=["GET"])
def get_all_appointments():
    return jsonify(appointments)

@app.route("/appointments/<int:appointment_id>", methods=["GET"])
def get_appointment(appointment_id: int):
    if appointment_id < len(appointments):
        return jsonify(appointments[appointment_id])
    return jsonify({"error": "Appointment not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
