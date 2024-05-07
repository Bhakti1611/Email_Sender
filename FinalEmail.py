import smtplib
from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import BOLD

main_window = Tk()
main_window.geometry("800x533")
main_window.maxsize(800, 533)
main_window.title("Email Sender")

image1 = Image.open("D:\\PYTHON\\python project\\2.jpg")

photo = ImageTk.PhotoImage(image1)
label1 = Label(main_window,image=photo)
label1.pack()


#bhaktisukhadiya16@gmail.com
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("stark45474195@gmail.com","cxsvwqzqdbuelquc")



Label(main_window,text='E-MAIL',width=20,font=('Arial',35),foreground=('black'),background=('light pink')).place(x=100,y=10)

Label(main_window,text='From : stark45474195@gmail.com',width = 30,font=('Arial',25),foreground=('white'),background=('purple')).place(x=30,y=100)

Label(main_window,text='To :',font=('Arial',25),foreground=('black'),background=('light pink')).place(x=30,y=170)

Label(main_window,text='Message :',font=('Arial',25),foreground=('white'),background=('purple')).place(x=30,y=240)

ans = Label(main_window,text='',font=('Arial',25),background='light pink')
ans.place(x=215,y=400)


To = Entry(main_window,width=33,font=('Arial',20,BOLD),borderwidth=5,background=('white'),foreground=('black'))
To.place(x=100,y=170)

Massage = Entry(main_window,width=30,font=('Arial',22,BOLD),borderwidth=5)
Massage.place(x=190,y=240)

def on_click():
    receiver_id = To.get()
    message = Massage.get()
    To.delete(0,END)
    Massage.delete(0,END)

    s.sendmail("stark45474195@gmail.com",receiver_id,message)
    a = 'Mail Send Sucessfully'
    ans.config(text=a)
    s.quit()


Button(main_window,text='SEND',command=on_click,width=20,height=2,font=('Arial',15,BOLD),foreground=('white'),background=('purple')).place(x=250,y=325)

main_window.mainloop()