from ChatBot import chat
from tkinter import *
from myimages import *
from os import getenv
from sys import exit
from dbsync import db

HEIGHT = 690
WIDTH = 1024

lst=["\n	Hello\n", "\nHey there!\n", "\n  Hi\n", None]
chk=["yes", "no", "thanks"]

class Example:
    staticVariable = ""
    staticanswer = ""
    staticval=0
    staticent=None
    staticLines=0.0
    staticC=''

userName=getenv('username')

def get_input(sentence,n):
    sentence=sentence.lower()
    if(sentence not in chk):
        instance.staticVariable = sentence 
    if(sentence=="quit"):
        sys.exit()
    s='\nSorry! Found nothing for "%s". Please try with different keywords, like WR, DB, What is Mpie, CRM, OMS etc.\n\n In the meantime, \n I have logged your query in this path: C:\\Users\\%s\\Downloads\\user_records.db\n Log name: ~ user_records.db ~ which is located in your "Downloads" folder.\n\n Please close the application and share this log file with Sangeet at some point, so that I can learn more from\n you.      Email id: sangeet.bhowmick@amdocs.com\n\n\n Thanks,\n S.I.R.I.U.S.' % (sentence,userName)
    data_string = StringVar()
    #c=chat.respond(sentence)
    #data_string.set(str(c))
    c=chat.respond(sentence)
    if(c not in lst):# lst=["hi", "hello", "hey",None]
        instance.staticanswer = c
        c='%s\n\n Was this helpful?\n\n\t\tplease reply with ~ yes or no ~\n\n\n\n\n Thanks,\n S.I.R.I.U.S.' % (c)
    if(sentence in chk):# chk=["yes", "no"]
        c='\n Thanks for your feedback!\n\n\n In the meantime, \n I have logged your query in this path: C:\\Users\\%s\\Downloads\\user_records.db\n Log name: ~ user_records.db ~ which is located in your "Downloads" folder.\n\n Please close the application and share this log file with Sangeet at some point, so that I can learn more from\n you.      Email id: sangeet.bhowmick@amdocs.com\n\n\n Thanks,\n S.I.R.I.U.S.' % (userName)
        db.execute('insert into user_query (question, answer, helpful, extra1) values  ("%s", "%s", "%s", "%s")' % (instance.staticVariable, instance.staticanswer, sentence,userName))
        db.commit()
    if(c==None):
        db.execute('insert into user_query (question) values  ("%s")' % (sentence))
        db.commit()
        sentence='%s\n\n' % (sentence)
        data_string.set(s)
#requst.get data from google search : h t t p s://realpython.com/python-requests/
    else:
        data_string.set(c)
#data_string.set(str(c))
#ent = Entry(lower_frame,textvariable=data_string, bg='#88cc00', fg="blue",bd=0,state="readonly")
    ent = Text(lower_frame, bg='#004d39', fg='white', font='Ariel', wrap=WORD)
    ent.insert('1.0',data_string.get())
#ent.set(background='green')
    ent.place(relwidth=1, relheight=1)
    ent.config(state=DISABLED)
    


def show(event=None):
    sentence=entry.get().lower()
    if(sentence not in chk):
        instance.staticVariable = sentence 
    if(sentence=="quit"):
        sys.exit()
    s='\nSorry! Found nothing for "%s". Please try with different keywords, like WR, DB, What is Mpie, CRM, OMS etc.\n\n In the meantime, \n I have logged your query in this path: C:\\Users\\%s\\Downloads\\user_records.db\n Log name: ~ user_records.db ~ which is located in your "Downloads" folder.\n\n Please close the application and share this log file with Sangeet at some point, so that I can learn more from\n you.      Email id: sangeet.bhowmick@amdocs.com\n\n\n Thanks,\n S.I.R.I.U.S.\n\n\n\n' % (sentence,userName)
    data_string = StringVar()
    #c=chat.respond(sentence)
    #data_string.set(str(c))
    c=chat.respond(sentence)
    if(c not in lst):# lst=["hi", "hello", "hey",None]
        instance.staticanswer = c
        c='[S.R.I.U.S.]: Your asked, "%s"\n%s\n\n\n Was this helpful?\n\n\t\tplease reply with ~ yes or no ~\n\n\n\n Thanks,\n S.I.R.I.U.S.\n\n\n\n' % (sentence,c)
    if(sentence in chk):# chk=["yes", "no"]
        c='\n Thanks for your feedback!\n\n\n In the meantime, \n I have logged your query in this path: C:\\Users\\%s\\Downloads\\user_records.db\n Log name: ~ user_records.db ~ which is located in your "Downloads" folder.\n\n Please close the application and share this log file with Sangeet at some point, so that I can learn more from\n you.      Email id: sangeet.bhowmick@amdocs.com\n\n\n Thanks,\n S.I.R.I.U.S.' % (userName)
        db.execute('insert into user_query (question, answer, helpful, extra1) values  ("%s", "%s", "%s", "%s")' % (instance.staticVariable, instance.staticanswer, sentence,userName))
        db.commit()
    if(c == None):
        db.execute('insert into user_query (question, extra1) values  ("%s", "%s")' % (sentence, userName))
        db.commit()
        sentence='%s\n\n' % (sentence)
        data_string.set(s)
        instance.staticLines = instance.staticLines + len(s.splitlines()) + 0.0
        instance.staticent.config(state="normal")
        #instance.staticent.see("end")
        instance.staticent.insert(END, data_string.get())
        instance.staticent.see(instance.staticLines)
        instance.staticent.config(state="disabled")
        entry.delete(0, 'end')
        instance.staticC=c
#requst.get data from google search : h t t p s://realpython.com/python-requests/
    else:
        data_string.set(c)
        instance.staticC=c
        instance.staticLines = instance.staticLines + len(instance.staticC.splitlines())
#data_string.set(str(c))
#ent = Entry(lower_frame,textvariable=data_string, bg='#88cc00', fg="blue",bd=0,state="readonly")
        if(instance.staticval==0):
            instance.staticent = Text(lower_frame, bg='#004d39', fg='white', font='Ariel', wrap=WORD)
            instance.staticent.insert(END, data_string.get())
#ent.set(background='green')
            instance.staticent.place(relwidth=1, relheight=1)
            entry.delete(0, 'end')
            instance.staticent.config(state=DISABLED)
            instance.staticval=1
            instance.staticC=c
        else:
            instance.staticent.config(state="normal")
        #instance.staticent.see("end")
            instance.staticent.insert(END, data_string.get())
            instance.staticent.see(instance.staticLines)
            instance.staticent.config(state="disabled")
            entry.delete(0, 'end')
            instance.staticC=c




#label['text'] = chat.respond(sentence)







root = Tk()


canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack(fill=BOTH)

#canvas.pack(fill=BOTH)

#canvas.configure(background='black')

pic=imageString
background_image = PhotoImage(data=pic)

background_label = Label(root, image=background_image, height=1920, width=1080)
#background_label.pack()
background_label.place(relwidth=1, relheight=1)

#label_image = PhotoImage(file='bot.png')



frame = Frame(root, bg='#80c1ff', bd=5)

frame.place(relx=0.5, rely=0.76, relwidth=0.75, relheight=0.1, anchor='n')

frame.configure(background='#3d3d5c')

instance = Example()
lower_frame = Frame(root, bg='#80c1ff', bd=10)

lower_frame.place(relx=0.5, rely=0.32, relwidth=0.75, relheight=0.4, anchor='n')

lower_frame.configure(background='#3d3d5c')


entry = Entry(frame, font=40)
entry.bind('<Return>', show)
entry.place(relwidth=0.65, relheight=1)



button = Button(frame, text="Get Answer", font=40, command=lambda: get_input(entry.get(), entry.delete(0, 'end')))
button.place(relx=0.7, relheight=1, relwidth=0.3)






label = Label(lower_frame, anchor='n', fg='white', font='Ariel')

label['text']=text='\n\
\n Hi %s, \n\nI am S.I.R.I.U.S. and I am here to help! \n\n \
Type your query in English language. Type quit to exit.\n\n' % (userName)

label.place(relwidth=1, relheight=1)
label.configure(background='#004d39')

root.title('')
root.mainloop()