from tkinter import *
import random
import time
from tkinter import messagebox as tkMessageBox

COUNTER = 0 

def get_index_by_val(Dict, value):
    # Returns the key of the given value from a dict..
    for key in Dict:
        if Dict[key] == value:
            return key
    return False


def main():
    def clearResp():
        ansLabel = Label(root, text="               ", font=("arial", 15)).place(
            x=130, y=120
        )

    def randElem():
        clearResp()
        global d
        with open('sample_dict.txt') as f:
          d = eval(f.read())
        global randAtom
        randAtom = random.choice(list(d.keys()))
        Label(
            root,
            text=randAtom,
            bd=3,
            font=("arial", 20, "bold"),
            relief="solid",
            width=3,
            height=1,
        ).place(x=142, y=70)

    def check_it():
        global randAtom, COUNTER
        clearResp()
        if name.get() == d[randAtom]:
            ansLabel = Label(root, text="Correct", font=("arial", 15)).place(
                x=130, y=120
            )
        elif name.get() == "":
            ansLabel = Label(root, text="No Input", font=("arial", 15)).place(
                x=130, y=120
            )
        elif name.get() not in d.values():
            ansLabel = Label(root, text="Invalid", font=("arial", 15)).place(
                x=130, y=120
            )
        else:
            if COUNTER == 4:
              tkMessageBox.showinfo('Game', "GAME OVER!")
              msg = tkMessageBox.askquestion('New Game', 'Do you want to start a new game?', icon='warning')
              if msg == "yes":
                root.destroy()
                main()
              else:
                root.destroy()
                exit()
            else:
              ansLabel = Label(root, text="Incorrect", font=("arial", 15)).place(
                  x=130, y=120
              )
              COUNTER += 1
            if name.get() in d.values():
                curr_atomic_number = get_index_by_val(d, name.get())
                curr_atomic_number = int(curr_atomic_number)
                if curr_atomic_number <  int(randAtom):
                    output = "The Correct answer is on the right"
                elif curr_atomic_number > int(randAtom):
                    output = "The Correct Answer is on the left"
                tkMessageBox.showinfo("Game", output)

    def answer():
        clearResp()
        ans = d[randAtom]
        Label(root, text=ans, font=("arial", 15)).place(x=157, y=120)
                

    root = Tk()

    root.title("GuessLement")

    root.geometry("350x300+0+0")

    head = Label(
        root, text="GuessLement", font=("arial", 25, "bold"), fg="black"
    ).pack()

    symbol = Label(
        root, text="Enter the symbol", font=("arial", 15, "bold"), fg="blue"
    ).place(x=90, y=40)

    name = StringVar()

    global entry_box

    entry_box = Entry(root, textvariable=name, width=10, bg="white", justify="center")

    entry_box.place(x=125, y=150)

    answer = Button(root, text="Answer", width=4, height=1, bg="white", command=answer).place(x=140, y=180)

    work = Button(root, text="Check", width=4, height=1, bg="white", command=check_it).place(x=140, y=210)

    rand = Button(
        root, text="New", width=4, height=1, bg="white", command=randElem
    ).place(x=140, y=240)

    randElem()

    root.mainloop()


main()