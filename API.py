import requests

url = "https://adsbexchange-com1.p.rapidapi.com/registration/%7Breg%7D/"

headers = {
    'x-rapidapi-host': "adsbexchange-com1.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)




