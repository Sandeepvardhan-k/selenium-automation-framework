#Selenium Web Automation Testing Framework

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen)
![Tests](https://img.shields.io/badge/Tests-8%20Passing-success)

End-to-end test automation framework built with Python and Selenium 
testing Flipkart — a real production e-commerce website. 
Implements industry-standard Page Object Model design pattern 
with Docker containerization and GitHub Actions CI/CD pipeline.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9 | Primary programming language |
| Selenium WebDriver | Browser automation |
| pytest | Test framework and execution |
| pytest-html | HTML test report generation |
| Page Object Model | Design pattern for maintainability |
| Docker | Containerization with headless Chrome |
| GitHub Actions | CI/CD — auto runs tests on every push |
| XPath + CSS Selectors | Element locator strategies |

---

## Project Structure
selenium-automation-framework/
├── pages/
│   ├── init.py
│   ├── login_page.py        # Login page interactions
│   └── flipkart_page.py     # Flipkart page interactions
├── tests/
│   ├── init.py
│   ├── test_login.py        # Login test cases
│   └── test_flipkart.py     # Flipkart test cases
├── reports/
│   └── report.html          # Generated HTML report
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions workflow
├── conftest.py
├── Dockerfile
├── requirements.txt
└── .gitignore

---

## Test Cases (8 Total)

### Login Tests — the-internet.herokuapp.com
| Test | Description | Type |
|------|-------------|------|
| test_valid_login | Login with correct credentials | Positive |
| test_invalid_login | Login with wrong credentials | Negative |

### Flipkart Tests — flipkart.com
| Test | Description | Type |
|------|-------------|------|
| test_flipkart_opens | Verify Flipkart loads correctly | Positive |
| test_search_product | Search iPhone 15 and verify results | Positive |
| test_search_results_appear | Verify search returns results | Positive |
| test_product_price_exists | Verify prices shown on results | Positive |
| test_search_url_changes | Verify URL updates after search | Positive |
| test_search_box_accepts_input | Verify search input works | Positive |

---

## Key Features

- **Page Object Model** — Separates page interaction logic
  from test logic for clean maintainable code
- **Explicit Waits** — WebDriverWait instead of time.sleep()
  for reliable test execution
- **Exception Handling** — try/except for graceful
  handling of dynamic elements like popups
- **Cross-environment** — Runs locally and in Docker
- **Auto CI/CD** — GitHub Actions triggers on every push
- **HTML Reports** — Visual test results with pytest-html
- **Positive + Negative Tests** — Complete test coverage

---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Google Chrome browser
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/Sandeepvardhan-k/selenium-automation-framework
cd selenium-automation-framework

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Tests
```bash
# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html

# Run specific file
pytest tests/test_flipkart.py -v

# Run specific test
pytest tests/test_flipkart.py::TestFlipkart::test_search_product -v
```

---

## How to Run with Docker
```bash
# Build Docker image
docker build -t selenium-tests .

# Run tests in container
docker run selenium-tests

# Rebuild fresh (no cache)
docker build --no-cache -t selenium-tests .
```

---

## CI/CD Pipeline

Every push to `main` branch automatically:
Push code → GitHub Actions triggered
→ Ubuntu server starts
→ Python 3.9 installed
→ Dependencies installed
→ Chrome installed
→ pytest runs all tests
→ HTML report saved
→ Pass/Fail shown on GitHub

View results: Go to **Actions** tab on GitHub

---

## Requirements
selenium
pytest
pytest-html

---

## Author

**Sandeepvardhan K**
- GitHub: [github.com/Sandeepvardhan-k](https://github.com/Sandeepvardhan-k)
- LinkedIn:[ [linkedin.com/in/sandeepvardhan-k](https://linkedin.com/in/sandeepvardhan-k)]
- Email: sandeepvardhan9381@gmail.com
