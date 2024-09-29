import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.status_code)
    categories = response.json()
    for categorie in categories:
        print(categorie['name'])
    # print(categories.name)

