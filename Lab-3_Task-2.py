class Library:
    def __init__(self):
        self.fiction = set()
        self.non_fiction = set()
        self.science = set()
        self.history = set()

    def add_book(self, genre, book):
        if genre == "Fiction":
            self.fiction.add(book)
        elif genre == "Non-Fiction":
            self.non_fiction.add(book)
        elif genre == "Science":
            self.science.add(book)
        elif genre == "History":
            self.history.add(book)
        else:
            print("Invalid genre")

    def remove_book(self, genre, book):
        if genre == "Fiction" and book in self.fiction:
            self.fiction.remove(book)
        elif genre == "Non-Fiction" and book in self.non_fiction:
            self.non_fiction.remove(book)
        elif genre == "Science" and book in self.science:
            self.science.remove(book)
        elif genre == "History" and book in self.history:
            self.history.remove(book)
        else:
            print("Books are not found in specified genre")

    def check_book(self, genre, book):
        if genre == "Fiction":
            return book in self.fiction
        elif genre == "Non-Fiction":
            return book in self.non_fiction
        elif genre == "Science":
            return book in self.science
        elif genre == "History":
            return book in self.history
        else:
            print("Invalid genre...")
            return False

    def union_books(self, genre1, genre2):
        return self.get_genre(genre1) | self.get_genre(genre2)

    def intersection_books(self, genre1, genre2):
        return self.get_genre(genre1) & self.get_genre(genre2)

    def difference_books(self, genre1, genre2):
        return self.get_genre(genre1) - self.get_genre(genre2)

    def get_genre(self, genre):
        if genre == "Fiction":
            return self.fiction
        elif genre == "Non-Fiction":
            return self.non_fiction
        elif genre == "Science":
            return self.science
        elif genre == "History":
            return self.history
        else:
            print("Invalid genre")
            return set()

library = Library()
library.add_book("Fiction", "Kamil")
library.add_book("Science", "Biology")
library.add_book("Science", "Chemistry")
library.add_book("Fiction", "Aamil")

print(library.union_books("Fiction", "Science"))
print(library.intersection_books("Science", "Fiction"))
print(library.difference_books("Science", "Fiction"))




