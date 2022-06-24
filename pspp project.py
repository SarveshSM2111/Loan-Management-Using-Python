from tkinter import *
from tkinter import ttk,messagebox
import pymysql


root=Tk()
root.title('Loan Management System')
root.geometry('1350x720')
title=Label(root,text='Loan Management System',font=('times new roman',40,'bold'),bg='yellow',fg='red',bd=10,relief=GROOVE)
title.pack(fill=X)
#===============VARIABLES======================
loanid=StringVar()
name=StringVar()
aadhar=StringVar()
add=StringVar()
pin=StringVar()
amount=StringVar()
mpay=StringVar()
tpay=StringVar()
rate=StringVar()
years=StringVar()
mob=StringVar()
#================Functions===================
def total():
    p=int(amount.get())
    r=float(rate.get())
    y=int(years.get())
    i=(p*r*y*12)/100
    m=(p+i)/(y*12)
    mpay.set(str(round(m,2)))
    tpay.set(str(p+i))
def addrecord():
    if loanid.get()=='':
        messagebox.showerror('Error','Customer Details Are Compulsary')
    else:
        total()
        db=pymysql.connect(host='localhost',user='root',password='hello123',database='emp')
        cursor=db.cursor()
        cursor.execute('select * from customer')
        rows=cursor.fetchall()
        for r in rows:
            if r[0]==loanid.get():
                messagebox.showerror('Error','Duplicate entry not allowed')
                return
        cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(loanid.get(),
                                                                      name.get(),
                                                                      years.get(),
                                                                      rate.get(),
                                                                      mpay.get(),
                                                                      tpay.get(),
                                                                      mob.get(),
                                                                      amount.get(),
                                                                      aadhar.get(),
                                                                      add.get(),
                                                                      pin.get()))
        db.commit()
        fetch()
        db.close()
def fetch():
    db=pymysql.connect(host='localhost',user='root',password='hello123',database='emp')
    cursor=db.cursor()
    cursor.execute('select * from customer')
    rows=cursor.fetchall()
    if len(rows)!=0:
        employee_table.delete(*employee_table.get_children())
        for r in rows:
            employee_table.insert('',END,values=r)
    db.commit()
    db.close()


def getcursor(ev):
    cur_row=employee_table.focus()
    content=employee_table.item(cur_row)
    row=content['values']
    loanid.set(row[0])
    name.set(row[1])
    years.set(row[2])
    rate.set(row[3])
    mpay.set(row[4])
    tpay.set(row[5])
    mob.set(row[6])
    amount.set(row[7])
    aadhar.set(row[8])
    add.set(row[9])
    pin.set(row[10])

def update():
    if loanid.get()=='':
        messagebox.showerror('Error','Input Data For Updation')
    else:
        db=pymysql.connect(host='localhost',user='root',password='hello123',database='emp')
        cursor=db.cursor()
        cursor.execute('update customer set name=%s,years=%s,interest_rate=%s,monthly_payment=%s,total_payment=%s,mobile=%s,amount=%s,aadhar=%s,address=%s,pincode=%s where loan_id=%s',(name.get(),
                                                                                                                                                                                         years.get(),
                                                                                                                                                                                         rate.get(),
                                                                                                                                                                                         mpay.get(),
                                                                                                                                                                                         tpay.get(),
                                                                                                                                                                                         mob.get(),
                                                                                                                                                                                         amount.get(),
                                                                                                                                                                                         aadhar.get(),
                                                                                                                                                                                         add.get(),
                                                                                                                                                                                         pin.get(),
                                                                                                                                                                                         loanid.get()))
        messagebox.showinfo('Info','Record updated successfully')
        db.commit()
        db.close()
        fetch()
        reset()

def delete():
    if loanid.get()=='':
        messagebox.showerror('Error','Input Data For Deletion')
    else:
        db=pymysql.connect(host='localhost',user='root',password='hello123',database='emp')
        cursor=db.cursor()
        cursor.execute('delete from customer where loan_id=%s',(loanid.get()))
        db.commit()
        db.close()
        fetch()
        messagebox.showinfo('Info','Record deleted successfully')
        reset()

def reset():
    loanid.set('')
    name.set('')
    aadhar.set('')
    add.set('')
    pin.set('') 
    amount.set('')
    mpay.set('')
    tpay.set('')
    rate.set('')
    years.set('')
    mob.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit?'):
        root.destroy()
    else:
        pass
    
        
    
                                                                                                                                                                                        
                       
        
    

#=============DETAIL FRAME========================
detail_f=Frame(root,bd=4,relief=RIDGE)
detail_f.place(x=10,y=90,width=520,height=620)

lbl_id=Label(detail_f,text='Loan Id',font=('times new roman',18,'bold'))
lbl_id.grid(row=0,column=1,padx=20,pady=10,sticky='w')
txt_id=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=loanid)
txt_id.grid(row=0,column=2,padx=20,pady=10,sticky='w')

lbl_name=Label(detail_f,text='Full Name',font=('times new roman',18,'bold'))
lbl_name.grid(row=1,column=1,padx=20,pady=10,sticky='w')
txt_name=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=name)
txt_name.grid(row=1,column=2,padx=20,pady=10,sticky='w')

lbl_mob=Label(detail_f,text='Mobile Number',font=('times new roman',18,'bold'))
lbl_mob.grid(row=2,column=1,padx=20,pady=10,sticky='w')
txt_mob=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=mob)
txt_mob.grid(row=2,column=2,padx=20,pady=10,sticky='w')

lbl_adhar=Label(detail_f,text='Aadhar Number',font=('times new roman',18,'bold'))
lbl_adhar.grid(row=3,column=1,padx=20,pady=10,sticky='w')
txt_adhar=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=aadhar)
txt_adhar.grid(row=3,column=2,padx=20,pady=10,sticky='w')

lbl_address=Label(detail_f,text='Address',font=('times new roman',18,'bold'))
lbl_address.grid(row=4,column=1,padx=20,pady=10,sticky='w')
txt_address=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=add)
txt_address.grid(row=4,column=2,padx=20,pady=10,sticky='w')

lbl_pin=Label(detail_f,text='Pincode',font=('times new roman',18,'bold'))
lbl_pin.grid(row=5,column=1,padx=20,pady=10,sticky='w')
txt_pin=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=pin)
txt_pin.grid(row=5,column=2,padx=20,pady=10,sticky='w')

lbl_amt=Label(detail_f,text='Amount Of Loan',font=('times new roman',18,'bold'))
lbl_amt.grid(row=6,column=1,padx=20,pady=10,sticky='w')
txt_amt=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=amount)
txt_amt.grid(row=6,column=2,padx=20,pady=10,sticky='w')

lbl_nyrs=Label(detail_f,text='Number Of Years',font=('times new roman',18,'bold'))
lbl_nyrs.grid(row=7,column=1,padx=20,pady=10,sticky='w')
txt_nyrs=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=years)
txt_nyrs.grid(row=7,column=2,padx=20,pady=10,sticky='w')

lbl_irate=Label(detail_f,text='Interest Rate',font=('times new roman',18,'bold'))
lbl_irate.grid(row=8,column=1,padx=20,pady=10,sticky='w')
txt_irate=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=rate)
txt_irate.grid(row=8,column=2,padx=20,pady=10,sticky='w')


lbl_mp=Label(detail_f,text='Monthly Payment',font=('times new roman',18,'bold'))
lbl_mp.grid(row=9,column=1,padx=20,pady=10,sticky='w')
txt_mp=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=mpay)
txt_mp.grid(row=9,column=2,padx=20,pady=10,sticky='w')

lbl_tp=Label(detail_f,text='Total Payment',font=('times new roman',18,'bold'))
lbl_tp.grid(row=10,column=1,padx=20,pady=10,sticky='w')
txt_tp=Entry(detail_f,font=('times new roman',18,'bold'),width=18,bd=3,relief=SUNKEN,textvariable=tpay)
txt_tp.grid(row=10,column=2,padx=20,pady=10,sticky='w')

#==============Right Frame=================

Rframe=Frame(root,bd=4,relief=RIDGE)
Rframe.place(x=535,y=90,width=800,height=520)

yscroll=Scrollbar(Rframe,orient=VERTICAL)

employee_table=ttk.Treeview(Rframe,column=('loanid','name','years','rate','mp','tp','mob'),yscrollcommand=yscroll)
yscroll.pack(side=RIGHT,fill=Y)
yscroll.config(command=employee_table.yview)
employee_table.heading('loanid',text='Loan ID')
employee_table.heading('name',text='Full Name')
employee_table.heading('years',text='Number Of Years')
employee_table.heading('rate',text='Interest Rate')
employee_table.heading('mp',text='Monthly Payment')
employee_table.heading('tp',text='Total Payment')
employee_table.heading('mob',text='Mobile Number')
employee_table['show']='headings'

employee_table.column('loanid',width=100)
employee_table.column('name',width=100)
employee_table.column('years',width=100)
employee_table.column('rate',width=100)
employee_table.column('mp',width=100)
employee_table.column('tp',width=100)
employee_table.column('mob',width=100)

employee_table.pack(fill=BOTH,expand=1)
fetch()
employee_table.bind('<ButtonRelease-1>',getcursor)

#===========buttonframe================================
btnframe=Frame(root,bd=4,relief=RIDGE)
btnframe.place(x=535,y=610,width=800,height=100)

btn1=Button(btnframe,text='Add Record',font='arial 18 bold',width=9,command=addrecord)
btn1.grid(row=0,column=0,padx=7,pady=10)

btn2=Button(btnframe,text='Update',font='arial 18 bold',width=9,command=update)
btn2.grid(row=0,column=1,padx=7,pady=10)

btn3=Button(btnframe,text='Delete',font='arial 18 bold',width=9,command=delete)
btn3.grid(row=0,column=2,padx=7,pady=10)

btn4=Button(btnframe,text='Reset',font='arial 18 bold',width=9,command=reset)
btn4.grid(row=0,column=3,padx=7,pady=10)

btn5=Button(btnframe,text='Exit',font='arial 18 bold',width=9,command=exit)
btn5.grid(row=0,column=4,padx=7,pady=10)














