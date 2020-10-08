import pytest

from Api.UsersApi import UsersApi
from Helpers.Client import ClientApi, ACCESS_TOKEN


@pytest.fixture(scope='module')
def client():
    yield ClientApi()


@pytest.fixture(scope='module')
def authorized_client():
    yield ClientApi(token=ACCESS_TOKEN)


@pytest.fixture(scope='module')
def get_users_api(client):
    return UsersApi(client)


@pytest.fixture(scope='module')
def get_authorized_users_api(authorized_client):
    return UsersApi(authorized_client)



