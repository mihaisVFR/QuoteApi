from author import Author
from schema import AuthorSchema


authors = [
   Author("1", "Alex"),
   Author("1", "Ivan"),
   Author("1", "Tom")
]
author = Author(1, "Alex", "alex5@mail.ru")
author_schema = AuthorSchema()
result = author_schema.dump(authors, many=True)
print(result)
