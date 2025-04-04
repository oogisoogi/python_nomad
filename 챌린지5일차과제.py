
import requests

movie_ids = [238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430]
url = "https://nomad-movies.nomadcoders.workers.dev/movies/"

BOLD = "\033[1m"
RESET = "\033[0m"

for movie_id in movie_ids:
    movie_urls = f"{url}{movie_id}"
    response = requests.get(movie_urls)
    data = response.json()

    print(f"{BOLD}Movie Information{RESET}")
    print(f"1.{BOLD}Title{RESET}: '{data.get('original_title')}'")
    print(f"2.{BOLD}Vote Average{RESET}: {data.get('vote_average')}")
    print(f"3.{BOLD}Overview{RESET}:")
    print(f"  {data.get('overview')}\n\n")

