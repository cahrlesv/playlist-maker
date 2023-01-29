import sys

def add_song_helper():
    ''' () -> file IO

    takes a song title and song lyrics and puts it formatted in the database of songs labelled mchacks10songs.txt
    
    
    '''
    #check that the song title is in format title - artist- catch errors.
    
    #print instructions for song input
    
    song_title = input("Input a song title: ")
    print("Input the song lyrics. (When you're done hit enter, cmd+D): ")
    
    song_lyrics = sys.stdin.read()
    
    
    fobj = open("mchacks10songs.txt", "a")
    fobj.write(song_title)
    fobj.write("\0")
    
    index = 0
    while index < len(song_lyrics):
        if song_lyrics[index] == "\n":
            song_lyrics = song_lyrics[:index]+" "+song_lyrics[index+1:]
        index = index+1
    
    
    fobj.write(song_lyrics)
    fobj.write("\n")
    
    fobj.close()
    
    
def get_song_dict():
    fobj = open("mchacks10songs.txt", "r")
    
    file_string = fobj.read()
    
    r_song_title = True
    r_song_lyrics = False
    
    title_key = ''
    lyrics_value = ''
    
    song_dict = {}
    
    for c in file_string:
        if c == "\0":
            r_song_title = False
            r_song_lyrics = True
            continue
        if c == "\n":
            if (title_key != '') and (lyrics_value != ''):
                song_dict[title_key] = lyrics_value
            r_song_lyrics = False
            r_song_title = True
            title_key = ''
            lyrics_value = ''
            continue
        
        if r_song_title:
            title_key += c
        elif r_song_lyrics:
            lyrics_value += c
        
        
    fobj.close()
    
    return song_dict

def add_song():
    add_song_helper()
    return get_song_dict()

'''try:
    song_title = input("enter a song title with this formatx2")
    space1 = False
    dash = False
    space2 = False
    for c in song_title:
        if c == "-":
            dash = True
            if c_prev == " ":
                space1 = True
        if c_prev == "-":
            if c == " ":
                space2 = True
    
    if !(dash and space1 and space2):
        raise 
        c_prev = c
        '''
            
    


    

