Chatbot Analytics & Optimization
Project Overview:
This project implements a chatbot system with analytics and visualization support for the module Chatbot Analytics & Optimization.
The system consists of a FastAPI backend, a frontend chatbot UI, and an analytics visualization script (figures.py).
Project Structure
Simple-Chatbot-main/
- backend/
  - main.py
  - .env
- frontend/
  - chatbotui/
    - src/
      - figures.py

Prerequisites:
- Python 3.10.x
- Node.js and npm
- pip
Python Dependencies:
pip install fastapi uvicorn pandas numpy matplotlib seaborn wordcloud python-dotenv

Backend Setup and Execution:
Navigate to the backend folder:
cd Simple-Chatbot-main/backend

Run the FastAPI backend:
uvicorn main:app --reload

Once running, open the API documentation:
http://127.0.0.1:8000/docs

Frontend – Running the Chatbot UI
Navigate to the frontend folder:
cd Simple-Chatbot-main/frontend/chatbotui

Install dependencies (one time):
npm install

Run the development server:
npm run dev

After startup, the terminal will show:
Local: http://localhost:5173/
Open this URL in your browser to access the chatbot UI.

Analytics & Visualizations (figures.py)
The analytics script generates 6 assignment-approved figures demonstrating chatbot analytics concepts.

Navigate to the figures folder:
cd Simple-Chatbot-main/frontend/chatbotui/src

Run figures with pop-up windows:
python figures.py

Run figures without pop-ups (optional):
python figures.py --headless
Generated Figures
1. Comprehensive Chatbot Analytics Dashboard
2. Confusion Matrix (Intent Recognition)
3. Intent Distribution
4. Session Heatmap (User Activity Patterns)
5. Fallback vs Non-Fallback Queries
6. Word Cloud (User Messages)

