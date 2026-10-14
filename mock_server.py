from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟数据
POSTS = [{"id": i, "title": f"标题{i}", "body": f"内容{i}", "userId": 1}
         for i in range(1, 101)]


@app.route("/posts", methods=["GET"])
def get_all_posts():
    return jsonify(POSTS)


@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    for p in POSTS:
        if p["id"] == post_id:
            return jsonify(p)
    return jsonify({"error": "not found"}), 404


@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    new_post = {
        "id": 101,
        "title": data.get("title"),
        "body": data.get("body"),
        "userId": data.get("userId", 1),
    }
    return jsonify(new_post), 201


@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.get_json()
    return jsonify({
        "id": post_id,
        "title": data.get("title"),
        "body": data.get("body"),
        "userId": data.get("userId", 1),
    })


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    return jsonify({}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)