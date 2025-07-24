class Book:
    def __init__(self, title, author):
        self.title = title
        self.author =author
        self.is_borrowed = False


    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Not Borrowed"
        return f'{self.title} by {self.author}-{status}'


class Library:
    def __init__(self):
        self.books = []


    def add_book(self, title,author):
        book = Book(title, author)
        self.books.append(book)
        print(f"{title} has been added to the library")


    def borrow_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f'{title} has been borrowed')
                else:
                    book.is_borrowed = True
                    print(f'You just borrowed {title}')
                return
        print(f'{title} cannot be found')


    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f'You just returned {book.title}')
                else:
                    print(f'The book {book.title} was not borrowed')


    def view_books(self):
        if not self.books:
            print(f'There are no books available')
        else:
            print('===Library Books===')
            for book in self.books:
                print(book)


def main():

        library = Library()

        while True:
            print('===Welcome To The Library===')
            print("1) Add books")
            print("2) Borrow book")
            print("3) Return books")
            print("4) View books")
            print("5) Exit Library")

            choice = input('Make a choice: ')

            if choice == '1':
                title = input('Enter title of the book ')
                author = input('Enter author of the book ')
                library.add_book(title, author)
            elif choice == '2':
                library.view_books()
                title = input('Enter title of the book ')
                library.borrow_book(title)
            elif choice == '3':
                title = input('Enter title of the book ')
                library.return_book(title)
            elif choice == '4':
                library.view_books()
            elif choice == '5':
                print('Thanks for visiting the library')
                break
            else:
                print('❌ Please make a choice between (1-5)')



if __name__ == "__main__":
        main()