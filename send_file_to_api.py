import requests

url = "https://image-captcha-solver.p.rapidapi.com/recognizeUrl"

payload = { "url": "https://creative-lebkuchen-cd3059.netlify.app/pic.png" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "9c00a992ecmsh0764f90751d8ba6p13b2d4jsn3bbe670f6f1f",
	"X-RapidAPI-Host": "image-captcha-solver.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())