from flask import Flask 
from reactpy import component,html
from reactpy.backend.flask import configure,Options,use_websocket
from simple_websocket import Client

@component
def number_input(label):
    return html.div(
        html.label(f"{label}:"),
        html.input({"type": "number"}),
    )

@component
def form():
    ws = Client("ws://localhost:5000")
    async def post(event):
        # print(event["target"]["elements"][0]["value"])
        ValueList = [x["value"] for x in event["target"]["elements"] if len(x["value"]) != 0]

        ws.send(ValueList)
        getbmi = ws.receive()
        print(getbmi)

    return html.form(
        {
            "on_submit":post,
        },
        number_input("体重"),
        number_input("身長"),
        html.button({
            "type": "submit"
        },"Submit"),
    )

@component
def layout():

    WebSocket_Server = use_websocket()
    data = WebSocket_Server.receive()
    bmi = data[0] / (data[1] / 100)**2
    WebSocket_Server.send(bmi)

    return html.div(
        html.h1("Title"),
        form(),
    )

app = Flask(__name__)
@app.route("/",websocket=True)
def Server
configure(app,layout,Options(cors=True))