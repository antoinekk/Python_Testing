import server
from tests.conftest import client

def test_logout(client):
    request = client.get("/logout")
    assert request.status_code == 302