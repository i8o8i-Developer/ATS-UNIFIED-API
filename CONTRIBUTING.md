# Contributing to ATS-Unified-API

<p align="center">
  <strong>Help Us Build The Future Of Recruitment Technology! 🚀</strong>
  <br />
  <em>Guidelines For Contributors</em>
</p>

<p align="center">
  <a href="#-getting-started">🚀 Getting Started</a> •
  <a href="#-development-setup">🛠️ Development Setup</a> •
  <a href="#-coding-standards">📝 Coding Standards</a> •
  <a href="#-testing">🧪 Testing</a> •
  <a href="#-pull-requests">📬 Pull Requests</a>
</p>

---

## 🚀 Getting Started

We Love Your Input! We Want To Make Contributing To This Project As Easy And Transparent As Possible, Whether It's:

- 🐛 Reporting A Bug
- 💡 Discussing The Current State Of The Code
- 🆕 Submitting A Fix
- 🚀 Proposing New Features
- 📚 Becoming A Maintainer

### Development Process

We Use GitHub To Host Code, To Track Issues And Feature Requests, As Well As Accept Pull Requests.

1. Fork The Repo And Create Your Branch From `main`.
2. If You've Added Code That Should Be Tested, Add Tests.
3. If You've Changed APIs, Update The Documentation.
4. Ensure The Test Suite Passes.
5. Make Sure Your Code Lints.
6. Issue That Pull Request!

---

## 🛠️ Development Setup

### Prerequisites

- 🐍 Python 3.8 or higher
- 📦 pip (Python Package Manager)
- 🌐 Node.js & npm (For Serverless Deployment)
- 🐙 Git

### Local Development

1. **Clone Your Fork** 📥
   ```bash
   git clone https://github.com/your-username/ATS-Unified-API.git
   cd ATS-Unified-API
   ```

2. **Set Up Python Environment** 🐍
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r Mock-ATS/Requirements.txt
   ```

3. **Run The Mock Server** 🚀
   ```bash
   cd Mock-ATS
   python Mock_Server.py
   ```

4. **Test The API** 🧪
   Open `http://localhost:5000/dashboard` in your browser

### Serverless Deployment Setup

1. **Install Serverless Framework** ☁️
   ```bash
   npm install -g serverless
   ```

2. **Configure AWS Credentials** 🔑
   ```bash
   serverless config credentials --provider aws --key YOUR_ACCESS_KEY --secret YOUR_SECRET_KEY
   ```

3. **Deploy To AWS Lambda** 🚀
   ```bash
   cd SVL-FRAMEWORK
   serverless deploy
   ```

---

## 📝 Coding Standards

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Style Guide
- Use 4 Spaces For Indentation
- Maximum Line Length: 88 Characters (Black Formatter Default)
- Use Type Hints Where Possible
- Write Docstrings For All Public Functions And Classes

### Commit Messages

- Use The Present Tense ("Add Feature" Not "Added Feature")
- Use The Imperative Mood ("Move Cursor To..." Not "Moves Cursor To...")
- Limit The First Line To 72 Characters Or Less
- Reference Issues And Pull Requests Liberally After The First Line

### File Naming

- Use `snake_case` For Python Files And Variables
- Use `PascalCase` For Class Names
- Use `UPPER_CASE` For Constants

---

## 🧪 Testing

### Running Tests

```bash
# Run The Mock Server Tests
cd Mock-ATS
python -m pytest  # If Tests Exist

# Manual Testing
# Open dashboard.html in browser
# Test API endpoints with curl or Postman
```

### Testing Guidelines

- Write Tests For New Features
- Ensure All Tests Pass Before Submitting PR
- Test Both Mock Server And Serverless Deployments
- Include Integration Tests For API Endpoints

---

## 📬 Pull Requests

1. **Fork The Repository** 🍴
2. **Create A Feature Branch** 🌿: `git checkout -b feature/AmazingFeature`
3. **Make Your Changes** ✏️
4. **Commit Your Changes** 💾: `git commit -m 'Add Some AmazingFeature'`
5. **Push To The Branch** ⬆️: `git push origin feature/AmazingFeature`
6. **Open A Pull Request** 📬

### PR Guidelines

- Provide A Clear Description Of The Changes
- Reference Any Related Issues
- Include Screenshots For UI Changes
- Ensure CI/CD Pipelines Pass
- Request Review From Maintainers

### Review Process

- All PRs Require At Least One Approval
- Maintainers May Request Changes
- Once Approved, A Maintainer Will Merge The PR

---

## 📋 Issue Reporting

### Bug Reports

- Use The Bug Report Template
- Include Steps To Reproduce
- Provide System Information
- Attach Screenshots If Applicable

### Feature Requests

- Use The Feature Request Template
- Describe The Problem You're Trying To Solve
- Explain Why This Feature Would Be Useful

---

## 📜 License

By Contributing, You Agree That Your Contributions Will Be Licensed Under The Same License As The Original Project (MIT License).

---

<div align="center">
  <strong>Thank You For Contributing! 🎉</strong>
  <br />
  <em>Your Efforts Help Make ATS-Unified-API Better For Everyone</em>
</div>