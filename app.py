from flask import Flask 
from reactpy import component,html,run
from reactpy.backend.flask import configure

@component
def HelloWorld():
    return html.h1("Hello world!")

@component
def layout():
    return html.div(
        html.h1("Title"),
        html.ul(
            html.li("aaa"),
            html.li("bbb"),
        ),
        HelloWorld(),
    )



app = Flask(__name__)
configure(app,layout)