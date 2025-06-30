import os
import json

# Define the path to your content directory relative to the script
# Script is in .github/scripts/, so '..' goes to .github/, and '..' again goes to the repository root.
CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
INDEX_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'rapture_sermons_index.json')

def generate_rapture_sermon_index():
    index_data = []
    # List all .json files directly in the CONTENT_DIR (repository root) that start with 'rapture_sermon_'
    sermon_files = sorted([f for f in os.listdir(CONTENT_DIR) if f.startswith('rapture_sermon_') and f.endswith('.json')])

    for filename in sermon_files:
        filepath = os.path.join(CONTENT_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                article_data = json.load(f)

            # Extract only the metadata needed for the index
            metadata = {
                "id": article_data.get("id"),
                "type": article_data.get("type"),
                "title": article_data.get("title"),
                "thumbnailUrl": article_data.get("thumbnailUrl"),
                "page": article_data.get("page"),
                "category": article_data.get("category")
            }
            index_data.append(metadata)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

    # Write the compiled index to the rapture_sermons_index.json file
    try:
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        print(f"Successfully generated {INDEX_FILE} with {len(index_data)} entries.")
    except Exception as e:
        print(f"Error writing index file: {e}")

if __name__ == "__main__":
    generate_rapture_sermon_index()
