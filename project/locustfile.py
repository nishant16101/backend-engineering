from locust import HttpUser, task, between


class TaskManagerUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def list_tasks(self):
        self.client.get("/tasks/")