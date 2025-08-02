# MSD Pipeline Homework - CI/CD Implementation

A hands-on CI/CD pipeline built for a Python project using GitHub Actions. This isn’t just a demo — it’s meant to mirror real-world DevOps standards like automated testing, quality checks, and structured releases.

## My Approach

### Why I Built It This Way

When I got the assignment, I didn’t want to just tick the boxes. I asked:

* How do teams catch issues early?
* What makes releases reliable and repeatable?
* How can we keep security and code quality in check?

From there, I split the pipeline into two workflows:

* One for PRs: to test and validate changes before merging
* One for releases: to bump versions, tag, and package

### What I’d Want as a Team Lead

* Tests that run on all major Python versions
* Lint and security checks baked into every PR
* Clean, tagged releases with artifacts and traceable changes

## Project Overview

A simple calculator app with two GitHub Actions workflows:

* **PR Workflow** – runs tests, linting, and security scans on pull requests
* **Release Workflow** – bumps version, builds the package, and simulates deployment

## Repo Structure

```
msd-pipeline-hw/
├── .github/workflows/
│   ├── pr.yml
│   └── release.yml
├── main.py
├── test_main.py
├── setup.py
├── requirements.txt
└── README.md
```

## The App

Basic calculator with:

* Add
* Subtract
* Multiply
* Divide (handles divide-by-zero)

## Why GitHub Actions?

* It’s already part of GitHub — no extra tools to manage
* Easy to learn, easy to share
* Lots of reusable actions in the marketplace

## Key Tools I Used

### Testing

* `unittest` — efficient and built-in
* `pytest + coverage` — for better test reporting
* Matrix testing — Python 3.8–3.12

### Quality & Security

* `flake8` — code style and bugs
* `bandit` — scans for security issues
* `safety` — checks for vulnerable dependencies

### Versioning

* `bump2version` — handles version bumps and tagging
* Semantic commits — for patch/minor/major logic

## Things I Ran Into

* **bump2version** failed on untracked files — solved it by handling version updates separately from git push
* **GITHUB\_TOKEN** didn’t allow pushing — fixed by explicitly setting permissions in the workflow
* **Publishing** — GitHub Package registry has strict naming rules, so I set it up but left it commented for now

## Pull Request Workflow

```mermaid
graph TB
    A[Developer creates PR] --> B[PR Workflow Triggers]
    B --> C{Setup Matrix}
    C --> D[Python 3.8]
    C --> E[Python 3.9]
    C --> F[Python 3.10]
    C --> G[Python 3.11]

    D --> H[Install Dependencies]
    E --> H
    F --> H
    G --> H

    H --> I[Run Linting]
    I --> J[Execute Tests]
    J --> K[Generate Coverage]
    K --> L[Security Scan]
    L --> M[Upload Reports]

    M --> N{All Checks Pass?}
    N -->|Yes| O[✅ PR Ready for Review]
    N -->|No| P[❌ Fix Issues Required]

    style O fill:#90EE90
    style P fill:#FFB6C1
```

## Release Workflow

```mermaid
graph TB
    A[Push to main / Manual trigger] --> B[Determine Version Bump]
    B --> C[Update Version in Files]
    C --> D[Create Git Tag]
    D --> E[Push Changes]

    E --> F[Checkout Updated Code]
    F --> G[Run Tests]
    G --> H[Build Package]
    H --> I[Validate Artifacts]

    I --> J[Upload to GitHub Releases]
    I --> K[Prepare for Artifactory]
    I --> L[Prepare for AWS S3]

    J --> M[Download Artifacts]
    K --> M
    L --> M

    M --> N[Simulate Deployments]
    N --> O{Deployment Success?}

    O -->|Yes| P[🎉 Release Complete]
    O -->|No| Q[❌ Notify Failure]

    style P fill:#90EE90
    style Q fill:#FFB6C1
```

## How to Run It

### PR Workflow:

```bash
git checkout -b feature/my-feature
git commit -m "feat: new stuff"
git push origin feature/my-feature
# Open PR to main
```

### Release Workflow (Auto):

```bash
git checkout main
git pull
# Push your changes
# Workflow triggers automatically
```

### Release Workflow (Manual):

* Go to GitHub → Actions → Release → Run Workflow
* Choose patch/minor/major

## Local Dev

```bash
git clone <repo>
cd msd-pipeline-hw
pip install -r requirements.txt
pip install -e .
```

### Run tests:

```bash
python -m unittest
pytest --cov=main --cov-report=term-missing
```

### Lint & Scan:

```bash
flake8 .
bandit -r .
safety check
```

### Build package:

```bash
python -m build
```

## Wrap-Up

This project shows how CI/CD can be clean, reliable, and team-friendly — even for small apps. It’s designed to scale and adapt to real team needs without the fluff.
