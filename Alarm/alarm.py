# Importing all the necessary modules
from time import strftime 
from tkinter import * 
import time
import datetime
from pygame import mixer

# Creating a Window
root = Tk() 
root.title("Alarm Clock")
root.geometry("265x200")
root.resizable(width=False,height=False)

#Functions
def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
		# Getting current time by using .striftime() method of the datetime module's datetime file's now function
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 13, 'bold'),
            text="Wake up!Wake up!Wake up",fg="Black").grid(row=9,columnspan=4)
            print("wake up!")
            mixer.init()
			# Playing a sound when the current time is the same as the alarm time
            mixer.music.load('alarm2.mp3')
            mixer.music.play()
            break

# Creating and placing all the components of the window
hrs=StringVar()
mins=StringVar()
secs=StringVar()

Label(root, font = ('arial', 16, 'bold'),
text="Set Your Alarm Clock!\n [ Its 24Hrs Clock ]\n").grid(row=1,columnspan=4,padx=9)


Label(root, font = ('arial', 11, 'bold'),
text="Hour").grid(row=3,column=1)

hrbtn=Entry(root,textvariable=hrs,width=5,
font =('arial', 18, 'bold')).grid(row=4,column=1)


Label(root, font = ('arial', 11, 'bold'),
text="Minute").grid(row=3,column=2)

minbtn=Entry(root,textvariable=mins,width=5,
font = ('arial', 18, 'bold')).grid(row=4,column=2)

Label(root, font = ('arial', 11, 'bold'),
text="Second").grid(row=3,column=3)

secbtn=Entry(root,textvariable=secs,width=5,font = ('arial', 18, 'bold')).grid(row=4,column=3)

setbtn=Button(root,text="Set Timer!",command=setalarm,bg="#D4AC0D",
fg="Black",font = ('arial', 13, 'bold')).grid(row=7,columnspan=5,pady=9)

timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid()
  
root.mainloop() 