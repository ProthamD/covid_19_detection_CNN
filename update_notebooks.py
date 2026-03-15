import json
import glob

notebooks = glob.glob('Notebooks/*.ipynb')

replacements = {
    'from tensorflow.keras.utils.np_utils import to_categorical': 'from tensorflow.keras.utils import to_categorical',
    'from tensorflow.keras_preprocessing import image': 'from tensorflow.keras.preprocessing import image',
    'from tensorflow.keras_preprocessing.image import ImageDataGenerator': 'from tensorflow.keras.preprocessing.image import ImageDataGenerator',
    '!unzip \\*.zip  && rm *.zip': '!unzip -q *.zip && rm *.zip'
}

for nb_path in notebooks:
    print(f"Updating {nb_path}...")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    modified = False
    for cell in nb.get('cells', []):
        if cell['cell_type'] == 'code':
            source = cell.get('source', [])
            for i, line in enumerate(source):
                for old_str, new_str in replacements.items():
                    if old_str in line:
                        source[i] = line.replace(old_str, new_str)
                        modified = True
                        
    if modified:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Saved changes to {nb_path}")
    else:
        print(f"No changes needed for {nb_path}")
