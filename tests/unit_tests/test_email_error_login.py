import server
from tests.conftest import client

def test_email_login(client):

    requestOk = client.post("/showSummary", data={"email": server.clubs[0]["email"]})
    requestEmpty = client.post("/showSummary", data={"email": ""})
    requestNok = client.post("/showSummary", data={"email": "abc123"})
    
    assert requestOk.status_code == 200
    assert f"{server.clubs[0]['email']}" in requestOk.data.decode()
    assert requestEmpty.status_code == 403
    assert "Field cannot be empty, please enter a valid email." in requestEmpty.data.decode()
    assert requestNok.status_code == 403
    assert "This is not a valid email. Try again." in requestNok.data.decode()
