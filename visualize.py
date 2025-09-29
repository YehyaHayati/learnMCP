from graph_rag_example_helpers.datasets.animals import fetch_documents

for item in fetch_documents():
    print(item, end = "\n\n") 