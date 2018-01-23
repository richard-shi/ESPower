
from microWebSrv import MicroWebSrv
from controller import Controller
import json

def setup_routes(controller=None):
    if controller is None:
        controller = Controller()

    def _status(client, response):
        print("GET status/ from {}".format(client.GetAddr()))

        response.WriteResponseJSONOk({
            "power": controller.status()
        })

    def _change_status(client, response):
        try:
            content = client.ReadRequestContent(1024)
            print("POST status/ from {} of {}".format(client.GetAddr(), content))

            status_request = json.loads(content)
            controller.change(status_request["power"])
            response.WriteResponseOk()
        except:
            client.WriteResponseBadRequest()

    return [
        ('/status', 'GET', _status),
        ('/status', 'POST', _change_status)
    ]

def start():
    print("Starting ESPower WebServer!")
    routes = setup_routes()
    server = MicroWebSrv(routeHandlers=routes, webPath="/www")
    server.Start(threaded=False)
