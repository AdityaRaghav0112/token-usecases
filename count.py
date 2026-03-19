
import tiktoken
import glob

enc = tiktoken.get_encoding("cl100k_base")

for file in sorted(glob.glob("uc*")):
    with open(file, 'r') as f:
        text = f.read()
        tokens = enc.encode(text)
        print(f"{file}: {len(tokens)} tokens ({len(text)} chars)")
