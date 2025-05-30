import sqlite3
import datetime

def db_ddl_dml_operation(q):
    con= sqlite3.connect("lib_operations.db")
    con.execute(q)
    con.commit()
    con.close

def create_all_tables():
    con = sqlite3.connect("lib_operations.db")
    con.execute("""
            create table all_books
            (
                bnum number(7),
                btitle varchar(25),
                bauthor varchar(25),
                bpublication varchar(25)
            )
                """)
    con.execute("""
            create table all_stud
            (
                enr number(10),
                sname varchar(25),
                sclass varchar(15),
                semail varchar(30),
                smob number(20)
            )
                """)
    con.execute("""
            create table all_issued
            (
                senr number(10),
                bnum number(7),
                idate varchar(20),
                rdate varchar(20)
            )
                """)
    con.commit()
    con.close()
    print("All Tables Created..")

def get_date():
  a = datetime.date.today()
  cdate = str(a.day) + "-" + str(a.month) + "-" + str(a.year)
  return cdate


# 1 - Issue Book Done
def issue_book():
    e = input("Enter Enrollment Number : ")
    b = input("Enter Book Number : ")
    idate = get_date()
    qry = "insert into all_issued values({0}, {1}, '{2}', '{3}')".format(e,b,idate,"NR")

    db_ddl_dml_operation(qry)
    print("Book Issued...")
    print()


# 2 - Return Book Done
def return_book():
    b = input("Enter Book Number to return : ")
    rdate = get_date()

    qry = "update all_issued set rdate='{0}' where bnum={1} and rdate='NR'".format(rdate,b)
    db_ddl_dml_operation(qry)
    print("Book Returned...")
    print()


# 3 - View Not Returned Books
def view_not_ret_books():
    pass


# 4 - Add New Student Done
def add_new_stud():
    e = input("Enter Enrollment Number : ")
    n = input("Enter Student Name : ")
    email = input("Enter Student Email : ")
    mno = input("Enter Student Mobile Number : ")
    c = input("Enter Student Class : ")
    idate = get_date()
    qry = "insert into all_stud values({0}, '{1}', '{2}', '{3}', {4})".format(e,n,c,email,mno)

    db_ddl_dml_operation(qry)
    print("Book Issued...")
    print()


# 5 - Add New Book Done
def add_new_book():
    e = input("Enter Book Number: ")
    btitle = input("Enter Book Title: ")
    bauthor = input("Enter Author Name: ")
    bpublication = input("Enter Publisher Name: ")
    idate = get_date()
    qry = "insert into all_books values(?, ?, ?, ?)"
    params = (e, btitle, bauthor, bpublication)

    con = sqlite3.connect("lib_operations.db")
    cur = con.cursor()
    cur.execute(qry, params)
    con.commit()
    con.close()
    print("New Book Added...")
    print()


# 6 - Search Student Done
def search_stud():
    e = input("Enter Enrollment Number: ")
    con = sqlite3.connect("lib_operations.db")
    cur = con.cursor()
    qry = "select * from all_stud where enr = ?"
    cur.execute(qry, (e,))
    rows = cur.fetchall()
    con.close()
    if rows:
        print("Student Found...")
        for row in rows:
            print(row)
    else:
        print("Student Not Found...")
    print()


# 7 - Search Book Done
def search_book():
    btitle = input("Enter Book Name: ")
    bnum = input("Enter Book Number: ")
    con = sqlite3.connect("lib_operations.db")
    cur = con.cursor()
    qry = "select * from all_books where bnum = ? and btitle = ?"
    cur.execute(qry, (bnum, btitle))
    rows = cur.fetchall()
    con.close()
    if rows:
        print("****Book Is Present ******")
        print("|No |  | Book Name |\t| Author |\t   | Publication |")
        for row in rows:
            print("|",row[0]," |\t  | ",row[1],"| \t |",row[2],"| \t\t|",row[3]," |")
    else:
        print("*****Book Not Present******")
    print()
    

# 8 - View Student History Done
def stud_history():
    e = input("Enter Enrollment Number: ")
    
    con = sqlite3.connect("lib_operations.db")
    cursor = con.cursor()
    cursor.execute("SELECT sname, smob FROM all_stud WHERE enr = ?", (e,))
    result = cursor.fetchone()
    
    if result:
        snam, smob = result
        print("Enrollment no.:", e)
        print("Student Name:", snam)
        print("Mobile Number:", smob)
    else:
        print("No student found with Enrollment Number:", e)
    
    con.close()
    print()


# 9 - View Book History Done
def view_book_history():
    roll_no = input("Enter Roll No: ")
    try:
        con = sqlite3.connect("lib_operations.db")
        cur = con.cursor()
        qry = "SELECT * FROM all_issued WHERE senr = ? AND rdate = 'NR'"
        cur.execute(qry, (roll_no,))
        res = cur.fetchall()
        con.close()

        if not res:
            print("NO BOOKS TO RETURN")
        else:
            print("Books Not Returned")
            print("|Roll No|   |Book No|\t|Book Title|\t|Issue Date|\t\t|Returned Date|")
            for row in res:
                book_no = row[1]
                qry = "SELECT btitle FROM all_books WHERE bnum = ?"
                cur = con.cursor()
                cur.execute(qry, (book_no,))
                book_title = cur.fetchone()[0]
                con.close()
                print(f" |{row[0]}|\t  |{row[1]}|\t|{book_title}|\t|{row[2]}|    \t|{row[3]}|")
        return roll_no, bool(res)
    except sqlite3.Error as e:
        print(f"An error occurred: {senr}")
    except Exception as e:
        print(f"An unexpected error occurred: {senr}")
    print(input())


#create_all_tables()
while True:
    print("Select operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - View Not Returned Books")
    print("4 - Add New Student")
    print("5 - Add New Book")
    print("6 - Search Student")
    print("7 - Search Book")
    print("8 - View Student History")
    print("9 - View Book History")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))
    if ch==1: issue_book()
    elif ch==2: return_book()
    elif ch==3: view_not_ret_books()
    elif ch==4: add_new_stud()
    elif ch==5: add_new_book()
    elif ch==6: search_stud()
    elif ch==7: search_book()
    elif ch==8: stud_history()
    elif ch==9: view_book_history()
    elif ch==0: exit(0)