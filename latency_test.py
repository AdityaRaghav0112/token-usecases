import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    print("Error: Real GEMINI_API_KEY not found in .env. Did you replace 'your_api_key_here'?")
    exit(1)

def test_code_snippet(filepath):
    with open(filepath, 'r') as f:
        code = f.read()
    
    prompt = f"Explain what this code does in 1-2 short sentences. Then suggest exactly one performance optimization.\n\nCode:\n{code}"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    start_time = time.time()
    try:
        response = requests.post(url, json=payload)
        end_time = time.time()
        
        latency = end_time - start_time
        
        if response.status_code == 200:
            data = response.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return latency, text.strip()
        else:
            return -1, f"API Error: {response.text}"
            
    except Exception as e:
        return -1, str(e)

files = [
    ("Python Verbose", "uc1_verbose.py"),
    ("Python Minified", "uc1_short.py"),
    ("JS Verbose", "uc2_verbose.js"),
    ("JS Minified", "uc2_short.js")
]

print("🚀 Starting LLM Latency & Comprehension Test...")
print("="*50)

for label, filename in files:
    print(f"\nTesting {label} ({filename})...")
    latency, response_text = test_code_snippet(filename)
    
    if latency != -1:
        print(f"⏱️  Latency: {latency:.2f} seconds")
        print(f"🤖 Gemini's Take:\n{response_text[:400]}...\n")
    else:
        print(f"❌ Error: {response_text}")

print("="*50)
print("Test Complete!")