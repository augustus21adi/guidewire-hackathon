from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

# In-memory DB
users = {}

# Risk mapping
risk_premium = {
    "low": 10,
    "medium": 20,
    "high": 30
}

coverage_plans = {
    "basic": 0.5,
    "standard": 0.75,
    "pro": 1.0
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    location = request.form['location']
    risk = request.form['risk']

    premium = risk_premium[risk]

    users[name] = {
        "location": location,
        "risk": risk,
        "premium": premium,
        "plan": None,
        "coverage": 0,
        "last_payout": 0,
        "fraud_flag": False
    }

    return redirect(f"/policy/{name}")

@app.route('/policy/<name>')
def policy(name):
    return render_template("policy.html", name=name)

@app.route('/select-plan', methods=['POST'])
def select_plan():
    name = request.form['name']
    plan = request.form['plan']

    users[name]["plan"] = plan
    users[name]["coverage"] = coverage_plans[plan]

    return redirect(f"/dashboard/{name}")

@app.route('/dashboard/<name>')
def dashboard(name):
    user = users.get(name)
    return render_template("dashboard.html", user=user, name=name)

@app.route('/simulate', methods=['POST'])
def simulate():
    name = request.form['name']
    event = request.form['event']

    user = users[name]

    payout = 0
    fraud_flag = False

    # Fake signals
    weather_ok = False
    activity_drop = random.choice([True, False])
    gps_valid = random.choice([True, False])

    if event == "rain":
        rain = random.randint(50, 120)
        if rain > 80:
            weather_ok = True
            payout = 300

    elif event == "heat":
        temp = random.randint(35, 50)
        if temp > 45:
            weather_ok = True
            payout = 200

    elif event == "pollution":
        aqi = random.randint(100, 500)
        if aqi > 300:
            weather_ok = True
            payout = 150

    # 3-signal fraud check
    signals = sum([weather_ok, activity_drop, gps_valid])

    if signals >= 2:
        payout = int(payout * user["coverage"])
    else:
        payout = 0
        fraud_flag = True

    user["last_payout"] = payout
    user["fraud_flag"] = fraud_flag

    return redirect(f"/dashboard/{name}")

if __name__ == '__main__':
    app.run(debug=True)
