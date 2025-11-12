```markdown
# Retrieve Operation

```python
retrieved = Book.objects.first()
print(retrieved.title, retrieved.author, retrieved.publication_year)