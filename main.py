from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
CORS(app)
app.config["debug"] = True

@app.route("/")
def welcome_page():
    """
    Welcome Page
    ---
    responses:
         200:
             description: All the input received correctly
    """

    return "<h1>Welcome to Smart Labelling</h1>" \
           "<ul><li href='https://www.medicines.org.uk/emc/product/1961/smpc'>/downloaded?url=</li>" \
           "<li>/run_model?template=&pil_ratio=</li>" \
           "<li>/parameters</li>" \
           "<li>/print_pil</li>" \
           "</ul>"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/