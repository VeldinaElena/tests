
class UsersApi:
    def __init__(self, client):
        self.client = client

    def get_users(self):
        url = '/public-api/users'
        return self.client.get(url=url)

    def create_user(self, user_data):
        url = '/public-api/users'
        body = user_data
        return self.client.post(url=url, data=body)

    def get_user_by_id(self, user_id):
        url = f'/public-api/users/{user_id}'
        return self.client.get(url=url)
