import mysql.connector as a
from tabulate import tabulate
con = a.connect(host="localhost", user="root", passwd="0426", database="library")

def usershistory():

    print('''                       Enter Your Choice  
     
                1. To search user History of Particular user
                
                2. To Display All The User History
                
                3. Go Back
                ''')
    lmao = input("Enter Your Choice : ")
    if lmao == "1":
        uiid=int(input("Enter The User ID to Acess Its History: "))
        dataaa=(uiid,)
        com = "select * from details where UserIDS = %s"
        c = con.cursor(buffered=True)
        c.execute(com, dataaa)
        con.commit()
        extract = c.fetchall()
        lst = []
        for i in extract:
            lst.append(i)
        print(tabulate(lst, headers=["Book Name", "User Name", "UserID", "Book Code", "Issue Date", "Submit Date"], tablefmt = "fancy_grid"))
        print('''

        ----------------------------------------------------------

                                ''')
        usershistory()


    elif lmao == "2":
        b = con.cursor()
        b.execute("select * from details ")
        myresult = b.fetchall()
        lst=[]
        for i in myresult:
            lst.append(i)
        print(tabulate(lst,headers=["Book Name", "User Name", "UserID","Book Code", "Issue Date", "Submit Date"],  tablefmt = "fancy_grid"))
        print('''

        ----------------------------------------------------------

                                ''')
        usershistory()
    elif lmao == "3":
        admain()
    else:
        print("Enter Correct Choice")
        print('''

        ----------------------------------------------------------

                                ''')
        usershistory()

def userdetails():
    print('''                       Enter Your Choice  

                    1. To Display User Details of Particular user

                    2. To Display All The User History

                    3. Go Back
                    ''')
    fk = input("Enter Your Choice : ")
    if fk == "1":
        uiiid = int(input("Enter The User ID to Acess Its Details: "))
        dataaa = (uiiid,)
        com = "select uid, Name, phone_no from users where uid = %s"
        c = con.cursor(buffered=True)
        c.execute(com, dataaa)
        con.commit()
        extract = c.fetchall()
        lst = []
        for i in extract:
            lst.append(i)
        print(tabulate(lst, headers=["User ID", "Name", "Phone Number"],
                       tablefmt="fancy_grid"))
        print('''

        ----------------------------------------------------------

                                ''')
        userdetails()
    elif fk == "2":
        b = con.cursor()
        b.execute("select uid, Name, phone_no from users")
        myresult = b.fetchall()
        lst=[]
        for i in myresult:
            lst.append(i)
        print(tabulate(lst, headers=["User ID", "Name", "Phone Number"],  tablefmt = "fancy_grid"))
        print('''

        ----------------------------------------------------------

                                ''')
        userdetails()
    elif fk == "3":
        admain()
    else:
        print("Enter Correct Choice")
        print('''

        ----------------------------------------------------------

                                ''')
        userdetails()

def pendingsubmits():
    print('''                       Enter Your Choice  

                        1. To Display Pending Submits from a Particular user

                        2. To Display All The Pending Submits

                        3. Go Back
                        ''')
    fkk = input("Enter Your Choice : ")
    if fkk == "1":
        uiiid = int(input("Enter The User ID to Acess Pending Submits: "))
        dataaa = (uiiid,)
        com = "select * from issue where UserID = %s"
        c = con.cursor(buffered=True)
        c.execute(com, dataaa)
        con.commit()
        extract = c.fetchall()
        if not extract:
            print('''No Pending Submition Found From This User
            ******---------------------------------********''')
            pendingsubmits()
        else:
            lst = []
            for i in extract:
                lst.append(i)
            print(tabulate(lst, headers=["Name Of Book", "UserID", "User Name", "Book Code", "Issue Date"], tablefmt  ="fancy_grid" ))
            pendingsubmits()
    elif fkk == "2":
        b = con.cursor()
        b.execute("select * from issue")
        myresult = b.fetchall()
        lst = []
        for i in myresult:
            lst.append(i)
        print(tabulate(lst, headers=["Name Of Book", "UserID", "User Name", "Book Code", "Issue Date"], tablefmt="fancy_grid"))
        print('''
        ***************-------------------------************
        ''')
        pendingsubmits()
    elif fkk == "3":
        admain()
    else:
        print("Enter Correct Choice")
        print('''
        
--------------***************-------------------------************

                ''')

        userdetails()



def search():
    print('''
    
    Choose Your Number According To The Way You Want To Explore 
    
             1.Search Book By Its Name.
             2.Search Book By Authors.
             3.Search Book By Subject.
             4.Go Back
    
    ''')
    ta = int(input("Enter Your Choice: "))
    if ta == 1:
        Nm = input("Enter The Book Name: ")
        datas=(Nm,)
        sql = "select * from book_info where Book_Name REGEXP %s"
        c = con.cursor(buffered=True)
        c.execute(sql, datas)
        con.commit()
        show = c.fetchall()
        #print(show)
        if show:
            lst = []
            for i in show:
                lst.append(i)
            print(tabulate(lst, headers=["Book Name", "Author Name", "Book Code", "Total Books", "Subject"],
                           tablefmt="fancy_grid"))
            Inpu = input("Enter Y to Issue A Book: ")
            if Inpu.upper() == "Y":
                issuebook()
            else:
                main()
        else:
            print('''
-------------------------------------------------------------------------
            No Books Found 
-------------------------------------------------------------------------''')
            search()
    elif ta == 2:
        Nm = input("Enter Author Name: ")
        datas = (Nm,)
        sql = "select * from book_info where Author_Name REGEXP %s"
        c = con.cursor(buffered=True)
        c.execute(sql, datas)
        con.commit()
        show = c.fetchall()
        if show:
            lst = []
            for i in show:
                lst.append(i)
            print(tabulate(lst, headers=["Book Name", "Author Name", "Book Code", "Total Books", "Subject"],
                           tablefmt="fancy_grid"))
            Inpu = input("Enter Y to Issue A Book: ")
            if Inpu.upper() == "Y":
                issuebook()
            else:
                main()
        else:
            print('''
            -------------------------------------------------------------------------
                        No Books Found 
            -------------------------------------------------------------------------''')
            search()


    elif ta == 3:
        Nm = input("Enter Subject: ")
        datas = (Nm,)
        sql = "select * from book_info where Subject REGEXP %s"
        asmit = con.cursor(buffered=True)
        asmit.execute(sql, datas)
        con.commit()
        show = asmit.fetchall()
        if show:
            lst = []
            for i in show:
                lst.append(i)
            print(tabulate(lst, headers=["Book Name", "Author Name", "Book Code", "Total Books", "Subject"],
                           tablefmt="fancy_grid"))
            Inpu = input("Enter Y to Issue A Book: ")
            if Inpu.upper() == "Y":
                issuebook()
            else:
                main()
        else:
            print('''
                        -------------------------------------------------------------------------
                                    No Books Found 
                        -------------------------------------------------------------------------''')
            search()

    elif ta == 4:
        main()
    else:
        print("Please Enter Right Choice")
        search()

def addbook():
    bn = input("Enter Book Name:")
    code = input("Enter Book Code:")
    au= input("Enter Author Name:")
    t = input("Total Books")
    s = input("Enter Subject:")
    data = (bn, au, code, t, s)
    sql = "insert into book_info values (%s, %s, %s, %s, %s)"
    c = con.cursor(buffered=True)
    c.execute(sql, data)
    con.commit()
    print("Following Data Entered successfully")
    tech=(code,)
    ccm = "select * from book_info where Book_Code=%s"
    q = con.cursor(buffered=True)
    q.execute(ccm, tech)
    myresult = q.fetchall()
    lst = []
    for i in myresult:
        lst.append(i)
    print(tabulate(lst, headers=["Book Name", "Author Name", "Book Code", "Total Books", "Subject"],
                   tablefmt="fancy_grid"))
    admain()

def issuebook():
    r = ext[0][0]
    xd = ext[0][2]
    co = input("Enter Book Code:")
    d = input("Enter Date:")
    data2 = (co,)
    cm = "select UserID from issue where bcode = %s AND UserID = %s"
    update = (co, r)
    c = con.cursor(buffered=True)
    c.execute(cm, update)
    con.commit()
    oj = c.fetchall()

    if oj:
        print("You cannot borrow multiple books of same type")
        main()
    else:
        cm = "select Book_Name from book_info where Book_Code= %s"
        c = con.cursor(buffered=True)
        c.execute(cm, data2)
        con.commit()
        data3 = c.fetchall()
        if data3:
            nm = data3[0][0]
            data = (nm, r, xd, co, d)
            a = "insert into issue values (%s, %s, %s, %s, %s)"
            c = con.cursor(buffered=True)
            c.execute(a, data)
            con.commit()
            print("Book Issued to:", xd)
            bookup(co, -1)
        else:
            print("No Books Found Associated With The Book Code")
            print('''

            ----------------------------------------------------------

                                    ''')
            main()

def submitb():
    r = ext[0][0]
    xd = ext[0][2]
    co = input("Enter Book Code:")
    d = input("Enter Date:")
    data2 = (co,)
    cm = "select UserID from issue where bcode = %s AND UserID = %s"
    updat = (co, r)
    c = con.cursor(buffered=True)
    c.execute(cm, updat)
    con.commit()
    ok = c.fetchall()
    if ok:
        cm = "select Book_Name from book_info where Book_Code= %s"
        c = con.cursor(buffered=True)
        c.execute(cm, data2)
        con.commit()
        data3 = c.fetchall()
        nm = data3[0][0]
        data = (nm, r, xd, co, d)
        date3 = "select issue_date from issue where bcode = %s "
        c = con.cursor(buffered=True)
        c.execute(date3, data2)
        con.commit()
        fetch=c.fetchall()
        fetch1 = fetch[0][0]
        datanew = (nm, xd, r, co, fetch1, d)
        #print(datanew)
        new = "insert into details values (%s, %s, %s, %s, %s, %s)"
        c = con.cursor(buffered=True)
        c.execute(new, datanew)
        con.commit()
        an = "DELETE FROM issue WHERE bcode = %s AND UserID = %s"
        c = con.cursor(buffered=True)
        set=(co, r)
        c.execute(an, set)
        con.commit()
        print("Book Submitted from:", xd)
        bookup(co, 1)

    else:
        print("Sorry You Have Not Borrowed This Book Or You Have Entered Invalid Book Code")
        main()

def bookup(co, u):
    a = "select Total from book_info where Book_Code = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    t = int(myresult[0]) + u
    sql = "update book_info set Total = %s where Book_Code = %s"
    d = (t, co)
    c.execute(sql,d)
    if lol == 1:
        admain()
    else:
        main()

def dbook():
    ac = input("Enter Book Code:")
    data = (ac,)
    a = "delete from book_info where Book_Code = %s"
    g = "select Book_Name from book_info where Book_Code = %s"
    d = con.cursor(buffered=True)
    d.execute(g, data)
    info = d.fetchall()
    if info:
        c = con.cursor(buffered=True)
        c.execute(a, data)
        con.commit()
        print(info[0][0], "Book Deleted Successfully")
        admain()
    else:
        print("No Book Found With This Book Code")
        print('''

----------------------------------------------------------

                        ''')
        admain()



def dispbook():
    b = con.cursor()
    b.execute("select * from book_info")
    myresult = b.fetchall()
    lst = []
    for i in myresult:
        lst.append(i)
    print(tabulate(lst, headers=["Book Name", "Author Name", "Book Code", "Total Books", "Subject"], tablefmt = "fancy_grid"))
    if lol == 1:
        admain()
    else:
        main()

def main():
    print('''                            
                                LIBRARY MANAGER 
    1. DISPLAY BOOKS 
    2. ISSUE BOOKS 
    3. SUBMIT BOOKS 
    4. SEARCH BOOKS
    5. TO GO BACK
    ''')

    choice =input("Enter Your Choice: ")
    if (choice == "1"):
        dispbook()
    elif (choice == "2"):
        issuebook()
    elif (choice == "3"):
        submitb()
    elif (choice == "4"):
        search()
    elif (choice == "5"):
        pswd()
    else:
        print("Wrong Choice Please Check Your Input !!")
        main()

AdminDetails = ["Admindms", "rajeshasmit" ]

def admain():
    print('''                            
                                    ADMIN PANEL 
        1. USERS HISTORY
        2. USER DETAILS
        3. PENDING SUBMITS
        4. DELETE BOOKS  
        5. ADD BOOKS
        6. TO GO BACK
        ''')

    choice = input("Enter Your Choice: ")
    if (choice == "1"):
        usershistory()
    elif (choice == "2"):
        userdetails()
    elif (choice == "3"):
        pendingsubmits()
    elif(choice == "4"):
        dbook()
    elif (choice == "5"):
        addbook()
    elif (choice == "6"):
        pswd()
    else:
        print("Wrong Choice Please Check Your Input !!")
        admain()



t=1
def Login():
    global id1
    id1 = int(input("Enter A 10 Digit Unique ID:"))
    l_str=str(id1)
    if len(l_str) == 10:
        data = (id1,)
        b = "select password from users where uid = %s"%(id1)
        print(b)
        c = con.cursor(buffered=True)
        c.execute(b)
        con.commit()
        d = c.fetchall()
        if not d:
            global t
            t = 0
    else:
        print("Enter 10 digit ")
        Login()

def ch():
    #print("ch enter")
    pcc = input("create a password that must be greater than 6:")
    che=0
    if len(pcc)>6:
        che+=1
    else:
        print("Password must be greater than 6 characters: ")
        ch()
    pc = int(input("enter your 10 digit phone number:"))
    b_str=str(pc)
    if len(b_str) == 10:
        che+=1
        if che == 2:
            global ps
            ps = pcc
            global ph
            ph = pc
            return che
    else:
        print("Enter A Valid Phone Number: ")
        ch()

def check():
    ps1 = input("Enter UID password:")
    if (d_a[0][0]) == ps1:
        print("successfull Login")
        data =(id2,)
        b = "select * from users where uid = %s"
        c = con.cursor(buffered=True)
        c.execute(b, data)
        con.commit()
        global ext
        ext=c.fetchall()
        #print(ext)
        main()
    else:
        print("wrong password")
        check()


def pswd():
    pss = input("Enter Root Password: ")
    if pss == "0426":
        print('''           
            1. To Access Admin Panel
            
            2. To Access User Panel
            
            ''')
        global lol
        lol = input("Enter Your Choice: ")
        if lol == "1":
            aname=input("Enter UserName: ")
            if AdminDetails[0] == aname:
                apass=input("Enter Password: ")
                if apass == AdminDetails[1]:
                    print("Login Successfull")
                    admain()
                else:
                    print("Wrong Password")
                    pswd()
            else:
                print("Wrong Username")
                pswd()

        elif lol == "2":
            print('''Hey There
             
                           Enter Y If You Are An New User 
                           
                                         AND 
                                         
                           N If You Are An Existing User :)
                           
                           ''')
            ent = input("Enter Your Choice")
            if ent.upper() == "Y":
                print('''Welcome to Library World. Enter Your Details To Create An Account
                
                ''')
                Login()
                if t == 0:
                    print("Yeah That Is Available. Let's Proceed")
                    nm = input("Enter Your Name:")
                    log_i = ch()
                    if log_i == 2:
                        data = (id1, ps, nm, ph)
                        print(data)
                        b = "insert into users values (%s, %s, %s, %s)"
                        c = con.cursor(buffered=True)
                        c.execute(b, data)
                        con.commit()
                        global ext
                        ext = [data]
                        main()

                    else:
                        print("You Have Entered Wrong Inputs: ")
                        Login()

                else:
                    print("The Entered ID Already Taken Please Try Another")
                    Login()


            else:
                global id2
                id2 = int(input("enter your uid:"))
                str_id=str(id2)
                if len(str_id) == 10:
                    data = (id2,)
                    b = "select password from users where uid = %s"
                    c = con.cursor(buffered=True)
                    c.execute(b, data)
                    con.commit()
                    global d_a
                    d_a = c.fetchall()
                    if d_a:
                        check()
                else:
                    print("Wrong Input")
                    pswd()



    else:
        print("Wrong Root Password :")
        pswd()



pswd()


