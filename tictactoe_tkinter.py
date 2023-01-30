from tkinter import *
from tkinter import messagebox
import trrttr2
import time

game = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
root = Tk()
root.title('Tic-Tac-Toe')

clicked = True
count = 0
vs_ai = True
ai_turn = False

symbol_turn = "O"

# disable all the buttons
def disable_all_buttons():
    for i in range(9):
        eval("b" + str(i+1)+".config(state=DISABLED)")


# Check to see if someone won
def check_if_won():
    winner = False
    win_spots_combo = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
    for spot in win_spots_combo:
        if eval("b" + str(spot[0]) + "['text'] == b" + str(spot[1]) + "['text'] == b" + str(spot[2]) + "['text']"):
            eval("b" + str(spot[0]) + ".config(bg='red')")
            eval("b" + str(spot[1]) + ".config(bg='red')")
            eval("b" + str(spot[2]) + ".config(bg='red')")
            winner = True
            symbol = eval("b" + str(spot[0]) + "['text']")
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS!  {symbol} Wins!!")
            disable_all_buttons()

    # Check if tie
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disable_all_buttons()


# Button clicked function
def b_click(b, symbol=symbol_turn, ai_turn=True):
    global clicked, count, symbol_turn
    spot_to_button = {1: b1, 2: b2, 3: b3, 4: b4, 5: b5, 6: b6, 7: b7, 8: b8, 9: b9}

    symbol_t = "O" if symbol_turn == "X" else "X"
    symbol_turn = symbol_t
    symbol = symbol_turn
    game[len(str(b["text"]))] = symbol
    b["text"] = symbol
    count += 1
    check_if_won()
    b.config(state=DISABLED)
    if ai_turn == True and vs_ai == True:
        spot_to_go = trrttr2.go(game)
        ai_turn = False
        b_click(spot_to_button[int(spot_to_go)], symbol=symbol_turn, ai_turn=False)

def set_adv():
    global vs_ai
    vs_ai = False

# Start the game over!
def reset(first_move=False, vs_ai_=True):
    global game
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count, vs_ai, ai_turn
    clicked = True
    count = 0
    game = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    vs_ai= True
    

    # Build our buttons
    b1 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(root, text="  ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))
    b4 = Button(root, text="   ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(root, text="    ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(root, text="     ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))
    b7 = Button(root, text="      ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(root, text="       ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(root, text="        ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))

    reset_button = Button(root, text="Reset Game", command=lambda: reset())
    turn_button = Button(root, text="Pass the fisrt move", command=lambda: reset(first_move=True))
    choose_adv = Button(root, text="1 vs 1", command=lambda: reset(vs_ai_=False))

    reset_button.grid(row=0, column=0)
    turn_button.grid(row=0, column=1)
    choose_adv.grid(row=0, column=2)

    # Grid our buttons to the screen
    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)

    if first_move:
        spot_to_button = {1: b1, 2: b2, 3: b3, 4: b4, 5: b5, 6: b6, 7: b7, 8: b8, 9: b9}
        spot_to_go = trrttr2.go(game)
        b_click(spot_to_button[int(spot_to_go)], symbol=symbol_turn, ai_turn=False)

    if vs_ai_==False:
        vs_ai=False
    root.mainloop()


# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)


reset()
root.mainloop()
