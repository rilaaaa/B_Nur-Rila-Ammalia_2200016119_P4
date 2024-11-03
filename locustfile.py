from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 to 5 seconds before each request

    @task
    def get_users(self):
        # GET request to retrieve a list of users
        self.client.get("/users")

    @task
    def create_user(self):
        # POST request to create a new user with sample data
        user_data = {
            "name": "Jane Doe",
            "username": "janedoe",
            "email": "janedoe@example.com"
        }
        self.client.post("/users", json=user_data)

    @task
    def update_user(self):
        # PUT request to update the information for user ID 1
        updated_data = {
            "name": "Jane Doe Updated",
            "username": "janedoe",
            "email": "janedoe_updated@example.com"
        }
        self.client.put("/users/1", json=updated_data)

    @task
    def delete_user(self):
        # DELETE request to remove user ID 1
        self.client.delete("/users/1")

    @task
    def patch_user(self):
        # PATCH request to partially update user information for user ID 1
        patch_data = {
            "email": "janedoe_patch@example.com"
        }
        self.client.patch("/users/1", json=patch_data)
