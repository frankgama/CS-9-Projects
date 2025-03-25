class Book:
    def __init__(self, title, author, year =None):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return self.title + 'by' + self.author

    def print(self):
        print(self.info())

    def print_details(self):
        print('This book in detail:')
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('Year: ', self.year)

book = Book('The Stand', 'Stephen King')

print(book.title)
print(book.author)

book2 = {
    'title': 'The Count of Monte Cristo',
    'author': 'Alexandre Dumas'
}

print(book2['title'])
print(book2['author'])

book.print()
book2.print

