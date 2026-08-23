class book:
    def __init__(self,book_name,author,copies):
        self.book_name=book_name
        self.author=author
        self.copies=copies
    def display_info(self):
        print(self.book_name)
        print(self.author)
class Member:
    def __init__(self, name, member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_book=[]
    def display_info(self):
        print(f"Member: {self.name} (ID: {self.member_id})")
        for i in self.borrowed_book:
            print(i.book_name)
            print(i.author)
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
    def add_member(self, member):
        self.members.append(member)        
    def issue_book(self, book_name, member_id):
        # step 1: search self.books for a book whose book_name matches
        book_found=0
        member_found=0
        for i in self.books:
            if (book_name==i.book_name):
                if (i.copies>0):
                    book_found=1
                    b=i
                break
        if (book_found==0):
            print('The book not found or not available')   
        # step 2: search self.members for a member whose member_id matches
        for i in self.members:
            if (member_id==i.member_id):
                member_found=1
                m=i
                break
        if (member_found==0):
            print("member id not found,please register")
        # step 3: if both found, append the book to member.borrowed_book
        if (book_found==1 and member_found==1):
            m.borrowed_book.append(b)
            b.copies-=1
            print('Book issued Successfully')
    def return_book(self,book_name,member_id):
        for i in self.members:
            if (member_id==i.member_id):
                for j in i.borrowed_book:
                    if (j.book_name==book_name):
                        j.copies+=1
                        print('book returned successfully')
                        i.borrowed_book.remove(j)
                        break
                break    
                  
b1=book('concepts of physics','hc verma',5)
b2=book('physics galaxy','ashish arora',8)
m1=Member('sai',1516)
l=Library()
l.add_book(b1)
l.add_book(b2)
l.add_member(m1)
print(b2.copies)
l.issue_book('physics galaxy',1516)
print(b2.copies)
l.return_book('physics galaxy',1516)
print(b2.copies)