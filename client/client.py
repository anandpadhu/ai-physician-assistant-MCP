import requests

MCP_SERVER = "http://localhost:8000"

def get_patient(patient_id):
    resp = requests.get(f"{MCP_SERVER}/patient/{patient_id}")
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Error fetching patient: {resp.text}")
        return None

def analyze_medications(meds):
    resp = requests.post(f"{MCP_SERVER}/medication/analyze", json={"medications": meds})
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Error analyzing meds: {resp.text}")
        return None

if __name__ == "__main__":
    patient_id = "patient-123"
    patient = get_patient(patient_id)
    if patient:
        print(f"Patient {patient['name']} ({patient['age']} yrs):")
        print(f"Conditions: {', '.join(patient['conditions'])}")
        print(f"Medications: {', '.join(patient['medications'])}")

        print("\nAnalyzing current medications for interactions...")
        result = analyze_medications(patient['medications'])
        if result:
            if result['interactions']:
                print("Interactions found:")
                for i in result['interactions']:
                    print(f"- {i}")
            else:
                print("No interactions found.")
