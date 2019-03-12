# USER CLASS
class User(object):
    def __eq__(self, compare_to_user):
        return self.name == compare_to_user.name and self.email == compare_to_user.email

    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}
        print("User {} created with the email {}\n".format(self.name,
                                                         self.email))
    def __repr__(self):
        return "User {}, email: {}, books read: {}".format(self.name, self.email, len(self.books))

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "Email address updated to {}".format(self.email)

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        #print("_+_+_+_+_+_+_+_+_+_+_+_ IN User.get_average_rating")
        count = 0
        for rating in self.books.values():
            count += rating
        return count / len(self.books.values())
# BOOK CLASS
class Book():
    def __eq__(self, compare_to_book):
        return self.title == compare_to_book.title and self.isbn == compare_to_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        print("Book {} with ISBN {} created.\n".format(self.title,self.isbn))

    def __repr__(self):
        return (self.title)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_average_rating(self):
        #print("+++++++++++++++++++++Book.get_average_rating")
        average = 0
        for rating in self.ratings:
            average += rating
        return average / len(self.ratings)

    def set_isbn(self, new_isbn):
        self.isbn=new_isbn
        return print("{}'s ISBN has been update to {}\n".format(self.title,
                                                                 self.isbn))
    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
            #print("Rating of {} added to {}.".format(rating, self.title))
        elif rating == None:
            None
        else:
            print("Invalid Rating")

# FICTION SUBCLASS OF BOOK
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author=author

    def __repr__(self):
        return('{} by {}').format(self.title, self.author)

    def get_author(self):
        return self.author


# NON_FICTION SUBCLASS OF BOOK
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def __repr__(self):
        return "{}, a {} book on {}".format(self.title, self.level, self.subject)
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
class TomeRater():
    def __init__(self):
        self.users={}
        self.books={}
        #print("TomeRater created!")

    def create_book(self, title, isbn):
        newbook = Book(title, isbn)
        return newbook

    def create_novel(self, title, author, isbn):
        newFiction = Fiction(title, author, isbn)
        return newFiction

    def create_non_fiction(self, title, subject, level, isbn):
        newNon_Fiction = Non_Fiction(title, subject, level, isbn)
        return newNon_Fiction

    def add_book_to_user(self, book, email, rating=None):
        add_user = self.users.get(email, None)
        if add_user:
            add_user.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book, 0) + 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        #print("------------------IN TomeRater.print_catalog----------------")
        for key in self.books:
            print(key)
        #print(self.books)

    def print_users(self):
        #print("--------------------IN TomeRater.print_users----------------")
        for user in self.users:
            print(user)
        #print(self.users)

    def most_read_book(self):
        # print("TomeRater.most_read_book")
        mostread = None
        highestreadcount = 0
        for book in self.books:
            value = self.books.get(book)
            if value > highestreadcount:
                mostread = book
                highestreadcount = value
        print("The most read book is: {} with {} reads!".format(mostread, highestreadcount))

    def highest_rated_book(self):
        # print("TomeRater.highest_reated_book")
        best_book = None
        high_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > high_rating:
                high_rating = User.get_average_rating(self)
                best_book = book
        return best_book

    def most_positive_user(self):
        # print("TomeRater.most_positive_user")
        high_rating = 0
        username = None
        for user in self.users.values():
            if User.get_average_rating(self) > high_rating:
                high_rating = User.get_average_rating(self)
                username = user
        return username
