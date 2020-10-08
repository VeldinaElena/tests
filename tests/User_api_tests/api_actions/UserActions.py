from Helpers.Constants import Gender, UserStatus
from Helpers.Helpers import generate_value, generate_email


def generate_user_data():
    return {'login': generate_value(length=10),
            'password': generate_value(length=10),
            'email': generate_email(),
            'name': generate_value(10),
            'gender': Gender.FEMALE,
            'status': UserStatus.ACTIVE
            }
