import tkinter as tk
window = tk.Tk()

frame1 = tk.Frame(master=window, width=1000, height=1000, bg="white")
frame1.pack(fill=tk.BOTH, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=1000, bg="black")
frame2.pack(fill=tk.BOTH, side=tk.LEFT)

#ADD SONG BUTTON
#add_button = tk.Button(
 #   master=frame1,
 #   text="Click to add a song to the database!",
 #   bg="black",
 #   fg="white",
 #   height=5
 #   )
#add_button.place(x=300,y=300)

#GENRE INSTRUCTION:
genre_instr = tk.Label(
    master=frame2,
    text="Choose a genre",
    bg="black",
    fg="white"
    )
genre_instr.place(x=275,y=20)

#GENRE BUTTONS: ##################################################
g1 = tk.Button(
    master=frame2,
    text="Happy",
    bg="white",
    fg="black",
    width=38
    )
g1.place(x=260,y=100)

g2 = tk.Button(
    master=frame2,
    text="Sad (villain era)",
    bg="white",
    fg="black",
    width=38
    )
g2.place(x=260,y=200)

g3 = tk.Button(
    master=frame2,
    text="Romantic",
    bg="white",
    fg="black",
    width=38
    )
g3.place(x=260,y=300)

g4 = tk.Button(
    master=frame2,
    text="Slay Queen",
    bg="white",
    fg="black",
    width=38
    )
g4.place(x=260,y=400)
######################################################################

#FIND ME A SONG BUTTON:

find_song = tk.Button(
    master=frame2,
    text="Find me a song!",
    bg="black",
    fg="black",
    width=38
    )
find_song.place(x=260,y=500)

answer = tk.Label(
    master=frame2,
    #text="this is a test a what",
    bg="black",
    fg="white"
    )
answer.place(x=260,y=650)

#BUTTON FUNCTIONS#####################################
choice=''

def g1_button_clicked(event):
    g1.configure(bg="Dark Turquoise")
    g2.configure(bg="white")
    g3.configure(bg="white")
    g4.configure(bg="white")
    find_song.configure(bg="DodgerBlue2")
    choice="happy"
    answer.configure(text="")

def g2_button_clicked(event):
    g1.configure(bg="white")
    g2.configure(bg="Dark Turquoise")
    g3.configure(bg="white")
    g4.configure(bg="white")
    find_song.configure(bg="DodgerBlue2")
    choice="sad"
    answer.configure(text="")

def g3_button_clicked(event):
    g1.configure(bg="white")
    g2.configure(bg="white")
    g3.configure(bg="Dark Turquoise")
    g4.configure(bg="white")
    find_song.configure(bg="DodgerBlue2")
    choice="romantic"
    answer.configure(text="")
    
def g4_button_clicked(event):
    g1.configure(bg="white")
    g2.configure(bg="white")
    g3.configure(bg="white")
    g4.configure(bg="Dark Turquoise")
    find_song.configure(bg="DodgerBlue2")
    choice="Slay queen"
    answer.configure(text="")
    
g1.bind("<Button-1>", g1_button_clicked)
g2.bind("<Button-1>", g2_button_clicked)
g3.bind("<Button-1>", g3_button_clicked)
g4.bind("<Button-1>", g4_button_clicked)

def find_click(event):
    '''the global variable called choice contains one of the following:
    "happy"/"sad"/"romantic"/"Slay queen"
    
    it should put the title of the song in the spot '''
    
    answer.configure(text= HERRRREEEEEEE )

find_song.bind("<Button-1>", find_click)

##########################################################
#left side:

add_label = tk.Label(
    master=frame1,
    text="Add a new song to the database: ",
    bg="white",
    fg="black"
    )
add_label.place(x=250,y=10)

title_label = tk.Label(
    master=frame1,
    text="Enter the song title and artist: ",
    bg="white",
    fg="black"
    )
title_label.place(x=128,y=50)

new_song_title = tk.Entry(
    master=frame1,
    width=50,
    bg="black",
    fg="white"
    )
new_song_title.place(x=128,y=100)

title_label = tk.Label(
    master=frame1,
    text="Copy the song lyrics and click done:  ",
    bg="white",
    fg="black"
    )
title_label.place(x=128,y=170)

done_button = tk.Button(
    master=frame1,
    text="DONE",
    bg="mediumorchid",
    fg="white"
    )
done_button.place(x=660,y=160)

new_song_lyrics = tk.Text(
    master=frame1,
    width=50,
    bg="black",
    fg="white"
    )
new_song_lyrics.place(x=128, y=220)

def done_button(event):
    song_lyrics= new_song_lyrics.get("1.0", tk.END)
    song_title=new_song_title.get()



#places to add code:
    #191 function- input the vars into the code that adds to file
    #136 put the output of the functions that pick a song.
    
    
window.mainloop()
