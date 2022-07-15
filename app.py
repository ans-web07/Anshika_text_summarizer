import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import*
import tkinter.filedialog
import nltk

#other pkgs
import time
timestr=time.strftime("%Y%m%d-%H%M%S")

#nlp pkgs
from spacy_summarization import text_summarizer
from nltk_summarization import nltk_summarizer

#web scrapping pkgs
from bs4 import BeautifulSoup
from urllib.request import urlopen


window=Tk()
window.title('Summarizer GUI')
window.geometry('700x500')

#style
style=ttk.Style(window)
style.configure('lefttab.TNotebook',tabposition='wn')

#tabs
tab_control=ttk.Notebook(window,style='lefttab.TNotebook')
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab4=ttk.Frame(tab_control)


#add tabs to interface
tab_control.add(tab1,text=f' {"Home":^50s}')
tab_control.add(tab2,text=f' {"File":^50s}')
tab_control.add(tab3,text=f' {"URL":^50s}')
tab_control.add(tab4,text=f' {"Comparer":^50s}')


#labels
label1=Label(tab1,text='Summaryzer',padx=70,pady=15,font=("Lucida", 25, "bold"))
label1.grid(column=0,row=0)
label2=Label(tab2,text='File processing',padx=50,pady=15,font=("Lucida", 25, "bold"))
label2.grid(column=1,row=0)
label3=Label(tab3,text='URL',padx=50,pady=15,font=("Lucida", 25, "bold"))
label3.grid(column=0,row=1)
label4=Label(tab4,text='Comparer',padx=50,pady=15,font=("Lucida", 25, "bold"))
label4.grid(column=1,row=0)


tab_control.pack(expand=1,fill='both')

#functions
def get_summary():
    raw_text=entry.get('1.0',tk.END)
    final_text=text_summarizer(raw_text)
    print(final_text)
    result='\nSummary: {}'.format(final_text)
    tab1_display.insert(tk.END,result)

def save_summary():
    raw_text=entry.get('1.0',tk.END)
    final_text=text_summarizer(raw_text)
    file_name='yoursummary'+timestr+'.txt'
    with open(file_name,'w') as f:
        f.write(final_text)
    result='\nName of file: {}'.format(file_name,final_text)
    tab1_display.insert(tk.END,result)
    


#clear function
def clear_text():
    entry.delete('1.0',END)

def clear_display_result():
    tab1_display.delete('1.0',END)

def clear_text_file():
    dispalyed_file.delete('1.0',END)

def clear_text_result():
    tab2_display_text.delete('1.0',END)

def clear_url_entry():
    url_entry.delete(0,END)

def clear_url_display():
    tab3_display_text.delete('1.0',END)

def clear_compare_text():
    entry1.delete('1.0',END)

def clear_compare_display_result():
    tab4_display.delete('1.0',END)




#open file function
def openfiles():
    file1=tkinter.filedialog.askopenfilename(filetype=(('Text Files',".txt"),("All files","*")))
    read_text=open(file1).read()
    dispalyed_file.insert(tk.END,read_text)

def get_file_summary():
    raw_text=dispalyed_file.get('1.0',tk.END)
    final_text=text_summarizer(raw_text)
    result='\nSummary: {}'.format(final_text)
    tab2_display_text.insert(tk.END,result)



#URL funcions
#fetch text from url
def get_text():
    raw_text=str(url_entry.get())
    page=urlopen(raw_text)
    soup=BeautifulSoup(page,'lxml')
    fetched_text=' '.join(map(lambda p:p.text,soup.find_all('p')))
    url_display.insert(tk.END,fetched_text)

def get_url_summary():
    raw_text=url_display.get('1.0',tk.END)
    final_text=text_summarizer(raw_text)
    result='\nSummary: {}'.format(final_text)
    tab3_display_text.insert(tk.END,result)




#comaparer funcions
def use_spacy():
    raw_text=entry1.get('1.0',tk.END)
    final_text=text_summarizer(raw_text)
    print(final_text)
    result='\nSummary: {}'.format(final_text)
    tab4_display.insert(tk.END,result)

def use_nltk():
    raw_text=entry1.get('1.0',tk.END)
    final_text=nltk_summarizer(raw_text)
    print(final_text)
    result='\nSummary: {}'.format(final_text)
    tab4_display.insert(tk.END,result)


#all tabs
#comparer tab
l1=Label(tab4,text='Enter text to summarize',padx=5,pady=5,font=("Lucida", 25, "bold"))
l1.grid(column=1,row=1)
entry1=ScrolledText(tab4,height=12,width=150)
entry1.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

#buttons
button1=Button(tab4,text='Reset',command=clear_compare_text,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab4,text='SpaCy',command=use_spacy,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab4,text='NLTK',command=use_nltk,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab4,text='Clear Result',command=clear_compare_display_result,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button4.grid(row=5,column=1,padx=10,pady=10)

#display screen for result for tab4
tab4_display=ScrolledText(tab4,height=12,width=150)
tab4_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)


#main home tab
l1=Label(tab1,text='Enter text to summarize',padx=5,pady=5,font=("Lucida", 25, "bold"))
l1.grid(column=0,row=1)
entry=ScrolledText(tab1,height=12,width=150)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#buttons
button1=Button(tab1,text='Reset',command=clear_text,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text='Summarize',command=get_summary,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab1,text='Clear Result',command=clear_display_result,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab1,text='Save',command=save_summary,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button4.grid(row=5,column=1,padx=10,pady=10)

#display screen for result for tab1
tab1_display=ScrolledText(tab1,height=12,width=150)
tab1_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)


#file processing tab
l1=Label(tab2,text='Open file to summarize',padx=5,pady=5,font=("Lucida", 25, "bold"))
l1.grid(column=1,row=1)

dispalyed_file=ScrolledText(tab2,height=12,width=150)
dispalyed_file.grid(row=2,column=0,columnspan=3,padx=5,pady=3)

#buttons for file processing tab
b1=Button(tab2,text='Open file',command=openfiles,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
b1.grid(row=3,column=0,padx=10,pady=10)

b2=Button(tab2,text='Reset',command=clear_text_file,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
b2.grid(row=3,column=1,padx=10,pady=10)

b3=Button(tab2,text='Summarize',command=get_file_summary,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
b3.grid(row=3,column=2,padx=10,pady=10)

b4=Button(tab2,text='Clear Result',command=clear_text_result,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
b4.grid(row=5,column=1,padx=10,pady=10)

b5=Button(tab2,text='Close',command=window.destroy,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
b5.grid(row=5,column=2,padx=10,pady=10)


#display screen for tab2
tab2_display_text=ScrolledText(tab2,height=20,width=150)
tab2_display_text.grid(row=15,column=0,columnspan=3,padx=5,pady=5)

#allows to edit
tab2_display_text.config(state=NORMAL)



#URL tab
l1=Label(tab3,text='Enter URL to summarize',padx=5,pady=5)
l1.grid(column=1,row=1)


raw_entry=StringVar()
url_entry=Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

#buttons
button1=Button(tab3,text='Reset',command=clear_url_entry,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab3,text='Get Text',command=get_text,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab3,text='Clear Result',command=clear_url_display,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab3,text='Summarize',command=get_url_summary,width=12,bg='#25d366',fg='#fff',borderwidth=0,font=("Lucida", 25, "bold"))
button4.grid(row=5,column=1,padx=10,pady=10)

#display screen for tab3
url_display=ScrolledText(tab3,height=10,width=150)
url_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

tab3_display_text=ScrolledText(tab3,height=10,width=150)
tab3_display_text.grid(row=10,column=0,columnspan=3,padx=5,pady=5)

window.mainloop()