# ✍️ Handwritten to Digital Text Converter

Convert handwritten notes into **clean, editable digital text**.  
Built with **FastAPI**, **Tesseract OCR**, **OpenCV**, and a lightweight **HTML/JS frontend**.  

---

## 🚀 Features
- 📷 Upload handwritten images
- 🧹 Smart preprocessing (denoise + threshold) for better OCR
- 🔤 Offline OCR with Tesseract
- 📄 Export as **PDF**
- 💾 Export as **JSON**
- 📋 Copy text to **Clipboard**
- ⚡ Fast & lightweight (runs locally, no cloud required)

---

## 🎯 Why this project?
- Saves time digitizing notes
- Great for students, researchers, and professionals
- Showcases practical use of **AI + OCR** in real workflows
- Hackathon-friendly (runs on any machine with Python)

---

## 🛠️ Tech Stack
- **Backend:** FastAPI, Python, Tesseract OCR, OpenCV, Pillow  
- **Frontend:** HTML, CSS, JavaScript  
- **Export Tools:** jsPDF (for PDF), JSON, Clipboard API  

---

## 🖥️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/handwriting-to-text.git
   cd handwriting-to-text

---

### Run the backend
```bash
python -m uvicorn main:app --reload
