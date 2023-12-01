import requests
from itertools import islice
print('\t\t\t\t ALU Free Movie Hub \n')
print('\t\t\t\t---------------') 
print('''
    1.Upcoming
    2.Popular
    3.Action
''')
search = float(input("Choose Category [1, 2, 3]: "))

upcoming = "https://moviesdatabase.p.rapidapi.com/titles/x/upcoming"
headers = {
	"X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}
response = requests.get(upcoming, headers=headers)
movie = (response.json().get('results'))

popular = "https://moviesminidatabase.p.rapidapi.com/movie/order/byPopularity/"

headers = {
	"X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
	"X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
}

response = requests.get(popular, headers=headers)
movie_p = (response.json().get('results'))
top_10 = islice(movie_p, 10)




if search == 1:
    print('\n\t\t\t\t Upcoming Movie \n')
    print('\t\t\t\t--------------------') 
    for i in movie:
        print(i.get('titleText',{}).get('text'))

elif search ==2:
    print('\n\t\t\t\t Popular Movie \n')
    print('\t\t\t\t--------------------') 
    for item in top_10:
        print(item.get('title'))

else:
    print('Select valid number between [1,2,3]')






