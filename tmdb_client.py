import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGY1MjJjYWJkNDQ2YTU5YjIyYjgyZWJiNDFjMDliNSIsInN1YiI6IjYwODE2ZjkxMDFiMWNhMDA3N2FhNzNjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._kjewxg2fFqqGDsyHmBw81-YVhoaaTKRaixzEgMPGPY"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()

def get_poster_url(poster_path, size = "w342"):
    return f'https://image.tmdb.org/t/p/{size}{poster_path}'

def get_movie_info(movie):
    return {"title": movie["title"], "source": movie["poster_path"]}

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


