from locust import HttpUser, TaskSet

def Create_user(l):
    l.client.post("/users", {"id": 3, "name": "Iaiceslav", "age": 113})

def Get_list(l):
    l.client.get("/Users")

def Update_user(l):
    l.client.put("/users/3", {"id": 3, "name": "Iaiceslav Velikii", "age": 113})

def Get_user(l):
    l.client.get("/users/3")

def Del_user(l):
    l.client.delete("/users/3")

class UserBehavior(TaskSet):
    tasks = {Get_list: 2, Update_user: 1, Get_user: 1}

    def on_start(self):
        Create_user(self)

    def on_stop(self):
        Del_user(self)

class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000