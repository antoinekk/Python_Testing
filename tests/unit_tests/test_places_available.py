import server
from tests.conftest import client

def test_places_available(client):

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
            "numberOfPlaces": "2"
        }
	]

    server.clubs = club
    server.competitions = competition

    places_purchased = 5

    request = client.post(
		"/purchasePlaces",
        data = {
			"places": places_purchased,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    assert request.status_code == 400
    assert "There are not enough places available." in request.data.decode()