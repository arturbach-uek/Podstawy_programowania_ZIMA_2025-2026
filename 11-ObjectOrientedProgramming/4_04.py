class EBook():
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1
        self.is_open = False
    
    def open_book(self):
        self.is_open = True
    
    def close_book(self):
        self.is_open = False

    def next_page(self):
        if not self.is_open:
            print("Cannot turn page. The book is closed.")
            return
        if self.current_page < self.total_pages:
            self.current_page += 1
        else:
            print("You are already at the last page.")

    def previous_page(self):
        if not self.is_open:
            print("Cannot turn page. The book is closed.")
            return
        if self.current_page > 1:
            self.curr_page -= 1
        else:
            print("You are already at the first page.")
    
    def show_status(self):
        status = f"Title: {self.title}, Author: {self.author}, Pages: {self.total_pages}, "
        status += f"Current Page: {self.current_page}, {'Open' if self.is_open else 'Closed'}"
        return status

my_book = EBook("Python Programming", "John Doe", 250)
    
print(my_book.show_status())

my_book.open_book()
print(my_book.show_status())

for _ in range(5):
    my_book.next_page()
    print(my_book.show_status())

my_book.close_book()
print(my_book.show_status())

my_book.next_page()
print(my_book.show_status())
