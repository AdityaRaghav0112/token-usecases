import tiktoken
import sys
import glob

enc = tiktoken.get_encoding("cl100k_base") # standard for modern OpenAI models

for file in sorted(glob.glob("uc*")):
    with open(file, 'r') as f:
        text = f.read()
        tokens = enc.encode(text)
        print(f"{file}: {len(tokens)} tokens ({len(text)} chars)")
