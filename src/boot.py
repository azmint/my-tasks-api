from flask import Flask

from infrastructure.flask.application_factory import create

app: Flask = create()

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
