from book import Book

library = [
    Book("Малентький Принц", "Антуан Экзюпери"),
    Book("Соль земли", " Георгий Марков"),
    Book("Книга рецептов", "Супер Бабка"),
]

for i in library:
    print(f"{i.title} - {i.autor}")
