import allure
import pytest
from api.posts_api import PostsApi


@allure.feature("文章接口模块")
class TestPosts:

    @pytest.fixture(autouse=True)
    def setup(self):
        """每个用例前创建 API 实例"""
        self.api = PostsApi()

    @allure.story("获取所有文章")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_get_all_posts(self):
        resp = self.api.get_all_posts()
        assert resp.status_code == 200, f"状态码异常：{resp.status_code}"
        data = resp.json()
        assert isinstance(data, list), "返回结果不是列表"
        assert len(data) == 100, f"文章数量不是 100，实际：{len(data)}"

    @allure.story("获取指定文章")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_get_single_post(self):
        resp = self.api.get_post(1)
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1, f"返回的 id 不是 1，实际：{data['id']}"
        assert "title" in data and "body" in data, "缺少必要字段"

    @allure.story("获取不存在的文章")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_get_nonexistent_post(self):
        resp = self.api.get_post(99999)
        assert resp.status_code == 404, f"状态码应为 404，实际：{resp.status_code}"

    @allure.story("创建文章")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.p0
    def test_create_post(self):
        resp = self.api.create_post("测试标题", "测试内容")
        assert resp.status_code == 201, f"状态码应为 201，实际：{resp.status_code}"
        data = resp.json()
        assert data["title"] == "测试标题"
        assert data["body"] == "测试内容"
        assert "id" in data, "返回结果缺少 id"

    @allure.story("更新文章")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_update_post(self):
        resp = self.api.update_post(1, "新标题", "新内容")
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "新标题"
        assert data["body"] == "新内容"

    @allure.story("删除文章")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.p1
    def test_delete_post(self):
        resp = self.api.delete_post(1)
        assert resp.status_code == 200, f"状态码应为 200，实际：{resp.status_code}"