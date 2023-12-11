import requests
import main
url = "https://netflix99.p.rapidapi.com/v1/title/similar"

querystring = {"id":"NjVlQWdxclFOOWJralRZL25mK01vbkFyWFVIbXlhQUZleUxzTE05Y2VzeERQWER6MXQ3K0luWVdBRUdab1VVT2owaVFTQ0pJMS90ZGEvYy9BVzF0V1F+fg~~"}

headers = {
	"X-RapidAPI-Key": "e1a6c5dc00msh6edef510fc58b16p1a9b74jsnb0fa182d337c",
	"X-RapidAPI-Host": "netflix99.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


print(open(main, 'r'))

