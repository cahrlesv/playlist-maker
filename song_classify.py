import cohere
from cohere.classify import Example

def classify(summ):
    genres = {"happy" : [],
              "sad" : [],
              "slay queen" : [],
              "romantic" : []}
    summ.keys = ["happy", "teardrops on my guitar", "good as hell", "Dancing on my own", "bad guy", "mine"]
    i = 0

    co = cohere.Client('mxOxA0OzCQz6obquuXxRAeB48MlbGNmiKqaZIPDA')
    classifications = co.classify(
        model ='large',
        inputs = summ.values,
        examples = [Example("feeling good and happy", "happy"),
                    Example("clapping, dancing and singing", "happy"),
                    Example("Sunny day and smiles","happy"),
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
            
            