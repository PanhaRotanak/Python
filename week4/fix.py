import json

with open('Messy E-Commerce Customer Database Rescue.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        # Clear outputs
        cell['outputs'] = []
        cell['execution_count'] = None
        
        # Modify source
        source = cell['source']
        for i, line in enumerate(source):
            if "if df['price'].dtype == 'O':" in line:
                source[i] = line.replace("if df['price'].dtype == 'O':", "if hasattr(df['price'], 'str'):")
            elif "if df['customer name'].dtype == 'O':" in line:
                source[i] = line.replace("if df['customer name'].dtype == 'O':", "if hasattr(df['customer name'], 'str'):")
            elif "if df['email'].dtype == 'O':" in line:
                source[i] = line.replace("if df['email'].dtype == 'O':", "if hasattr(df['email'], 'str'):")

with open('Messy E-Commerce Customer Database Rescue.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
