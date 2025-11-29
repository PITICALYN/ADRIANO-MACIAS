import re
import json
import sys

try:
    with open('google_form_full.html', 'r', encoding='utf-8') as f:
        html = f.read()

    match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);\s*<\/script>', html)

    if match:
        data = json.loads(match.group(1))
        questions = data[1][1]
        
        for q in questions:
            title = q[1]
            entry_id = q[4][0][0]
            options = q[4][0][1]
            
            print(f"Title: {title}")
            print(f"ID: {entry_id}")
            if options:
                print("Options:")
                for o in options:
                    print(f"  - \"{o[0]}\"")
            else:
                print("Type: Text/Other")
            print("---")
    else:
        print("Could not find FB_PUBLIC_LOAD_DATA_")

except Exception as e:
    print(f"Error: {e}")
