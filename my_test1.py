from locust import HttpUser, TaskSet

def start_get(l):
    l.client.get("/Users")

def get_user1(l):
    l.client.get("/users/1")

def get_user2(l):
    l.client.get("/users/2")

def finish_get(l):
    l.client.get("/users")

class UserBehavior(TaskSet):
    tasks = {get_user1: 2, get_user2: 1}

    def on_start(self):
        start_get(self)

    def on_stop(self):
        finish_get(self)

class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000