import server
from tests.conftest import client

def test_decrement_is_ok(client):

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
	places_purchased = 5
	club_points = int(club[0]["points"])
	
	request = client.post(
		"/purchasePlaces",
        data = {
			"places": places_purchased,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

	assert request.status_code == 200
	assert int(club[0]["points"]) == club_points - places_purchased