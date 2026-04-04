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

India's food delivery partners (Zomato, Swiggy) are the backbone of the urban gig economy. However, **external disruptions** — extreme rainfall, heatwaves, city-wide curfews, and local strikes — can wipe out 20–30% of their monthly income with zero recourse.

When a monsoon hits Mumbai at 7 PM on a Friday, a delivery partner doesn't just lose one order — they lose their entire evening shift, which is typically their highest-earning window of the week. Currently, **no financial safety net exists** for these workers.

**GigShield** solves this with automated, parametric income protection that pays out instantly when a verified disruption is detected — and intelligently tops up any remaining weekly income gap every Sunday night. Zero paperwork, zero human intervention.

> ⚠️ **Coverage Scope:** GigShield covers **loss of income ONLY**. We strictly exclude health insurance, life insurance, accident coverage, and vehicle repair payouts.

---

## Our Solution — The Four Pillars

GigShield is built on four tightly integrated ideas that together create a differentiated, fraud-resistant, and fair platform:

---

### 🕐 Pillar 1: Shift-Level Parametric Coverage

Most insurance products think in days. GigShield thinks in **shifts**.

Every delivery partner works two primary earning windows:

| Shift | Time Window | Avg Income Share |
|-------|-------------|-----------------|
| Morning Shift | 8 AM – 2 PM | ~35% of daily income |
| Evening Shift | 5 PM – 11 PM | ~65% of daily income |

If a disruption hits only the evening shift, the worker receives a **proportional payout for exactly those disrupted hours** — not a flat daily amount. This is precise, fair, and transparent.

**Payout Formula:**
```
Payout = (Avg Weekly Earning ÷ Active Weekly Hours) × Disrupted Hours × Coverage %
```

**Example:** Ravi earns ₹5,600/week working 56 hours. A 4-hour evening disruption:
```
(5600 ÷ 56) × 4 × 100% = ₹400 payout
```

---

### 🗺 Pillar 2: Delivery Zone Intelligence (Zone Risk Score)

Every city is not equal. Mumbai's Kurla zone floods differently than Bandra. GigShield builds a **Zone Risk Score (ZRS)** for every active delivery zone.

**ZRS is calculated weekly using:**
- Historical IMD weather data for that zone
- Past flood/waterlogging records (municipal data / mock)
- Historical claim frequency from that zone
- Upcoming 7-day weather forecast

**ZRS drives dynamic premium adjustment:**

| Zone Risk Score | Premium Adjustment | Example Zone |
|----------------|-------------------|--------------|
| 0 – 30 (Low) | −₹8/week | Bandra, Koramangala |
| 31 – 60 (Medium) | No change | Andheri, Whitefield |
| 61 – 80 (High) | +₹10/week | Kurla, Bommanahalli |
| 81 – 100 (Very High) | +₹18/week | Dharavi, Bellandur |

Workers in safer zones are rewarded with lower premiums. Workers in high-risk zones pay slightly more but receive **more frequent, faster payouts** — a fair exchange.

---

### 🔀 Pillar 3: 3-Signal Fraud Validation

The most innovative part of GigShield. Instead of trusting any single data source, **every claim must pass a 3-signal corroboration check** before a payout is released.

```
Signal 1: WEATHER ──────────────────┐
Signal 2: PLATFORM ACTIVITY DROP ───┼──► 2 of 3 PASS → AUTO APPROVE
Signal 3: GPS ZONE VALIDATION ──────┘ 0-1 of 3 PASS → FLAG FOR REVIEW
```

**Why this works:**
- Fake weather claims are caught because platform order volumes don't drop
- GPS spoofing is caught because real weather + platform drops won't match spoofed coordinates
- Colluding workers can't easily fake all three signals simultaneously

This replaces expensive human claim review with a deterministic, auditable AI pipeline.

---

### 📈 Pillar 4: Income Smoothing Algorithm (ISA)

The most worker-centric innovation in GigShield. Every other insurance product pays based on **event severity**. GigShield pays based on **actual income impact** — which is what the worker truly cares about.

**Core Idea:** Every worker has a *Rolling Income Baseline (RIB)* — their personal average weekly income calculated from the last 4 weeks. If a verified disruption causes their actual earnings to fall below this baseline, GigShield **automatically tops up the difference** based on their coverage tier.

```
Rolling Income Baseline (RIB) = (W-1 + W-2 + W-3 + W-4 earnings) ÷ 4
Income Gap = RIB − Actual Week Earning

If Income Gap > 0 AND verified disruption occurred this week:
  Payout = Income Gap × Tier Coverage %
```

**Tier Coverage on Income Gap:**

| Tier | Gap Coverage % | Example |
|------|---------------|---------|
| 🔵 Basic Shield | 50% of gap | Gap ₹1,800 → Payout ₹900 |
| 🟡 Standard Guard | 75% of gap | Gap ₹1,800 → Payout ₹1,350 |
| 🔴 Pro Armor | 100% of gap | Gap ₹1,800 → Payout ₹1,800 |

**Real Example:**
- Ravi's RIB (last 4 weeks avg) = ₹5,600/week
- This week: 2 disrupted evenings due to heavy rain → actual earnings = ₹3,800
- Income Gap = ₹5,600 − ₹3,800 = **₹1,800**
- Pro Armor tier → **₹1,800 credited automatically on Sunday night**

**Guard Rail — Prevents Gaming:**
ISA only triggers if a **verified parametric event** (from Pillars 1–3) occurred that week. An earnings drop with no disruption trigger = no payout.

**RIB Update Logic:**
- RIB is recalculated every Sunday night using the last 4 completed weeks
- Weeks where a payout was received are excluded from the RIB calculation
- New workers: RIB is seeded from platform onboarding data (simulated) for the first 4 weeks

---

## Persona & Scenarios

### 👤 Primary Persona: Ravi, 28 — Zomato Delivery Partner, Bangalore

- Works Morning + Evening shifts, 6 days/week
- Average weekly earning: ₹5,000–₹6,500
- Peak earning: 12–2 PM (lunch) and 7–10 PM (dinner)
- Operates in HSR Layout and Koramangala zones
- Smartphone-first user, no tolerance for complex processes
- Zero savings buffer — one disrupted evening shift is a real financial setback

---

### 📋 Scenario 1: Heavy Rainfall — Auto Claim Triggered ✅

**What happens:** Bangalore receives 65mm of rainfall between 6 PM–9 PM on a Tuesday (trigger threshold: >40mm/3hr). Zomato's simulated order volume in Koramangala drops 72%.

**GigShield's 3-Signal Check:**
- Signal 1 — Weather API: ✅ Heavy rain confirmed, exceeds threshold
- Signal 2 — Platform Activity: ✅ Order volume drop >60% in zone
- Signal 3 — GPS Validation: ✅ Ravi's last ping was inside Koramangala zone

**Result:** Claim auto-approved in < 3 minutes. ₹400 credited to Ravi's UPI.

**Ravi's experience:** Zero action needed. He gets a notification: *"Evening shift disrupted. ₹400 credited. Stay safe 🌧"*

---

### 📋 Scenario 2: Unplanned Curfew — Partial Payout ⚠️

**What happens:** Section 144 imposed in HSR Layout from 2–6 PM on a Saturday due to a local protest.

**GigShield's 3-Signal Check:**
- Signal 1 — Government Alert API: ✅ Curfew order verified
- Signal 2 — Platform Activity: ✅ Order volume near-zero in zone
- Signal 3 — GPS Validation: ✅ Last active location was HSR Layout

**Result:** Partial payout of ₹200 for 2 hours of disrupted afternoon window. Evening shift unaffected — no payout for that period.

---

### 📋 Scenario 3: Fraud Attempt — Blocked ❌

**What happens:** A bad actor tries to claim for a "heat disruption" on a day where temperatures were 36°C (below the 42°C trigger threshold) and GPS-spoofs into an affected zone.

**GigShield's 3-Signal Check:**
- Signal 1 — Weather API: ❌ Temperature below trigger threshold
- Signal 2 — Platform Activity: ❌ Orders in zone were flowing normally
- Signal 3 — GPS Validation: ⚠️ Location pattern flagged as inconsistent

**Result:** Claim denied. Worker's fraud risk score increases. Insurer dashboard flagged for review.

---

### 📋 Scenario 4: Income Smoothing — Weekly Top-Up 💰

**What happens:** Monday had heavy rain (2 hrs disrupted), Thursday had a local strike (3 hrs disrupted). Each event triggered shift-level payouts. But by Sunday, total weekly earnings are still ₹3,800 — well below RIB of ₹5,600.

**ISA Sunday Night Check:**
- RIB = ₹5,600 (4-week rolling average)
- Actual week earning = ₹3,800
- Income Gap = ₹1,800
- Verified disruptions this week: ✅
- Tier: Pro Armor → Coverage = 100%

**Result:** ₹1,800 automatically credited to Ravi's UPI at 11 PM Sunday.

**Ravi's experience:** *"Weekly income protection applied. ₹1,800 added to keep your week on track. See you next week 💪"*

> **Note:** Shift-level payouts (Pillars 1–3) and ISA top-up (Pillar 4) work together — shift payouts are credited instantly during the week, ISA fills the remaining gap at week-end. No double counting.

---

## Application Workflow

```
╔══════════════════════════════════════════════════════════╗
║                      WORKER JOURNEY                      ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  [1] ONBOARDING                                          ║
║      → Register with Zomato/Swiggy Partner ID            ║
║      → Zone auto-detected from delivery history          ║
║      → AI Risk Profile generated (ZRS + persona data)    ║
║      → Weekly premium quoted dynamically                 ║
║                                                          ║
║  [2] POLICY SELECTION                                    ║
║      → Choose coverage tier (Basic / Standard / Pro)     ║
║      → Select shifts to cover (Morning / Evening / Both) ║
║      → Pay weekly premium via UPI / wallet               ║
║      → Policy active immediately                         ║
║                                                          ║
║  [3] ACTIVE MONITORING (Background, Zero Touch)          ║
║      → Real-time weather API polling (every 15 min)      ║
║      → Platform activity monitoring (simulated)          ║
║      → GPS zone tracking (with consent)                  ║
║                                                          ║
║  [4] DISRUPTION DETECTED                                 ║
║      → Trigger threshold crossed                         ║
║      → 3-Signal fraud check runs automatically           ║
║      → If 2/3 signals pass → Claim auto-approved         ║
║      → If <2 signals pass → Flagged for admin review     ║
║                                                          ║
║  [5] INSTANT PAYOUT (Shift-Level)                        ║
║      → Payout calculated: hours lost × hourly rate       ║
║      → Sent to registered UPI ID instantly               ║
║      → Push notification to worker                       ║
║      → Claim logged on worker dashboard                  ║
║                                                          ║
║  [6] SUNDAY NIGHT — ISA WEEKLY CHECK                     ║
║      → RIB calculated from last 4 weeks earnings         ║
║      → Actual week earning fetched from platform API     ║
║      → If Gap > 0 AND disruption verified this week      ║
║      → Top-up payout credited automatically              ║
║      → Worker notified: "Weekly income protected ✅"     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

## Weekly Premium Model

### Base Tiers

| Tier | Weekly Premium | Max Weekly Payout | Best For |
|------|---------------|-------------------|----------|
| 🔵 Basic Shield | ₹29/week | ₹500 | Part-time, morning-only riders |
| 🟡 Standard Guard | ₹49/week | ₹1,000 | Regular riders, one peak shift |
| 🔴 Pro Armor | ₹79/week | ₹2,000 | Full-time, both shifts covered |

### Dynamic Adjustments (AI-Powered)

| Factor | Adjustment | Logic |
|--------|-----------|-------|
| Zone Risk Score (High) | +₹10 to +₹18 | Worker in flood-prone zone |
| Zone Risk Score (Low) | −₹5 to −₹8 | Worker in historically safe zone |
| Upcoming 7-day forecast (rain predicted) | +₹5 | Pre-emptive risk pricing |
| Streak Bonus (4 clean weeks) | −₹5 | Loyalty + moral hazard reduction |
| Historical claim frequency (>3 claims/month) | +₹8 | Higher personal risk profile |

### Streak Protection Bonus

Workers who go **4 consecutive weeks without a claim** earn a ₹5 discount on their 5th week's premium. This rewards low-risk behavior, reduces moral hazard, and builds long-term platform loyalty.

---

## Parametric Triggers

GigShield uses **5 automated triggers** mapped to real income loss events for food delivery partners:

| # | Trigger | Threshold | Data Source | Signal Type |
|---|---------|-----------|-------------|-------------|
| 1 | Heavy Rainfall | > 40mm in 3 hours | IMD API / OpenWeatherMap | Environmental |
| 2 | Extreme Heat | > 42°C sustained 2+ hours | IMD API | Environmental |
| 3 | Severe Air Pollution | AQI > 400 (Hazardous) | CPCB API / IQAir | Environmental |
| 4 | Curfew / Section 144 | Official government alert in zone | Govt alert API (mock) | Social |
| 5 | Platform Outage | >70% order volume drop in zone | Simulated platform API | Platform |

> All thresholds are set at levels that verifiably prevent outdoor work for delivery partners — not mild inconveniences.

---

## AI/ML Integration Plan

### 1. Zone Risk Scoring Model
- **Type:** Supervised regression (Random Forest / XGBoost)
- **Inputs:** Zone ID, month, historical weather events, past claim count, day-of-week patterns, flood map overlay
- **Output:** Zone Risk Score (0–100), updated every Monday
- **Training Data:** IMD historical weather data (public) + synthetic claim data
- **Why Random Forest:** Explainable, handles mixed feature types, no large dataset required

### 2. Dynamic Premium Engine
- **Type:** Rule-based + ML hybrid
- **Layer 1 (Rules):** Base tier × zone risk adjustment
- **Layer 2 (ML):** Personalized adjustment based on worker's claim history, shift patterns, zone transitions
- **Output:** Weekly premium quote per worker

### 3. Payout Calculation Engine
- **Type:** Deterministic formula (no ML needed — transparency is key)
- **Formula:** `(Avg Weekly Earning ÷ Active Hours) × Disrupted Hours × Tier Coverage %`

### 4. Fraud Detection Model
- **Type:** Rule-based anomaly detection + lightweight ML flag scoring
- **3-Signal Check (Rule-based):** Fast, auditable, deterministic
- **Fraud Risk Score (ML):** Rolling score based on claim frequency, location patterns, claim timing vs weather data lag
- **GPS Spoof Detection:** Checks for stationary GPS with moving timestamps, impossible travel speeds, coordinate clustering inconsistencies

### 5. Income Smoothing Algorithm (ISA) Engine
- **Type:** Deterministic formula + weekly batch job
- **RIB Calculation:** Runs every Sunday at 10 PM
- **Gap Calculation:** `RIB − Actual Week Earning` — only triggered if verified parametric event occurred
- **Anti-Gaming Logic:** Cross-references weekly disruption log before releasing ISA payout
- **Output:** Automated UPI top-up transaction per eligible worker

### 6. Claim Auto-Approval Bot
- **Type:** Event-driven pipeline
- **Flow:** Trigger detected → Pull active policies in zone → Run 3-signal check → Calculate payout → Push to payment API → Log claim
- **SLA:** < 5 minutes from trigger detection to UPI credit

---

## Fraud Detection Architecture

```
┌─────────────────────┐
│  DISRUPTION TRIGGER │
│  (Weather/Social/   │
│   Platform)         │
└──────────┬──────────┘
           │
┌──────────▼──────────────────────┐
│       3-SIGNAL VALIDATOR        │
│                                 │
│  [S1] Weather API Confirmation  │
│       Was threshold crossed?    │
│                                 │
│  [S2] Platform Activity Check   │
│       Did order volume drop >60%│
│                                 │
│  [S3] GPS Zone Validation       │
│       Was worker in zone?       │
└────────┬───────────────┬────────┘
         │               │
      2–3 Signals     0–1 Signal
      Confirmed       Confirmed
         │               │
┌────────▼──────┐  ┌─────▼──────────────┐
│ AUTO APPROVE  │  │  FLAG FOR REVIEW   │
│ + Payout UPI  │  │  Fraud Score ↑     │
└───────────────┘  │  Admin Dashboard   │
                   └────────────────────┘
```

**Additional Fraud Safeguards:**
- **Duplicate claim prevention:** One active claim per worker per shift window
- **Claim velocity check:** >3 claims in 7 days triggers manual review
- **GPS spoofing detection:** Impossible speed, stationary anomaly, coordinate clustering checks
- **Zone boundary check:** Worker must have been active in affected zone in last 2 hours before trigger

---

## Platform Choice — Web vs Mobile

**Decision: Mobile-First Progressive Web App (PWA)**

| Factor | Reasoning |
|--------|-----------|
| Target user | Delivery partners are smartphone-first, app-native users |
| Friction reduction | PWA = no Play Store install needed, works offline, fast |
| Admin dashboard | Web-first for insurers — complex analytics need larger screen |
| Development speed | Single HTML/CSS/JS codebase serves both worker and admin needs |
| Low-end device support | Lighter than native app, works on budget Android phones |

The worker-facing UI is designed for **one-thumb operation** — the most common interaction mode for a rider who just parked their bike.

---

## Tech Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Frontend | Vanilla HTML + CSS + JavaScript | Mobile-first PWA, zero build tooling, fully functional demo |
| Backend | Node.js + Express | Fast API development, good ecosystem |
| Database | PostgreSQL | Relational structure fits policy/claims data model |
| ML Models | Python (scikit-learn / XGBoost) | Zone risk scoring, fraud detection |
| ML Serving | FastAPI (Python) | Lightweight ML inference API |
| Weather API | OpenWeatherMap (free tier) | Real-time + forecast data |
| AQI API | OpenAQ / IQAir (free tier) | Pollution trigger |
| Platform API | Mocked (JSON server) | Simulates Zomato order volume data |
| Payment | Razorpay Test Mode | Simulates UPI payouts |
| GPS / Maps | Leaflet.js + OpenStreetMap | Zone visualization, free |
| Hosting | Render / Railway (free tier) | Quick deployment for demo |

---

## Development Plan

### Phase 1 (Weeks 1–2): Ideation & Foundation ✅ — Completed March 20

- [x] Problem analysis and persona definition
- [x] Solution architecture design (Shift-level + Zone Intelligence + 3-Signal Fraud)
- [x] Weekly premium model design
- [x] Parametric trigger definition
- [x] Tech stack finalization
- [x] README documentation
- [x] 2-minute strategy video

---

### Phase 2 (Weeks 3–4): Automation & Protection ✅ — Completed April 4

- [x] Worker registration + onboarding flow (with AI Risk Profile generation)
- [x] Zone Risk Score model — dynamic ZRS with 6 zones, interactive UI
- [x] Dynamic premium calculation engine (base tier + zone adjustment + streak bonus)
- [x] Policy creation and management UI (3 tiers, shift selection, premium breakdown)
- [x] 5 parametric trigger integrations — Weather, AQI, Curfew, Platform, Heat (simulated)
- [x] Income Smoothing Algorithm (ISA) — RIB display, gap calculation, Sunday top-up simulation
- [x] 3-Signal fraud validation pipeline (visual validator with signal-level feedback)
- [x] Claims management module (history, auto-approve animation, simulate disruption)
- [x] Worker dashboard (metrics, shift indicators, earnings chart, streak tracker)
- [x] Admin / Insurer dashboard (loss ratio, zone risk bars, fraud queue, predictive analytics)

---

### Phase 3 (Weeks 5–6): Scale & Optimise — Due April 17

- [ ] Advanced GPS spoof detection (backend logic)
- [ ] Razorpay test mode payout integration (live UPI simulation)
- [ ] Real OpenWeatherMap API integration (replace mocked triggers)
- [ ] Worker dashboard: full earnings history, weekly coverage status
- [ ] End-to-end demo: trigger rainstorm → auto-approve → UPI payout in < 5 min
- [ ] Final pitch deck (PDF)
- [ ] 5-minute walkthrough video

---

## Why GigShield Wins

| Dimension | Generic Competitor | GigShield |
|-----------|-------------------|-----------|
| Coverage granularity | Day-level payout | **Shift-level payout** |
| Pricing fairness | Flat premium | **Zone Risk Score-adjusted** |
| Fraud defense | Single signal check | **3-Signal corroboration** |
| Claim process | Worker files manually | **Zero-touch auto-trigger** |
| Income protection | Fixed event payout | **Personalized weekly income top-up (ISA)** |
| Worker loyalty | No incentive to stay | **Streak Bonus discount** |
| Payout speed | Days / weeks | **< 5 minutes (shift) + Sunday top-up (ISA)** |

demo video: https://youtu.be/dET2CezY9_I 

try it out: https://augustus21adi.github.io/guidewire-hackathon/

github repo: https://github.com/augustus21adi/guidewire-hackathon

---

*Built with ❤️ for India's gig workers. Because when the rain doesn't stop, the bills don't either.*
