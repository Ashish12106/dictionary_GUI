from tkinter import *
from tkinter import scrolledtext
import tkinter
from PyDictionary import PyDictionary

dic = PyDictionary()
window = Tk()

window.geometry('650x450')

window.config(bg= '#b9bdc4')

window.title('Py Dictionary')

def dict():
     if dic.meaning(word.get()) :
          meaning.insert(INSERT,dic.meaning(word.get()))
     else :
          meaning.insert(INSERT,"not found in dictionary")
     
     if dic.synonym(word.get()) :
          synonym.insert(INSERT,dic.synonym(word.get()))

     else :
          synonym.insert(INSERT,"not found in dictionary")
     
     if dic.antonym(word.get()) :
          antonym.insert(INSERT,dic.antonym(word.get()))
    
     else :
          antonym.insert(INSERT,"not found in dictionary ")


def clean():
     meaning.delete('1.0',END)
     synonym.delete('1.0',END)
     antonym.delete('1.0',END)

Label(window,text='Py Dictionary',font=('arial 20 bold'), fg='blue').pack(pady=10)

frame= Frame(window)

Label(frame,text='Type the Word = ',font=('arial 15 bold'), fg='orange').pack(side=LEFT)

word= Entry(frame , font=("Helvetica 10 bold"),width=30)

word.pack()
frame.pack(pady=10)

frame5=Frame(window)
Button(frame5,text='Submit ', font=('arial 15 bold'), fg='green', command=dict).pack(side=LEFT,padx=30)
Button(frame5,text='Clear ', font=('arial 15 bold'), fg='green', command=clean).pack()
frame5.pack(pady=10)

frame1 = Frame(window)

Label(frame1,text='Meaning :-  ',font=('arial 10 bold'), fg='orange').pack(side=LEFT)

meaning = scrolledtext.ScrolledText(frame1, font=('Helvetica 10 '),width=80,height=3)
meaning.insert(INSERT,"")
meaning.pack()
frame1.pack(pady=10)

frame2 = Frame(window)

Label(frame2,text='Synonym :-  ',font=('arial 10 bold'), fg='orange').pack(side=LEFT)

synonym = scrolledtext.ScrolledText(frame2, font=('Helvetica 10 '),width=80,height=3)
synonym.insert(INSERT,"")

synonym.pack()
frame2.pack(pady=10)


frame3 = Frame(window)

Label(frame3,text='Antonym :-  ',font=('arial 10 bold'), fg='orange').pack(side=LEFT)

antonym = scrolledtext.ScrolledText(frame3, font=('Helvetica 10 '),width=80,height=3)
antonym.insert(INSERT,"")

antonym.pack()
frame3.pack(pady=10)
  



window.mainloop()


