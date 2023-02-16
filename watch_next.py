import spacy

nlp = spacy.load('en_core_web_md')

prime_description = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

def watch_next(description):
    movie_list = []
    max_similarity = 0

    with open ("movies.txt","r+",encoding="UTF-8") as loadfile:

        for index, line in enumerate(loadfile):
            movie = line.replace("\n","").split(":")
            movie_list.append(movie)

        for movie in movie_list:
            check_description = nlp(movie[1])
            prime_description = nlp(description)
            similarity = prime_description.similarity(check_description)

            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_file = movie[0]

    return(most_similar_file)

file_recommendation = watch_next(prime_description)

print(f"We think you will like {file_recommendation}")