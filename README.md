# The witty senior

## 1. What is this about?

AI Witty Tutor is an interactive learning assistant designed to support programming practice through guided problem-solving, adaptive feedback, and light gamification.
Instead of simply giving answers, the tutor focuses on diagnosing mistakes, guiding reasoning, and encouraging deeper understanding—while maintaining a subtle, engaging personality.

## 2. Goal

The goal of this project is to build a AI system that:

- Helps users learn programming through active problem-solving
- Provides structured feedback, not just solutions
- Tracks learning progress and mistakes over time
- Balances deep work with light gamification elements
- Demonstrates clean architecture, maintainability, and scalable design

From a technical perspective, the project aims to showcase:

- LLM integration and orchestration
- Backend system design with clear separation of concerns
- Code evaluation and feedback systems
- State management for personalized learning

## 3. Structure

the-witty-senior/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── routes/               # API endpoints
│   │   └── tutor.py
│   │
│   ├── services/             # Core logic
│   │   ├── llm_service.py    # LLM interaction wrapper
│   │   ├── tutor_service.py  # Tutoring logic (guidance, hints)
│   │   ├── eval_service.py   # Code evaluation & feedback
│   │   └── gamification.py   # XP, streaks, progress logic
│   │
│   ├── models/               # Data models (Pydantic / ORM)
│   │   ├── user.py
│   │   ├── session.py
│   │   └── attempt.py
│   │
│   ├── core/                 # Core utilities
│   │   ├── config.py         # Settings/configuration
│   │   ├── logging.py        # Logging setup
│   │   └── database.py       # DB connection
│   │
│   └── infra/                # External integrations
│       ├── llm_client.py     # API client
│       └── code_runner.py    # Safe code execution
│
├── tests/                    # Unit & integration tests
│   ├── test_eval.py
│   └── test_tutor.py
│
├── scripts/                  # Utility scripts
│   └── seed_data.py
│
├── .pre-commit-config.yaml   # Linting & formatting hooks
├── pyproject.toml            # Dependencies & tooling
├── Dockerfile                # Containerization
└── README.md

## 4. Small example

User task:

``` python
# Write a function that returns the sum of numbers from 1 to n
def sum_to_n(n):
    pass
```

User attempt:

``` python
def sum_to_n(n):
    return n * (n + 1)
```

System Behavior:

- Evaluation Layer:
  - Detects incorrect formula (missing division by 2)
- Tutor Response
  - Does NOT give the answer directly
  - Provides a hint:
  >“You're very close 👀
  >This looks like a known formula—are you missing a small factor that keeps the result from growing too fast?”

- Gamification Layer
  - Tracks attempt count
  - Adjusts difficulty or hint level
  - Updates streak/XP if corrected
