<div align="center">

# 🎓 EduMentor AI
### Adaptive Study Planner Based on Learning Patterns

*~ Calibrate your focus. Quantify your grit.*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)

</div>

---

## 📌 Overview

**EduMentor AI** is a Machine Learning + Web Development project that helps students improve their academic performance by analyzing their learning behavior and automatically generating personalized study plans.

Traditional study methods apply a one-size-fits-all approach — EduMentor AI breaks that mold. By capturing behavioral and academic metrics, the system predicts performance levels, flags weak subjects, and synthesizes dynamic weekly timetables tailored to each student's unique profile.

---

## 👥 Builders

| Name | Email | LinkedIn |
|------|-------|----------|
| **Prakhar Upadhyay** | prakhar.24bsa10143@vitbhopal.ac.in | [Connect](https://www.linkedin.com/in/prakhar-upadhyay-997bb434b/) |
| **Utsav Kaushal** | utsav.24bcy10321@vitbhopal.ac.in | [Connect](https://www.linkedin.com/in/utsav-kaushal-b5608b369/) |

---

## 🚨 The Problem

Students across the world suffer from the same systemic failures in academic planning:

- 📉 **Poor Time Management** — no smart allocation based on task complexity or energy levels
- 🧠 **Cognitive Decay** — studying without tracking retention curves leads to rapid forgetting
- ⏱️ **Unmonitored Attention Spans** — long continuous sessions exceed focus limits, causing burnout
- 🔁 **Repetitive Error Loops** — unchecked mistake patterns crystallize into knowledge gaps
- ❓ **Vague Subject Awareness** — no clear mathematical distinction between strong and weak areas

---

## ✅ The EduMentor AI Solution

EduMentor AI replaces guesswork with **data-driven, adaptive study planning**. By building an end-to-end ML ecosystem integrated with a web frontend, the system:

- 🔮 **Predicts Performance Levels** — High / Medium / Low, based on behavioral and academic data
- 🎯 **Isolates Weak Subjects** — automatically flags areas needing immediate intervention
- 📊 **Quantifies Daily Habits** — converts sleep, mood, and active hours into a productivity index
- 📅 **Generates Dynamic Schedules** — personalized weekly planners and hourly timetables
- 🏆 **Gamifies Academic Discipline** — streaks and badges for consistent engagement

---

## 🏗️ System Architecture

```
Student
   │
   ▼
Frontend Form          ← Inputs behavioral data & academic metrics via HTML Form
   │
   ▼
Flask Backend          ← Receives multi-part payloads & initializes request handler
   │
   ▼
Feature Extraction     ← Normalizes inputs into numeric feature vectors
   │
   ▼
ML Model               ← Loads trained model.pkl & encoder.pkl dynamically
   │
   ▼
Prediction             ← Outputs categorical tier: High / Medium / Low
   │
   ▼
AI Analysis Engine     ← Calculates productivity index, flags weak subjects, structures planner
   │
   ▼
Dashboard              ← Renders personalized metrics, timetables & gamified badges
```

---

## 🗂️ Folder Structure

```
EduMentorAI/
│
├── app.py
├── train_model.py
├── dataset.csv
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

---

## 🛠️ Technology Stack

### Frontend
| Technology | Purpose |
|-----------|---------|
| HTML5 & CSS3 | Structural layouts and clean, minimalist UI |
| Bootstrap | Fluid dashboard rendering across devices |
| Jinja2 Templates | Server-side rendering of dynamic variables and badge icons |

### Backend
| Technology | Purpose |
|-----------|---------|
| Python | Core scripting, logic execution, numerical operations |
| Flask | API routing, form payload handling, inference serving |

### Machine Learning & Data
| Technology | Purpose |
|-----------|---------|
| Scikit-Learn | Data pipelines, train/test splitting, Random Forest Classifier |
| Pandas | Structured data matrix alignment and feature selection |
| NumPy | High-performance vectorized operations on feature arrays |

---

## 🤖 Machine Learning Model

EduMentor AI uses a **Random Forest Classifier** with **300 decision trees** — chosen for its resilience to noise from self-reported data and its strong generalization ability.

### How it works

Each of the 300 trees evaluates a randomized subset of student features and casts a classification vote. The final prediction is determined by **majority consensus**:

```
Input Feature Array
├──> Tree 001  →  High
├──> Tree 002  →  High
├──> Tree 003  →  Medium
      ...
└──> Tree 300  →  High

Majority Vote  →  ✅ Final Output: High
```

### Dataset Features (11 inputs → 1 target)

| Feature | Type | Description |
|---------|------|-------------|
| `Study_Time` | Float | Daily study hours |
| `Attention_Span` | Integer | Focus duration before distraction (minutes) |
| `Revision_Count` | Integer | Weekly structured content reviews |
| `Mistakes` | Integer | Incorrect responses in self-assessments |
| `Sleep_Hours` | Float | Average daily sleep (hours) |
| `Attendance` | Float | Class/platform engagement (%) |
| `Math_Score` | Integer | Math score (0–100) |
| `Physics_Score` | Integer | Physics score (0–100) |
| `Chemistry_Score` | Integer | Chemistry score (0–100) |
| `English_Score` | Integer | English score (0–100) |
| `CS_Score` | Integer | Computer Science score (0–100) |
| **`Performance_Level`** | Categorical | **Target**: High / Medium / Low |

### Performance Clusters

| Cluster | Profile | Example |
|---------|---------|---------|
| 🟢 High Performance | High study time, long focus, frequent revision, low errors | Study=7h, Attention=60min, Revisions=5, Mistakes=2 → **High** |
| 🔴 High Friction | Low focus, high errors, poor attendance, sleep deficit | Study=2h, Attention=15min, Revisions=1, Mistakes=14 → **Low** |

### Data Split

```
Total Dataset: 1,000 synthetic student profiles
├── Training Set (80%): 800 records
└── Testing Set  (20%): 200 records   [random_state=42]
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/EduMentorAI.git
cd EduMentorAI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python train_model.py

# 4. Run the app
python app.py
```

Then open your browser at `http://localhost:5000`

## 📈 How to Use

1. Open the app and fill in the **study form** with your academic and behavioral data
2. Submit the form — the ML model instantly predicts your **performance tier**
3. View your personalized **dashboard** with:
   - Performance prediction (High / Medium / Low)
   - Weak subject flags
   - Productivity index
   - Custom weekly study timetable
   - Achievement badges and streaks

---

## 🏆 Gamification

EduMentor AI keeps students engaged through behavioral reinforcement:

- 🔥 **Streaks** — consecutive days of following the plan
- 🥇 **Badges** — earned for hitting performance milestones
- 📊 **Progress Tracking** — visual metrics to celebrate growth

---

## 🔮 Future Scope

- [ ] Real student data integration (with consent)
- [ ] Deep learning upgrade for higher prediction accuracy
- [ ] Mobile app (React Native / Flutter)
- [ ] Multi-subject timetable optimization engine
- [ ] Parent/teacher dashboard view
- [ ] Integration with LMS platforms (Google Classroom, Moodle)

---

## 📄 License

This project is built for academic and educational purposes.

---

<div align="center">

**Built with 💡 by Prakhar Upadhyay & Utsav Kaushal**  
*VIT Bhopal University*

⭐ Star this repo if EduMentor AI helped you study smarter!

</div>
