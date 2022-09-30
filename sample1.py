from locust import HttpUser, task

class WireMockTests(HttpUser):

    # GET all contacts for companyId=123
    @task
    def allContacts(self):
        self.client.get("/v1/contacts",name="All contacts")
        print("[GET] all contacts")
