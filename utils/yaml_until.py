import yaml
import os


def load_yaml(file_path):
    """读取 YAML 文件并返回 Python 对象"""
    # 如果传入的是相对路径，基于项目根目录解析
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_login_cases():
    """加载登录测试数据"""
    data = load_yaml("data/login_data.yaml")
    return data["login_cases"]