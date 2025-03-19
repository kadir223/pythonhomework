import requests
import random


# Task 1: Fetch weather data
def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data.")


# Task 2: Fetch movie recommendations
def get_movie_recommendation(genre):
    api_key = "YOUR_TMDB_API_KEY"  # Replace with your API key
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"

    genre_response = requests.get(genre_url)
    if genre_response.status_code != 200:
        print("Error fetching genres.")
        return

    genres = genre_response.json()["genres"]
    genre_dict = {g["name"].lower(): g["id"] for g in genres}

    if genre.lower() not in genre_dict:
        print("Genre not found.")
        return

    genre_id = genre_dict[genre.lower()]
    movie_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    movie_response = requests.get(movie_url)

    if movie_response.status_code == 200:
        movies = movie_response.json()["results"]
        if movies:
            random_movie = random.choice(movies)
            print(f"Recommended Movie: {random_movie['title']}")
            print(f"Overview: {random_movie['overview']}")
        else:
            print("No movies found for this genre.")
    else:
        print("Error fetching movie data.")

