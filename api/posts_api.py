from api.base_api import BaseApi


class PostsApi(BaseApi):
    """文章相关接口"""

    def get_all_posts(self):
        return self.get("/posts")

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, title, body, user_id=1):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.post("/posts", json=payload)

    def update_post(self, post_id, title, body, user_id=1):
        payload = {"id": post_id, "title": title, "body": body, "userId": user_id}
        return self.put(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")