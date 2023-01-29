import cohere
import time
import pandas as pd
api_key = '1as4ho87uKIb1qDHZMEiSb92UreZUalaawXbMenl'
co = cohere.Client(api_key)

def song_summary(song_lyric_dict: dict) -> dict:
#lower temperature to reduce randomness
    
    song_summary_dict = {}       
    for song in song_lyric_dict:
        prompt = '''"
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
        Feel the beat from the tambourine, oh yeah"
        '''
        prompt += song_lyric_dict[song] + "\nIn summary:"
        n_generations = 5
        prediction = co.generate(
            model='xlarge',
            prompt=prompt,
            return_likelihoods = 'GENERATION',
            end_sequences=['\n'],
            max_tokens=100,
            temperature=0.0,
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
        song_summary_dict[song] = df.loc[0].iat[0]
        
    return song_summary_dict 
            
#print('''Candidate summaries for the song: You are the dancing queen
        #Young and sweet, only seventeen
        #Dancing queen
        #Feel the beat from the tambourine, oh yeah)
#print(df)
print(song_summary({'Love Story': '''
"Romeo take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince, and I'll be the princess
It's a love story, baby, just say yes"
'''}))
    
    