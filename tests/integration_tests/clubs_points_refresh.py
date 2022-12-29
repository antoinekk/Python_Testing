import server
from tests.conftest import client

def test_clubs_points_refresh(client):
    
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
    
    points_before_purchase = int(club[0]["points"])
    places_purchased = 5

    client.post(
        "/purchasePlaces",
        data = {
			"places": places_purchased,
            "club": club[0]["name"],
            "competition": competition[0]["name"]
        }
    )

    request = client.get("/clubsPoints")

    assert request.status_code == 200
    assert f"<td>{club[0]['name']}</td>" in request.data.decode()
    assert f"<td>{points_before_purchase - places_purchased}</td>" in request.data.decode()

