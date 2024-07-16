from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
class LibraryManagementsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x900+0+0")


        self.book_counts = {
    'To Kill a Mockingbird': 3,
    '1984': 3,
    'Pride and Prejudice': 3,
    'The Great Gatsby': 3,
    'Moby-Dick': 2,
    'War and Peace': 2,
    'Ulysses': 2,
    'The Catcher in the Rye': 2,
    'The Lord of the Rings': 1,
    'One Hundred Years of Solitude': 1,
    'Brave New World': 1,
    'The Brothers Karamazov': 1,
    'Crime and Punishment': 3,
    'Wuthering Heights': 3,
    'Jane Eyre': 3,
    'Anna Karenina': 3,
    'Catch-22': 2,
    'The Hobbit': 2,
    'Fahrenheit 451': 2,
    'The Adventures of Huckleberry Finn': 2,
    'The Odyssey by Homer': 1,
    'Don Quixote': 1,
    'Frankenstein by Mary Shelley': 1
        }


       # ======================================variable===============================================

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.dateofissue_var=StringVar()
        self.daysonbook=StringVar()
        self.latereturnfine_var=StringVar()
        self.actualprice=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.authorname_var=StringVar()
        self.duedate_var=StringVar()
    
    




        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="blue", fg="black", bd=18, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=470)

        # ================================DataFrameLeft===============================================

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="black", bd=20, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=0, y=5, width=850, height=450)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 17, "bold"), width=23, state='readonly', textvariable=self.member_var)
        comMember['values'] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1, padx=2, pady=6)

        lblPRN_NO = Label(DataFrameLeft, bg="powder blue", text="PRN NO", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblPRN_NO.grid(row=1, column=0, sticky=W)

        txtPRN_NO = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.prn_var, width=25)
        txtPRN_NO.grid(row=1, column=1, padx=2, pady=6)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=1, column=2, sticky=W)

        txtActualPrice = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.actualprice, width=13)
        txtActualPrice.grid(row=1, column=3, padx=2, pady=6)

        lblID = Label(DataFrameLeft, bg="powder blue", text="ID Number", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblID.grid(row=2, column=0, sticky=W)

        txtID = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.id_var, width=25)
        txtID.grid(row=2, column=1, padx=2, pady=6)

        lblBookID = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblBookID.grid(row=2, column=2, sticky=W)

        txtBookID = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.bookid_var, width=13)
        txtBookID.grid(row=2, column=3, padx=2, pady=6)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)

        txtFirstName = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.firstname_var, width=25)
        txtFirstName.grid(row=3, column=1, padx=2, pady=6)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=3, column=2, sticky=W)

        txtBookTitle = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.booktitle_var, width=13)
        txtBookTitle.grid(row=3, column=3, padx=2, pady=6)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)

        txtLastName = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.lastname_var, width=25)
        txtLastName.grid(row=4, column=1, padx=2, pady=6)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author Name", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=4, column=2, sticky=W)

        txtAuthor = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.authorname_var, width=13)
        txtAuthor.grid(row=4, column=3, padx=2, pady=6)

        lblAddress = Label(DataFrameLeft, bg="powder blue", text="Address", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblAddress.grid(row=5, column=0, sticky=W)

        txtAddress = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.address_var, width=25)
        txtAddress.grid(row=5, column=1, padx=2, pady=6)

        lblDueDate = Label(DataFrameLeft, bg="powder blue", text="Due Date", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblDueDate.grid(row=5, column=2, sticky=W)

        txtDueDate = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.duedate_var, width=13)
        txtDueDate.grid(row=5, column=3, padx=2, pady=6)

        lblMobileNo = Label(DataFrameLeft, bg="powder blue", text="Mobile No", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblMobileNo.grid(row=6, column=0, sticky=W)

        txtMobileNo = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.mobile_var, width=25)
        txtMobileNo.grid(row=6, column=1, padx=2, pady=6)

        lblDateOfIssue = Label(DataFrameLeft, bg="powder blue", text="Date of Issue", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblDateOfIssue.grid(row=7, column=0, sticky=W)

        txtDateOfIssue = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.dateofissue_var, width=25)
        txtDateOfIssue.grid(row=7, column=1, padx=2, pady=6)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days on Book", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=8, column=0, sticky=W)

        txtDaysOnBook = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.daysonbook, width=25)
        txtDaysOnBook.grid(row=8, column=1, padx=2, pady=6)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("times new roman", 17, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=9, column=0, sticky=W)

        txtLateReturnFine = Entry(DataFrameLeft, font=("times new roman", 17, "bold"), textvariable=self.latereturnfine_var, width=25)
        txtLateReturnFine.grid(row=9, column=1, padx=2, pady=6)

        # ================================DataFrameRight===============================================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="black", bd=20, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=870, y=5, width=630, height=450)

        self.txtBox=Text(DataFrameRight,font=("arial", 12, "bold"),width=31,height=20,padx=2,pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight,orient=VERTICAL)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks = {
    'To Kill a Mockingbird': 3,
    '1984': 3,
    'Pride and Prejudice': 2,
    'The Great Gatsby': 3,
    'Moby-Dick': 2,
    'War and Peace': 2,
    'Ulysses': 2,
    'The Catcher in the Rye': 2,
    'The Lord of the Rings': 1,
    'One Hundred Years of Solitude': 1,
    'Brave New World': 1,
    'The Brothers Karamazov': 1,
    'Crime and Punishment': 3,
    'Wuthering Heights': 3,
    'Jane Eyre': 3,
    'Anna Karenina': 3,
    'Catch-22': 2,
    'The Hobbit': 2,
    'Fahrenheit 451': 2,
    'The Adventures of Huckleberry Finn': 2,
    'The Odyssey by Homer': 1,
    'Don Quixote': 1,
    'Frankenstein by Mary Shelley': 1
}
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="To Kill a Mockingbird"):
                self.booktitle_var.set("To Kill a Mockingbird")
                self.authorname_var.set("Harper Lee")
                self.bookid_var.set("BKID4555")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.700")

            elif (x=="1984"):
                self.booktitle_var.set("1984")
                self.authorname_var.set("George Orwell")
                self.bookid_var.set("BKID4667")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.900")

            elif (x=="Pride and Prejudice"):
                self.booktitle_var.set("Pride and Predjudice")
                self.authorname_var.set("Jane Austen")
                self.bookid_var.set("BKID8251")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.850") 

            elif (x=="The Great Gatsby"):
                self.booktitle_var.set("The Great Gatsby")
                self.authorname_var.set("F.Scott Fitzgerald")
                self.bookid_var.set("BKID8221")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.1200") 

                      
            elif (x=="Moby-Dick"):
                self.booktitle_var.set("Moby-Dick")
                self.authorname_var.set("Herman Melville")
                self.bookid_var.set("BKID8310")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.1500") 

            elif (x=="War and Peace"):
                self.booktitle_var.set("War and Peace")
                self.authorname_var.set("Leo Tolstoy")
                self.bookid_var.set("BKID8510")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.1700")     

            elif (x=="Ulysses"):
                self.booktitle_var.set("Ulysses")
                self.authorname_var.set("James Joyce")
                self.bookid_var.set("BKID8401")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2000") 


            elif (x=="The Catcher in the Rye"):
                self.booktitle_var.set("The Catcher in the Rye")
                self.authorname_var.set("J.D. Salinger")
                self.bookid_var.set("BKID7001")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.1600") 

            elif (x=="The Lord of the Rings"):
                self.booktitle_var.set("The Lord of the Rings")
                self.authorname_var.set("J.R.R. Tolkien")
                self.bookid_var.set("BKID8990")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.1200")

            elif (x=="One Hundred Years of Solitude"):
                self.booktitle_var.set("One Hundred Years of Solitude")
                self.authorname_var.set("Gabriel Garcia Marquez")
                self.bookid_var.set("BKID8255")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2300") 


            elif (x=="Brave New World"):
                self.booktitle_var.set("Brave New World")
                self.authorname_var.set("Mark dawson")
                self.bookid_var.set("BKID8276")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2400") 

            
            elif (x=="The Brothers Karamazov"):
                self.booktitle_var.set("The Brothers Karamazov")
                self.authorname_var.set("roseeou brothers")
                self.bookid_var.set("BKID8285")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2200") 

            
            elif (x=="Crime and Punishment"):
                self.booktitle_var.set("Crime and Punishment")
                self.authorname_var.set("Hary bages")
                self.bookid_var.set("BKID8299")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2100") 
            
            elif (x=="Wuthering Heights"):
                self.booktitle_var.set("Wuthering Heights")
                self.authorname_var.set("william gilbert")
                self.bookid_var.set("BKID8277")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2000") 


            elif (x=="Jane Eyre"):
                self.booktitle_var.set("Jane Eyre")
                self.authorname_var.set("hienrich wood")
                self.bookid_var.set("BKID8277")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.1900") 


            elif (x=="Anna Karenina"):
                self.booktitle_var.set("Anna Karenina")
                self.authorname_var.set("antony das")
                self.bookid_var.set("BKID8001")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2500") 

            elif (x=="Catch-22"):
                self.booktitle_var.set("Catch-22")
                self.authorname_var.set("tony vielby")
                self.bookid_var.set("BKID8009")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2300") 

            elif (x=="The Hobbit"):
                self.booktitle_var.set("The Hobbit")
                self.authorname_var.set("hobert huerick")
                self.bookid_var.set("BKID8255")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2700") 

            elif (x=="Fahrenheit 451"):
                self.booktitle_var.set("Fahrenheit 451")
                self.authorname_var.set("bosil kee")
                self.bookid_var.set("BKID8255")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d3)
                self.dateofissue_var.set(d1)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.actualprice.set("Rs.2200") 
                     
                    


            listbox=Listbox(DataFrameRight,font=("arial", 12, "bold"))
            

        
        listBox=Listbox(DataFrameRight,font=("arial", 12, "bold"),width=20,height=19)
        listBox.bind("<<ListboxSelect>>",SelectBook)

        
        listBox.grid(row=0, column=0, padx=2, pady=6)

        listScrollbar.config(command=listBox.yview)
        
    

        for item in listBooks:
            listBox.insert(END,item)



        # ======================================Buttons Frame============================================
        Framebutton = Frame(self.root, bd=13, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=600, width=1530, height=50)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data", font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data", font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update", font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete", font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset", font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit", font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0, column=5)

        self.btnIssueBook = Button(Framebutton, text="Issue Book", font=("arial", 12, "bold"), width=20, bg="blue",fg="white", command=self.issue_book)
        self.btnIssueBook.grid(row=0, column=6,)


        # ======================================Information Frame============================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=650, width=1530, height=200)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idnumber","firstname","lastname","address",
                                                            "mobile no","dateofissue","daysonbook","latereturnfine",
                                                            "actualprice","bookid","booktitle","authorname","duedate"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO")
        self.library_table.heading("idnumber",text="ID Number")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("mobile no",text="Mobile No")
        self.library_table.heading("dateofissue",text="Date of Issue")
        self.library_table.heading("daysonbook",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("actualprice",text="Actual Price")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("authorname",text="Author Name")
        self.library_table.heading("duedate",text="Due Date")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=120)
        self.library_table.column("prnno",width=120)
        self.library_table.column("idnumber",width=120)
        self.library_table.column("firstname",width=120)
        self.library_table.column("lastname",width=120)
        self.library_table.column("address",width=120)
        self.library_table.column("mobile no",width=120)
        self.library_table.column("dateofissue",width=120)
        self.library_table.column("daysonbook",width=120)
        self.library_table.column("latereturnfine",width=120)
        self.library_table.column("actualprice",width=120)
        self.library_table.column("bookid",width=120)
        self.library_table.column("booktitle",width=120)
        self.library_table.column("authorname",width=120)
        self.library_table.column("duedate",width=120)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="library_management",
                database="mydata"
            )
            cursor = conn.cursor()

            # Get entered values from GUI
            entered_id = self.id_var.get()
            entered_prn=self.prn_var.get()
            entered_first_name = self.firstname_var.get()
            entered_last_name = self.lastname_var.get()

            # Query to check if student details exist in student_details table
            query = """
            SELECT * FROM mydata.student_details 
            WHERE id_number = %s AND first_name = %s AND last_name = %s AND prn_no = %s
            """
            cursor.execute(query, (entered_id, entered_first_name, entered_last_name,entered_prn))
            result = cursor.fetchone()

            if result:
                # If match found, insert data into library table
                insert_query = """
                INSERT INTO library (`Member`, `PRN_NO`,`ID Number`, `First Name`, `Last Name`, `Address`, `Mobile no`, `Date of Issue`, `Days on Book`, `Late Return Fine`, `Actual Price`, `Book ID`, `Book Title`, `Author Name`, `Due Date`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                    self.member_var.get(),
                    self.prn_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address_var.get(),
                    self.mobile_var.get(),
                    self.dateofissue_var.get(),
                    self.daysonbook.get(),
                    self.latereturnfine_var.get(),
                    self.actualprice.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.authorname_var.get(),
                    self.duedate_var.get()
                ))
                conn.commit()
                self.fatch_data()  # Update GUI or perform any necessary actions
                messagebox.showinfo("Success", "Member has been inserted successfully")
            else:
                # If no match found, display error message
                messagebox.showerror("Error", "Record not found. Access denied.")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to read record from MySQL table: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()





    
    

    def update(self):
       conn = mysql.connector.connect(host="localhost", username="root", password="prachi", database="library_management")
       my_cursor = conn.cursor()
       my_cursor.execute("""
        UPDATE library 
        SET `Member`=%s, `ID number`=%s, `First Name`=%s, `Last Name`=%s, `Address`=%s,`Mobile no` =%s, `Date of Issue`=%s, 
        `Days on Book`=%s, `Late Return Fine`=%s,`Actual Price`=%s,`Book ID`=%s, `Book Title`=%s,`Author Name`=%s,`Due Date=%s`
        WHERE `PRN_NO`=%s
    """,                                                                                     (
                                                                                                 self.member_var.get(),
                                                                                                 self.id_var.get(),
                                                                                                 self.firstname_var.get(),
                                                                                                 self.lastname_var.get(),
                                                                                                 self.address_var.get(),
                                                                                                 self.mobile_var.get(),
                                                                                                 self.dateofissue_var.get(),
                                                                                                 self.daysonbook.get(),
                                                                                                 self.latereturnfine_var.get(),
                                                                                                 self.actualprice.get(),
                                                                                                 self.bookid_var.get(),
                                                                                                 self.booktitle_var.get(),
                                                                                                 self.authorname_var.get(),
                                                                                                 self.duedate_var.get(),
                                                                                                 self.prn_var.get()
                                                                                                 
                                                                                                 
                                                                                ))

       conn.commit()
       self.fatch_data()
       self.reset()
       conn.close()

       messagebox.showinfo("Success", "Member has been updated.")



    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="prachi",database="library_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)<15:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)

            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.dateofissue_var.set(row[7]),
        self.daysonbook.set(row[8]),
        self.latereturnfine_var.set(row[9]),
        self.actualprice.set(row[10]),
        self.bookid_var.set(row[11]),
        self.booktitle_var.set(row[12]),
        self.authorname_var.set(row[13]),
        self.duedate_var.set(row[14])
    


    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n") 
        self.txtBox.insert(END,"PRN NO:\t\t"+self.prn_var.get()+"\n") 
        self.txtBox.insert(END,"ID NO:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address:\t\t"+self.address_var.get()+"\n")
        self.txtBox.insert(END,"Mobile NO:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Date of Issue:\t\t"+self.dateofissue_var.get()+"\n")
        self.txtBox.insert(END,"Days on Book:\t\t"+self.daysonbook.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+self.actualprice.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author Name:\t\t"+self.authorname_var.get()+"\n")
        self.txtBox.insert(END,"Due Date :\t\t"+self.duedate_var.get()+"\n")


    def reset(self):
        self.member_var.set("") 
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.mobile_var.set("")
        self.dateofissue_var.set("")
        self.daysonbook.set("")
        self.latereturnfine_var.set("")
        self.actualprice.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.authorname_var.set("")
        self.duedate_var.set("")
        self.txtBox.delete("1.0",END)
    




    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

        



    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prachi",database="library_management")
            my_cursor=conn.cursor()
            query= "DELETE FROM library WHERE PRN_NO = %s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()


            messagebox.showinfo("Success","Member has been deleted.")



    def issue_book(self):
        book_title = self.booktitle_var.get()
        if book_title in self.book_counts:
            if self.book_counts[book_title] > 0:
                self.book_counts[book_title] -= 1
                messagebox.showinfo("Success", f"Issued '{book_title}'. Remaining copies: {self.book_counts[book_title]}")
            else:
                messagebox.showerror("Error", f"No more copies of '{book_title}' available")
        else:
            messagebox.showerror("Error", f"'{book_title}' not found in library")


        



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementsystem(root)
    root.mainloop()