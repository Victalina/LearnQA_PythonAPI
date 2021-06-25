import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response1.status_code)
print(response1.text)

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response2.status_code)
print(response2.text)

response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})

print(response3.status_code)
print(response3.text)

list_of_methods = ["GET", "POST", "PUT", "DELETE"]

for method in list_of_methods:
    for t in list_of_methods:
        if t == "GET":
            response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': method})
            print(f"Тип запроса {t}, метод {method}, статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if t != method and response4.text == '{"success":"!"}':
                print(f"Найдено не соответствие: параметр {t} и тип запроса {method} возвращает успешный результат")
        elif t == "POST":
            response4 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Тип запроса {t}, метод {method}, статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if t != method and response4.text == '{"success":"!"}':
                print(f"Найдено не соответствие: параметр {t} и тип запроса {method} возвращает успешный результат")
        elif t == "PUT":
            response4 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Тип запроса {t}, метод {method}, статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if t != method and response4.text == '{"success":"!"}':
                print(f"Найдено не соответствие: параметр {t} и тип запроса {method} возвращает успешный результат")
        elif t == "DELETE":
            response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Тип запроса {t}, метод {method}, статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if t != method and response4.text == '{"success":"!"}':
                print(f"Найдено не соответствие: параметр {t} и тип запроса {method} возвращает успешный результат")