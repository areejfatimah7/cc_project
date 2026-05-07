# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello demo"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Search and Upload Image</h2>

    <form action="/download" method="POST">
        <input type="text" name="query" placeholder="Enter image keyword" required>
        <button type="submit">Search & Download</button>
    </form>
    """

@app.route("/download", methods=["POST"])
def download():

    query = request.form["query"]

    # Random image based on keyword
    image_url = f"https://source.unsplash.com/600x400/?{query}"

    response = requests.get(image_url)

    filename = f"{query}.jpg"

    with open(filename, "wb") as file:
        file.write(response.content)

    return f"""
    <h3>Image downloaded successfully!</h3>

    <p>Keyword: {query}</p>

    <img src="{image_url}" width="400"><br><br>

    <p>Saved as: {filename}</p>

    <a href="/">Search Again</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)