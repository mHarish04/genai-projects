# Smart Resume Analyzer – GenAI Transition Project

This project is a beginner-friendly, end-to-end GenAI-powered app that analyzes resume content using OpenAI's GPT models. It was built to support my transition from traditional web development (Drupal, PHP) into emerging GenAI technologies.

---

## Objective

To build a small but practical GenAI project that:
- Helps analyze resumes using LLMs
- Uses modern tools like Streamlit for the UI
- Gives hands-on experience with OpenAI APIs

---

## Tools & Technologies Used

- Python 3.8+
- Streamlit (for frontend)
- OpenAI (GPT model for backend)
- python-dotenv (to manage API keys securely)
- Virtual environment (to isolate dependencies)

---

## Process Overview

1. **Environment Setup**
   - Installed Python on Windows
   - Created a virtual environment using `venv`
   - Activated the environment

2. **Project Folder Structure**
   - Created a new folder for the project
   - Added required files: `app.py`, `.env`, `requirements.txt`

3. **API Integration**
   - Signed up on OpenAI and generated an API key
   - Created a `.env` file to store the API key securely
   - Installed the latest OpenAI Python SDK (v1.x)
   - Updated API usage to match the new version

4. **Building the App**
   - Created a Streamlit web interface
   - Added a text area to paste resume content
   - Connected the UI to OpenAI backend using chat completions
   - Handled basic errors (e.g., empty input, invalid API key, quota issues)

5. **Running the App**
   - Installed dependencies via `requirements.txt`
   - Launched the app using `streamlit run app.py`
   - Interacted with the browser-based interface at `http://localhost:8501`

6. **Troubleshooting Done**
   - Fixed Python not found error by adjusting system PATH
   - Resolved OpenAI version mismatch by migrating to the new SDK
   - Handled rate limit/quota error by considering alternatives like AWS Bedrock

---

## Outcome

- A working web app that accepts resume text and provides GPT-powered suggestions
- Gained hands-on experience with LLMs, API integration, and basic frontend using Streamlit
- Built confidence to experiment with GenAI projects beyond tutorials

---

## Learning Goals Achieved

✅ Setup a GenAI development environment  
✅ Built and ran a full GenAI project  
✅ Gained practical experience with OpenAI APIs  
✅ Broke the inertia of starting something in GenAI  

---

## Target Audience

This project is ideal for:
- Mid to senior developers transitioning into AI
- Non-AI folks exploring LLM integration
- Anyone looking for a real-world mini project in GenAI

---

## Author

Harish M
