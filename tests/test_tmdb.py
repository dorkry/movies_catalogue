import tmdb_client, pytest
from unittest.mock import Mock    

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
    mock_single_movie = {'title': "Batman Forever"}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    single_movie = tmdb_client.get_single_movie(22)
    assert single_movie == mock_single_movie

def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = {"cast": ['aaa', 'bbb']}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    single_movie_cast = tmdb_client.get_single_movie_cast(3)
    assert single_movie_cast is not None

def test_get_poster_url(monkeypatch):
   mock_poster_path = "some-poster-path"
   request_mock = Mock()
   response = request_mock.return_value
   response.return_value = mock_poster_path
   expected_default_size = 'w342'
   monkeypatch.setattr("tmdb_client.requests.get", request_mock)
   
   poster_url = tmdb_client.get_poster_url(poster_path = mock_poster_path)
   assert expected_default_size in poster_url

def test_get_popular_movies(monkeypatch):
    mock_get_popular_movies = {"cast": ['aaa', 'bbb']}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_get_popular_movies
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    single_movie_cast = tmdb_client.get_single_movie_cast("popular")
    assert single_movie_cast is not None
