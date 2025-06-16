from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "./data/patients.json"

# Load patients data at startup
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"Patient data file not found at {DATA_FILE}")

with open(DATA_FILE) as f:
    patients_data = json.load(f)


class MedicationAnalysisRequest(BaseModel):
    medications: list[str]

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    patient = next((p for p in patients_data if p['id'] == patient_id), None)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.post("/medication/analyze")
def analyze_medications(request: MedicationAnalysisRequest):
    meds = request.medications
    interactions = []

    # Basic interaction check: duplicated medications
    if len(set(meds)) < len(meds):
        interactions.append("Warning: Duplicate medications detected")

    # Example: simple drug conflict rules (expand as needed)
    conflicts = {
        ("Lisinopril", "Ibuprofen"): "Risk of kidney damage",
        ("Warfarin", "Aspirin"): "Increased bleeding risk"
    }

    for i in range(len(meds)):
        for j in range(i + 1, len(meds)):
            pair = (meds[i], meds[j])
            rev_pair = (meds[j], meds[i])
            if pair in conflicts:
                interactions.append(f"Interaction between {pair[0]} and {pair[1]}: {conflicts[pair]}")
            elif rev_pair in conflicts:
                interactions.append(f"Interaction between {rev_pair[0]} and {rev_pair[1]}: {conflicts[rev_pair]}")

    return {
        "interactions": interactions,
        "recommendations": "Consult physician if interactions found."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
