from faker import Faker
from gevent.pool import Group
from urllib import response
from locust import HttpUser, task, TaskSet



class WireMockParallelTests(TaskSet):

    # PARALLEL GET all contacts for companyId=123
    @task
    def parallelAllContacts(self):
        group = Group()
        for i in range(0, 5):
             group.spawn(lambda:self.client.get("/v1/contacts"))
        group.join()
        print("GET all contacts")


    # PARALLEL POST Create company
    @task
    def createNewCompany(self):
        group = Group()
        fake = Faker()

        for i in range(0, 10):
            group.spawn(lambda:self.client.post("/v1/companies", json=
            {
                "id": fake.random_int(min=1, max=500),
                "name": fake.name()
            }
        ))
      
        group.join()
        print("POST Create company")
        
    
            


# Main
class LoadTest(HttpUser):
    host = "http://localhost:8000"
    tasks = [WireMockParallelTests]
