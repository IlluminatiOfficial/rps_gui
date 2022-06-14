# 3RD ATTEMPT GOTTA DO IT RIGHT NOW
# WRITE DOWN IN PAPER FIRST

# Necessary libraries
import functools
import tkinter as tk
from random import randint
from PIL import ImageTk, Image

# Defining function

 # Computer choice - returns one of the 3 options
def computer_choice():
    choice_dict = {'1':"rock",'2':"paper",'3':"scissor"}
    choice = randint(1,3)
    return choice_dict[str(choice)]
 # point score - compares player and computer choice and return score
def point_score(your_choice,computer_choice):
    global player_score
    global computer_score
    global player_score_label
    global computer_score_label
    global round
    win_condition = {'rock':'scissor','paper':'rock','scissor':'paper'}
    lose_condition = {'scissor':'rock','rock':'paper','paper':'scissor'}
    # check tie
    if your_choice == computer_choice:
        pass
    else:

    # check win or lose
        if win_condition[your_choice] == computer_choice:
            player_score += 1
            player_score_label.config(text= player_score)
        elif  lose_condition[your_choice] == computer_choice:
            computer_score += 1
            computer_score_label.config(text= computer_score )

# Image display func
img1 = Image.open(r'default.png')
img1 = img1.resize((60,60))
p_img1 = Image.open(r'rock_player.png')
p_img2 = Image.open(r'paper_player.png')
p_img3 = Image.open(r'scissor_player.png')
c_img1 = Image.open(r'rock_comp.png')
c_img2 = Image.open(r'paper_comp.png')
c_img3 = Image.open(r'scissor_comp.png')
def img_display(your_choice,computer_choice):
    global img1 , p_img1 , p_img2, p_img3, c_img1, c_img2, c_img3
    global p_img_label, c_img_label
    p_dict = {'rock':p_img1,'paper':p_img2,'scissor':p_img3}
    c_dict = {'rock':c_img1,'paper':c_img2,'scissor':c_img3}
    p_img = p_dict[your_choice].resize((60,60))
    c_img = c_dict[computer_choice].resize((60,60))
    player_img = ImageTk.PhotoImage(p_img)
    computer_img = ImageTk.PhotoImage(c_img)
    p_img_label.config(image = player_img)
    p_img_label.image = player_img
    c_img_label.config(image = computer_img)
    c_img_label.image = computer_img
    
# Game over
def game_over():
    global round
    global r_bt, p_bt, s_bt
    global player_score, computer_score
    global res_label
    if round == 10:
        r_bt.config(state= 'disabled')
        p_bt.config(state= 'disabled')
        s_bt.config(state= 'disabled')
        res = final_win_check(player_score,computer_score)
        res_label.config(text = f"Result: {res}",  width = 8, height = 2, bg = 'blue', fg = 'black')
        res_label.place(relx= .44, rely = .5)
        
        
# CHECK WIN
def final_win_check(your_score,computer_score):
    if your_score > computer_score:
        res = 'win'
    elif computer_score > your_score:
        res= 'lose'
    else:
        res = 'tie'
    
    return res

# Reset function
def reset():
    global player_score 
    global computer_score 
    global round, res_label
    global r_bt, p_bt, s_bt 
    global p_img_label, c_img_label, img
    if round == 0: 
        pass
    elif round < 10:
        player_score = 0
        computer_score = 0
        round = 0
        r_bt.config(state= 'active')
        p_bt.config(state= 'active')
        s_bt.config(state= 'active')
        p_img_label.config(image = img)
        c_img_label.config(image = img)
    elif round == 10:
        player_score = 0
        computer_score = 0
        round = 0
        r_bt.config(state= 'active')
        p_bt.config(state= 'active')
        s_bt.config(state= 'active')  
        p_img_label.config(image = img)
        p_img_label.image = img
        c_img_label.config(image = img)   
        c_img_label.image = img    
        res_label.destroy()

    player_score_label.config(text= player_score)
    computer_score_label.config(text= computer_score )
    round_label.config(text = f'Round: {round}')  

reset_game = functools.partial(reset)


# FINAL BUTTON CLICK FUNCTION
def button_click(your_choice):
    global round
    global round_label
    cc = computer_choice()
    pc = your_choice
    point_score(pc,cc)
    img_display(pc,cc)
    round += 1
    round_label.config(text = f'Round: {round}')
    game_over()
    

# ROCK, PAPER, SCISSOR BUTTON COMMANDS
rock = functools.partial(button_click, your_choice = 'rock')
paper = functools.partial(button_click, your_choice = 'paper')
scissor = functools.partial(button_click, your_choice = 'scissor')

player_score = 0
computer_score = 0
y_img_add = r"C:\Users\HP\OneDrive\Desktop\Python Projects\Rock_paper_scissor_GUI\default.png"
c_img_add = r"C:\Users\HP\OneDrive\Desktop\Python Projects\Rock_paper_scissor_GUI\default.png"
round = 0

# GAME SET UP
rps_game = tk.Tk()
rps_game.title('ROCK PAPER SCISSOR GAME')
rps_game.configure(bg= 'grey', width= 600, height= 400)

tk.Label(rps_game,text='ROCK PAPER SCISSOR', font = 'normal 20 bold', fg = 'blue' , bg = 'grey').place(relx = .22 , rely = 0)
round_label = tk.Label(rps_game, text = 'Round: 0', font = 'normal 18 bold', bg = 'grey', fg = 'blue')
round_label.place(relx = .41 , rely = .1)


# PLAYER VS COMPUTER label
pl = tk.Label(text = 'Player        ', bg ='grey', font = 'normal 15 bold').place(relx = .18, rely = .3)
comp =tk. Label(text = 'Computer', bg = 'grey', font = 'normal 15 bold').place(relx = .68, rely = .3)
vs = tk.Label(text = '   Vs         ', bg = 'grey', font = 'normal 15 bold').place(relx = .44, rely = .3)

#SCORE
player_score_label = tk.Label(text = 0, bg = 'grey', font = 'normal 15 bold')
player_score_label.place(relx = .23, rely = .4)
computer_score_label = tk.Label(text = 0, bg = 'grey', font = 'normal 15 bold')
computer_score_label.place(relx = .75, rely = .4)

# IMAGE
img = ImageTk.PhotoImage(img1)
p_img_label = tk.Label(image = img, bg = 'grey')
p_img_label.place(relx = .18, rely = .5)
c_img_label = tk.Label(image = img, bg = 'grey')
c_img_label.place(relx = .71, rely = .5)


# RESULT 
res_label = tk.Label(rps_game, text = None,  width = 6, height = 2, bg = 'grey', fg = 'black')
res_label.place(relx= .45, rely = .5)


# ROCK PAPER SCISSOR BUTTONS
r_bt = tk.Button(rps_game,text= 'ROCK', width = 6, height = 2, bg = 'blue', fg = 'black',command = rock)
r_bt.place(relx = .19, rely = .7)
p_bt = tk.Button(rps_game,text= 'PAPER', width = 6, height = 2, bg = 'blue', fg = 'black',command = paper)
p_bt.place(relx = .45, rely = .7)
s_bt = tk.Button(rps_game,text= 'SCISSOR', width = 6, height = 2, bg = 'blue', fg = 'black',command = scissor)
s_bt.place(relx = .72, rely = .7)

# RESET BUTTON
reset_bt = tk.Button(rps_game, text = 'RESET', command= reset_game,  width = 6, height = 2, bg = 'blue', fg = 'black')
reset_bt.place(relx = .45, rely= .9)

rps_game.mainloop()


