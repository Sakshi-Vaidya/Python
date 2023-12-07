from tkinter import *    
from gtts import gTTS    
from playsound import playsound   

root = Tk()                  
root.geometry('300x300')     
root.resizable(0,0) 
root.config(bg = 'Cyan4')    
root.title('TEXT TO SPEECH') 

Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='sky blue').pack()
Label(root, text ='Enter Text', font ='Helvetica', bg ='sky blue').place(x=30,y=60)
Label(root, text ='By Askii' , font ='arial 15 bold', bg = 'sky blue').pack(side = BOTTOM)

Msg = StringVar()

entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

def Text_to_speech():
    
    Message = entry_field.get()
    speech = gTTS(text = Message, lang='en', slow=False)  
    speech.save('sakshi.mp3')  
    playsound('sakshi.mp3')    

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg = 'sky blue', width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'sky blue').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, bg= 'sky blue').place(x=175 , y =140)

root.mainloop()
