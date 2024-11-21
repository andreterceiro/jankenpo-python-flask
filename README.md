# jakenpo-python-flask

This is a simple Jankenpo game in Python with the Flask framework


# Code

The code is simple. The logic is in the file `index.py`. It renders a HTML code (`index.html` who uses some assets that are in the `assets` folder).

`index.py` have two methods related to requests. One, `index()`, only renders a template that allows the user to select his option and send to the `process` method through `POST` method . The other, `process`, process the request with user option, select an computer random option, compares the this options and sends to the post request:
- The computer option;
- The winner;

(The page already know the user option)


# Execution

After cloning the repository, please install Flask:
```
pip install flask
```

Then execute the code with this command:
```
python index.py
```

You can interact with the game opening this URL in a browser:
```
http://127.0.0.1:7000
```


# Demo
[Vídeo](https://youtu.be/JPPvAEw8l3s)


# Requeirements

Please see [requirements.txt](requirements.txt)


# Application port

I changed in november 21, 2024 the application port to **7000**.