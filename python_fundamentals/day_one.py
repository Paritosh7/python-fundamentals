import requests

URL = "https://api.github.com/search/repositories"
def fetch_data(languages):

    query = create_query(languages)
    parameters = {
        "q" : query,
        "sort" : "stars",
        "order" : "desc",
    }

    response = requests.get(URL,params = parameters)
    status_code = response.status_code

    if status_code == 200:
        response_json = response.json()
        
        items = response_json["items"]
        return items


    else:
        raise RuntimeError(f"An error occured with the status code of {status_code}")

def create_query(languages,min_stars = 50000):
    query = f"stars:>={min_stars} "

    for language in languages:
        query += f"language:{language} " 
    
    return query
    


if __name__ == "__main__":
        # Have a main method here
    languages = ["Javascript", "Python", "Ruby"]
    results = fetch_data(languages)
    
    for result in results:
        print(f" url : {result['owner']['html_url']}")
    