from flask import Flask, request

from utils import query

# app = Flask(
#     __name__,
#     static_url_path="/source",  # default to "/static"
#     static_folder="./static_object",  # default to "./static"
# )

# static_url_path default to "/static"
# static_folder default to "./static"
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<h1>Hello Flask!</h1>"

# GET /two_sum/<x>/<y>
# @app.route("/two_sum/<x>/<y>")
# def two_sum(x, y):
#     return str(int(x) + int(y))
@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x, y):
    return str(x + y)

# REST API, RESTful API
# GET /api/v1/get-emp?dep_id=123&emp_id=456
# CRUD
# Read:     GET /api/v1/emp/<str:dep_id>/<str:emp_id>
# Create:   POST /api/v1/emp/<str:dep_id>/<str:emp_id> ; body: {token:"123123"}
# Update:   UPDATE /api/v1/emp/<str:dep_id>/<str:emp_id> ; body: {token:"123123"}
# Delete:   DELETE /api/v1/emp/<str:dep_id>/<str:emp_id> ; body: {token:"123123"}
@app.route("/api/v1/emp/<string:dep_id>/<string:emp_id>")
def emp(dep_id, emp_id):
    query_sql = f"""
    select dep_id, emp_id, emp_name from emp
    where dep_id = '{dep_id}'
    and emp_id = '{emp_id}'
    """
    result = query(query_sql)
    return result

# GET /hello?username=Allen
@app.route("/hello")
def hello():
    username = request.args.get("username")
    if not username:
        return "What is your name?"
    return f"Hello {username}!"


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    form_html = """
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>
        <button type="submit">Submit</button>
    </form>
    """
    request_method = request.method
    if request_method == "POST":
        username = request.form.get("username")
        form_html += f"""
        <h6>Hello {username}!</h6>
        """

    return form_html

@app.route("/show_image")
def show_image():
    return """
    <img src="/static/logo_123456.svg">
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
