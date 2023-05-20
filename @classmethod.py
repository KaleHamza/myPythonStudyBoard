Class Book:
  TYPES = {"hardcover", "paperback"}
  
  def __init__(self, name, book_type, weight):
      self.name = name
      self.book_type = book_type
      self.weight = weight
      
  def __repr__(self):
      return f"<Book {self.name}, {self.book_type}, {self.weight}>"
    
  @classmethod
  def hardcover(cls, name, page_weight):
    return Book(name, Book.TYPES[0], page_weight +100)
  
  @classmethod
  def paperback(cls, name, page_weight):
    return Book(name, Book.TYPES[1], page_weight)
  
book = Book.hardcover("Python", 1000)
light = Book.paperback("Nexus", 300)

print(book)
print(light)
