# ✨ VaultIQ – AI-Powered Google Drive Search Assistant

VaultIQ Frontend is a modern Streamlit-based user interface that enables users to intelligently search and explore their Google Drive files using AI-powered natural language queries.

The application provides a clean chat-based experience where users can ask questions such as:

* "Find all PDFs related to finance"
* "Show recent documents"
* "Find presentations uploaded this month"
* "Search files containing budget reports"

The frontend communicates with the VaultIQ backend AI agent, which processes queries and retrieves relevant files from Google Drive.

---

## 🔗 Project Links

- 🌐 Frontend Demo: https://vaultiqfrontend-c6udvznwvjeym32qcqtudt.streamlit.app/
- 🎨 Frontend Repository: https://github.com/shaikakhila26/vaultIQ-frontend
- ⚙️ Backend Repository: https://github.com/shaikakhila26/vaultIQ-backend


## 🌟 Features

### 🤖 AI-Powered File Search

* Search Google Drive using natural language
* Semantic file discovery
* Context-aware query handling
* Conversational search experience

### 💬 Chat Interface

* Interactive chat-based UI
* Persistent chat history during session
* Quick action prompts
* Recent search tracking

### 📁 Google Drive Integration

* Connected Google Drive workspace
* Intelligent file retrieval
* Search across documents, PDFs, spreadsheets, and presentations
* Fast access to relevant files

### 🎨 Modern User Experience

* Responsive Streamlit interface
* Clean dashboard layout
* Gradient-based modern design
* Sidebar navigation
* User-friendly workflow

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* Python
* Requests
* HTML/CSS Styling

### Backend Communication

* FastAPI
* LangChain
* LangGraph
* Groq LLM
* Google Drive API
* REST APIs
---

## 📂 Project Structure

```text
vaultIQ_frontend/
│
├── app.py
├── requirements.txt
└── .devcontainer/
    └── devcontainer.json
```

---

## 🏗️ Architecture

```text
User Query
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
AI Agent (LangGraph + Groq LLM)
    ↓
Google Drive API
    ↓
Relevant Files Returned
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/shaikakhila26/vaultIQ-frontend.git

cd vaultIQ-frontend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
BACKEND_URL=https://vaultiq-backend-mluv.onrender.com
```

For local development:

```env
BACKEND_URL=http://localhost:8000
```

### 6. Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 🔗 Backend Integration

The frontend communicates with the VaultIQ backend for:

* Natural language query processing
* AI reasoning
* Google Drive search operations
* File retrieval and ranking
* Search result generation

Backend Repository:

https://github.com/shaikakhila26/vaultIQ-backend

---

## 🎯 Example Queries

Users can search using natural language:

```text
Find all PDFs in my drive
```

```text
Show recent documents
```

```text
Find financial reports from last month
```

```text
Search presentations related to AI
```

```text
Find spreadsheets containing sales data
```

---

## 🌟 Key Highlights

* AI-powered Google Drive search
* Conversational file discovery
* Streamlit-based responsive UI
* FastAPI backend integration
* Real-time search experience
* Modern and intuitive design

---
## 💡 What Makes VaultIQ Unique?

- Natural language search over Google Drive files
- AI-powered semantic file discovery
- Conversational search experience
- LangGraph-based agent workflow
- Real-time file retrieval and ranking
- Modern Streamlit interface
  
---

## 🚀 Future Enhancements

* File previews
* Advanced filtering options
* Search result categorization
* User authentication
* Multi-drive support
* Search analytics dashboard
* Dark mode support
* Export search results

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Shaik Akhila**

GitHub: https://github.com/shaikakhila26

LinkedIn: https://www.linkedin.com/in/akhila-shaik-8100b2344/

Email: [akhilashaik2605@gmail.com](mailto:akhilashaik2605@gmail.com)

---

⭐ If you found this project useful, consider giving it a star on GitHub.
