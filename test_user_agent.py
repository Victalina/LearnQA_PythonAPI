import requests
import pytest


class TestUserAgent:
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
         "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
         "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
         "Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_user_agent(self, user_agent):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                headers={'User-Agent': user_agent})
        response_dict = response.json()
        assert 'platform' in response_dict, "В ответе нет platform"
        assert 'browser' in response_dict, "В ответе нет browser"
        assert 'device' in response_dict, "В ответе нет device"

        platform_value = response_dict['platform']
        browser_value = response_dict['browser']
        device_value = response_dict['browser']

        if user_agent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) " \
                         "AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            assert platform_value == 'Mobile', "У первого user_agent не соответствует platform"
            assert browser_value == 'No', "У первого user_agent не соответствует browser"
            assert device_value == 'Android', "У первого user_agent не соответствует device"
        if user_agent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
                         "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            assert platform_value == 'Mobile', "У второго user_agent не соответствует platform"
            assert browser_value == 'Chrome', "У второго user_agent не соответствует browser"
            assert device_value == 'iOS', "У второго user_agent не соответствует device"
        if user_agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            assert platform_value == 'Googlebot', "У третьего user_agent не соответствует platform"
            assert browser_value == 'Unknown', "У третьего user_agent не соответствует browser"
            assert device_value == 'Unknown', "У третьего user_agent не соответствует device"
        if user_agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                         "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            assert platform_value == 'Web', "У четверого user_agent не соответствует platform"
            assert browser_value == 'Chrome', "У четвертого user_agent не соответствует browser"
            assert device_value == 'No', "У четвертого user_agent не соответствует device"
        if user_agent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 " \
                         "(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            assert platform_value == 'Mobile', "У пятого user_agent не соответствует platform"
            assert browser_value == 'No', "У пятого user_agent не соответствует browser"
            assert device_value == 'iPhone', "У пятого user_agent не соответствует device"







