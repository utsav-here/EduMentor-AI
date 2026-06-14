from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# ===============================
# LOAD ML MODEL
# ===============================

model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

# ===============================
# DAILY PRODUCTIVITY SCORE
# ===============================

def calculate_daily_score(
    study_hours,
    questions,
    mock_score,
    sleep
):

    score = (
        study_hours * 10
        + questions * 0.5
        + mock_score * 0.4
        + sleep * 3
    )

    return round(score)


# ===============================
# PRODUCTIVITY LEVEL
# ===============================

def productivity_level(score):

    if score >= 120:
        return "Excellent"

    elif score >= 90:
        return "Good"

    elif score >= 60:
        return "Average"

    else:
        return "Needs Improvement"


# ===============================
# BADGE SYSTEM
# ===============================

def get_badge(score):

    if score >= 120:
        return "🏆 Gold Scholar"

    elif score >= 90:
        return "🥈 Silver Scholar"

    elif score >= 60:
        return "🥉 Bronze Scholar"

    else:
        return "📖 Beginner"


# ===============================
# BURNOUT CHECK
# ===============================

def burnout_check(sleep):

    if sleep < 5:
        return "High"

    elif sleep < 7:
        return "Moderate"

    return "Low"


# ===============================
# STUDY STREAK
# ===============================

def study_streak(hours):

    if hours >= 6:
        return "🔥 Excellent"

    elif hours >= 4:
        return "⚡ Consistent"

    return "📚 Beginner"


# ===============================
# WEEKLY PLAN
# ===============================

def generate_weekly_plan(weak_subject):

    return {

        "Monday":
        f"{weak_subject} Revision",

        "Tuesday":
        "Practice Questions",

        "Wednesday":
        f"{weak_subject} Problem Solving",

        "Thursday":
        "Formula Revision",

        "Friday":
        "Mock Test",

        "Saturday":
        "Error Analysis",

        "Sunday":
        "Complete Revision"

    }


# ===============================
# DAILY TIMETABLE
# ===============================

def generate_daily_plan(slot):

    if slot == "Morning":

        return [

            "6:00 AM - Wake Up",
            "6:30 AM - Revision",
            "8:00 AM - Classes",
            "4:00 PM - Practice Questions",
            "8:00 PM - Revision",
            "10:00 PM - Sleep"

        ]

    elif slot == "Night":

        return [

            "8:00 AM - Wake Up",
            "10:00 AM - Classes",
            "5:00 PM - Practice",
            "8:00 PM - Deep Study",
            "10:00 PM - Mock Test",
            "12:00 AM - Sleep"

        ]

    else:

        return [

            "7:00 AM - Wake Up",
            "9:00 AM - Classes",
            "4:00 PM - Study Session",
            "6:00 PM - Practice",
            "8:00 PM - Revision",
            "10:30 PM - Sleep"

        ]


# ===============================
# HOME PAGE
# ===============================

@app.route("/")
def home():

    return render_template("index.html")


# ===============================
# PREDICTION ROUTE
# ===============================

@app.route("/predict", methods=["POST"])
def predict():

    # -------------------------
    # BASIC DETAILS
    # -------------------------

    name = request.form["name"]

    study_time = float(
        request.form["study_time"]
    )

    attention = int(
        request.form["attention"]
    )

    revision = int(
        request.form["revision"]
    )

    mistakes = int(
        request.form["mistakes"]
    )

    sleep = float(
        request.form["sleep"]
    )

    attendance = int(
        request.form["attendance"]
    )

    # -------------------------
    # SUBJECT SCORES
    # -------------------------

    math = int(
        request.form["math"]
    )

    physics = int(
        request.form["physics"]
    )

    chemistry = int(
        request.form["chemistry"]
    )

    english = int(
        request.form["english"]
    )

    cs = int(
        request.form["cs"]
    )

    # -------------------------
    # LEARNING STYLE
    # -------------------------

    learning_style = request.form[
        "learning_style"
    ]

    study_slot = request.form[
        "study_slot"
    ]

    goal = request.form[
        "goal"
    ]

    # -------------------------
    # DAILY TRACKER
    # -------------------------

    # Safer method to grab form inputs without risking a 400 crash
    daily_study = float(request.form.get("daily_study", 0.0))

    questions = int(
        request.form["questions"]
    )

    mock_score = int(
        request.form["mock_score"]
    )

    daily_sleep = float(
        request.form["daily_sleep"]
    )

    mood = request.form[
        "mood"
    ]

    # ==========================
    # ML MODEL INPUT
    # ==========================

    features = np.array([[

        study_time,
        attention,
        revision,
        mistakes,
        sleep,
        attendance,
        math,
        physics,
        chemistry,
        english,
        cs

    ]])

    prediction = model.predict(
        features
    )

    performance = encoder.inverse_transform(
        prediction
    )[0]

    # ==========================
    # SUBJECT ANALYSIS
    # ==========================

    subjects = {

        "Mathematics": math,
        "Physics": physics,
        "Chemistry": chemistry,
        "English": english,
        "Computer Science": cs

    }

    strong_subject = max(
        subjects,
        key=subjects.get
    )

    weak_subjects = [

        subject

        for subject, score

        in subjects.items()

        if score < 60

    ]

    weakest_subject = (

        weak_subjects[0]

        if weak_subjects

        else "General Revision"

    )

    # ==========================
    # PRODUCTIVITY
    # ==========================

    daily_score = calculate_daily_score(

        daily_study,
        questions,
        mock_score,
        daily_sleep

    )

    rating = productivity_level(
        daily_score
    )

    badge = get_badge(
        daily_score
    )

    streak = study_streak(
        daily_study
    )

    burnout = burnout_check(
        daily_sleep
    )

    # ==========================
    # READINESS
    # ==========================

    readiness = round(

        (
            math +
            physics +
            chemistry +
            english +
            cs

        ) / 5

    )

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    report = []

    report.append(
        f"Your strongest subject is {strong_subject}."
    )

    if weak_subjects:

        report.append(
            "Spend more time on: "
            + ", ".join(weak_subjects)
        )

    if attention < 25:

        report.append(
            "Use the Pomodoro Technique."
        )

    if mistakes > 10:

        report.append(
            "Review mistakes after every practice session."
        )

    if revision < 2:

        report.append(
            "Increase revision frequency."
        )

    if sleep < 6:

        report.append(
            "Improve your sleep schedule."
        )

    if learning_style == "Visual":

        report.append(
            "Use diagrams, flowcharts and videos."
        )

    elif learning_style == "Reading":

        report.append(
            "Use notes and written summaries."
        )

    else:

        report.append(
            "Practice through projects and exercises."
        )

    # ==========================
    # STUDY PLANS
    # ==========================

    weekly_plan = generate_weekly_plan(
        weakest_subject
    )

    daily_plan = generate_daily_plan(
        study_slot
    )

    # ==========================
    # DASHBOARD
    # ==========================

    return render_template(

        "dashboard.html",

        name=name,

        performance=performance,

        strong_subject=strong_subject,

        weak_subjects=weak_subjects,

        report=report,

        math=math,
        physics=physics,
        chemistry=chemistry,
        english=english,
        cs=cs,

        readiness=readiness,

        daily_score=daily_score,

        rating=rating,

        badge=badge,

        streak=streak,

        burnout=burnout,

        questions=questions,

        mock_score=mock_score,

        daily_study=daily_study,

        daily_sleep=daily_sleep,

        mood=mood,

        goal=goal,

        weekly_plan=weekly_plan,

        daily_plan=daily_plan

    )


# ===============================
# RUN APPLICATION
# ===============================

if __name__ == "__main__":

    app.run(
        debug=True
    )