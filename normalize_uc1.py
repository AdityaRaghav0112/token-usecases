# This script will use normalizer.py to normalize uc1_verbose.py and save the result as uci_normalized.py
from normalizer import rename_variables

with open('uc1_verbose.py', 'r') as f:
    code = f.read()

normalized_code = rename_variables(code)

with open('uc1_normalized.py', 'w') as f:
    f.write(normalized_code)

print('Normalization complete. Output saved to uc1_normalized.py')
