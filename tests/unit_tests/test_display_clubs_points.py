import server
from tests.conftest import client

def test_display_club_points(client):
    
    
    clubs = [
        {
            "name": "Club de Reims",
            "email": "reimsclub@gmail.com",
            "points": "10"
        },

        {
            "name": "Club de Paris",
            "email": "parisclub@gmail.com",
            "points": "10"
        }
    ]

    server.clubs = clubs

    request = client.get("/clubsPoints")

    assert request.status_code == 200
    assert clubs[0]['name'] in request.data.decode()
    assert clubs[0]['points'] in request.data.decode()