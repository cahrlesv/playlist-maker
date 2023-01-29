import cohere
import random
import sys
import pandas as pd
from cohere.classify import Example
co = cohere.Client('mxOxA0OzCQz6obquuXxRAeB48MlbGNmiKqaZIPDA')

songs = {"dancing queen" : '''"
            Because I'm happy
            Clap along if you feel like happiness is the truth
            In Summary: Clap if you are happy!
            Ain't no more tears
            Ain't gonna cry
            Boy, I'll do anything to get you off my mind
            I'm gonna dance
            Under the lights
            In summary: I broke up with you but I don't need you anymore!
            You are the dancing queen
            Young and sweet, only seventeen
            Dancing queen
            Feel the beat from the tambourine, oh yeah
            In summary:"'''}

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

def function2(dic):
    dict2 = {}
    k = dic.keys()
    
    for x in k:
        dict2.update({x : summarize(dic.get(x))})
        
    return dict2

def summarize(lyrics):
    '''Returns a dictionary of song-summary pairs
    '''
        #song_summary_dict = {}
        #for song in song_lyric_dict:       
    prompt = lyrics

    n_generations = 5
    prediction = co.generate(
    model='xlarge',
    prompt=prompt,
    return_likelihoods = 'GENERATION',
    stop_sequences=['"'],
    max_tokens=100,
    temperature=0.7,
    num_generations=n_generations,
    k=0,
    p=0.75)

            # Get list of generations
    gens = []
    likelihoods = []
    for gen in prediction.generations:
        gens.append(gen.text)
        sum_likelihood = 0
        for t in gen.token_likelihoods:
            sum_likelihood += t.likelihood
            # Get sum of likelihoods
        likelihoods.append(sum_likelihood)
    pd.options.display.max_colwidth = 200
    # Create a dataframe for the generated sentences and their likelihood scores
    df = pd.DataFrame({'generation':gens, 'likelihood': likelihoods})
    # Drop duplicates
    df = df.drop_duplicates(subset=['generation'])
    # Sort by highest sum likelihood
    df = df.sort_values('likelihood', ascending=False, ignore_index=True)
            #for value in likelihood:
                #if value == max(likelihood):
                    #song_summary_dict[song] = gen

    return df.loc[0].iat[0]

def classify(dict3):
    genres = {"happy" : [],
              "sad" : [],
              "slay queen" : [],
              "romantic" : []}
    songs = list(dict3.keys())
    i = 0

    classifications = co.classify(
        model ='large',
        inputs = list(dict3.values()),
        examples = [Example("feeling good and happy", "happy"),
                    Example("clapping, dancing and singing", "happy"),
                    Example("Feeling the groove on a sunny day","happy"),
                    Example("I'm all alone and crying", "sad"),
                    Example("My heart is so broken", "sad"),
                    Example("I hate that they left me", "sad"),
                    Example("All the reasons I love you", "romantic"),
                    Example("You're the only one for me", "romantic"),
                    Example("I would do anything for you", "romantic"),
                    Example("I feel like I'm on top of the world", "slay queen"),
                    Example("Getting revenge on my enemies", "slay queen"),
                    Example("You can't take me down", "slay queen"),
                    ])
    for x in classifications.classifications:
        for y in genres:
            if x.prediction == y:
                genres.get(y).append(songs[i])
                i += 1
                
    return genres


def output_string(genre, genre_titles):
    low_genre=genre.lower()
    if low_genre not in genre_titles.keys():
        return "no such genre exists, try another genre!"
    else:
        if genre_titles.get(low_genre) == []:
            return "no songs available, please add songs"
        else:
            rand_pos=random.randint(0,len(genre_titles[low_genre])-1)
            rand_song=genre_titles[low_genre][rand_pos]
            return rand_song

#print(output_string(genre, genre_titles))
    
#function2(songs)
add_song()    
    
def song_rec():
    print('enter genre')
    genre=input()
    genre_titles = classify(function2(get_song_dict()))
    
    print(output_string(genre, genre_titles))

            