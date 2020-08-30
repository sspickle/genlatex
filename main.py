import flaskApp

app = flaskApp.create_app()

@app.shell_context_processor
def make_shell_context():

    return {'app': app}


