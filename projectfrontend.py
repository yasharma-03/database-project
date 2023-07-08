'''
a program that stores this book information:
title,author
year,ID

user can:
view all records
search an entry
add entry
update entry
delete
close
'''
from tkinter import *
import backendproject2

def get_selected_row(event):
        try:
                global selectedtuple
                index=list1.curselection()[0]
                #print(index)
                selectedtuple=list1.get(index)
                e1.delete(0,END)
                e1.insert(END,selectedtuple[0])
                e2.delete(0,END)
                e2.insert(END,selectedtuple[1])
                e3.delete(0,END)
                e3.insert(END,selectedtuple[2])
                e4.delete(0,END)
                e4.insert(END,selectedtuple[3])
        except IndexError:
                pass

def viewcommand():
        list1.delete(0,END)
        for row in backendproject2.view():
                list1.insert(END,row)

def searchcommand():
        list1.delete(0,END)
        for row in backendproject2.search(title_text.get(),author_text.get(),year_text.get(),id_text.get()):
                list1.insert(END,row)

def insertcommand():
        list1.delete(0,END)
        backendproject2.insert(title_text.get(),author_text.get(),year_text.get(),id_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),id_text.get()))

def deletecommand():
        backendproject2.delete(selectedtuple[3])
        
def updatecommand():
        print('the title ,author and year can be updated')
        backendproject2.update(id_text.get(),title_text.get(),author_text.get(),year_text.get())

                

window=Tk()

window.title('BOOKSHOP DATABASE')

l1=Label(window,text='Title',fg='black')
l1.grid(row=0,column=0)

l2=Label(window,text='Author',fg='black')
l2.grid(row=0,column=2)

l3=Label(window,text='Year',fg='black')
l3.grid(row=1,column=0)

l4=Label(window,text='ID',fg='black')
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text,bg='white',fg='black')
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text,bg='white',fg='black')
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text,bg='white',fg='black')
e3.grid(row=1,column=1)

id_text=StringVar()
e4=Entry(window,textvariable=id_text,bg='white',fg='black')
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35,bg='light grey',fg='blue')
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text='View All',width=15,command=viewcommand,bg='dodger blue',fg='black')
b1.grid(row=2,column=3)

b2=Button(window,text='Search Entry',width=15,command=searchcommand,bg='dodger blue',fg='black')
b2.grid(row=3,column=3)

b3=Button(window,text='Add Entry',width=15,command=insertcommand,bg='dodger blue',fg='black')
b3.grid(row=4,column=3)

b4=Button(window,text='Update selected',width=15,command=updatecommand,bg='dodger blue',fg='black')
b4.grid(row=5,column=3)

b5=Button(window,text='Delete selected',width=15,command=deletecommand,bg='dodger blue',fg='black')
b5.grid(row=6,column=3)

b6=Button(window,text='Close',width=15,command=window.destroy,bg='dodger blue',fg='black')
b6.grid(row=7,column=3)


window.mainloop()
