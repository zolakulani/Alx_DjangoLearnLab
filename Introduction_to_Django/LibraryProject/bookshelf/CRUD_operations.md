```markdown
# CRUD Operations Summary

All operations performed in `python manage.py shell`.

| Operation | Command | Result |
|---------|--------|--------|
| Create | `Book.objects.create(title="1984", ...)` | `1984 by George Orwell (1949)` |
| Retrieve | `Book.objects.first()` | Returns book with title "1984" |
| Update | `book.title = "Nineteen Eighty-Four"; book.save()` | Title updated |
| Delete | `book.delete()` | Book removed, count = 0 |

Final Git Push