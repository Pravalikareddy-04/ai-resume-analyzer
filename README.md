# AI Resume Analyzer & Job Recommendation System
## Project Description
AI Resume Analyzer & Job Recommendation System is a Python-based application that analyzes a resume and recommends suitable job roles.
The system extracts text from the resume, cleans the text, identifies skills and compares the resume with predefined job roles. It also shows matched and missing skills and generates a personalized learning roadmap based on the missing skills.
## Features
- Resume upload
- PDF, DOCX and TXT support
- Resume text extraction
- Text preprocessing
- Skill extraction using a skill dictionary
- TF-IDF based text similarity
- Cosine similarity
- Skill-based job matching
- Job role recommendation
- Match percentage calculation
- Matched and missing skill identification
- Personalized learning roadmap
- Downloadable analysis report
## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- PyPDF
- Python-docx
- CSV
## Matching Method
The system uses both skill matching and TF-IDF similarity to recommend job roles.
The final match score is calculated using:
Final Score = (Skill Matching × 70%) + (TF-IDF Similarity × 30%)
The recommended job roles are displayed in descending order of their match percentage.
## Project Structure
ai_resume_analyzer/
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── sample_resumes/
├── reports/
└── tests/
    └── test_cases.csv
## How to Run
Create and activate a virtual environment:
python -m venv venv
Activate the virtual environment:
venv\Scripts\activate
Install the required packages:
pip install -r requirements.txt
Run the application:
streamlit run app.py
The application will open in the browser.
## Workflow
1. Upload a resume.
2. Extract text from the resume.
3. Clean the extracted text.
4. Detect skills using the skill dictionary.
5. Compare the detected skills with available job roles.
6. Calculate the job match percentage.
7. Display recommended job roles.
8. Show matched and missing skills.
9. Generate a personalized learning roadmap.
10. Download the analysis report.
## Dataset
The project uses two CSV files:
### job_roles.csv
Contains:
- Job Role
- Required Skills
- Job Description
### skill_dictionary.csv
Contains the list of skills used by the system for resume skill extraction.
## Future Enhancements
- Add more job roles and skills
- Improve NLP-based skill extraction
- Support scanned resumes using OCR
- Add experience and education analysis
- Consider additional job requirements such as location and experience
- Add learning resources for missing skills
- Deploy the application online
- Add a database for storing analysis history

## Demo Video

[Watch the Demo Video](https://drive.google.com/file/d/1t6-EjiFy5gFB3SsP_xIqRHsQKDI4uoHB/view?usp=sharing)