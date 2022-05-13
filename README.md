# Puzzle Verifier

Allows validation of puzzles via a local web app.

It is written in Python and uses Flask to open a local web app for a localhost port.

## Usage

### Install flask for python
```
pip install flask
```
### Open a localhost port

```
python main.py --port [PORT]
```

The ``[PORT]``-parameter needs to be an integer. Best between 5000 and 8000. Default port is 8000. \
The console must remain open while the web app is in use.

### Open localhost

```
http://localhost:[PORT]/
```
