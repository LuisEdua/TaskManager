from flask import Flask
from src.TaskManager.Infrestructure.Routes import task_routes
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(task_routes.task_bp, url_prefix='/tasks')
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
