This FastAPI code defines a simple backend for patient data retrieval and medication interaction analysis. Let's break down what it's doing step by step:
Uses FastAPI to create a web API.
Uses Pydantic's BaseModel to define data schemas.
Uses json and os to load data from a local file.
Loads patient records from a JSON file (./data/patients.json) at startup.
If the file doesn't exist, it raises an error and won't start the server.
**Endpoint 1**: GET /patient/{patient_id}  **Purpose**: Retrieve patient data by their ID. **Returns** the patient's record if found, or a 404 error if not
**Endpoint 2:** POST /medication/analyze.Accepts a list of medications and checks for: Duplicate entries Known harmful drug interactions


**Summary**
**Feature	Purpose**
**/patient/{id}	**Retrieve patient record from JSON file
**/medication/analyze**	Detect duplicate meds and known dangerous interactions
**patients.json**	Simulates patient database
**conflicts dict	**Hardcoded clinical rules for drug interactions
