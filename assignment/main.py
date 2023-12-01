import requests

url = "https://moviesdatabase.p.rapidapi.com/titles/x/upcoming"

headers = {
	"X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())