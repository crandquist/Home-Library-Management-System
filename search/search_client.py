from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Adjust the number of 'parent' calls based on your project structure

def make_microservice_request(author, title):
    input_file_path = BASE_DIR / 'input.json'
    output_file_path = BASE_DIR / 'output.json'

    try:
        with open(input_file_path, 'w') as input_file:
            json.dump({"author": author, "title": title}, input_file, indent=4)
        
        # Read the results from output.json
        with open(output_file_path, 'r') as output_file:
            results = json.load(output_file)

        # Clear both input and output files after displaying results
        with open(input_file_path, 'w') as input_file, open(output_file_path, 'w') as output_file:
            json.dump({}, input_file, indent=4)
            json.dump({}, output_file, indent=4)

        if not results:
            return {"error": "No results found."}

        return results
    except FileNotFoundError:
        return {"error": "File not found."}
