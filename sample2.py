from faker import Faker
from urllib import response
from locust import HttpUser, task, constant, events, between, constant_pacing, TaskSet



class WireMockTests(TaskSet):

    
    # GET all contacts for companyId=123
    @task
    def allContacts(self):
        self.client.get("/v1/contacts",name="All contacts")
        print("[GET] all contacts")
       

    
    # GET specific contact and verify the response if it contains to companyId=123
    @task
    def specificContact(self):
        with self.client.get("/v1/contacts/10", catch_response=True, name="Specific contact companyId=123") as response:
            if response.status_code == 200 and "10" in response.text:
                response.success()
            else: 
                response.failure("[GET] Error")
                print("ERROR")
                

    
    # GET specific info for contactId=20
    @task
    def displayContactInfo(self):
        with self.client.get("/v1/contacts/20", catch_response=True, name="Specific contact info") as response:
            if response.status_code == 200:
                print("[GET] Contact info: "+response.text)
            else:
                print("[GET] No response found")

    
    # POST Create a new company
    @task
    def createNewCompany(self):
        fake = Faker()
    
        response = self.client.post("/v1/companies", json=
        {
            "id": fake.random_int(min=1, max=500),
            "name": fake.name()
        }
        )
        print("[POST] Create company response: " + response.text)


        
    # START script to execute as pre-condition
    @events.test_start.add_listener
    def on_test_start(**kw):
        print("[START] Test execution starts")


    # STOP script to execute as post-condition
    @events.test_stop.add_listener
    def on_test_start(**kw):
        print("[STOP] Test execution stops")



# Main
class LoadTest(HttpUser):
    host = "http://localhost:8000"
    tasks = [WireMockTests]
