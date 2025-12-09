<h1 align="center"> A Unified API Solution for Applicant Tracking Systems (ATS) 💚</h1>

<p align="center">
  <strong>Transform Your Recruitment Process With A Powerful, Scalable Mock ATS API</strong>
  <br />
  <em>Built With ❤️ For Developers And HR Teams</em>
</p>

<p align="center">
  <a href="#-features">✨ Features</a> •
  <a href="#-installation">📦 Installation</a> •
  <a href="#-api-endpoints">📡 API Docs</a> •
  <a href="#-contributing">🤝 Contributing</a>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/ATS-Unified-API-🚀-brightgreen?style=for-the-badge" alt="ATS-Unified-API Logo" />
  <br />
  <img src="https://img.shields.io/github/stars/i8o8i-Developer/ATS-Unified-API?style=social" alt="GitHub Stars" />
  <img src="https://img.shields.io/github/forks/i8o8i-Developer/ATS-Unified-API?style=social" alt="GitHub Forks" />
  <img src="https://img.shields.io/github/issues/i8o8i-Developer/ATS-Unified-API?style=flat-square" alt="GitHub Issues" />
  <br />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT" />
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/Flask-2.0+-lightgrey.svg?style=flat-square" alt="Flask 2.0+" />
  <img src="https://img.shields.io/badge/AWS%20Lambda-Ready-orange.svg?style=flat-square" alt="AWS Lambda Ready" />
  <img src="https://img.shields.io/badge/RESTful-API-green.svg?style=flat-square" alt="RESTful API" />
</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Project Structure](#-project-structure)
- [🛠️ Technologies Used](#-technologies-used)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📡 API Endpoints](#-api-endpoints)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)
- [👥 Authors](#-authors)
- [📄 License](#-license)

---

## ✨ Features

<div align="center">
  <table>
    <tr>
      <td align="center">
        <h3>🔐 Secure & Scalable</h3>
        <p>RESTful API with Bearer Token Auth & CORS Support</p>
      </td>
      <td align="center">
        <h3>📊 Comprehensive Data Management</h3>
        <p>Jobs, Candidates, & Applications with Full CRUD Operations</p>
      </td>
      <td align="center">
        <h3>☁️ Cloud-Ready</h3>
        <p>Serverless Framework Integration for AWS Lambda</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <h3>🎯 Mock Data Included</h3>
        <p>Pre-populated Sample Data for Immediate Testing</p>
      </td>
      <td align="center">
        <h3>🖥️ Interactive Dashboard</h3>
        <p>Web-Based Testing Interface for Easy API Exploration</p>
      </td>
      <td align="center">
        <h3>🔧 Developer-Friendly</h3>
        <p>Simple Setup, Clear Documentation, & Extensible Code</p>
      </td>
    </tr>
  </table>
</div>

### 🌟 Key Highlights

- **RESTful API Design** 🏗️: Clean, Stateless Endpoints for Seamless Integration
- **Job Management** 💼: Create & Retrieve Job Postings with Status Tracking
- **Candidate Management** 👥: Handle Profiles with Contact Info & CVs
- **Application Tracking** 📋: Link Candidates to Jobs with Status Updates
- **Authentication** 🔒: Bearer Token-Based Security for API Access
- **CORS Support** 🌐: Cross-Origin Resource Sharing for Web Apps
- **Serverless Ready** ☁️: AWS Lambda Integration via Serverless Framework
- **Mock Data** 📁: Pre-Populated Samples for Instant Testing
- **Interactive Dashboard** 🎮: Web-Based Interface for API Exploration

---

## 🏗️ Project Structure

```
ATS-Unified-API/
├── 📁 Mock-ATS/                 # Flask-Based Mock Server 🐍
│   ├── Mock_Server.py        # Main Flask Application 🚀
│   ├── Jobs.json             # Job Postings Data 💼
│   ├── Candidates.json       # Candidate Profiles Data 👥
│   ├── Applications.json     # Application Records Data 📋
│   ├── Requirements.txt      # Python Dependencies 📦
│   └── dashboard.html        # Testing Dashboard 🎮
├── 📁 SVL-FRAMEWORK/            # Serverless Framework Integration ☁️
│   ├── handler.py            # Lambda Function Handler ⚡
│   └── serverless.yml        # Serverless Configuration 📄
├── 📁 Testing/                  # Testing Utilities 🧪
│   └── index.html            # Additional Testing Interface 🔍
├── README.md                 # Project Documentation 📖
└── LICENSE                   # MIT License 📜
```

---

## 🛠️ Technologies Used

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white" alt="AWS Lambda" />
  <img src="https://img.shields.io/badge/Serverless-000000?style=for-the-badge&logo=serverless&logoColor=white" alt="Serverless" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</div>

- **Backend** : Python 🐍, Flask 🌶️
- **Data Storage** : JSON Files 📄 (Easily Replaceable with Databases 🗄️)
- **Authentication** : Bearer Token 🔑
- **Deployment** : Serverless Framework ☁️, AWS Lambda ⚡
- **Testing** : HTML/JavaScript Dashboards 🎮
- **Version Control** : Git 📚

---

## 📦 Installation

### Prerequisites

- 🐍 Python 3.8 or higher
- 📦 pip (Python Package Manager)
- 🌐 Node.js & npm (For Serverless Deployment)

### Setup Steps

1. **Clone the Repository** 📥
   ```bash
   git clone https://github.com/i8o8i-Developer/ATS-Unified-API.git
   cd ATS-Unified-API
   ```

2. **Install Python Dependencies** 🛠️
   ```bash
   cd Mock-ATS
   pip install -r Requirements.txt
   ```

3. **Install Serverless Framework (Optional)** ☁️
   ```bash
   npm install -g serverless
   npm install serverless-offline --save-dev
   ```

> 🎉 **Done!** Your ATS API Is Ready To Run.

---

## 🚀 Usage

### Running the Mock Server

1. **Navigate to the Mock-ATS Directory** 📂:
   ```bash
   cd Mock-ATS
   ```

2. **Start the Flask Server** ▶️:
   ```bash
   python Mock_Server.py
   ```

3. **API Available At** 🌐: `http://localhost:5000`

### API Authentication

Include the Bearer Token in Your Request Headers 🔐:
```
Authorization: Bearer Dummy_Key_1608
```

### Testing the API

- 🎮 Open `dashboard.html` in Your Browser for Interactive Testing
- 🛠️ Use Tools Like Postman, Insomnia, or Curl

---

## 📡 API Endpoints

<div align="center">
  <table>
    <thead>
      <tr>
        <th>Method</th>
        <th>Endpoint</th>
        <th>Description</th>
        <th>Auth Required</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>GET</code></td>
        <td><code>/offers</code></td>
        <td>Retrieve Job Postings (Paginated) 💼</td>
        <td>✅</td>
      </tr>
      <tr>
        <td><code>POST</code></td>
        <td><code>/candidates</code></td>
        <td>Create a New Candidate Profile 👤</td>
        <td>✅</td>
      </tr>
      <tr>
        <td><code>GET</code></td>
        <td><code>/candidates</code></td>
        <td>Retrieve Candidate Profiles (Paginated) 👥</td>
        <td>✅</td>
      </tr>
      <tr>
        <td><code>POST</code></td>
        <td><code>/applications</code></td>
        <td>Create a New Job Application 📝</td>
        <td>✅</td>
      </tr>
      <tr>
        <td><code>GET</code></td>
        <td><code>/applications</code></td>
        <td>Retrieve Applications (Filtered by Job_ID) 📋</td>
        <td>✅</td>
      </tr>
    </tbody>
  </table>
</div>

### Sample API Usage

**Get Job Offers** 🔍:
```bash
curl -H "Authorization: Bearer Dummy_Key_1608" http://localhost:5000/offers?page=1&per_page=5
```

**Create a Candidate** ➕:
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer Dummy_Key_1608" \
  -d '{"first_name":"John","last_name":"Doe","emails":[{"value":"john@example.com","type":"work"}]}' \
  http://localhost:5000/candidates
```

---

## 🧪 Testing

- **Interactive Dashboard** 🎮: Open `Mock-ATS/dashboard.html` in Your Browser
- **Additional Testing** 🔍: Check `Testing/index.html` for Extended Scenarios
- **API Testing Tools** 🛠️: Postman, Insomnia, or Curl Commands

---

## 🤝 Contributing

We Welcome Contributions! 🎉 Please Follow These Steps:

1. **Fork the Repository** 🍴
2. **Create a Feature Branch** 🌿: `git checkout -b feature/AmazingFeature`
3. **Commit Your Changes** 💾: `git commit -m 'Add Some AmazingFeature'`
4. **Push to the Branch** ⬆️: `git push origin feature/AmazingFeature`
5. **Open a Pull Request** 📬

See [CONTRIBUTING.md](CONTRIBUTING.md) for Detailed Guidelines.

---

## 👥 Authors

<div align="center">
  <a href="https://github.com/i8o8i-Developer">
    <img src="https://img.shields.io/badge/Maintainer-i8o8i-Developer-blue?style=for-the-badge&logo=github" alt="Maintainer" />
  </a>
  <br />
  <p><strong>Built With ❤️ By The ATS-Unified-API Individual</strong></p>
</div>

---

## 📄 License

This Project Is Licensed Under The MIT License 📜 - See The [LICENSE](LICENSE) File For Details.

---

<div align="center">
  <h3>⭐ Star This Repo If You Found It Helpful! ⭐</h3>
  <p>
    <a href="https://github.com/i8o8i-Developer/ATS-Unified-API">GitHub</a> •
    <a href="https://twitter.com/your-handle">Twitter</a> •
    <a href="https://linkedin.com/in/your-profile">LinkedIn</a>
  </p>
  <p><em>Made with ❤️ for Efficient Recruitment Processes</em></p>
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Built with Love" />
</div>