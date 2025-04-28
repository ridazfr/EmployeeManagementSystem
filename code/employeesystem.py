#                                                                     IMPORT STATEMENTS

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import csv

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                     FUNCTION DEFINITIONS

def show():
    global showpbutton,passw,uname
    content2=passw.get()
    messagebox.showinfo("Password",'Password entered by you: '+content2)
    showpbutton.destroy()
    passw.delete(0,END)
    uname.delete(0,END)

   
def return_entry():
    global window,showpbutton
    uname_content = uname.get()
    pw=''
    def return_entry2():
        nonlocal pw
        pw=passw.get()
    return_entry2()
    if uname_content=='' or pw=='':
        messagebox.showerror('Error','Both Fields Required')
    elif uname_content!='' and pw=='a':
        messagebox.showinfo("Log In Status", "SUCCESSFULLY LOGGED IN")
        global con
        global cur
        con=mysql.connector.connect(host='localhost',user='root',password='123456',db='School')
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Employee(Eno INT(3) NOT NULL PRIMARY KEY,Ename VARCHAR(20),Eaddress VARCHAR(50),Eemailid VARCHAR(50),\
Ephone CHAR(10),Department VARCHAR(20))")
        cur.execute("CREATE TABLE IF NOT EXISTS Pay(PayID INT(3) NOT NULL PRIMARY KEY, BasicPay INT, Allowance INT, Deduction INT, NetPay INT,\
Eno INT(3) REFERENCES Employee(Eno) ON UPDATE CASCADE ON DELETE CASCADE)")
        cur.execute("CREATE TABLE IF NOT EXISTS Awards(AwardID INT(3) NOT NULL PRIMARY KEY, Year INT(4), Particulars VARCHAR(50),\
Eno INT(3) REFERENCES Employee(Eno) ON UPDATE CASCADE ON DELETE CASCADE)")
        global win2
        win2=Tk()
        window.withdraw()
        window2()
    else:
        messagebox.showerror("Log In Status", "WRONG PASSWORD")
        showpbutton=Button(window, text=" Show Password ", bg='gray98',fg='#ce3531',command=show,font=('Times New Roman',12,))
        showpbutton.place(x=555,y=450,width=120,height=50)
        

def choice1():
    global c1
    b1=Button(win2,text='Add to Table Employee',fg='black',bg='#D9D9AE',font=('Times New Roman',16),command=Employee)
    b1.place(x=820,y=150,width=300,height=50)
    b2=Button(win2,text='Add to Table Pay',fg='black',bg='#D9D9AE',font=('Times New Roman',16),command=Pay)
    b2.place(x=820,y=250,width=300,height=50)
    b3=Button(win2,text='Add to Table Awards',fg='black',bg='#D9D9AE',font=('Times New Roman',16),command=Awards)
    b3.place(x=820,y=350,width=300,height=50)

def choice2():
    global c2
    b1=Button(win2,text='Modify Table Employee',fg='black',bg='#D9D9AE',font=('Times New Roman',16),command=ModifyEmployee)
    b1.place(x=820,y=150,width=300,height=50)
    b2=Button(win2,text='Modify Table Pay',fg='black',bg='#D9D9AE',font=('Times New Roman',16),command=ModifyPay)
    b2.place(x=820,y=250,width=300,height=50)
    b3=Button(win2,text='Modify Table Awards',fg='black',bg='#D9D9AE',font=('Times New Roman',16),command=ModifyAwards)
    b3.place(x=820,y=350,width=300,height=50)

def disable_button():
    win2.withdraw()
    window.deiconify()
    uname.delete(0, END)
    passw.delete(0, END)
    
def window2():
    global c1
    win2.geometry("1200x630")
    win2.resizable(False,False)
    win2.title('EMPLOYEE MANAGEMENT SYSTEM')
    Label(win2,text='EMPLOYEE MANAGEMENT SYSTEM',font=('Times New Roman',50,),bg='#ce3531',fg='#D9D9AE',justify='center').pack()
    win2.configure(bg='#ce3531')
    c1=Canvas(win2,width=400,height=500,bg='gray98')
    c1.place(x=400,y=100)
    button1=Button(win2,text='Add An Employee',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=choice1)
    button1.place(x=450,y=150,width=300,height=30)
    
    button2=Button(win2,text='Display All Employee Details',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=Display_All)
    button2.place(x=450,y=200,width=300,height=30)

    button3=Button(win2,text='Delete An Employee',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=Delete_Emp)
    button3.place(x=450,y=250,width=300,height=30)

    button4=Button(win2,text='Modify Details Of An Employee',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=choice2)
    button4.place(x=450,y=300,width=300,height=30)
    
    button5=Button(win2,text='Display Based On Department',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=DisplayDept)
    button5.place(x=450,y=350,width=300,height=30)
    
    button6=Button(win2,text='Display Based On Awards',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=DisplayAwards)
    button6.place(x=450,y=400,width=300,height=30)

    button7=Button(win2,text='Display Pay Details Of Employee',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=DisplaySal)
    button7.place(x=450,y=450,width=300,height=30)

    button8=Button(win2,text='Log Out',fg='black',bg='#d9d9ae',font=('Times New Roman',14),command=disable_button)
    button8.place(x=450,y=500,width=300,height=30)
    



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                     TABLE EMPLOYEE

L=[]
def eget1():
    global entry1,s1,s2,B1,B2
    entry1=s1.get()
    if entry1=='':
        messagebox.showerror("Error","Enter Employee ID")
    elif (entry1.isdigit()==True) and (len(entry1)==3):
        q="select eno from employee"
        cur.execute(q)
        res=cur.fetchall()
        if (int(entry1),) not in res:
            L.append(int(entry1))
            messagebox.showinfo("Done","Saved")
            s1.config(state= "disabled")
            B1["state"]="disable"
            ename=Label(Ewindow,text='Employee Name ',fg='black',bg='#EFE0E0',font='Times 16')
            ename.place(x=80,y=150)
            s2=Entry(Ewindow,width=30)
            s2.place(x=350,y=150)
            B2=Button(Ewindow,text='Save',fg='black',bg='#EFE0E0',command=eget2)
            B2.place(x=550,y=150,width=50,height=25)                          
        else:
            messagebox.showerror("Error","Employee Already Exists")
    else:
        messagebox.showerror('Error','Enter ID of integer(3) datatype')

def eget2():
    global entry2,s2,s3,B2,B3
    entry2=s2.get()
    if entry2=='':
        messagebox.showerror("Error","Enter Employee Name")
    elif (entry2.isalpha()==False):
        messagebox.showerror("Error","Enter String Type")
    else:
        L.append(entry2)
        messagebox.showinfo("Done","Saved")
        s2.config(state= "disabled")
        B2["state"]="disable"
        eadd=Label(Ewindow,text='Employee Address ',fg='black',bg='#EFE0E0',font='Times 16')
        eadd.place(x=80,y=200)
        s3=Entry(Ewindow,width=30)
        s3.place(x=350,y=200)
        B3=Button(Ewindow,text='Save',fg='black',bg='#EFE0E0',command=eget3)
        B3.place(x=550,y=200,width=50,height=25)

def eget3():
    global entry3,s3,s4,B3,B4
    entry3=s3.get()
    if entry3=='':
        messagebox.showerror("Error","Enter Employee Address")
    else:
        L.append(entry3)
        messagebox.showinfo("Done","Saved")
        s3.config(state= "disabled")
        B3["state"]="disable"
        egid=Label(Ewindow,text='Employee Email ID ',fg='black',bg='#EFE0E0',font='Times 16')
        egid.place(x=80,y=250)
        s4=Entry(Ewindow,width=30)
        s4.place(x=350,y=250)
        B4=Button(Ewindow,text='Save',fg='black',bg='#EFE0E0',command=eget4)
        B4.place(x=550,y=250,width=50,height=25)

def eget4():
    global entry4,s4,s5,B4,B5
    entry4=s4.get()
    if entry4=='':
        messagebox.showerror("Error","Enter Employee Email")
    else:
        if '@' in entry4:
            if entry4[-4:]=='.com':
                L.append(entry4)
                messagebox.showinfo("Done","Saved")
                s4.config(state= "disabled")
                B4["state"]="disable"
                ephone=Label(Ewindow,text='Employee Phone Number ',fg='black',bg='#EFE0E0',font='Times 16')
                ephone.place(x=80,y=300)
                s5=Entry(Ewindow,width=30)
                s5.place(x=350,y=300)
                B5=Button(Ewindow,text='Save',fg='black',bg='#EFE0E0',command=eget5)
                B5.place(x=550,y=300,width=50,height=25)

            else:
                messagebox.showerror('Error','Format example:username@gmail.com')
        else:
            messagebox.showerror('Error','Format example:username@gmail.com')

def eget5():
    global entry5,s5,s6,B5,B6,drop2
    entry5=s5.get()
    try:
        if type(entry5)==str and len(str(entry5))==10 and (entry5.isdigit()==True):
            L.append(entry5)
            messagebox.showinfo("Done","Saved")
            s5.config(state= "disabled")
            B5["state"]="disable"
            did=Label(Ewindow,text=' Department Name ',fg='black',bg='#EFE0E0',font='Times 16')
            did.place(x=80,y=350)
            drop2=ttk.Combobox(Ewindow,value=['Search by..','Marketing','Administration','Teaching Staff','Non-Teaching Staff'],width=27)
            drop2.current(0)
            drop2.place(x=350,y=350)
            B6=Button(Ewindow,text='Save',fg='black',bg='#EFE0E0',command=eget6)
            B6.place(x=550,y=350,width=50,height=25)
        elif len(str(entry5))!=10:
            messagebox.showerror('Error','Enter 10 digits')
        else:
            messagebox.showerror('Error','Enter 10 digits')
    except ValueError:
        messagebox.showerror("Error","Enter Phone Number")

def eget6():
    global entry6,B6,drop2
    entry6=drop2.get()
    if entry6!='' and entry6!='Search by..':
        L.append(entry6)
        messagebox.showinfo("Done","Saved")
        B6["state"]="disable"
        button=Button(Ewindow,text='Done',fg='black',bg='#EFE0E0',command=insert_employee)
        button.place(x=280,y=500,width=70,height=50)
    else:
        messagebox.showerror("Error","Select a Column")
        

#Iserting Values
def insert_employee():
    global L,Ewindow
    q="INSERT INTO Employee VALUES(%s,%s,%s,%s,%s,%s)"
    v=tuple(L)
    print(v)
    if L==[] or len(L)!=6:
        messagebox.showerror("Error","Empty fields not allowed, Re-enter fields")
        L=[]        
        Ewindow.withdraw()
        Employee()
    else:
        cur.execute(q,v)
        con.commit()
        L=[]
        messagebox.showinfo('Details Updated',"Details Updated")
        Ewindow.withdraw()
        Employee()
        
def Employee():
    global Ewindow
    Ewindow=Tk()
    win2.withdraw()
    Ewindow.title('TABLE EMPLOYEE')
    Ewindow.geometry("700x630")
    Ewindow.resizable(False,False)
    Ewindow.configure(bg='#ce3531')
    label=Label(Ewindow,text='Table: Employee',fg='#D9D9AE',bg='#ce3531',font='Times 30').pack()
    eno=Label(Ewindow,text='Employee ID ',fg='black',bg='#EFE0E0',font='Times 16')
    eno.place(x=80,y=100)
    global s1
    s1=Entry(Ewindow,width=30)
    s1.place(x=350,y=100)
    global B1
    B1=Button(Ewindow,text='Save',fg='black',bg='#EFE0E0',command=eget1)
    B1.place(x=550,y=100,width=50,height=25)
    
    D=Button(Ewindow,text='Back',fg='black',bg='#EFE0E0',command=resize1)
    D.place(x=280,y=580,width=70,height=50)


def resize1():
    Ewindow.withdraw()
    win2.deiconify()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            TABLE PAY
LP=[]  
def pget1():
    global pentry1,p1,p2,pu1,pu2
    pentry1=p1.get()
    if pentry1!='':
        if (pentry1.isdigit()==True) and (len(pentry1)==3):
            q='select PayID from pay'
            cur.execute(q)
            res=cur.fetchall()
            if (int(pentry1),) not in res:
                LP.append(int(pentry1))
                messagebox.showinfo("Done","Saved")
                p1.config(state= "disabled")
                pu1["state"]="disable"
                pname=Label(Pwindow,text=' Basic Pay ',fg='black',bg='#EFE0E0',font='Times 16')
                pname.place(x=120,y=150)
                p2=Entry(Pwindow,width=30)
                p2.place(x=300,y=150)
                pu2=Button(Pwindow,text='Save',fg='black',bg='#EFE0E0',command=pget2)
                pu2.place(x=500,y=150,width=50,height=25)
                
            else:
                messagebox.showerror("Error","PayID Already Exists")
        else:
            messagebox.showerror('Error','Enter Integer Value(3)')
    else:
        messagebox.showerror('Error','Enter Pay ID')
      
def pget2():
    global pentry2,p2,p3,pu2,pu3
    pentry2=p2.get()
    if pentry2.isdigit()==True:
        LP.append(int(pentry2))
        messagebox.showinfo("Done","Saved")
        p2.config(state= "disabled")
        pu2["state"]="disable"
        alpay=Label(Pwindow,text=' Allowance ',fg='black',bg='#EFE0E0',font='Times 16')
        alpay.place(x=120,y=200)
        p3=Entry(Pwindow,width=30)
        p3.place(x=300,y=200)
        pu3=Button(Pwindow,text='Save',fg='black',bg='#EFE0E0',command=pget3)
        pu3.place(x=500,y=200,width=50,height=25)
    else:
        messagebox.showerror("Error","Enter Integer Value")
    

def pget3():
    global pentry3,p3,p4,pu3,pu4
    pentry3=p3.get()
    if pentry3.isdigit()==True:
        LP.append(int(pentry3))
        messagebox.showinfo("Done","Saved")
        p3.config(state= "disabled")
        pu3["state"]="disable"
        depay=Label(Pwindow,text=' Deduction ',fg='black',bg='#EFE0E0',font='Times 16')
        depay.place(x=120,y=250)
        p4=Entry(Pwindow,width=30)
        p4.place(x=300,y=250)
        pu4=Button(Pwindow,text='Save',fg='black',bg='#EFE0E0',command=pget4)
        pu4.place(x=500,y=250,width=50,height=25)
    else:
        messagebox.showerror("Error","Enter Integer Value")
    


def pget4():
    global pentry2,pentry3,pentry4,p4,p5,pu4,pu5
    pentry4=p4.get()
    if pentry4.isdigit()==True:
        if int(pentry4)<(int(pentry2)*0.05):
            LP.append(int(pentry4))
            messagebox.showinfo("Done","Saved")
            p4.config(state= "disabled")
            pu4["state"]="disable"
            LP.append(int(pentry2)+int(pentry3)-int(pentry4))
            eno=Label(Pwindow,text=' Employee ID ',fg='black',bg='#EFE0E0',font='Times 16')
            eno.place(x=120,y=300)
            p5=Entry(Pwindow,width=30)
            p5.place(x=300,y=300)
            pu5=Button(Pwindow,text='Save',fg='black',bg='#EFE0E0',command=pget5)
            pu5.place(x=500,y=300,width=50,height=25)
        else:
            messagebox.showerror("Error","Enter Less than 5% of Basic Pay")
            
    else:
        messagebox.showerror("Error","Enter Integer Value")

def pget5():
    global pentry5,p5,pu5,pu6
    pentry5=p5.get()
    if pentry5=='':
        messagebox.showerror("Error","Enter Employee ID")
    elif (pentry5.isdigit()==True) and (len(pentry5)==3):
        q="select eno from employee"
        cur.execute(q)
        res=cur.fetchall()
        if (int(pentry5),) in res:
            q="select eno from pay"
            cur.execute(q)
            res=cur.fetchall()
            if (int(pentry5),) not in res:
                LP.append(int(pentry5))
                messagebox.showinfo("Done","Saved")
                p5.config(state= "disabled")
                pu5["state"]="disable"
                button=Button(Pwindow,text='Done',fg='black',bg='#EFE0E0',command=insert_pay)
                button.place(x=300,y=500,width=70,height=50)
            else:
                messagebox.showerror("Error","Pay Details Of Employee Already Exists")
        else:
            messagebox.showerror("Error","Employee Doesn't Exist")
    else:
        messagebox.showerror('Error','Enter ID of integer(3) datatype')

def insert_pay():
    global LP,Pwindow
    q="INSERT INTO Pay VALUES(%s,%s,%s,%s,%s,%s)"
    v=tuple(LP)
    if LP==[] or len(LP)!=6:
        messagebox.showerror("Error","Empty Fields Not Allowed, Re-enter Fields")
        LP=[]
        Pwindow.withdraw()
        Pay()
    else:
        cur.execute(q,v)
        con.commit()
        LP=[]
        messagebox.showinfo('Details Updated',"Details Updated")
        Pwindow.withdraw()
        Pay()

def Pay():
    global Pwindow
    Pwindow=Tk()
    win2.withdraw()
    Pwindow.title('TABLE PAY')
    Pwindow.geometry("800x800")
    Pwindow.resizable(False,False)
    Pwindow.configure(bg='#ce3531')
    label=Label(Pwindow,text='Table: Pay',fg='#d9d9ae',bg='#ce3531',font='Times 30').pack()
    pid=Label(Pwindow,text=' Pay ID ',fg='black',bg='#EFE0E0',font='Times 16')
    pid.place(x=120,y=100)
    global p1
    p1=Entry(Pwindow,width=30)
    p1.place(x=300,y=100)
    global pu1
    pu1=Button(Pwindow,text='Save',fg='black',bg='#EFE0E0',command=pget1)
    pu1.place(x=500,y=100,width=50,height=25)
    P=Button(Pwindow,text='Back',fg='black',bg='#EFE0E0',command=resize2)
    P.place(x=300,y=580,width=70,height=50)

def resize2():
    Pwindow.withdraw()
    win2.deiconify()



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            TABLE AWARDS

LA=[]
def aget1():
    global aentry1,a1,a2,au1,au2
    aentry1=a1.get()
    if aentry1!='':
        if (aentry1.isdigit()==True) and (len(aentry1)==3):
            q='select AwardID from Awards'
            cur.execute(q)
            res=cur.fetchall()
            if (int(aentry1),) not in res:
                LA.append(int(aentry1))
                messagebox.showinfo("Done","Saved")
                a1.config(state= "disabled")
                au1["state"]="disable"
                aparticulars=Label(Awindow,text=' Year Awarded ',fg='black',bg='#EFE0E0',font='Times 16')
                aparticulars.place(x=120,y=150)
                a2=Entry(Awindow,width=30)
                a2.place(x=300,y=150)
                au2=Button(Awindow,text='Save',fg='black',bg='#EFE0E0',command=aget2)
                au2.place(x=500,y=150,width=50,height=25)
            else:
                messagebox.showerror("Error","AwardID Already Exists")
        else:
            messagebox.showerror('Error','Enter Integer Value(3)')
    else:
        messagebox.showerror('Error','Enter Award ID')

def aget2():
    global aentry2,a2,a3,au2,au3
    aentry2=a2.get()
    if (len(aentry2)==4) and (aentry2.isdigit()==True):
        LA.append(int(aentry2))
        messagebox.showinfo("Done","Saved")
        a2.config(state= "disabled")
        au2["state"]="disable"
        ayear=Label(Awindow,text=' Partculars ',fg='black',bg='#EFE0E0',font='Times 16')
        ayear.place(x=120,y=200)
        a3=Entry(Awindow,width=30)
        a3.place(x=300,y=200)
        au3=Button(Awindow,text='Save',fg='black',bg='#EFE0E0',command=aget3)
        au3.place(x=500,y=200,width=50,height=25)
    else:
        messagebox.showerror("Error","Enter Year as Integer(4)")
        

def aget3():
    global aentry3,a3,a4,au3,au4
    aentry3=a3.get()
    if aentry3!='':
        LA.append(aentry3)
        messagebox.showinfo("Done","Saved")
        a3.config(state= "disabled")
        au3["state"]="disable"
        eno=Label(Awindow,text=' Employee ID ',fg='black',bg='#EFE0E0',font='Times 16')
        eno.place(x=120,y=250)
        a4=Entry(Awindow,width=30)
        a4.place(x=300,y=250)
        au4=Button(Awindow,text='Save',fg='black',bg='#EFE0E0',command=aget4)
        au4.place(x=500,y=250,width=50,height=25)
    else:
        messagebox.showerror('Error','Enter Award Particulars')

def aget4():
    global aentry4,a4,au4,au5
    aentry4=a4.get()
    if aentry4=='':
        messagebox.showerror("Error","Enter Employee ID")
    elif (aentry4.isdigit()==True) and (len(aentry4)==3):
        q="select eno from employee"
        cur.execute(q)
        res=cur.fetchall()
        if (int(aentry4),) in res:
            LA.append(int(aentry4))
            messagebox.showinfo("Done","Saved")
            a4.config(state= "disabled")
            au4["state"]="disable"
            button=Button(Awindow,text='Done',fg='black',bg='#EFE0E0',command=insert_awards)
            button.place(x=300,y=500,width=70,height=50)                     
        else:
            messagebox.showerror("Error","Employee Doesn't Exist")
    else:
        messagebox.showerror('Error','Enter ID of integer(3) datatype')
    
def insert_awards():
    global LA,Awindow
    q="INSERT INTO Awards VALUES(%s,%s,%s,%s)"
    v=tuple(LA)
    if LA==[] or len(LA)!=4:
        messagebox.showerror("Error","Empty Fields Not Allowed, Re-enter Fields")
        LA=[]
        Awindow.withdraw()
        Awards()
    else:
        cur.execute(q,v)
        con.commit()
        LA=[]
        messagebox.showinfo('Details Updated',"Details Updated")
        Awindow.withdraw()
        Awards()


def Awards():
    global Awindow
    Awindow=Tk()
    win2.withdraw()
    Awindow.title('TABLE AWARDS')
    Awindow.geometry("800x800")
    Awindow.resizable(False,False)
    Awindow.configure(bg='#ce3531')
    label=Label(Awindow,text='Table: Awards',fg='#d9d9ae',bg='#ce3531',font='Times 30').pack()
    aid=Label(Awindow,text=' Award ID ',fg='black',bg='#EFE0E0',font='Times 16')
    aid.place(x=120,y=100)
    global a1
    a1=Entry(Awindow,width=30)
    a1.place(x=300,y=100)
    global au1
    au1=Button(Awindow,text='Save',fg='black',bg='#EFE0E0',command=aget1)
    au1.place(x=500,y=100,width=50,height=25)
    A=Button(Awindow,text='Back',fg='black',bg='#EFE0E0',command=resize3)
    A.place(x=300,y=580,width=70,height=50)

def resize3():
    Awindow.withdraw()
    win2.deiconify()
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                         DISPLAYING EMPLOYEE DETAILS

def Display_All():
    global Disp
    Disp=Tk()
    win2.withdraw()
    Disp.title('DISPLAY DETAILS')
    Disp.geometry("700x630")
    Disp.resizable(True,True)
    Disp.configure(bg='#ce3531')
    label=Label(Disp,text='DETAILS',fg='#d9d9ae',bg='#ce3531',font='Times 30').pack()

    
    trv=ttk.Treeview(Disp, selectmode='browse')
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading', background="#EFE0E0")
    trv.pack()
    trv['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14')
    trv['show']='headings'
    trv.column('1',width=75,anchor='c',stretch=NO)
    trv.column('2',width=100,anchor='c')
    trv.column('3',width=150,anchor='c')
    trv.column('4',width=150,anchor='c')
    trv.column('5',width=70,anchor='c')
    trv.column('6',width=100,anchor='c')
    trv.column('7',width=50,anchor='c',stretch=NO)
    trv.column('8',width=60,anchor='c')
    trv.column('9',width=65,anchor='c')
    trv.column('10',width=65,anchor='c')
    trv.column('11',width=60,anchor='c')
    trv.column('12',width=60,anchor='c',stretch=NO)
    trv.column('13',width=60,anchor='c')
    trv.column('14',width=170,anchor='c')
    trv.heading('1',text='Employee ID')
    trv.heading('2',text='Name')
    trv.heading('3',text='Address')
    trv.heading('4',text='Email')
    trv.heading('5',text='Telephone')
    trv.heading('6',text='Department')
    trv.heading('7',text='Pay ID')
    trv.heading('8',text='Basic Pay')
    trv.heading('9',text='Allowance')
    trv.heading('10',text='Deduction')
    trv.heading('11',text='Net Pay')
    trv.heading('12',text='Award ID')
    trv.heading('13',text='Year')
    trv.heading('14',text='Particulars')
    
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='School')
    cur=con.cursor()
    q="select e.eno,e.ename,e.eaddress,e.eemailid,e.ephone,e.department,\
p.payid,p.basicpay,p.allowance,p.deduction,p.netpay,\
a.awardid,a.year,a.particulars from employee e left join pay p on e.eno=p.eno left join awards a on e.eno=a.eno"
    cur.execute(q)
    res=cur.fetchall()
    for dt in res:
        trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11],dt[12],dt[13]))
    back4()

def resize4():
    Disp.withdraw()
    win2.deiconify()

def back4():
    D=Button(Disp,text='Back',fg='black',bg='#EFE0E0',command=resize4)
    D.pack()
        

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                          DELETE AN EMPLOYEE
def return_d():
    global delete_e
    content1=delete_e.get()
    try:
        if content1!='':
            messagebox.showinfo("Deletion Status", "Searching for record..")
            q='select eno from employee'
            cur.execute(q)
            res=cur.fetchall()
            if (int(content1),) not in res:
                messagebox.showerror('Deletion Status',"Employee doesn't exist")
            else:
                q1="DELETE FROM EMPLOYEE WHERE Eno=%s"
                v=(int(content1),)
                cur.execute(q1,v)
                res=cur.fetchone()
                con.commit()
                if res is None:
                    q2="DELETE FROM PAY WHERE Eno=%s"
                    v=(int(content1),)
                    cur.execute(q1,v)
                    res=cur.fetchone()
                    con.commit()
                    if res is None:
                        q3="DELETE FROM AWARDS WHERE Eno=%s"
                        v=(int(content1),)
                        cur.execute(q1,v)
                        res=cur.fetchone()
                        con.commit()
                        if res is None:
                            messagebox.showinfo("Deletion Status", "Record deleted")
        else:
            messagebox.showerror('Error','ID not entered')
    except ValueError:
        messagebox.showerror("Error","Enter Integer Value")



def Delete_Emp():
    global delbox,delete_e
    delbox=Tk()
    delbox.title('DELETE DETAILS')
    delbox.geometry("700x630")
    delbox.resizable(False,False)
    delbox.configure(bg='#ce3531')
    label=Label(delbox,text='DELETE EMPLOYEE',fg='#D9D9AE',bg='#ce3531',font='Times 30').pack(pady=10)
    Label(delbox,text='Enter Employee ID to delete:',fg='#D9D9AE',bg='#ce3531',font='Times 16').pack(pady=10)
    delete_e=Entry(delbox,width=30)
    delete_e.pack()
    Label(delbox,text='',bg='#ce3531').pack(pady=10)
    Button(delbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=return_d).pack()
    back5()

def resize5():
    delbox.withdraw()
    win2.deiconify()

def back5():
    D=Button(delbox,text='Back',fg='black',bg='#EFE0E0',command=resize5)
    D.pack()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                      MODIFY DETAILS

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            MODIFY TABLE EMPLOYEEs
def search():
    global searchentry,searched,enterbutton
    q=''
    searched=searchentry.get()
    if searched!='':
        messagebox.showinfo("Updation Status", "Searching for record..")
        q="select eno from employee"
        cur.execute(q)
        res=cur.fetchall()
        if searched.isdigit()==True:
            if (int(searched),) not in res:
                messagebox.showerror('Updation Status',"Employee doesn't exist")
                
            else:
                q="select * from employee where eno=%s"       
                v=(int(searched),)
                cur.execute(q,v)
                res=cur.fetchall()
                if not res:
                    pass
            
                else:
            
                    trv=ttk.Treeview(empmodbox, selectmode='browse',height=1)
                    s = ttk.Style()
                    s.theme_use('clam')
                    s.configure('Treeview.Heading', background="#EFE0E0")
                    trv.pack()
                    trv['columns']=('1','2','3','4','5','6')
                    trv['show']='headings'
                    trv.column('1',width=75,anchor='c',stretch=NO)
                    trv.column('2',width=100,anchor='c')
                    trv.column('3',width=150,anchor='c')
                    trv.column('4',width=150,anchor='c')
                    trv.column('5',width=70,anchor='c')
                    trv.column('6',width=150,anchor='c')
                    trv.heading('1',text='Employee ID')
                    trv.heading('2',text='Name')
                    trv.heading('3',text='Address')
                    trv.heading('4',text='Email')
                    trv.heading('5',text='Telephone')
                    trv.heading('6',text='Department')
                    
                    for dt in res:
                        trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
                    choose_column()
                    
                    def disable_entry():
                        global searchentry
                        searchentry.config(state= "disabled")
                    disable_entry()
                    enterbutton["state"]="disable"
        else:
            messagebox.showerror('Error',"Enter Integer(3) Datatype")
    
    else:
        messagebox.showerror('Error',"Enter Employee ID")
        
def choose_column():
    global empmodbox,drop2,entrybutton2,searched
    if searched!='':
        Label(empmodbox,text='',fg='#ce3531',bg='#ce3531').pack()
        columnlabel=Label(empmodbox,text="Enter Column To Be Modified",bg='#ce3531',fg='#D9D9AE',font='Times 14')
        columnlabel.pack()
        Label(empmodbox,text='',fg='#ce3531',bg='#ce3531').pack()
        drop2=ttk.Combobox(empmodbox,value=['Search by..','Employee Name','Employee Address','Employee Email','Telephone','Department'])
        drop2.current(0)
        drop2.pack()
        entrybutton2=Button(empmodbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=modifycolumn)
        entrybutton2.pack()
    else:
        messagebox.showerror("Error","Enter Employee ID")
        
def modifycolumn():
    global empmodbox,drop2,entrybutton2,modifybutton,cname,modify_entry,depbutton,drop3
    cname=drop2.get()
    if cname!='' and cname!='Search by..':
        if cname!='Department' and cname not in ['Employee Name','Employee Address','Employee Email','Telephone']:
            messagebox.showerror("Error","Select a Column From Drop-down Menu")
        elif cname in ['Employee Name','Employee Address','Employee Email','Telephone']:
            modifylabel=Label(empmodbox,text="Enter New Value",bg='#ce3531',fg='#D9D9AE',font='Times 14')
            modifylabel.pack()
            modify_entry=Entry(empmodbox,width=30)
            modify_entry.pack()
            modifybutton=Button(empmodbox,text='Modify',fg='black',bg='#EFE0E0',command=updation)
            modifybutton.pack()
            entrybutton2["state"]="disable"
        elif cname=='Department':
            entrybutton2["state"]="disable"
            modifylabel=Label(empmodbox,text="Enter New Value",bg='#ce3531',fg='#D9D9AE',font='Times 14')
            modifylabel.pack()
            drop3=ttk.Combobox(empmodbox,value=['Search by..','Marketing','Administration','Teaching Staff','Non-Teaching Staff'],width=27)
            drop3.current(0)
            drop3.pack()
            depbutton=Button(empmodbox,text='Modify',bg='#EFE0E0',fg='black',width=7,command=updation)
            depbutton.pack()
    else:
        messagebox.showerror("Error","Select a Column From Drop-down Menu")

def updation2():
    global empmodbox,q,updatedvalue,searched,depbutton,dep,cname,modify_entry
    if cname=='Department':
        v=(dep,searched)
        depbutton["state"]="disable"
    else:
        v=(updatedvalue,searched)
        modifybutton["state"]="disable"
        def disable_entry():
            global modify_entry
            modify_entry.config(state= "disabled")
        disable_entry()
    cur.execute(q,v)
    con.commit()
    messagebox.showinfo("Updation Status","Record Modified")
    
    q="select * from employee where eno=%s"            
    v=(int(searched),)
    cur.execute(q,v)
    res=cur.fetchall()
    if not res:
        pass
    else:
        trv=ttk.Treeview(empmodbox, selectmode='browse',height=1)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#EFE0E0")
        trv.pack()
        trv['columns']=('1','2','3','4','5','6')
        trv['show']='headings'
        trv.column('1',width=75,anchor='c',stretch=NO)
        trv.column('2',width=100,anchor='c')
        trv.column('3',width=150,anchor='c')
        trv.column('4',width=150,anchor='c')
        trv.column('5',width=70,anchor='c')
        trv.column('6',width=150,anchor='c')
        trv.heading('1',text='Employee ID')
        trv.heading('2',text='Name')
        trv.heading('3',text='Address')
        trv.heading('4',text='Email')
        trv.heading('5',text='Telephone')
        trv.heading('6',text='Department')    
        for dt in res:
            trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
        back6()
        
def updation():
    global empmodbox,modify_entry,mb,updatedvalue,cname,q,itemsearch,searched,depbutton,dep
    q=''
    if cname!='Department':
        updatedvalue=modify_entry.get()
        if updatedvalue=='':
            messagebox.showerror('Error','Enter New Value')
            if cname=='Employee Name':
                if (updatedvalue.isalpha())==False:
                    messagebox.showerror("Error","Enter String Type of First Name")
                else:
                    q="UPDATE Employee SET Ename=%s WHERE Eno=%s"
                    updation2()
                
            elif cname=='Employee Address':
                q="UPDATE Employee SET EAddress=%s WHERE Eno=%s"
                updation2()

            elif cname=='Employee Email':
                if '@' in updatedvalue:
                    if updatedvalue[-4:]=='.com':
                        q="UPDATE Employee SET Eemailid=%s WHERE Eno=%s"
                        updation2()
                    else:
                        messagebox.showerror('Error','Format example:username@gmail.com')
                else:
                    messagebox.showerror('Error','Format example:username@gmail.com')

            elif cname=='Telephone':
                if type(updatedvalue)==str and len(str(updatedvalue))==10 and (updatedvalue.isdigit()):
                    q="UPDATE Employee SET Ephone=%s WHERE Eno=%s"
                    updation2()
                elif len(str(updatedvalue))!=10:
                    messagebox.showerror('Error','Enter 10 digits')
                else:
                    messagebox.showerror("Error","Enter Phone Number")
    else:
        dep=drop3.get()
        if dep!='' and dep!='Search by..' and dep in ['Marketing','Administration','Teaching Staff','Non-Teaching Staff']:
            q="UPDATE Employee SET Department=%s WHERE Eno=%s"
            updation2()
        else:
            messagebox.showerror("Error","Select a Column From Drop-down Menu")          

def ModifyEmployee():
    global empmodbox,searchentry,enterbutton
    empmodbox=Tk()
    empmodbox.title('MODIFY DETAILS')
    empmodbox.geometry("700x630")
    empmodbox.resizable(True,True)
    empmodbox.configure(bg='#ce3531')
    label=Label(empmodbox,text='MODIFY EMPLOYEE DETAILS',bg='#ce3531',fg='#D9D9AE',font='Times 30').pack(pady=10)
    Label(empmodbox,text='Enter Employee ID to search:',bg='#ce3531',fg='#D9D9AE',font='Times 16').pack(pady=10)
    searchentry=Entry(empmodbox,width=30)
    searchentry.pack(pady=10)
    enterbutton=Button(empmodbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=search)
    enterbutton.pack()
    
    

def resize6():
    empmodbox.withdraw()
    win2.deiconify()

def back6():
    D=Button(empmodbox,text='Back',fg='black',bg='#EFE0E0',command=resize6)
    D.pack()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            MODIFY TABLE PAY

def psearch():
    global psearchentry,psearched,penterbutton
    q=''
    psearched=psearchentry.get()
    if psearched!='':
        messagebox.showinfo("Updation Status", "Searching for record..")
        q="select payid from pay"
        cur.execute(q)
        res=cur.fetchall()
        if psearched.isdigit()==True:
            if (int(psearched),) not in res:
                messagebox.showerror('Updation Status',"Pay Details don't exist")
                
            else:
                q="select * from pay where payid=%s"       
                v=(int(psearched),)
                cur.execute(q,v)
                res=cur.fetchall()
                if not res:
                    pass
            
                else:
            
                    trv=ttk.Treeview(paymodbox, selectmode='browse',height=1)
                    s = ttk.Style()
                    s.theme_use('clam')
                    s.configure('Treeview.Heading', background="#EFE0E0")
                    trv.pack()
                    trv['columns']=('1','2','3','4','5','6')
                    trv['show']='headings'
                    trv.column('1',width=75,anchor='c',stretch=NO)
                    trv.column('2',width=100,anchor='c')
                    trv.column('3',width=150,anchor='c')
                    trv.column('4',width=150,anchor='c')
                    trv.column('5',width=70,anchor='c')
                    trv.column('6',width=100,anchor='c')
                    trv.heading('1',text='Pay ID')
                    trv.heading('2',text='Basic Pay')
                    trv.heading('3',text='Allowance')
                    trv.heading('4',text='Deduction')
                    trv.heading('5',text='Net Pay')
                    trv.heading('6',text='Employee ID')
                    
                    for dt in res:
                        trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
                    pchoose_column()
                    
                    def disable_entry():
                        global psearchentry
                        psearchentry.config(state= "disabled")
                    disable_entry()
                    penterbutton["state"]="disable"
        else:
            messagebox.showerror('Error',"Enter Integer(3) Datatype")
     
    else:
        messagebox.showerror('Error',"Enter Pay ID")
        
def pchoose_column():
    global paymodbox,drop2,pentrybutton2,psearched
    
    if psearched!='':
        Label(paymodbox,text='',fg='#ce3531',bg='#ce3531').pack()
        columnlabel=Label(paymodbox,text="Enter Column To Be Modified",bg='#ce3531',fg='#D9D9AE',font='Times 14')
        columnlabel.pack()
        Label(paymodbox,text='',fg='#ce3531',bg='#ce3531').pack()
        drop2=ttk.Combobox(paymodbox,value=['Search by..','Basic Pay','Allowance','Deduction'])
        drop2.current(0)
        drop2.pack()
        pentrybutton2=Button(paymodbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=pmodifycolumn)
        pentrybutton2.pack()
    else:
        messagebox.showerror("Error","Enter Pay ID")
        
def pmodifycolumn():
    global paymodbox,drop2,pentrybutton2,pmodifybutton,pcname,pmodify_entry
    pcname=drop2.get()
    if pcname!='' and pcname!='Search by..' and pcname in ['Basic Pay','Allowance','Deduction']:
        modifylabel=Label(paymodbox,text="Enter New Value",bg='#ce3531',fg='#D9D9AE',font='Times 14')
        modifylabel.pack()
        pmodify_entry=Entry(paymodbox,width=30)
        pmodify_entry.pack()
        pmodifybutton=Button(paymodbox,text='Modify',fg='black',bg='#EFE0E0',command=updation)
        pmodifybutton.pack()
        pentrybutton2["state"]="disable"
    else:
        messagebox.showerror("Error","Select a Column From Drop-down Menu")
        
def pupdation2():
    global paymodbox,q,pupdatedvalue,psearched
    v=(pupdatedvalue,psearched)
    cur.execute(q,v)
    con.commit()
    #update net pay
    q="update pay set netpay=basicpay+allowance-deduction where payid=%s"
    v=(int(psearched),)
    cur.execute(q,v)
    con.commit()
    messagebox.showinfo("Updation Status","Record Modified")
    pmodifybutton["state"]="disable"
    def disable_entry():
        global pmodify_entry
        pmodify_entry.config(state= "disabled")
    disable_entry()
    q="select * from pay where payid=%s"            
    v=(int(psearched),)
    cur.execute(q,v)
    res=cur.fetchall()
    if not res:
        pass
    else:
        trv=ttk.Treeview(paymodbox, selectmode='browse',height=1)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#EFE0E0")
        trv.pack()
        trv['columns']=('1','2','3','4','5','6')
        trv['show']='headings'
        trv.column('1',width=75,anchor='c',stretch=NO)
        trv.column('2',width=100,anchor='c')
        trv.column('3',width=150,anchor='c')
        trv.column('4',width=150,anchor='c')
        trv.column('5',width=70,anchor='c')
        trv.column('6',width=100,anchor='c')
        trv.heading('1',text='Pay ID')
        trv.heading('2',text='Basic Pay')
        trv.heading('3',text='Allowance')
        trv.heading('4',text='Deduction')
        trv.heading('5',text='Net Pay')
        trv.heading('6',text='Employee ID')  
        for dt in res:
            trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
        back7()
        
def pupdation():
    global paymodbox,pmodify_entry,pmb,pupdatedvalue,pcname,q,pitemsearch,psearched
    q=''
    pupdatedvalue=pmodify_entry.get()
    if pupdatedvalue=='':
        messagebox.showerror('Error','Enter New Value')
    else:
        if pcname=='Basic Pay':
            if pupdatedvalue.isdigit()==True:
                q="UPDATE Pay SET BasicPay=%s WHERE Payid=%s"
                pupdation2()
            else:
                messagebox.showerror("Error","Enter Integer Type")

        elif pcname=='Allowance':
            if pupdatedvalue.isdigit()==True:
                q="UPDATE Pay SET Allowance=%s WHERE Payid=%s"
                pupdation2()
            else:
                messagebox.showerror("Error","Enter Integer Type")

        elif pcname=='Deduction':
            if pupdatedvalue.isdigit()==True:
                q="select basicpay from pay where payid=%s"
                v=(psearched,)
                cur.execute(q,v)
                res=cur.fetchone()
                print(res)
                if int(pupdatedvalue)<(res[0]*0.05):
                    q="UPDATE Pay SET Deduction=%s WHERE Payid=%s"
                    pupdation2()
                else:
                    messagebox.showerror("Error","Enter Less than 5% of Basic Pay")
            else:
                messagebox.showerror("Error","Enter Integer Type")


def ModifyPay():
    global paymodbox,psearchentry,penterbutton
    paymodbox=Tk()
    paymodbox.title('MODIFY DETAILS')
    paymodbox.geometry("700x630")
    paymodbox.resizable(True,True)
    paymodbox.configure(bg='#ce3531')
    label=Label(paymodbox,text='MODIFY EMPLOYEE DETAILS',bg='#ce3531',fg='#D9D9AE',font='Times 30').pack(pady=10)
    Label(paymodbox,text='Enter Pay ID to search:',bg='#ce3531',fg='#D9D9AE',font='Times 16').pack(pady=10)
    psearchentry=Entry(paymodbox,width=30)
    psearchentry.pack(pady=10)
    penterbutton=Button(paymodbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=psearch)
    penterbutton.pack()
    
    

def resize7():
    global paymodbox
    paymodbox.withdraw()
    win2.deiconify()

def back7():
    D=Button(paymodbox,text='Back',fg='black',bg='#EFE0E0',command=resize7)
    D.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            MODIFY TABLE AWARDS

def asearch():
    global asearchentry,asearched,aenterbutton
    q=''
    asearched=asearchentry.get()
    if asearched!='':
        messagebox.showinfo("Updation Status", "Searching for record..")
        q="select awardid from awards"
        cur.execute(q)
        res=cur.fetchall()
        if asearched.isdigit()==True:
            if (int(asearched),) not in res:
                messagebox.showerror('Updation Status',"Award Details don't exist")
            
            else:
                q="select * from awards where awardid=%s"       
                v=(int(asearched),)
                cur.execute(q,v)
                res=cur.fetchall()
                if not res:
                    pass
            
                else:
            
                    trv=ttk.Treeview(awardmodbox, selectmode='browse',height=1)
                    s = ttk.Style()
                    s.theme_use('clam')
                    s.configure('Treeview.Heading', background="#EFE0E0")
                    trv.pack()
                    trv['columns']=('1','2','3','4')
                    trv['show']='headings'
                    trv.column('1',width=75,anchor='c',stretch=NO)
                    trv.column('2',width=100,anchor='c')
                    trv.column('3',width=170,anchor='c')
                    trv.column('4',width=150,anchor='c')
                    trv.heading('1',text='Award ID')
                    trv.heading('2',text='Year')
                    trv.heading('3',text='Particulars')
                    trv.heading('4',text='Employee ID')
                    
                    for dt in res:
                        trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3]))
                    achoose_column()
                    
                    def disable_entry():
                        global asearchentry
                        asearchentry.config(state= "disabled")
                    disable_entry()
                    aenterbutton["state"]="disable"
        else:
            messagebox.showerror('Error',"Enter Integer(3) datatype")

    else:
        messagebox.showerror('Error',"Enter Award ID")
        
def achoose_column():
    global awardmodbox,drop2,aentrybutton2,asearched
    if asearched!='':
        Label(awardmodbox,text='',fg='#ce3531',bg='#ce3531').pack()
        columnlabel=Label(awardmodbox,text="Enter Column To Be Modified",bg='#ce3531',fg='#D9D9AE',font='Times 14')
        columnlabel.pack()
        Label(awardmodbox,text='',fg='#ce3531',bg='#ce3531').pack()
        drop2=ttk.Combobox(awardmodbox,value=['Search by..','Year','Particulars'])
        drop2.current(0)
        drop2.pack()
        aentrybutton2=Button(awardmodbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=amodifycolumn)
        aentrybutton2.pack()
    else:
        messagebox.showerror("Error","Enter Award ID")
        
def amodifycolumn():
    global awardmodbox,drop2,aentrybutton2,amodifybutton,acname,amodify_entry
    acname=drop2.get()
    if acname!='' and acname!='Search by..' and acname in ['Year','Particulars']:
        modifylabel=Label(awardmodbox,text="Enter New Value",bg='#ce3531',fg='#D9D9AE',font='Times 14')
        modifylabel.pack()
        amodify_entry=Entry(awardmodbox,width=30)
        amodify_entry.pack()
        amodifybutton=Button(awardmodbox,text='Modify',fg='black',bg='#EFE0E0',command=aupdation)
        amodifybutton.pack()
        aentrybutton2["state"]="disable"
    else:
        messagebox.showerror("Error","Select a Column From Drop-down Menu")
    
def aupdation2():
    global awardmodbox,q,aupdatedvalue,asearched
    v=(aupdatedvalue,asearched)
    cur.execute(q,v)
    con.commit()
    messagebox.showinfo("Updation Status","Record Modified")
    amodifybutton["state"]="disable"
    def disable_entry():
        global amodify_entry
        amodify_entry.config(state= "disabled")
    disable_entry()
    q="select * from awards where awardid=%s"            
    v=(int(asearched),)
    cur.execute(q,v)
    res=cur.fetchall()
    if not res:
        pass
    else:
        trv=ttk.Treeview(awardmodbox, selectmode='browse',height=1)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#EFE0E0")
        trv.pack()
        trv['columns']=('1','2','3','4')
        trv['show']='headings'
        trv.column('1',width=75,anchor='c',stretch=NO)
        trv.column('2',width=100,anchor='c')
        trv.column('3',width=170,anchor='c')
        trv.column('4',width=150,anchor='c')
        trv.heading('1',text='Award ID')
        trv.heading('2',text='Year')
        trv.heading('3',text='Particulars')
        trv.heading('4',text='Employee ID')
        for dt in res:
            trv.insert('','end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3]))
        back8()
        
def aupdation():
    global awardmodbox,amodify_entry,amb,aupdatedvalue,acname,q,aitemsearch,asearched
    q=''
    aupdatedvalue=amodify_entry.get()
    if aupdatedvalue=='':
        messagebox.showerror('Error','Enter New Value')
    else:
        if acname=='Year':
            if aupdatedvalue.isdigit()==True and (len(aupdatedvalue)==4):
                q="UPDATE Awards SET Year=%s WHERE AwardID=%s"
                aupdation2()
            else:
                messagebox.showerror("Error","Enter Year as Integer(4)")

        elif acname=='Particulars':
            if aupdatedvalue!='':
                q="UPDATE Awards SET Particulars=%s WHERE AwardID=%s"
                aupdation2()
            else:
                messagebox.showerror('Error','Enter Award Particulars')

def ModifyAwards():
    global awardmodbox,asearchentry,aenterbutton
    awardmodbox=Tk()
    awardmodbox.title('MODIFY DETAILS')
    awardmodbox.geometry("700x630")
    awardmodbox.resizable(True,True)
    awardmodbox.configure(bg='#ce3531')
    label=Label(awardmodbox,text='MODIFY EMPLOYEE DETAILS',bg='#ce3531',fg='#D9D9AE',font='Times 30').pack(pady=10)
    Label(awardmodbox,text='Enter Award ID to search:',bg='#ce3531',fg='#D9D9AE',font='Times 16').pack(pady=10)
    asearchentry=Entry(awardmodbox,width=30)
    asearchentry.pack(pady=10)
    aenterbutton=Button(awardmodbox,text='Enter',bg='#EFE0E0',fg='black',width=7,command=asearch)
    aenterbutton.pack()
    
    

def resize8():
    awardmodbox.withdraw()
    win2.deiconify()

def back8():
    D=Button(awardmodbox,text='Back',fg='black',bg='#EFE0E0',command=resize8)
    D.pack()



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   DISPLAY BASED ON DEPARTMENT

def dept_search():
    global searchentry,ddb,drop2
    searched=drop2.get()
    try:
        if searched!='' and searched!='Search by..' and searched in ['Marketing','Administration','Teaching Staff','Non-Teaching Staff']:
            q="SELECT eno,ename,department FROM employee WHERE Department=%s"
            v=(searched,)
            cur.execute(q,v)
            res=cur.fetchall()
            trv=ttk.Treeview(ddisp, selectmode='browse')
            s = ttk.Style()
            s.theme_use('clam')
            s.configure('Treeview.Heading', background="#EFE0E0")
            trv.pack()
            trv['columns']=('1','2','3')
            trv['show']='headings'
            trv.column('1',width=75,anchor='c')
            trv.column('2',width=100,anchor='c')
            trv.column('3',width=110,anchor='c')
            trv.heading('1',text='Employee ID')
            trv.heading('2',text='Name')
            trv.heading('3',text='Department Name')

            for dt in res:
                trv.insert('','end',iid=dt[1],values=(dt[0],dt[1],dt[2]))
            ddb["state"]="disable"
        else:
            messagebox.showerror('Error','Select A Column')
    except ValueError:
        messagebox.showerror("Error","Enter Integer Value")

def DisplayDept():
    global ddisp,searchentry,ddb,drop2
    ddisp=Tk()
    win2.withdraw()
    ddisp.title('DISPLAY DEPARTMENT DETAILS')
    ddisp.geometry("700x630")
    ddisp.resizable(True,True)
    ddisp.configure(bg='#ce3531')
    label=Label(ddisp,text='DISPLAY BASED ON DEPARTMENT',fg='#D9D9AE',bg='#ce3531',font='Times 30').pack()
    Label(ddisp,text='Enter Department Name to search:',fg='#D9D9AE',bg='#ce3531',font='Times 16').pack(pady=10)
    drop2=ttk.Combobox(ddisp,value=['Search by..','Marketing','Administration','Teaching Staff','Non-Teaching Staff'],width=27)
    drop2.current(0)
    drop2.pack()
    Label(ddisp,text='',fg='#ce3531',bg='#ce3531').pack()
    ddb=Button(ddisp,text='Enter',bg='#EFE0E0',fg='black',width=7,command=dept_search)
    ddb.pack()
    back9()


def resize9():
    ddisp.withdraw()
    win2.deiconify()

def back9():
    A=Button(ddisp,text='Back',fg='black',bg='#EFE0E0',command=resize9)
    A.pack()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   DISPLAY BASED ON AWARDS

def award_search():
    global searchentry,adb
    searched=searchentry.get()
    try:
        if searched!='':
            q="SELECT eno,ename,department,awardid,year,particulars FROM employee natural join awards WHERE AwardID=%s"
            v=(searched,)
            cur.execute(q,v)
            res=cur.fetchall()
            if not res:
                messagebox.showerror('Error',"Award doesn't exist")
            else:
                trv=ttk.Treeview(adisp, selectmode='browse')
                s = ttk.Style()
                s.theme_use('clam')
                s.configure('Treeview.Heading', background="#EFE0E0")
                trv.pack()
                trv['columns']=('1','2','3','4','5','6')
                trv['show']='headings'
                trv.column('1',width=75,anchor='c')
                trv.column('2',width=100,anchor='c')
                trv.column('3',width=110,anchor='c')
                trv.column('4',width=60,anchor='c')
                trv.column('5',width=60,anchor='c')
                trv.column('6',width=170,anchor='c')
                trv.heading('1',text='Employee ID')
                trv.heading('2',text='Name')
                trv.heading('3',text='Department Name')
                trv.heading('4',text='Award ID')
                trv.heading('5',text='Year')
                trv.heading('6',text='Particulars')

                for dt in res:
                    trv.insert('','end',iid=dt[1],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
                def disable_entry():
                    global searchentry
                    searchentry.config(state= "disabled")
                disable_entry()
                adb["state"]="disable"
        else:
            messagebox.showerror('Error','ID not entered')
    except ValueError:
        messagebox.showerror("Error","Enter Integer Value")           
    
def DisplayAwards():
    global adisp,searchentry,adb
    adisp=Tk()
    win2.withdraw()
    adisp.title('DISPLAY AWARD DETAILS')
    adisp.geometry("700x630")
    adisp.resizable(True,True)
    adisp.configure(bg='#ce3531')
    label=Label(adisp,text='DISPLAY BASED ON AWARDS',fg='#D9D9AE',bg='#ce3531',font='Times 30').pack()
    Label(adisp,text='Enter Award ID to search:',fg='#D9D9AE',bg='#ce3531',font='Times 16').pack(pady=10)
    searchentry=Entry(adisp,width=30)
    searchentry.pack(pady=10)
    adb=Button(adisp,text='Enter',bg='#EFE0E0',fg='black',width=7,command=award_search)
    adb.pack()
    back10()


def resize10():
    adisp.withdraw()
    win2.deiconify()

def back10():
    A=Button(adisp,text='Back',fg='black',bg='#EFE0E0',command=resize9)
    A.pack()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       DISPLAY PAY DETAILS OF EMPLOYEE

def sal_search():
    global searchentry
    searched=searchentry.get()
    try:
        if searched!='':
            q="SELECT eno,ename,department,payid,basicpay,allowance,deduction,netpay FROM employee natural join pay WHERE Eno=%s"
            v=(searched,)
            cur.execute(q,v)
            res=cur.fetchall()
            if not res:
                messagebox.showerror('Error',"Employee doesn't exist")
            else:
                trv=ttk.Treeview(sdisp, selectmode='browse',height=1)
                s = ttk.Style()
                s.theme_use('clam')
                s.configure('Treeview.Heading', background="#EFE0E0")
                trv.pack()
                trv['columns']=('1','2','3','4','5','6','7','8')
                trv['show']='headings'
                trv.column('1',width=75,anchor='c')
                trv.column('2',width=100,anchor='c')
                trv.column('3',width=110,anchor='c')
                trv.column('4',width=50,anchor='c')
                trv.column('5',width=60,anchor='c')
                trv.column('6',width=65,anchor='c')
                trv.column('7',width=65,anchor='c')
                trv.column('8',width=60,anchor='c')
                trv.heading('1',text='Employee ID')
                trv.heading('2',text='Name')
                trv.heading('3',text='Department Name')
                trv.heading('4',text='Pay ID')
                trv.heading('5',text='Basic Pay')
                trv.heading('6',text='Allowance')
                trv.heading('7',text='Deduction')
                trv.heading('8',text='Net Pay')

                for dt in res:
                    trv.insert('','end',iid=dt[1],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
                def disable_entry():
                    global searchentry
                    searchentry.config(state= "disabled")
                disable_entry()
                dsb["state"]="disable"
                
        else:
            messagebox.showerror('Error','ID not entered')
    except ValueError:
        messagebox.showerror("Error","Enter Integer Value")

    
def DisplaySal():
    global sdisp,searchentry,dsb
    sdisp=Tk()
    win2.withdraw()
    sdisp.title('DISPLAY PAY DETAILS')
    sdisp.geometry("700x630")
    sdisp.resizable(True,True)
    sdisp.configure(bg='#ce3531')
    label=Label(sdisp,text='DISPLAY PAY DETAILS',fg='#D9D9AE',bg='#ce3531',font='Times 30').pack()
    Label(sdisp,text='Enter Employee ID to search:',fg='#D9D9AE',bg='#ce3531',font='Times 16').pack(pady=10)
    searchentry=Entry(sdisp,width=30)
    searchentry.pack(pady=10)
    dsb=Button(sdisp,text='Enter',bg='#EFE0E0',fg='black',width=7,command=sal_search)
    dsb.pack()
    back11()


def resize11():
    sdisp.withdraw()
    win2.deiconify()

def back11():
    S=Button(sdisp,text='Back',fg='black',bg='#EFE0E0',command=resize10)
    S.pack()
    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#======================================================================================================================================================================
#-----------------------------------------------------------------------CSV--------------------------------------------------------------------------------------------
#function to incorporate csv files 
def close_abt():
    abt_pg.withdraw()
    window.deiconify()
def csvv():
    global abt_pg,window
    window.withdraw()
    abt_pg = Toplevel(window)
    abt_pg.title('About')
    abt_pg.geometry('1100x700')
    abt_pg.configure(bg='gray98')
    abt_pg.resizable(False,False)


    label = Label(abt_pg,fg ='#ce3531',bg='gray98',text="ABOUT OUR PROJECT",font=('Times New Roman',23,'bold'))
    label.place(x=352,y=10)

    # FOR TABLE EMPLOYEE
    emp_label= Label(abt_pg,fg ='#ce3531',bg='gray98',text="EMPLOYEE",font=('Times New Roman',16,'bold'))
    emp_label.place(x=50,y=70)
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading', background="gray98")
    etree = ttk.Treeview(abt_pg,selectmode='browse',height=8)
    etree.place(x=50,y=100)
    etree['show']='headings'
    etree['columns']=('1','2','3')
    etree.column('1',anchor=W,width=80)
    etree.column('2',anchor=W,width=110)
    etree.column('3',anchor=W,width=250)
    etree.heading('1',text='Field Name',anchor=W)
    etree.heading('2',text='Datatype',anchor=W)
    etree.heading('3',text='Task',anchor=W)

    f = open("employee.csv")
    robj = csv.reader(f)
    for i in robj:
        etree.insert(parent='',index='end', iid=i,text='',values=(i[0],i[1],i[2]))

    # FOR TABLE PAY
    pay_label= Label(abt_pg,fg ='#ce3531',bg='gray98',text="PAY",font=('Times New Roman',16,'bold'))
    pay_label.place(x=600,y=70)
    ptree = ttk.Treeview(abt_pg,selectmode='browse',height=8)
    ptree.place(x=600,y=100)
    ptree['show']='headings'
    ptree['columns']=('1','2','3')
    ptree.column('1',anchor=W,width=80)
    ptree.column('2',anchor=W,width=110)
    ptree.column('3',anchor=W,width=250)
    ptree.heading('1',text='Field Name',anchor=W)
    ptree.heading('2',text='Datatype',anchor=W)
    ptree.heading('3',text='Task',anchor=W)

    f = open("pay.csv")
    robj = csv.reader(f)
    for i in robj:
        ptree.insert(parent='',index='end', iid=i,text='',values=(i[0],i[1],i[2]))

# FOR TABLE AWARDS
    pay_label= Label(abt_pg,fg ='#ce3531',bg='gray98',text="AWARD",font=('Times New Roman',16,'bold'))
    pay_label.place(x=320,y=370)
    atree = ttk.Treeview(abt_pg,selectmode='browse',height=8)
    atree.place(x=320,y=400)
    atree['show']='headings'
    atree['columns']=('1','2','3')
    atree.column('1',anchor=W,width=80)
    atree.column('2',anchor=W,width=110)
    atree.column('3',anchor=W,width=250)
    atree.heading('1',text='Field Name',anchor=W)
    atree.heading('2',text='Datatype',anchor=W)
    atree.heading('3',text='Task',anchor=W)

    f = open("awards.csv")
    robj = csv.reader(f)
    for i in robj:
        atree.insert(parent='',index='end', iid=i,text='',values=(i[0],i[1],i[2]))

    back_btn = Button(abt_pg,width=8, text='BACK',fg ='#ce3531',bg='white',font=('Times New Roman',10,'bold'),command=close_abt)
    back_btn.place(x=520,y=640)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                        CREATING LOGIN WINDOW
window=Tk()
window.resizable(False,False)
window.title('EMPLOYEE MANAGEMENT SYSTEM')
window.geometry('1200x700')
bg=PhotoImage(file="employee2new.png")
piclabel=Label(window,image=bg)
piclabel.place(x=0,y=0,relwidth=1,relheight=1)
Label(window,text='EMPLOYEE MANAGEMENT SYSTEM',font=('Times New Roman',53,),fg='#ce3531',justify='center',bg='gray98').pack()

abt_button=Button(window,text=' About Our Database ',bg='gray98',fg='#ce3531',command=csvv,font=('Times New Roman',18,))
abt_button.place(x=840,y=560,width=300,height=50)

#USER LOG IN
username=Label(window,text=' Username ',font=('Times New Roman',23,),fg='#ce3531',bg='gray98')
username.place(x=60,y=200)
uname=Entry(window)
uname.place(x=280,y=200,width=150,height=40)
password=Label(window,text=' Password ',font=('Times New Roman',23,),fg='#ce3531',bg='gray98')
password.place(x=790,y=200)
passw=Entry(window,show="*")
passw.place(x=1000,y=200,width=150,height=40)
login=Button(window,text=' SIGN IN ',bg='gray98',fg='#ce3531',command=return_entry,font=('Times New Roman',23,))

uname.bind('<Return>', return_entry) 

login.place(x=540,y=400,width=150,height=40)



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()


