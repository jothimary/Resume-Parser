import json
from pyresparser import extract_text

def parse_resume(file_path):
    try:
        data = extract_text(file_path)
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python parseresume.py <resume_file>")
        sys.exit(1)

    resume_file = sys.argv[1]
    result = parse_resume(resume_file)
    print(result)
