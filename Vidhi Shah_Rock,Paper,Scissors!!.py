#!/usr/bin/env python
# coding: utf-8

# In[43]:


#import library
from tkinter import *
import random
import colorama
from colorama import Fore

#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='black')


#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 25 bold', bg = 'cyan',).place(x=60,y=25)


##user choice
user_take = StringVar()
Label(root, text = 'Choose any one: Rock, Paper ,Scissors' , font='arial 18 bold', bg = 'Yellow').place(x = 20,y=90)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'red').place(x=95 , y = 140)



#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    



##function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
        
    
##fun to reset
def Reset():
    Result.set("") 
    user_take.set("")

##fun to exit
def Exit():
    root.destroy()


###### button
Entry(root, font = 'arial 12 bold', textvariable = Result, bg ='red',width = 50,).place(x=20, y = 260)

Button(root, font = 'arial 15 bold italic', text = 'PLAY'  ,padx =5,bg ='blue' ,command = play).place(x=150,y=200)

Button(root, font = 'arial 15 bold italic', text = 'RESET'  ,padx =5,bg ='magenta' ,command = Reset).place(x=70,y=320)

Button(root, font = 'arial 15 bold italic', text = 'EXIT'  ,padx =5,bg ='magenta' ,command = Exit).place(x=230,y=320)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




