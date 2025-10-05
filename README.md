# 📊 Stack Overflow Dashboard  
### Dynamic Analysis of Stack Overflow Question Trends  

---

### 🏷️ Badges & Status  
| Badge | Status |
|-------|---------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) |
| **Framework** | ![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey) |
| **Deployment** | ![Render](https://img.shields.io/badge/Render-Deployed-success) |
| **Status** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) |

---

## 📝 Description  
This project is a **modern, interactive web dashboard** built with **Flask** and **Python** to visualize **trends in technology tags** from Stack Overflow questions.  

It processes historical data from a local CSV file, calculates the **relative popularity of major tags over time**, and presents the results through a **responsive web interface** (HTML + Chart.js visualizations).  

The application is lightweight, modular, and pre-configured for easy deployment.  

---

## ✨ Features  
✅ **Data Processing** – Reads question data from `stackoverflow_questions.csv`.  
✅ **Trend Analysis** – Calculates and visualizes yearly tag popularity trends.  
✅ **API Endpoint** – Provides JSON data at `/api/data` for frontend visualizations.  
✅ **Dynamic Web Interface** – Interactive dashboard served via `/` using Flask templates.  

---

## 🛠️ Tech Stack  
**Backend Framework:** Flask (v2.3.3)  
**Web Server:** Gunicorn (v21.2.0)  
**Data Analysis:** Pandas (v2.2.1), NumPy (v1.26.4)  
**CORS Handling:** Flask-Cors (v4.0.0)  

---

## 🚀 Getting Started  

### Prerequisites  
Make sure **Python 3.8+** is installed on your system.  

### Installation  

```bash
# Clone the repository
git clone https://github.com/YourUsername/your-project-name.git
cd your-project-name

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # For macOS/Linux
.env\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt
```

### Running Locally  
Ensure your virtual environment is active, then run:  

```bash
python app.py
```

The app will start on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).  

---

## ⚙️ Deployment  

This project includes a `render.yaml` file for **automatic deployment on Render**.

### Steps to Deploy on Render  
1. Sign up or log in at [Render](https://render.com).  
2. Connect your GitHub repository.  
3. Render will auto-detect the `render.yaml` blueprint.  
4. Confirm the following configuration:  

| Setting | Value |
|----------|--------|
| **Service Type** | web |
| **Name** | stackoverflow-dashboard |
| **Environment** | python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

The environment variable `FLASK_ENV` is automatically set to **production**.  

---

## 📂 Data Source  

The dashboard uses the local CSV file:  
**`stackoverflow_questions.csv`**

**Required Columns:**  
- `Question Number`  
- `Tag`  
- `Upload Time`  

🧠 *If the CSV is missing, the app auto-generates sample data for testing purposes.*

---

## 🧾 License  
This project is open-source and available under the [MIT License](LICENSE).  

---

## 💡 Author  
**Developed by:** [Your Name](https://github.com/YourUsername)  
📧 *Feel free to fork, star ⭐, and contribute!*
