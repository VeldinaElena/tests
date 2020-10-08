from Helpers.Constants import ServiceCodes
from tests.User_api_tests.api_actions.UserActions import generate_user_data


class TestUsers:

    def test_get_users(self, get_users_api):
        response = get_users_api.get_users()
        assert response['code'] == ServiceCodes.OK
        assert response['data'], 'There is no user'

    def test_create_user(self, get_authorized_users_api, get_users_api):
        user_data = generate_user_data()
        response_create_user = get_authorized_users_api.create_user(user_data)
        assert response_create_user['code'] == ServiceCodes.CREATED
        user_id = response_create_user['data']['id']
        response_get_user = get_users_api.get_user_by_id(user_id)
        assert response_get_user['code'] == ServiceCodes.OK
        assert response_create_user['data'] == response_get_user['data']

    def test_create_user_unauthorized(self, get_users_api):
        user_data = generate_user_data()
        response = get_users_api.create_user(user_data)
        assert response['code'] == ServiceCodes.UNAUTHORIZED

    def test_create_user_unprocessable_entity(self, get_authorized_users_api):
        user_data = []
        response = get_authorized_users_api.create_user(user_data)
        assert response['code'] == ServiceCodes.UNPROCESSABLE_ENTITY
