from flask import Flask
import sys

app = Flask(__name__)


@app.route("/")
def hello_world():
    with open("index.html") as file:
        return file.read()


if __name__ == "__main__":
    port = 8000

    for i in range(len(sys.argv)):
        if sys.argv[i] == "--port":
            try:
                port = int(sys.argv[i + 1])

            except IndexError:
                print("fatal: No port specified after --port")
                exit()

            except ValueError:
                print("fatal: Specified port is not a number")
                exit()

    app.run(port=port)
