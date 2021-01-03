from tkinter import *
import winsound
import turtle



john = turtle.Turtle()
def ButtonGoBrr():  
    winsound.PlaySound("randomsound.wav", winsound.SND_ASYNC)
    
    john.hideturtle()
    john.penup()
    john.speed(0)
    john.left(120)
    john.forward(120)
    john.left(90)
    john.color("red")
    john.pendown()
    john.circle(140)
    for i in range(30):
        john.left(10)
        john.circle(140)
    john.penup()
    john.color("green")
    style1 = ("Times", 40, "bold")
    john.write("Button!", font=style1, align='center')
    john.forward(200)
    

root = Tk()

root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

main_menu = Menu(root)


file_menu = Menu(root)

file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)

main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)

messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

scrollbarY = Scrollbar(root, command=chatWindow.yview, cursor="star").place(x=375,y=5, height=385)


Button = Button(root, command =ButtonGoBrr, text="Send",  width="12", height=5, bd=0, bg="#0080ff",repeatdelay=500, repeatinterval=100, cursor="ur_angle", relief = RAISED, activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12)).place(x=6, y=400, height=88)


root.mainloop()
wn = turtle.Screen()
