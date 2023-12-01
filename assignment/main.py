import requests

url = "https://moviesdatabase.p.rapidapi.com/titles/x/upcoming"

headers = {
	"X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# print(response.json())

todo_list = []

for x in response:
    todo_list.append("\t {}".format(x["text"]))
    print(todo_list)