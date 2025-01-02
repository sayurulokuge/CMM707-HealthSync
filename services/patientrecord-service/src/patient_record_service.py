from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded patient data
patients = [
    {
        "patient_id": 1,
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "medical_history": ["Hypertension", "Asthma"],
        "prescriptions": ["Amlodipine", "Ventolin"]
    },
    {
        "patient_id": 2,
        "name": "Jane Smith",
        "age": 25,
        "gender": "Female",
        "medical_history": ["Diabetes"],
        "prescriptions": ["Metformin"]
    }
]

@app.route("/patients/", methods=["GET"])
def get_patients():
    return jsonify(patients)

@app.route("/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id: int):
    patient = next((p for p in patients if p["patient_id"] == patient_id), None)
    if patient:
        return jsonify(patient)
    return jsonify({"error": "Patient not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
