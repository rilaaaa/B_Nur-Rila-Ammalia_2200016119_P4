from locust import HttpUser , task, between

class MyUser (HttpUser ):
    wait_time = between(1, 3)  # Waktu tunggu antara permintaan

    @task(3)  # Memberikan prioritas lebih tinggi pada endpoint ini
    def get_posts(self):
        """Endpoint untuk mendapatkan daftar posting."""
        response = self.client.get("/posts")
        if response.status_code != 200:
            print(f"Failed to get posts: {response.status_code}")

    @task(2)  # Memberikan prioritas lebih rendah pada endpoint ini
    def get_user_by_id(self):
        """Endpoint untuk mendapatkan detail pengguna berdasarkan ID."""
        user_id = 1  # Ganti dengan ID pengguna yang ingin diuji
        response = self.client.get(f"/users/{user_id}")
        if response.status_code != 200:
            print(f"Failed to get user: {response.status_code}")

    @task(1)  # Memberikan prioritas terendah pada endpoint ini
    def get_comments(self):
        """Endpoint untuk mendapatkan komentar."""
        post_id = 1  # Ganti dengan ID posting yang ingin diuji
        response = self.client.get(f"/posts/{post_id}/comments")
        if response.status_code != 200:
            print(f"Failed to get comments: {response.status_code}")