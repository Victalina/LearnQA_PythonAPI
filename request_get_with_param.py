from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "user"})
print(response.text)
parsed_response_text = response.json()
print(parsed_response_text["answer"])
print(response.status_code)

response = requests.get("https://playground.learnqa.ru/api/get_text")

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
