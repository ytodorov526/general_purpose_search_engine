import json
from elasticsearch import Elasticsearch

# Point this to your local Elasticsearch instance once it's running
es = Elasticsearch("http://localhost:9200")

def index_pages(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        pages = json.load(f)

    for i, page in enumerate(pages):
        # Just an example index name "pages"
        es.index(index="pages", document=page)

if __name__ == "__main__":
    # For testing, read data from a sample file
    # In practice, you'd pass crawler output (like output.json)
    sample_file = "sample_output.json"
    # Create a small JSON file with something like: [{"title": "Test Title"}]
    index_pages(sample_file)
    print("Indexing complete!")

