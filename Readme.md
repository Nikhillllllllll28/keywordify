# 🔍 KeyWordify

KeyWordify is a simple, elegant web application built with Flask that extracts **single-word keywords** from research papers or articles using **RAKE (Rapid Automatic Keyword Extraction)** powered by **spaCy**.

![KeyWordify Screenshot](static\preview.png) <!-- Optional: Replace with your actual screenshot path -->

---

## 🚀 Features

- 📄 Paste full-text research articles or content
- 🧠 NLP-powered keyword extraction using `rake-spacy`
- 🌗 Dark & Light mode toggle
- 🎨 Clean, responsive UI with optional gradients
- 💡 Extracts **single-word** keywords only
- 📱 Mobile-friendly layout

---

## 🔧 Tech Stack

- **Python 3.10+**
- **Flask** – Web backend
- **spaCy** – NLP engine
- **rake-spacy** – Keyword extraction
- **HTML/CSS/JS** – Frontend UI

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/keywordify.git
cd keywordify
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
