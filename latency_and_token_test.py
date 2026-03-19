import os
import time
from dotenv import load_dotenv
from google import genai
import tiktoken

# Load the API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
enc = tiktoken.get_encoding("cl100k_base")

def test_code_snippet(filepath):
    try:
        with open(filepath, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        return -1, -1, -1, "File not found."

    tokens = len(enc.encode(code))
    chars = len(code)
    
    prompt = f"Explain what this code does in 1-2 short sentences. Then suggest exactly one performance optimization. \n\nCode:\n{code}"
    
    start_time = time.time()
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        end_time = time.time()
        latency = end_time - start_time
        return tokens, chars, latency, response.text.strip()
    except Exception as e:
        # Fallback to 2.0 if 2.5 fails
        try:
            start_time = time.time()
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt,
            )
            end_time = time.time()
            latency = end_time - start_time
            return tokens, chars, latency, response.text.strip()
        except Exception as e2:
            return tokens, chars, -1, str(e2)

files = [
    ("Python Verbose", "uc1_verbose.py"),
    ("Python Normalized", "uc1_normalized.py")
]

print("🚀 Starting LLM Token & Latency Test...")
for label, filename in files:
    print(f"\nTesting {label} ({filename})...")
    tokens, chars, latency, response_text = test_code_snippet(filename)
    if tokens != -1:
        print(f"📏 Size: {tokens} tokens ({chars} chars)")
        if latency != -1:
            print(f"⏱️  Latency: {latency:.2f} seconds")
            print(f"🤖 Gemini's Take:\n{response_text}\n")
        else:
            print(f"❌ Error: {response_text}")
    else:
        print(f"❌ Error: {response_text}")
