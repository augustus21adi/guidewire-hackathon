# 🛵 GigShield — AI-Powered Parametric Income Insurance for Delivery Partners

> **Guidewire DEVTrails 2026 | Phase 1 Submission**
> Protecting the livelihoods of delivery partners from uncontrollable external disruptions.

---

## 📌 Problem Statement

India’s food delivery partners (Zomato, Swiggy) are a critical part of the gig economy. However, external disruptions such as heavy rainfall, extreme heat, pollution, curfews, or platform outages can reduce their working hours and cause **20–30% income loss**.

Currently, there is **no financial safety net** to protect them from such uncontrollable situations.

⚠️ **Coverage Scope:**
GigShield covers **LOSS OF INCOME ONLY**.
It strictly excludes:

* Health insurance
* Accident coverage
* Vehicle repair

---

## 💡 Our Solution — GigShield

GigShield is an **AI-powered parametric insurance platform** that automatically compensates delivery workers for income loss caused by real-world disruptions.

✔ Zero manual claims
✔ Real-time monitoring
✔ Instant payouts

The system detects events using APIs and triggers payouts automatically when predefined conditions are met.

---

## 🧠 Core Innovations

### 1. Shift-Level Coverage

Instead of daily payouts, GigShield compensates workers based on **disrupted working hours (shifts)**.

**Formula:**

```
Payout = (Avg Weekly Earning ÷ Total Hours) × Lost Hours × Coverage %
```

---

### 2. Zone Risk Score (ZRS)

Each delivery zone is assigned a **risk score (0–100)** based on:

* Historical weather data
* Flood/heat patterns
* Claim frequency

This score dynamically adjusts premiums.

---

### 3. 3-Signal Fraud Detection

Claims are validated using three signals:

* Weather Data
* Platform Activity Drop
* GPS Location

✔ If 2 out of 3 match → Auto approval
❌ Otherwise → Flag for review

---

### 4. Income Smoothing Algorithm (ISA)

Workers are protected at a **weekly level**, not just per event.

```
Rolling Income Baseline (RIB) = Avg of last 4 weeks
Income Gap = RIB − Current Week Earnings
```

If disruption occurred:

```
Payout = Income Gap × Coverage %
```

---

## 🧑‍💼 Target Persona

**Food Delivery Riders (Zomato/Swiggy)**

* Weekly income: ₹4,000–₹6,500
* Peak earnings during lunch & dinner
* Highly sensitive to weather disruptions
* No financial buffer

---

## ⚙️ Application Workflow

1. User registers on platform
2. AI generates risk profile (Zone Risk Score)
3. Weekly premium is calculated
4. User selects coverage plan
5. System continuously monitors:

   * Weather
   * Platform activity
   * GPS location
6. Disruption detected → claim auto-triggered
7. Instant payout credited
8. Weekly income check → additional top-up if needed

---

## 🌦️ Parametric Triggers

| Trigger         | Threshold        |
| --------------- | ---------------- |
| Heavy Rainfall  | > 40mm (3 hours) |
| Extreme Heat    | > 42°C           |
| Air Pollution   | AQI > 400        |
| Curfew          | Govt restriction |
| Platform Outage | > 70% order drop |

---

## 💰 Weekly Premium Model

### Base Plans

| Tier           | Weekly Premium | Coverage |
| -------------- | -------------- | -------- |
| Basic Shield   | ₹29            | 50%      |
| Standard Guard | ₹49            | 75%      |
| Pro Armor      | ₹79            | 100%     |

---

### Dynamic Adjustments

* High-risk zone → +₹10 to ₹18
* Low-risk zone → −₹5 to ₹8
* Weather forecast risk → +₹5
* Low claim history → Discount

---

## 🤖 AI/ML Integration

### Risk Scoring Model

* Predicts zone risk using historical data

### Dynamic Pricing Engine

* Adjusts premiums per user

### Fraud Detection System

* Detects anomalies using multi-signal validation

### Income Smoothing Algorithm

* Ensures stable weekly income

---

## 🔐 Fraud Prevention

* GPS validation
* Duplicate claim prevention
* Multi-signal verification
* Claim frequency monitoring

---

## 🖥️ Platform Choice

**Progressive Web App (PWA)**

* Mobile-first design
* No installation required
* Works on low-end devices

---

## 🧰 Tech Stack

Frontend:

* React.js (PWA)

Backend:

* Node.js + Express

Database:

* PostgreSQL

AI/ML:

* Python (Scikit-learn / XGBoost)

APIs:

* OpenWeather API
* AQI API
* Mock Platform API

Payments:

* Razorpay (Test Mode)

---

## 🗓️ Development Plan

### Phase 1 (Ideation & Foundation)

* Problem analysis ✅
* Persona definition ✅
* Workflow design ✅
* AI planning ✅
* README creation ✅
* Video explanation ⏳

---

### Phase 2 (Automation & Protection)

* User registration
* Policy management
* Premium calculation
* Claim automation

---

### Phase 3 (Scale & Optimization)

* Fraud detection system
* Payment integration
* Worker & admin dashboards
* Final demo & pitch

---

## 🎥 Demo Video

👉 https://photos.app.goo.gl/HG7jmjUoDGJVfBj27

---

## 🔗 GitHub Repository

👉 https://github.com/augustus21adi/guidewire-hackathon

---

## 🚀 Why GigShield?

* Shift-based accurate payouts
* AI-driven dynamic pricing
* Fully automated claims
* Strong fraud detection
* Weekly income protection

---

## ❤️ Final Note

GigShield ensures that when disruptions stop work,
**income doesn’t stop.**
