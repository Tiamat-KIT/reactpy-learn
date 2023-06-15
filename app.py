from flask import Flask 
from reactpy import component,html,run
#from reactpy.backend.flask import configure,Options,use_websocket
from simple_websocket import Client

@component
def number_input(label):
    return html.div(
        html.label(f"{label}:"),
        html.input({"type": "number"}),
    )

@component
def form():
    async def post(event):
        # print(event["target"]["elements"][0]["value"])
        ValueList = [x["value"] for x in event["target"]["elements"] if len(x["value"]) != 0]
        # ws.send(ValueList)
        # getbmi = ws.receive()
        # print(getbmi)
        print(ValueList)
        bmi = float(ValueList[0]) / ((float(ValueList[1]) / 100)** 2)
        print(bmi)


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
    # ws = Client("http://localhost:5000")
    

    return html.div(
        html.h1("Title"),
        form(),
        html.div({"id": "result","style": "padding: 5px"},["結果:"])
    )

run(layout)
#app = Flask(__name__)

#@app.route("/",websocket=True)
#def server():
    #configure(app,layout,Options(cors=True))
    #WebSocket_Server = use_websocket()
    #data = WebSocket_Server.receive()
    #bmi = data[0] / (data[1] / 100)**2
    #WebSocket_Server.send(bmi)
