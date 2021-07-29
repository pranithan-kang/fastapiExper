import helper.jwt_helper as jwt_helper
from datetime import timedelta

def test_create_access_token():
    print(jwt_helper.create_access_token(data={
        "sub": "test_user",
        "scopes": ["role_1", "role_2"]
    }, expires_delta=timedelta(minutes=30)))
