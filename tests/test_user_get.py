import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Get user info cases")
class TestUserGet(BaseCase):
    @allure.description("This test get user info without authorization (only username)")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")
        Assertions.assert_json_has_not_key(response, "email")

    @allure.description("This test get user info with authorization (all fields)")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid})
        expected_fields = ["username", "firstName", "lastName", "email"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("This test get user info with authorization with different user (only username)")
    def test_get_user_details_auth_as_different_user(self):
        # LOGIN WITH USER 1
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')

        # CREATE USER 2
        register_data = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        user_id_different = self.get_json_value(response2, "id")

        # GET USER 2 WITH USER 1
        response3 = MyRequests.get(f"/user/{user_id_different}",
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid})
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_key(response3, "firstName")
        Assertions.assert_json_has_not_key(response3, "lastName")
        Assertions.assert_json_has_not_key(response3, "email")