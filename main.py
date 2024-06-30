from tkinter import *
from PIL import ImageTk, Image
import tkinter.scrolledtext as st
from functools import partial

#init the start menu using tkinter
start_menu = Tk()
#set the window size correctly
start_menu.geometry("550x350")
#set the title of the window
start_menu.title("Hunt for the Bluemoon - Start Menu")

#global variable to track the level the player is on
curr_level = 1
#item list to track progress
item_list = [False, False, False, False, False, False, False, False, False, False, False]

#the game loop itself
#has level select parameter to choose what level the player starts on
def play_game(level_select):
    global curr_level #grabbing the global variable
    
    start_menu.withdraw() #remove the start menu from view
    
    #init new window that has the actual game
    root = Toplevel(start_menu)
    root.geometry("550x350") #set window size
    root.title("Bluemoon Headquarters - Floor 1") #set title of window
    
    #function so the user can return to start menu
    def back_to_start():
        root.withdraw() #remove game from view
        start_menu.deiconify() #bring back the start menu
    
    #function so the user can go to the level select menu
    def back_select():
        root.withdraw() #remove game from view
        try: #if the level menu has been init...
            level_menu.deiconify() #bring it back
        except: #if not, just run the function that creates it
            select_level()
    
    #menu bar for the functions above
    top_menu = Menu(root) #attach top menu to the game window
    top_menu.add_command(label="Start Menu", command=back_to_start) #button for back to start
    top_menu.add_command(label="Level Select", command=back_select) #button for back select
    
    #function to continue to next level
    def next_level():
        global curr_level #grab that global variable
        
        if curr_level == 6: #if we reached the last level, end the game
            back_to_start()
        else: #else just go to next level
            curr_level += 1
            root.title("Bluemoon Headquarters - Floor {}".format(curr_level)) #fix title of the level
        update_gui() #update the buttons and menu
    
    #update the gui for the game
    def update_gui():
        global curr_level #grab that global variable
        continue_btn.config(state = "disabled") #disable the next level button
        
        #clear the message box
        msg_box.config(state = "normal") #enable it
        msg_box.delete(1.0, END) #clear everything inside
        msg_box.config(state = "disabled") #disable it, so the user cant edit
        
        #reset the action menu to avoid bugs
        reset_actions()
        
        #for each level, assign the following things (in this order)
        # - the init world message to describe situation
        # - the init message from the player-character
        # - what each button is named and what their function is
        # - - we use partial to pass parameters into tkinter commands
        if curr_level == 2:
            send_msg("sys2")
            send_hint("sys2")
            button1.config(text = "Check phone", command = partial(get_clue, 4))
            button2.config(text = "Inspect the lamp", command = partial(get_clue, 5))
            button3.config(text = "Inspect the water glass", command = partial(get_clue, 6))
            button4.config(text = "Inspect trash can", command = partial(get_clue, 7))
            button5.config(text = "Use keypad", command = partial(get_clue, 8))
        elif curr_level == 3:
            send_msg("sys3")
            send_hint("sys4")
            button1.config(text = "Check phone", command = partial(get_clue, 9))
            button2.config(text = "Read first paper", command = partial(get_clue, 10))
            button3.config(text = "Read second paper", command = partial(get_clue, 11))
            button4.config(text = "Inspect the drawing", command = partial(get_clue, 12))
            button5.config(text = "Inspect the door", command = partial(get_clue, 13))
        elif curr_level == 4:
            send_msg("sys4")
            send_hint("sys6")
            button1.config(text = "Check phone", command = partial(get_clue, 14))
            button2.config(text = "Use whiteboard", command = partial(get_clue, 15))
            button3.config(text = "Read the newspaper", command = partial(get_clue, 16))
            button4.config(text = "Inspect poster", command = partial(get_clue, 17))
            button5.config(text = "Inspect chicken bones", command = partial(get_clue, 18))
        elif curr_level == 5:
            send_msg("sys5")
            send_hint("sys7")
            button1.config(text = "Check phone", command = partial(get_clue, 19))
            button2.config(text = "Eat the chicken", command = partial(get_clue, 20))
            button3.config(text = "Drink the soda", command = partial(get_clue, 21))
            button4.config(text = "Use the keypad", command = partial(get_clue, 22))
            button5.config(text = "Use the lever system", command = partial(get_clue, 23))
        elif curr_level == 6:
            send_msg("sys6")
            send_hint("sys8")
            button1.config(text = "Eliminate the CEO", command = partial(get_clue, 24))
            button2.config(text = "N/A", command = "")
            button3.config(text = "N/A", command = "")
            button4.config(text = "N/A", command = "")
            button5.config(text = "N/A", command = "")
    
    #function to reset each action to blank
    def reset_actions():
        action1.config(command = '')
        action2.config(command = '')
        action3.config(command = '')
        action4.config(command = '')
        action5.config(command = '')
    
    #function to give clues for each menu selection and set actions accordingly
    def get_clue(clue_id):
        global item_list #grab that global item_list
        reset_actions() #reset actions to avoid bugs
        
        #for reach clue, send the world message needed
        #additionally, if its an action selection, configure each action button
        #if needed, check if item has been gotten, if it has make the action unusable
        if clue_id == 0:
            send_msg(0)
        elif clue_id == 1:
            send_msg(1)
            if item_list[0] == False:
                action1.config(command = partial(acquire_item, 0))
            else:
                action1.config(command = partial(send_hint, "sys1"))
            action2.config(command = partial(send_hint, 2))
        elif clue_id == 2:
            send_msg(3)
            if item_list[1] == False:
                action1.config(command = partial(send_msg, 4))
            else:
                action1.config(command = '')
        elif clue_id == 3:
            send_msg(6)
            if item_list[3] == False:
                action1.config(command = partial(acquire_item, 3))
            else:
                action1.config(command = partial(send_hint, "sys1"))
            action2.config(command = partial(send_hint, 7))
        elif clue_id == 4:
            send_msg(8)
        elif clue_id == 5:
            send_msg(9)
        elif clue_id == 6:
            send_msg(10)
        elif clue_id == 7:
            send_msg(11)
        elif clue_id == 8:
            send_msg(12)
            if item_list[4] == False:
                action1.config(command = partial(send_hint, "sys3"))
                action2.config(command = partial(send_hint, "sys3"))
                action3.config(command = partial(send_hint, "sys3"))
                action4.config(command = partial(acquire_item, 4))
                action5.config(command = partial(send_hint, "sys3"))
        elif clue_id == 9:
            send_msg(14)
        elif clue_id == 10:
            send_msg(15)
            if item_list[5] == False:
                action1.config(command = partial(send_hint, 13))
                action2.config(command = partial(acquire_item, 5))
                action3.config(command = partial(send_hint, 13))
        elif clue_id == 11:
            send_msg(16)
            if item_list[6] == False:
                action1.config(command = partial(send_hint, 13))
                action2.config(command = partial(send_hint, 13))
                action3.config(command = partial(acquire_item, 6))
        elif clue_id == 12:
            send_msg(17)
        elif clue_id == 13:
            send_msg(18)
        elif clue_id == 14:
            send_msg(22)
        elif clue_id == 15:
            send_msg(23)
            if item_list[7] == False:
                action1.config(command = partial(send_hint, 21))
                action2.config(command = partial(acquire_item, 7))
                action3.config(command = partial(send_hint, 21))
                action4.config(command = partial(send_hint, 21))
        elif clue_id == 16:
            send_msg(24)
        elif clue_id == 17:
            send_msg(25)
        elif clue_id == 18:
            send_msg(26)
        elif clue_id == 19:
            send_msg(28)
        elif clue_id == 20:
            send_msg(29)
        elif clue_id == 21:
            send_msg(30)
        elif clue_id == 22:
            send_msg(31)
            if item_list[8] == False:
                action1.config(command = partial(send_hint, "sys3"))
                action2.config(command = partial(acquire_item, 8))
                action3.config(command = partial(send_hint, "sys3"))
                action4.config(command = partial(send_hint, "sys3"))
                action5.config(command = partial(send_hint, "sys3"))
        elif clue_id == 23:
            send_msg(32)
            if item_list[9] == False:
                action1.config(command = partial(send_hint, "sys3"))
                action2.config(command = partial(send_hint, "sys3"))
                action3.config(command = partial(acquire_item, 9))
        elif clue_id == 24:
            send_msg(35)
            if item_list[10] == False:
                action1.config(command = partial(acquire_item, 10))
                action2.config(command = partial(send_hint, 33))
                action3.config(command = partial(send_hint, 33))
                
    #function that sets the item list if the user got a puzzle correct
    def acquire_item(x):
        global item_list #grab that item list global
        global curr_level #grab that curr_level global
        item_list[x] = True
        if x == 0:
            reset_actions()
            send_msg(2)
        elif x == 2:
            button4.config(command = partial(send_hint, "sys1"))
            send_msg(5)
        elif x == 3:
            reset_actions()
            send_msg(7)
        elif x == 4:
            send_msg(13)
            reset_actions()
        elif x == 5:
            send_msg(19)
            reset_actions()
            button2.config(command = partial(send_hint, "sys5"))
        elif x == 6:
            send_msg(20)
            reset_actions()
            button3.config(command = partial(send_hint, "sys5"))
        elif x == 7:
            reset_actions()
            button2.config(command = partial(send_hint, "sys01"))
        elif x == 8:
            send_hint(29)
            send_msg(34)
            reset_actions()
            button3.config(command = partial(send_hint, "sys5"))
        elif x == 9:
            send_hint(30)
            send_msg(34)
            reset_actions()
            button3.config(command = partial(send_hint, "sys5"))
        elif x == 10:
            send_hint(34)
            reset_actions()
            button1.config(command = partial(send_hint, "sys5"))
            
        #this also checks if the user got all the required items for a level
        #if they dude, then we unlock the continue button and let them pass
        #we also send another world message if needed
        if curr_level == 1:
            if (item_list[0] == True) and (item_list[2] == True) and (item_list[3] == True):
                continue_btn.config(state = 'normal')
                send_msg("sys1")
        elif curr_level == 2:
            if item_list[4] == True:
                continue_btn.config(state = 'normal')
        elif curr_level == 3:
            if (item_list[5] == True) and (item_list[6] == True):
                continue_btn.config(state = 'normal')
                send_msg(21)
        elif curr_level == 4:
            if item_list[7] == True:
                continue_btn.config(state = 'normal')
                send_msg(27)
        elif curr_level == 5:
            if (item_list[8] == True) and (item_list[9] == True):
                continue_btn.config(state = 'normal')
                send_msg(33)
        elif curr_level == 6:
            if item_list[10] == True:
                continue_btn.config(state = 'normal')
                send_msg(36)
    
    #function to send things into the message box
    #it can be worldbuilding or reactions to doing actions/picking menu buttons
    def send_msg(msg_id):
        #if not a system entry, skip to end of last line
        if type(msg_id) is int:
            msg_box.see('end')
        
        #items with sys are worldbuilding init messages, the regular numbers are just reacitons to menu buttons
        if msg_id == "sys0":
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, "You have reached the first floor of the Bluemoon Headquarters. It's a nice and somber place... but it's not time for relaxation.\n")
            msg_box.insert(INSERT, "A door stands between you and your objective. It has 3 different locks.\n\n")
            msg_box.insert(INSERT, "Looking around the room, you see a small array of decor. A lone purple vase hangs in the table standing in the dead center of the room.\n")
            msg_box.insert(INSERT, "An ugly red and orange rug is lain under the aforementioned table.\n")
            msg_box.insert(INSERT, "You see the painting of Paris, specifically the Eiffel Tower glaring at you.\n\n")
            msg_box.insert(INSERT, "Suddenly, your phone buzzes. It's probably your boss.\n\n")
            msg_box.config(state = 'disabled')
        elif msg_id == "sys1":
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, "You have finally collected all the keys. You can now unlock the door!")
            msg_box.config(state = 'disabled')
        elif msg_id == "sys2":
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, "You have reached the second floor of the Bluemoon Headquarters. The room has bright blue walls, but is void of any real decor.\n")
            msg_box.insert(INSERT, "Another door stands in front of you, but it is locked by a keypad.\n")
            msg_box.insert(INSERT, "3 items are also littered in front of you. You see a small glass of water, a trashcan, and a large lamp... all in that exact order.\n")
            msg_box.insert(INSERT, "Your phone buzzes once more, but it's not your boss.\n\n")
            msg_box.config(state = 'disabled')
        elif msg_id == "sys3":
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, "You have reached the third floor of the Bluemoon Headquarters. The room is painted black and has a large antique table in its center.\n")
            msg_box.insert(INSERT, "The table holds 2 papers with riddles. A lone pen sits nearby. It looks like you have to answer them.\n")
            msg_box.insert(INSERT, "You take a closer look at the 3rd door, it seems to have some kind of image scanner attached to it.\n")
            msg_box.insert(INSERT, "You hear a faint ringtone. It looks like your boss texted you again.\n\n")
            msg_box.config(state = 'disabled')
        elif msg_id == "sys4":
            msg_box.config(state = "normal")
            msg_box.insert(INSERT, "You have reached the fourth floor. You feel even more tired than before you came to this place. To your dismay, you see yet another door and table combo before you. But this time there is a whiteboard next to said table.\n")
            msg_box.insert(INSERT, "On the whiteboard, you see another image scanner along with an unfinished sequence. It looks like you have to write the last digit using the marker on the whiteboard's holder.\n")
            msg_box.insert(INSERT, "On the table, you see a rolled up newspaper and an old and worn poster.\n")
            msg_box.insert(INSERT, "You also notice that the door has something carved into it.\n\n")
            msg_box.config(state = "disabled")
        elif msg_id == "sys5":
            msg_box.config(state = "normal")
            msg_box.insert(INSERT, "You have reached the fifth floor. You are about to reach the end. You see the usual door and table once more.\n")
            msg_box.insert(INSERT, "The door seems to have a keypad with 5 numbers and 3 levers on opposite sides.\n")
            msg_box.insert(INSERT, "On table you see a large fried chicken platter along with a soda can.\n")
            msg_box.insert(INSERT, "Your phone buzzes for the first time in a while. Your boss has sent you another message.\n\n")
            msg_box.config(state = "disabled")
        elif msg_id == "sys6":
            msg_box.config(state = "normal")
            msg_box.insert(INSERT, "You finally reach the sixth floor and see your boss facing you. He points his pistol at you.\n")
            msg_box.insert(INSERT, "\"It ends now kid,\" he says. \"It seems I underestimated you. I sent you to die but it seems you simply won't.\"\n")
            msg_box.insert(INSERT, "\"Let's make this interesting. If you solve my riddle: you can kill me.\"\n\n")
            msg_box.config(state = "disabled")
        elif msg_id == 0:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at your phone and find a message from your boss.\n\n')
            msg_box.insert(INSERT, "The message says the following: \"Better get your detective cap on, kid. Each door will be locked and you'll have to get through 'em all. Just search around the room for stuff.\"\n\n")
            msg_box.config(state="disabled")
            send_hint(0)
        elif msg_id == 1:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You inspect the purple vase. Orange flowers rest in its interior. However, you see something shimmering inside of it.\n\n')
            msg_box.insert(INSERT, 'You have 2 actions available here.\n')
            msg_box.insert(INSERT, '1. Take the shimmering object.\n')
            msg_box.insert(INSERT, '2. Eat the orange flowers.\n')
            msg_box.config(state="disabled")
            send_hint(1)
        elif msg_id == 2:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You grab the shimmering object and find a key. Good work!\n')
            msg_box.config(state = 'disabled')
            send_hint(3)
        elif msg_id == 3:
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, '> You inspect the painting. Upon closer inspection, you notice it is actually upside down... weird.\n\n')
            msg_box.insert(INSERT, 'You have 1 action available here.\n')
            msg_box.insert(INSERT, '1. Rotate the painting into the right position.\n')
            msg_box.config(state = 'disabled')
            send_hint(4)
        elif msg_id == 4:
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, '> You fix the painting and suddenly a hole opens up in the wall next to it. Inside you see a silver key.\n\n')
            msg_box.config(state = 'disabled')
            send_hint(5)
            button4.config(text = "Get key from hole.", command = partial(acquire_item, 2))
            action1.config(command = partial(send_hint, "sys1"))
        elif msg_id == 5:
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, '> You got the key from the hole in the wall. Great work!')
            msg_box.config(state = 'disabled')
            send_hint(3)
        elif msg_id == 6:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You inspect the tacky rug. As you put your hands on it, you feel a lump... there must be something under it.\n\n')
            msg_box.insert(INSERT, 'You have 2 actions available here.\n')
            msg_box.insert(INSERT, '1. Get the object under the rug.\n')
            msg_box.insert(INSERT, '2. Smell the rug.\n')
            msg_box.config(state="disabled")
            send_hint(6)
        elif msg_id == 7:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You lift up a part of the rug and see a key. Nice job!\n')
            msg_box.config(state = 'disabled')
            send_hint(3)
        elif msg_id == 8:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at your phone and find a message from a [REDACTED] number.\n\n')
            msg_box.insert(INSERT, "The message says the following: \"Don't let small things trick your head...\"\n\n")
            msg_box.config(state="disabled")
            send_hint(8)
        elif msg_id == 9:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at the large lamp. You see 2 numbers written in red marker.\n')
            msg_box.insert(INSERT, "The numbers are \"5\" and \"2\"\n\n")
            msg_box.config(state="disabled")
            send_hint(9)
        elif msg_id == 10:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at the small water glass. You see another 2 numbers written in red marker.\n')
            msg_box.insert(INSERT, "The numbers are \"2\" and \"4\"\n\n")
            msg_box.config(state="disabled")
            send_hint(9)
        elif msg_id == 11:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at the empty trash can. You see yet another 2 numbers written in red marker.\n')
            msg_box.insert(INSERT, "The numbers are \"3\" and \"1\"\n\n")
            msg_box.config(state="disabled")
            send_hint(9)
        elif msg_id == 12:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at the keypad. It awaits the correct sequence of numbers.\n\n')
            msg_box.insert(INSERT, 'You have 5 actions to choose from. Choose the right code.\n')
            msg_box.insert(INSERT, '1. 522431 \n2. 245231 \n3. 55555 \n4. 243152 \n5. 312452\n\n')
            msg_box.config(state = 'disabled')
        elif msg_id == 13:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You put in the right sequence! Good work!\n')
            msg_box.config(state = 'disabled')
            send_hint(10)
        elif msg_id == 14:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You look at your phone and find another message from your boss.\n\n')
            msg_box.insert(INSERT, "The message says the following: \"Hey, kid. Make sure not to overthink the riddles alright? They are simpler than you think. Also did you see that image scanner? It uses something called computer vision... really high tech stuff!\"\n\n")
            msg_box.config(state="disabled")
            send_hint(11)
        elif msg_id == 15:
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, '> You read the first paper\'s riddle.\n\n"What has 4 legs in the morning, 2 legs in the afternoon, and 3 legs at night?"\n')
            msg_box.insert(INSERT, 'You have 3 actions to choose from. Choose the correct answer to write down.\n')
            msg_box.insert(INSERT, '1. A dog \n2. A man \n3. A burrito\n\n')
            msg_box.config(state = 'disabled')
            send_hint(12)
        elif msg_id == 16:
            msg_box.config(state = 'normal')
            msg_box.insert(INSERT, '> You read the second paper\'s riddle.\n\n"I have no mouth, but I can speak. I have no ears but I can hear. What am I?"\n')
            msg_box.insert(INSERT, 'You have 3 actions to choose from. Choose the correct answer to write down.\n')
            msg_box.insert(INSERT, '1. An ideology \n2. The sun \n3. An echo\n\n')
            msg_box.config(state = 'disabled')
            send_hint(14)
        elif msg_id == 17:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You notice a crude drawing scraped into the table. It looks like a man in a ninja suit wearing green goggles.\n\n')
            msg_box.config(state = 'disabled')
            send_hint(16)
        elif msg_id == 18:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You take a closer look at the door with the scanner. You knock on it and the sound reverberates around the room.\n\n')
            msg_box.config(state = 'disabled')
            send_hint(17)
        elif msg_id == 19:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You answered the first riddle correctly! Great job!\n\n')
            msg_box.config(state = 'disabled')
            send_hint(15)
        elif msg_id == 20:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, '> You answered the second riddle correctly! Great job!\n\n')
            msg_box.config(state = 'disabled')
            send_hint(15)
        elif msg_id == 21:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, 'You answered both of the riddles correctly! You can now open the door!\n')
            msg_box.config(state = 'disabled')
            send_hint(15)
        elif msg_id == 22:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You look at your phone and see that you have no messages.\n\n")
            msg_box.config(state= 'disabled')
            send_hint(18)
        elif msg_id == 23:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You stand in front of the whiteboard, whilst grabbing the marker, and start reading it. \n\n")
            msg_box.insert(INSERT, "The whiteboard pattern goes as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, _.\n")
            msg_box.insert(INSERT, "What is the next number? You have 4 actions to choose here.\n")
            msg_box.insert(INSERT, "1. 24 \n2. 34 \n3. 10 \n4. 233\n\n")
            msg_box.config(state= 'disabled')
            send_hint(19)
        elif msg_id == 24:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You unroll the newspaper and begin to read it. \n\n")
            msg_box.insert(INSERT, '"BREAKING! Italian mathematician makes fascinating discovery!"\n')
            msg_box.config(state= 'disabled')
            send_hint(22)
        elif msg_id == 25:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You pick up the poster and begin inspecting it. \n\n")
            msg_box.insert(INSERT, '"The principles of addition! Combining two numbers to create new ones! Soon we will combine hearts into one for world peace!"\n')
            msg_box.config(state= 'disabled')
            send_hint(23)
        elif msg_id == 26:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You look closely at the door and something written in marker. \n\n")
            msg_box.insert(INSERT, '"L e A r N T HE s E q U en ce!!!!"\n')
            msg_box.config(state= 'disabled')
            send_hint(24)
        elif msg_id == 27:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> The scanner glows green and the door is unlocked! You chose the correct number! Great work!\n\n")
            msg_box.config(state= 'disabled')
            send_hint(20)
        elif msg_id == 28:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You check your phone for the last time. You read the message from your boss.\n")
            msg_box.insert(INSERT, "The message says the following: \"Hey kid. You are at the end of the road now it seems. Take a break and eat some chicken. Let me help you out with the last puzzle. The right button on the keypad to press is the floor that had a water glass. For the lever, it's the floor with the drawing of the foreign commando. Good luck kid. Stay safe.\"\n\n")
            msg_box.config(state= 'disabled')
            send_hint(25)
        elif msg_id == 29:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You take a piece of chicken from the platter and eat it.\n\n")
            msg_box.config(state= 'disabled')
            send_hint(26)
        elif msg_id == 30:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You take a sip from the soda.\n\n")
            msg_box.config(state= 'disabled')
            send_hint(27)
        elif msg_id == 31:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You inspect the keypad and prepare to enter a number.\n\n")
            msg_box.insert(INSERT, "You have 5 actions to choose here.\n")
            msg_box.insert(INSERT, "1. Press 1 \n2. Press 2 \n3. Press 3 \n4. Press 4 \n5. Press 5\n\n")
            msg_box.config(state= 'disabled')
            send_hint(28)
        elif msg_id == 32:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You inspect the keypad and prepare to enter a number.\n\n")
            msg_box.insert(INSERT, "You have 3 actions to choose here.\n")
            msg_box.insert(INSERT, "1. Flip the first lever \n2. Flip the second lever \n3. Flip the third lever\n\n")
            msg_box.config(state= 'disabled')
            send_hint(28)
        elif msg_id == 33:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You solved the second to last puzzle! Good job!\n\n")
            msg_box.config(state= 'disabled')
            send_hint(31)
        elif msg_id == 34:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You entered the right answer!\n\n")
            msg_box.config(state= 'disabled')
        elif msg_id == 35:
            msg_box.config(state = "normal")
            msg_box.insert(INSERT, "> You accept his challenge.\n\n")
            msg_box.insert(INSERT, "\"Ok, kid. What is Dr. Cazalas' motto?\"\n")
            msg_box.insert(INSERT, "You have 3 actions to choose from.\n")
            msg_box.insert(INSERT, "1. Kick the ball!!! \n2. Eat the ball!!! \n3. Shoot the ball!!!\n\n")
            msg_box.config(state = "disabled")
        elif msg_id == 36:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "> You said the right answer and immediately pull out your pistol. You shoot your former boss and he lies dead.\n\n")
            msg_box.insert(INSERT, "The end.")
            msg_box.config(state= 'disabled')
        elif msg_id == 37:
            msg_box.config(state='normal')
            msg_box.insert(INSERT, "\"Wrong,\" says your boss.\n\n")
            msg_box.config(state= 'disabled')
            
    def send_hint(hint_id):
        #delete current hint before continuing
        hint_box.config(state = "normal") #makes it available to edit
        hint_box.delete(1.0, END)
        hint_box.config(state = "disabled") #closes it back so the player cant do anything
        #now check the hints id and do each according action
        #hints with sys in front of a number just denotes system messages for completing puzzles and other misc things
        #everything else is just for general hints
        if hint_id == "sys0":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "This music isn't half bad. Whatever, time to find those keys.")
            hint_box.config(state = "disabled")
        elif hint_id == "sys01":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "I already figured this one out.")
            hint_box.config(state = "disabled")
        elif hint_id == "sys02":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "I already figured this one out.")
            hint_box.config(state = "disabled")
        elif hint_id == "sys1":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "I already got something from this place.")
            hint_box.config(state = "disabled")
        elif hint_id == "sys2":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Maybe these things have to do with that keypad...")
            hint_box.config(state = "disabled")
        elif hint_id == "sys3":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Welp. That didn't do anything.")
            hint_box.config(state = "disabled")
        elif hint_id == "sys4":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "What is with these bizarre placements?")
            hint_box.config(state = "disabled")
        elif hint_id == "sys5":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "I already solved this riddle.")
            hint_box.config(state = "disabled")
        elif hint_id == "sys6":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "This is like a personal hell. When will this ride end?")
            hint_box.config(state = "disabled")
        elif hint_id == "sys7":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Am I reaching the end?")
            hint_box.config(state = "disabled")
        elif hint_id == "sys8":
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Boss... you betrayed me?")
            hint_box.config(state = "disabled")
        elif hint_id == 0:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Tch. Stating the obvious...")
            hint_box.config(state = "disabled")
        elif hint_id == 1:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "This vase looks interesting.")
            hint_box.config(state = "disabled")
        elif hint_id == 2:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Ugh. This tastes AWFUL. Why did I do that?")
            hint_box.config(state = "disabled")
        elif hint_id == 3:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Heck yeah. I got a key.")
            hint_box.config(state = "disabled")
        elif hint_id == 4:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "What the... hm. I wonder what happens if I fix it.")
            hint_box.config(state = "disabled")
        elif hint_id == 5:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Hey, that's pretty cool!")
            hint_box.config(state = "disabled")
        elif hint_id == 6:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Just how old is this thing?")
            hint_box.config(state = "disabled")
        elif hint_id == 7:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "YIKES! This smells like trash!")
            hint_box.config(state = "disabled")
        elif hint_id == 8:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Who the heck sent this?!")
            hint_box.config(state = "disabled")
        elif hint_id == 9:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "These numbers must be important.")
            hint_box.config(state = "disabled")
        elif hint_id == 10:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Another puzzle solved!")
            hint_box.config(state = "disabled")
        elif hint_id == 11:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Where does he even get this information? Wait a minute... does he know I made it to the third floor?")
            hint_box.config(state = "disabled")
        elif hint_id == 12:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "How can something lose and gain a leg? This is stupid.")
            hint_box.config(state = "disabled")
        elif hint_id == 13:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "The scanner blinked red. Looks like I got it wrong.")
            hint_box.config(state = "disabled")
        elif hint_id == 14:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "This seems overly complex.")
            hint_box.config(state = "disabled")
        elif hint_id == 15:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "The scanner blinked green! Let's go!")
            hint_box.config(state = "disabled")
        elif hint_id == 16:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Looks like some kind of foreign commando...")
            hint_box.config(state = "disabled")
        elif hint_id == 17:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Huh.")
            hint_box.config(state = "disabled")
        elif hint_id == 18:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Well that's bizarre. Guess he finally decided to leave me alone.")
            hint_box.config(state = "disabled")
        elif hint_id == 19:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Hmm... This seems oddly familiar.")
            hint_box.config(state = "disabled")
        elif hint_id == 20:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "The image scanner is shining the green light! That's a win!")
            hint_box.config(state = "disabled")
        elif hint_id == 21:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "...And it blinked red. Great.")
            hint_box.config(state = "disabled")
        elif hint_id == 22:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "How in the world do you pronounce that name? Fib-o-what?")
            hint_box.config(state = "disabled")
        elif hint_id == 23:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Math is such a bizarre subject.")
            hint_box.config(state = "disabled")
        elif hint_id == 24:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "I can't even read this.")
            hint_box.config(state = "disabled")
        elif hint_id == 25:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Something ain't right about this...")
            hint_box.config(state = "disabled")
        elif hint_id == 26:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Needs some salt, but it's pretty good!")
            hint_box.config(state = "disabled")
        elif hint_id == 27:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Ah. That hits the spot.")
            hint_box.config(state = "disabled")
        elif hint_id == 28:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Gotta remember that phone message.")
            hint_box.config(state = "disabled")
        elif hint_id == 29:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Here we go...")
            hint_box.config(state = "disabled")
        elif hint_id == 30:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Another one bites the dust...")
            hint_box.config(state = "disabled")
        elif hint_id == 31:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "This is it.")
            hint_box.config(state = "disabled")
        elif hint_id == 32:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "It's over now!")
            hint_box.config(state = "disabled")
        elif hint_id == 33:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Wait, no!")
            hint_box.config(state = "disabled")
            send_msg(37)
        elif hint_id == 34:
            hint_box.config(state = "normal")
            hint_box.insert(INSERT, "Goodbye, forever.")
            hint_box.config(state = "disabled")
            
    #note: pack essentially renders each tkinter item
    
    #create the frames to properly organize each of parts of the screen
    main_dash = Frame(root)
    main_dash.pack(pady=20)
    
    #subdash that contains the message box, unlock button, and hint box in the center of the screen
    sub_dash = Frame(main_dash)
    sub_dash.pack(side=LEFT, padx=20)
    #init the continue button, make sure its disabled
    continue_btn = Button(sub_dash, text = "Unlock Door", command = next_level, width = 20, state="disabled", relief = GROOVE)
    continue_btn.pack()
    
    #init message box, with a scrolling text box
    #make sure the font is times new roman
    msg_box = st.ScrolledText(sub_dash, height = 5, width = 50, state = "disabled", font = ("Times New Roman", 10), wrap=WORD, relief = GROOVE)
    msg_box.pack(pady=5)
    send_msg("sys0")
    
    #add the image of the main character using canvas
    canvas = Canvas(sub_dash, width=64, height=64) #init the canvas
    canvas.pack(side=LEFT)
    daf = Image.open('dog_sideview.png') #import image
    daf = daf.resize((64, 64), Image.LANCZOS)
    daf2 = ImageTk.PhotoImage(daf)
    root.daf2=daf2
    canvas.create_image(0, 0, image=daf2, anchor="nw") #add the image

    #init the hint box, and set it next to the image.
    hint_box = st.ScrolledText(sub_dash, height = 5, width = 40, state = "disabled", font = ("Times New Roman", 10), wrap=WORD, relief = GROOVE)
    hint_box.pack(pady=5)
    send_hint("sys0")
    
    #side dash that holds the buttons, make sure it stays on the right side of screen
    side_dash = Frame(main_dash, bg="#06051f")
    side_dash.pack(side=RIGHT, padx=20)
    #create each menu button
    #init them to the level 1 selection
    button1 = Button(side_dash, text = "Check phone", command = partial(get_clue, 0), width = 20, relief = GROOVE)
    button1.pack()
    button2 = Button(side_dash, text = "Inspect vase", command = partial(get_clue, 1), width = 20, relief = GROOVE)
    button2.pack()
    button3 = Button(side_dash, text = "Inspect painting", command = partial(get_clue, 2), width = 20, relief = GROOVE)
    button3.pack()
    button4 = Button(side_dash, text = "?????", command = '', width = 20, relief = GROOVE)
    button4.pack()
    button5 = Button(side_dash, text = "Inspect rug", command = partial(get_clue, 3), width = 20, relief = GROOVE)
    button5.pack()
    
    #bottom dash that stays at the bottom of screen
    #contains the action buttons
    bottom_dash = Frame(root)
    bottom_dash.pack(pady=30)
    #action buttons, init to "empty"
    action1 = Button(bottom_dash, text = "Action 1", width = 10, relief = GROOVE)
    action1.pack(side=LEFT, padx=5)
    action2 = Button(bottom_dash, text = "Action 2", width = 10, relief = GROOVE)
    action2.pack(side=LEFT, padx=5)
    action3 = Button(bottom_dash, text = "Action 3", width = 10, relief = GROOVE)
    action3.pack(side=LEFT, padx=5)
    action4 = Button(bottom_dash, text = "Action 4", width = 10, relief = GROOVE)
    action4.pack(side=LEFT, padx=5)
    action5 = Button(bottom_dash, text = "Action 5", width = 10, relief = GROOVE)
    action5.pack(side=LEFT, padx=5)

    #misc window
    root.resizable(False, False) #make sure the game window is not resizable (to avoid bugs)
    #if the level select is not the first level then...
    if level_select != 1:
        curr_level = level_select - 1 #set the current level to one less...
        next_level() #so we can easily transition to next level and fix gui
    
    #attach the top_menu to the game window
    root.config(menu=top_menu)

#function that creates level select menu
def select_level():
    level_menu = Toplevel(start_menu) #create new window that houses the level select
    #level_menu.geometry("230x400")
    level_menu.title("Hunt for the Bluemoon - Level Select") #set the title accordingly
    
    #if the user chose a level then this function...
    def level_chosen(lvl):
        play_game(lvl) #creates the game window at that level
        level_menu.withdraw() #deletes level select menu
    
    #fancy text
    subtitle = Label(level_menu, text = "Choose the level you want to play.", font = ("Arial", 10), width = 50, height = 2, bg = "#06051f", fg = "white")
    subtitle.pack(fill=BOTH)
    
    #generates the level buttons
    for i in range(6):
        temp = Button(level_menu, text = "Level {}".format(i + 1), command = partial(level_chosen, i + 1), relief = GROOVE)
        temp.pack(pady=10)
    
    level_menu.resizable(False, False) #make level select unresizable

#creates the fancy title and subtitle
title = Label(start_menu, text = "Hunt for the Bluemoon", font = ("Arial Black", 30), width = 50, height = 2, bg = "#150e9c", fg = "white")
title.pack()
subtitle = Label(start_menu, text = "A Tedros Lafalaise Game", font = ("Arial", 10), width = 50, height = 2, bg = "#06051f", fg = "white")
subtitle.pack(fill=BOTH, pady=10)

#create buttons for the menu
#this button starts the game and calls the play_game func
begin_btn = Button(start_menu, text = "Start Game", command = partial(play_game, 1), font = ("Arial", 10), width = 20, relief = GROOVE)
begin_btn.pack(pady=10)
#this button starts the level select and calls the level_select func
level_btn = Button(start_menu, text = "Level Select", command = select_level, font = ("Arial", 10), width = 20, relief = GROOVE)
level_btn.pack(pady=10)
#this button exists the game and destroys the tkinter windows
exit_btn = Button(start_menu, text = "Exit Game", command = start_menu.destroy, font = ("Arial", 10), width = 20, relief = GROOVE)
exit_btn.pack(pady=10)

start_menu.resizable(False, False) #make menu unresizable
start_menu.mainloop() #start the tkinter loop (essentially a while loop)
