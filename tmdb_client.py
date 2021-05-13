import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGY1MjJjYWJkNDQ2YTU5YjIyYjgyZWJiNDFjMDliNSIsInN1YiI6IjYwODE2ZjkxMDFiMWNhMDA3N2FhNzNjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._kjewxg2fFqqGDsyHmBw81-YVhoaaTKRaixzEgMPGPY"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

#def get_movies_list(list_type):
   #return call_tmdb_api(f"movie/{list_type}")

def get_movies_list(list_type):
    return call_tmdb_api(f'movie/{list_type}')

def get_poster_url(poster_path, size = "w342"):
    return f'https://image.tmdb.org/t/p/{size}{poster_path}'

def get_movie_info(movie):
    return {"title": movie["title"], "source": movie["poster_path"]}

def get_popular_movies(list_type):
    return call_tmdb_api(f'movie/{list_type}')

def get_movies(how_many, list_type = "popular"):
    print("get list: ", list_type)
    data = get_popular_movies(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f'movie/{movie_id}')
    
def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_resp = call_tmdb_api(f'movie/{movie_id}/credits')
    return api_resp["cast"]

def get_list_types():
    return ['now_playing' , 'popular', 'top_rated', 'upcoming']

