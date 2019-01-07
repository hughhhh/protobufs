from cookiecutter.main import cookiecutter

cookiecutter('flask-blueprint/',
             no_input=True,
             extra_context={'app_dir': 'my_app_dir_test'}) # extra context will overwrite whatever is in cookiecutter.json
