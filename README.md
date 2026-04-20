# 🚨 GenAI Customer Churn Early-Warning System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange)
![Groq](https://img.shields.io/badge/Powered%20by-Groq%20LPUs-black)
![Llama 3](https://img.shields.io/badge/Model-Llama%203.1%208B-green)

## 📌 The Business Problem
Most SaaS companies only realize a customer is angry *after* they hit the cancellation button. By then, the revenue is already lost. 

This project solves that by acting as an **Event-Driven AI Routing Layer**. It analyzes unstructured customer support chat logs in real-time, calculates sentiment drift, and instantly flags high-churn risks so human retention specialists can intervene.

## 🏗️ Architecture & Tech Stack
* **Inference Engine:** Meta's `Llama-3.1-8B-Instant`.
* **Compute:** Deployed via **Groq API** (LPU architecture) for sub-second inference latency.
* **Prompt Engineering:** Implemented **Few-Shot Prompting** and strictly enforced JSON schema outputs to ensure the pipeline is programmatically parseable.
* **Frontend:** Wrapped in **Gradio** for immediate user testing.

## 📊 Rigorous Evaluation
Unlike standard GenAI prototypes, this system was mathematically evaluated against a human-labeled baseline dataset.
* **Metric Used:** [Cohen’s Kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa) (Inter-annotator agreement).
* **Result:** Achieved a **Kappa Score of 1.0 (100%)**, proving the prompt engineering is robust enough for production A/B testing without hallucinating risk levels.
* *(See `notebooks/01_model_evaluation.ipynb` for the evaluation pipeline).*

## 🚀 Try the Live Demo
You can interact with the live deployed model here: 
**[Insert your Hugging Face Spaces Link Here]**

---

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Tanmay-Hadke/customer-churn-prediction-genai.git](https://github.com/Tanmay-Hadke/customer-churn-prediction-genai.git)
   cd customer-churn-prediction-genai

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. ***Set up your Environment Variables:***
   #### Rename .env.example to .env.
   #### Add your free Groq API key: GROQ_API_KEY=your_key_here.
4. **Run the App:**
   ```bash
   python app.py   
   #### The Gradio app will launch locally at http://127.0.0.1:7860/

### Final Instructions:
1. Create a new repository on GitHub.
2. Download your Colab notebook as an `.ipynb` file and put it in a folder named `notebooks`.
3. Create the other files exactly as formatted above.
4. Push to GitHub.