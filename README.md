# protobufs
Playground for me to learn how to us leverage protos

## Run flask-blueprint generation
```bash
$ source venv/bin/activate
$ python hellomars_gen/cli.py

>> `my_app` directory should have the flaskblueprint app
```
## Run template app
```bash
$ source venv/bin/activate
$ cd my_app/
$ flask run

# Check if the app is running properly
$ curl http://127.0.0.1:5000/
>> OK
```
