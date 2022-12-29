from locust import HttpUser, task, between

class TestProjectPerformance(HttpUser):

    wait_time = between(0,5)

    @task
    def login(self):
        self.client.get("/")
        self.client.post("/showSummary", data={'email': "john@simplylift.co"})
    
    @task
    def booking(self):
        self.client.get(f"/book/Spring Festival/Simply Lift")
    
    @task
    def purchase(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 0,
                "club": "Simply Lift",
                "competition": "Spring Festival"
            }
        )
    
    @task
    def getPoints(self):
        self.client.get("/clubsPoints")
    
    @task
    def logout(self):
        self.client.get("/logout")


