import random
genre="depressION"
genre_titles={"happy":["Happy - Pharell Williams", "I Feel Good - Pink Sweat$"], "depression":["Hate Everything - GSoul", "this is me trying - Taylor Swift"]}

def output_string(genre, genre_titles):
    low_genre=genre.lower()
    if low_genre not in genre_titles:
        return "no such genre exists, try another genre!"
    else:
        rand_pos=random.randint(0,len(genre_titles[low_genre])-1)
        rand_song=genre_titles[low_genre][rand_pos]
        return rand_song
print(output_string(genre, genre_titles))