import requests
from itertools import islice

def get_upcoming_movies():
    upcoming_url = "https://moviesdatabase.p.rapidapi.com/titles/x/upcoming"
    headers = {
        "X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }
    response = requests.get(upcoming_url, headers=headers)
    movies = response.json().get('results')

    print('\n\t\t\t\t Upcoming Movies \n')
    print('\t\t\t\t--------------------')
    for movie in movies:
        print('-- ' + movie.get('titleText', {}).get('text'))
    print('\n\n Thank you !!!! \n')

def get_popular_movies():
    popular_url = "https://moviesminidatabase.p.rapidapi.com/movie/order/byPopularity/"
    headers = {
        "X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
        "X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
    }
    response = requests.get(popular_url, headers=headers)
    popular_movies = response.json().get('results')
    top_10 = islice(popular_movies, 10)

    print('\n\t\t\t\t Popular Movies \n')
    print('\t\t\t\t--------------------')
    for movie in top_10:
        print('-- ' + movie.get('title'))
    print('\n\n Thank you !!!! \n')

def main():
    while True:
        print('\t\t\t\t ALU Movie Hub \n')
        print('\t\t\t\t---------------')
        print('''
            1. Upcoming
            2. Popular
            3. Exit
        ''')
        search = float(input("Choose Category [1, 2, 3]: "))

        if search == 1:
            get_upcoming_movies()
        elif search == 2:
            get_popular_movies()
        elif search == 3:
            print("\n Exiting the ALU Movie Hub. Thank you! \n")
            break  # exit the loop and end the program
        else:
            print('Select a valid number between [1, 2, 3]')
            continue  # go back to the start of the loop

if __name__ == "__main__":
    main()
