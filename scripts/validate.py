import json
import os
import sys

FILES = [
    'data/kerata_basa.json',
    'data/sanepa.json',
    'data/paribasan.json',
    'data/neptu.json'
]

def check_duplicates(data, filename, key_field):
    seen = set()
    errors = []
    for item in data:
        value = item.get(key_field)
        if not value:
            errors.append(f"Missing '{key_field}' in {filename}")
            continue
        
        # Normalize for check (lowercase)
        norm_value = str(value).lower().strip()
        if norm_value in seen:
            errors.append(f"Duplicate entry found in {filename}: '{value}'")
        seen.add(norm_value)
    return errors

def main():
    has_error = False
    
    for file_path in FILES:
        if not os.path.exists(file_path):
            print(f"⚠️  File missing: {file_path}")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            print(f"✅ JSON Syntax OK: {file_path}")
            
            # Specific checks based on file type
            if 'kerata_basa' in file_path:
                errs = check_duplicates(data, file_path, 'word')
            elif 'sanepa' in file_path:
                errs = check_duplicates(data, file_path, 'phrase')
            elif 'paribasan' in file_path:
                errs = check_duplicates(data, file_path, 'proverb')
            
            if errs:
                has_error = True
                for e in errs:
                    print(f"❌ {e}")

        except json.JSONDecodeError as e:
            print(f"❌ JSON Syntax Error in {file_path}: {e}")
            has_error = True
            
    if has_error:
        sys.exit(1)
    else:
        print("🎉 All data valid.")

if __name__ == "__main__":
    main()