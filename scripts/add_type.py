import json

# Load the books file
with open('books.txt', 'r', encoding='utf-8') as f:
    books = json.load(f)

# Add the 'type' field to each book
for book in books:
    book['type'] = 'sarvamoola'  # or 'other' for non-sarvamoola books

# Save to a new file
with open('books.txt', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=2)

print("Added 'type' field to all books.")