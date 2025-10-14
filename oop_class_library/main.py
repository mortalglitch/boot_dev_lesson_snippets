
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        keep_list = []
        for current_book in self.books:
            if current_book.title != book.title and current_book.author != book.author:
                keep_list.append(current_book)
        self.books = keep_list
                

    def search_books(self, search_string):
        match_list = []
        for current_book in self.books:
            book_title_breakdown = current_book.title.split()
            book_author_breakdown = current_book.author.split()
            combined_breakdown = book_title_breakdown + book_author_breakdown

            for word in combined_breakdown:
                if word.lower() == search_string.lower():
                    match_list.append(current_book)
            
        return(match_list)
