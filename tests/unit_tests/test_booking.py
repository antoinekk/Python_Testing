import server
from tests.conftest import client

def test_booking(client):
	
	club = [
		{
			"name": "Club de Reims",
			"email": "reimsclub@gmail.com",
			"points": "10"
		}
	]
	
	competition = [
		{
            "name": "Reims competition",
            "date": "2018-11-18 08:00:00",
            "numberOfPlaces": "15"
        }
	]
	
	server.clubs = club
	server.competitions = competition
	
	request = client.get(f"/book/{competition[0]['name']}/{club[0]['name']}")
	bad_request = client.get(f"/book/test/{club[0]['name']}")
	
	assert request.status_code == 200
	assert bad_request.status_code == 404
	assert "Something went wrong. Please try again." in bad_request.data.decode()