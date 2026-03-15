import json
import glob
import ast

notebooks = glob.glob('Notebooks/*.ipynb')

for nb_path in notebooks:
    print(f"--- Analyzing {nb_path} ---")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for i, cell in enumerate(nb.get('cells', [])):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            
            # Check for drive links
            if 'drive' in source.lower() or 'colab' in source.lower():
                print(f"Cell {i} has drive/colab link:")
                print(source)
                print("-" * 20)
                
            # Check syntax, stripping magics
            clean_source = "\n".join([line for line in source.split('\n') if not line.strip().startswith('!') and not line.strip().startswith('%')])
            try:
                ast.parse(clean_source)
            except SyntaxError as e:
                print(f"Cell {i} Syntax Error: {e}")
                print(f"Source:\n{clean_source}")
                print("-" * 20)
