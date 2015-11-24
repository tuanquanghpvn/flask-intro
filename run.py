from flask import Flask
app = Flask(__name__)

# register blueprint
from apps.admin import admin

app.register_blueprint(admin)

if __name__ == '__main__':
    app.run(debug=True)
