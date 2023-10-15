import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
# User info
    user_info = ["Computer Science", "Raleigh, North Carolina", "Hiking, Astronomy, Music", "East High School", "IKE"]

    # Dictionary of profiles
    profiles = {
        'Emily Davis': ["Psychology", "Portland, Oregon", "Hiking, Painting, Yoga", "Jefferson High School", "LAR"],
        'James Anderson': ["Computer Science", "Austin, Texas", "Video Games, Programming, Music", "Austin High School", "Allen Hall"],
        'Olivia Ramirez': ["Biology", "Miami, Florida", "Scuba Diving, Photography, Salsa Dancing", "Coral Gables High School", "Snyder"],
        'Ethan Turner': ["Engineering", "Seattle, Washington", "Basketball, Robotics, Reading", "Ballard High School", "PAR"],
        'Sophia Patel': ["Business Administration", "New York City, New York", "Fashion, Networking, Travel", "Stuyvesant High School", "Wassaja"],
        'Liam Johnson': ["History", "Charleston, South Carolina", "Sailing, Archaeology, Cooking", "Charleston High School", "IKE"],
        'Mia Smith': ["Environmental Science", "Boulder, Colorado", "Rock Climbing, Hiking, Sustainability", "Fairview High School", "IKE"],
        'Aiden Martinez': ["Film Production", "Los Angeles, California", "Filmmaking, Acting, Skateboarding", "Hollywood High School", "FAR"],
        'Harper Brown': ["English Literature", "Boston, Massachusetts", "Writing, Theater, Coffee", "Boston Latin School", "PAR"],
        'Oliver Clark': ["Physics", "San Francisco, California", "Astronomy, Chess, Hiking", "Lowell High School", "FAR"],
        'Chloe Nguyen': ["Nursing", "Houston, Texas", "Volunteering, Cooking, Basketball", "Memorial High School", "IKE"],
        'Mason Jackson': ["Computer Engineering", "San Diego, California", "Video Game Development, Surfing, Music", "La Jolla High School", "IKE"],
        'Ava Walker': ["Political Science", "Washington, D.C.", "Debate, Photography, Public Policy", "Georgetown Preparatory School", "PAR"],
        'Caleb Robinson': ["Mathematics", "Denver, Colorado", "Chess, Hiking, Astronomy", "East High School", "IKE"],
        'Lily Kim': ["Graphic Design", "Chicago, Illinois", "Illustration, Anime, Ice Skating", "Lincoln Park High School", "ISR"],
        'Jackson Adams': ["Economics", "Atlanta, Georgia", "Stock Trading, Soccer, Jazz Music", "Peachtree High School", "IKE"],
        'Isabella Rodriguez': ["Environmental Studies", "San Antonio, Texas", "Bird Watching, Gardening, Hiking", "Alamo Heights High School", "Allen"],
        'William Foster': ["Chemistry", "Philadelphia, Pennsylvania", "Lab Research, Playing the Guitar, Reading", "Central High School", "PAR"],
        'Amelia Turner': ["Sociology", "Nashville, Tennessee", "Community Service, Music Festivals, Writing", "Nashville High School", "LAR"],
        'Henry White': ["Mechanical Engineering", "Minneapolis, Minnesota", "Robotics, Ice Hockey, 3D Printing", "Lakeview High School","ISR"]
        }

    # Combine the user info and profile data into a single list of texts
    all_texts = [','.join(user_info)] + [','.join(profile) for profile in profiles.values()]

    # Create a TfidfVectorizer to convert the texts into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Calculate cosine similarity between the user info and all profiles
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    # Create a list of tuples with profile names and their cosine similarity scores
    similarity_scores = list(zip(profiles.keys(), cosine_similarities[0]))

    # Sort the list by cosine similarity in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    # Print the profiles ranked by similarity
    for profile, score in similarity_scores:
        print(f'{profile}: {score:.4f}')

    return render_template('index.html', profiles=similarity_scores)

if __name__ == '__main__':
    app.run(debug=True)
