import gradio as gr
from groq import Groq
import json
import os
from dotenv import load_dotenv

# Load environment variables for local testing
load_dotenv()

# Initialize Groq client
api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

def analyze_churn_risk(chat_log):
    if not api_key:
        return "Error: Missing API Key", "Please set GROQ_API_KEY in your .env file."
    if not chat_log.strip():
        return "Warning", "Please enter a customer message to analyze."

    system_prompt = """
    You are an expert Customer Success API. 
    Analyze customer support chat logs and determine the churn risk as "Low", "Medium", or "High".
    You must reply in valid JSON format with exactly two keys: "risk_level" and "reasoning".
    """
    
    user_prompt = f"""
    Examples:
    Chat: "How do I reset my password?"
    Output: {{"risk_level": "Low", "reasoning": "Standard technical query, no frustration shown."}}
    
    Chat: "I've been waiting for 3 days for a reply. This is unacceptable."
    Output: {{"risk_level": "Medium", "reasoning": "Customer is expressing frustration over wait times."}}
    
    Chat: "Cancel my subscription. Your product is a waste of money."
    Output: {{"risk_level": "High", "reasoning": "Explicit statement of cancellation and severe dissatisfaction."}}
    
    Now, analyze the following chat:
    Chat: "{chat_log}"
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.1, 
            response_format={"type": "json_object"} 
        )
        
        response_text = chat_completion.choices[0].message.content
        result = json.loads(response_text)
        
        risk = result.get('risk_level', 'Unknown')
        reasoning = result.get('reasoning', 'No reasoning provided')
        
        if risk == "High":
            risk_display = "🚨 HIGH RISK"
        elif risk == "Medium":
            risk_display = "⚠️ MEDIUM RISK"
        elif risk == "Low":
            risk_display = "✅ LOW RISK"
        else:
            risk_display = risk
            
        return risk_display, reasoning
        
    except Exception as e:
        return "Error", f"API or Parsing Failure: {str(e)}"

# Gradio UI Setup
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚨 Customer Churn Early-Warning System")
    gr.Markdown(
        "**Powered by Groq LPUs & Llama 3.1**\n\n"
        "This tool acts as an AI routing layer for customer support. "
        "It analyzes the sentiment and intent of an incoming customer message "
        "and instantly routes high-risk customers to retention specialists."
    )
    
    gr.HTML("<hr>")
    
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                lines=6, 
                label="Customer Support Message", 
                placeholder="e.g., I've been trying to get this to work for three days. If someone doesn't call me back today, I'm canceling."
            )
            analyze_btn = gr.Button("Analyze Risk Level", variant="primary")
        
        with gr.Column():
            risk_output = gr.Textbox(label="Predicted Risk Level", interactive=False)
            reasoning_output = gr.Textbox(label="AI Reasoning Engine", lines=4, interactive=False)
    
    analyze_btn.click(
        fn=analyze_churn_risk, 
        inputs=user_input, 
        outputs=[risk_output, reasoning_output]
    )

if __name__ == "__main__":
    demo.launch()