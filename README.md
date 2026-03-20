# 🛵 GigShield — AI-Powered Parametric Income Insurance for Food Delivery Partners

> **Guidewire DEVTrails 2026 | University Hackathon**
> Protecting the livelihoods of Zomato & Swiggy delivery partners from uncontrollable external disruptions — one shift at a time.

---

## 📌 Table of Contents

1. [Problem Statement](#problem-statement)
2. [Our Solution — The Four Pillars](#our-solution--the-four-pillars)
3. [Persona & Scenarios](#persona--scenarios)
4. [Application Workflow](#application-workflow)
5. [Weekly Premium Model](#weekly-premium-model)
6. [Parametric Triggers](#parametric-triggers)
7. [AI/ML Integration Plan](#aiml-integration-plan)
8. [Fraud Detection Architecture](#fraud-detection-architecture)
9. [Platform Choice — Web vs Mobile](#platform-choice--web-vs-mobile)
10. [Tech Stack](#tech-stack)
11. [Development Plan](#development-plan)

---

## Problem Statement

India's food delivery partners (Zomato, Swiggy) are the backbone of the urban gig economy. However, **external disruptions** — extreme rainfall, heatwaves, curfews, and local strikes — can wipe out **20–30% of their monthly income**.

Currently, **no financial safety net exists** for these workers.

GigShield solves this with **automated, parametric income protection** that pays out instantly when a verified disruption is detected.

> ⚠ **Coverage Scope:** Loss of income ONLY (no health, accident, or vehicle coverage)

---

## 💡 Our Solution — The Four Pillars

### 🕐 Pillar 1: Shift-Level Parametric Coverage

GigShield compensates workers based on **actual disrupted hours**, not full days.

| Shift   | Time         | Income Share |
| ------- | ------------ | ------------ |
| Morning | 8 AM – 2 PM  | ~35%         |
| Evening | 5 PM – 11 PM | ~65%         |

**Formula:**

```
Payout = (Avg Weekly Earnings ÷ Total Hours) × Lost Hours × Coverage %
```

---

### 🗺 Pillar 2: Zone Risk Score (ZRS)

Each delivery zone is assigned a risk score (0–100).

**Based on:**

* Weather history
* Flood/heat patterns
* Claim frequency
* Forecast

| Risk Level | Adjustment |
| ---------- | ---------- |
| Low        | −₹8        |
| Medium     | No change  |
| High       | +₹10       |
| Very High  | +₹18       |

---

### 🔀 Pillar 3: 3-Signal Fraud Validation

Claims must pass:

* Weather Data
* Platform Activity Drop
* GPS Location

✔ 2/3 signals → Auto approve
❌ Else → Flag for review

---

### 📈 Pillar 4: Income Smoothing Algorithm (ISA)

Ensures **weekly income stability**.

```
RIB = Avg of last 4 weeks
Income Gap = RIB − Current Earnings
Payout = Income Gap × Coverage %
```

---

## 🧑‍💼 Persona & Scenarios

### 👤 Persona: Ravi (Zomato Rider)

* Weekly income: ₹5,000–₹6,500
* Works 6 days/week
* Peak: lunch & dinner
* No financial backup

---

### 📋 Scenario 1: Heavy Rain ✅

* Rain detected
* Orders drop
* GPS confirmed

👉 ₹400 auto credited

---

### 📋 Scenario 2: Curfew ⚠

* Govt restriction detected
* Orders drop

👉 Partial payout

---

### 📋 Scenario 3: Fraud ❌

* No weather match
* No order drop

👉 Claim rejected

---

### 📋 Scenario 4: Weekly Income Drop 💰

* Income below baseline

👉 Weekly top-up credited

---

## ⚙️ Application Workflow

1. User registers
2. Risk profile generated
3. Premium calculated
4. System monitors conditions
5. Disruption detected
6. Auto claim triggered
7. Instant payout
8. Weekly income check

---

## 💰 Weekly Premium Model

### Base Plans

| Tier     | Premium | Coverage |
| -------- | ------- | -------- |
| Basic    | ₹29     | 50%      |
| Standard | ₹49     | 75%      |
| Pro      | ₹79     | 100%     |

---

### Dynamic Adjustments

* High-risk zone → +₹10 to ₹18
* Low-risk zone → −₹5 to ₹8
* Weather forecast risk → +₹5
* Low claims → discount

---

## 🌦️ Parametric Triggers

| Trigger         | Threshold  |
| --------------- | ---------- |
| Rain            | > 40mm     |
| Heat            | > 42°C     |
| AQI             | > 400      |
| Curfew          | Govt alert |
| Platform outage | >70% drop  |

---

## 🤖 AI/ML Integration Plan

* Risk scoring model
* Dynamic pricing engine
* Fraud detection system
* Income smoothing algorithm

---

## 🔐 Fraud Detection Architecture

```
Trigger → 3-Signal Check → Approve / Reject
```

---

## 🖥️ Platform Choice

**PWA (Progressive Web App)**

* Mobile-first
* No install needed
* Works on low-end devices

---

## 🧰 Tech Stack

| Layer    | Tech         |
| -------- | ------------ |
| Frontend | React        |
| Backend  | Node.js      |
| DB       | PostgreSQL   |
| ML       | Python       |
| APIs     | Weather, AQI |
| Payments | Razorpay     |

---

## 🗓️ Development Plan

### Phase 1 ✅

* Idea
* README
* Planning

---

### Phase 2

* Registration
* Policy system
* Claims automation

---

### Phase 3

* Fraud detection
* Payments
* Dashboard

---

## 🎥 Demo Video

👉 https://photos.app.goo.gl/HG7jmjUoDGJVfBj27

---

## 🔗 GitHub Repo

👉 https://github.com/augustus21adi/guidewire-hackathon

---

## 🚀 Why GigShield?

* Shift-based payouts
* AI pricing
* Auto claims
* Fraud-resistant
* Weekly protection

---

## ❤️ Final Note

When disruptions stop work,
**GigShield ensures income doesn’t stop.**
