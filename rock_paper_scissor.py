from tkinter import *
from PIL import Image,ImageTk
from random import randint

window=Tk()
window.geometry('840x400')
window.title("Game Rock paper and scissors")
window.configure(background="black")

image_rock1=ImageTk.PhotoImage(Image.open("rock1.jpg"))
image_paper1=ImageTk.PhotoImage(Image.open("paper1.jpg"))
image_scissor1=ImageTk.PhotoImage(Image.open("scissor1.jpg"))

image_rock2=ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper2=ImageTk.PhotoImage(Image.open("paper.jpg"))
image_scissor2=ImageTk.PhotoImage(Image.open("scissor2.jpg"))

label_player=Label(window, image= image_scissor1)
label_computer=Label(window, image= image_scissor2)
label_computer.place(x=0,y=80)
label_player.place(x=684,y=80)

computer_score=Label(window,text=0,font=('arial',60,'bold'),fg="blue")
player_score=Label(window,text=0,font=("arial",60,'bold'),fg="blue")
computer_score.place(x=250,y=100)
player_score.place(x=550,y=100)

player_indicator=Label(window,font=("arial",40,'bold'),text="PLAYER",bg="orange",fg="blue")
computer_indicator=Label(window,font=("arial",40,'bold'),text="COMPUTER",bg="orange",fg="blue")
computer_indicator.place(x=150,y=0)
player_indicator.place(x=500,y=0)

def updateMessage(a):
	final_message['text']=a

def Computer_Update():
	final=int(computer_score['text'])
	final+=1
	computer_score["text"]=str(final)

def Player_Update():
	final=int(player_score['text'])
	final+=1
	player_score["text"]=str(final)

def winner_check(p,c):
	if p==c:
		updateMessage("It's a tie!!")
	elif p=="rock":
		if c=="paper":
			updateMessage("Computer Wins!!")
			Computer_Update()
		else:
			updateMessage("Player Wins!!")
			Player_Update()
	elif p=="paper":
		if c=="scissor":
			updateMessage("Computer Wins!!")
			Computer_Update()
		else:
			updateMessage("Player Wins!!")
			Player_Update()
	elif p=="scissor":
		if c=="rock":
			updateMessage("Computer Wins!!")
			Computer_Update()
		else:
			updateMessage("Player Wins!!")
			Player_Update()

	else:
		pass

to_select=["rock","paper","scissor"]

def choice_update(a):
	choice_computer=to_select[randint(0,2)]
	if choice_computer=="rock":
		label_computer.configure(image=image_rock2)
	elif choice_computer=="paper":
		label_computer.configure(image=image_paper2)
	else:
		label_computer.configure(image=image_scissor2)

	if a=="rock":
		label_player.configure(image=image_rock1)
	elif a=="paper":
		label_player.configure(image=image_paper1)
	else:
		label_player.configure(image=image_scissor1)

	winner_check(a,choice_computer)

final_message=Label(window,width=15,height=0,font=('arial',40,'bold'),bg='red',fg='white')
final_message.place(x=180,y=310)

button_rock=Button(window,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).place(x=180,y=250)
button_paper=Button(window,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).place(x=345,y=250)
button_scissor=Button(window,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor")).place(x=520,y=250)

window.mainloop()