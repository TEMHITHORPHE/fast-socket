from time import sleep
import websocket  # You can use either "python3 setup.py install" or "pip3 install websocket-client"

# to install this library.

try:
    import thread
except ImportError:
    import _thread as thread


endpoint = "Enter the Endpoint given by GFDL"
apikey = "Enter the APIKEY given by GFDL"


def Authenticate(ws):
    print("Authenticating...")
    ws.send('{"MessageType":"Authenticate","Password":"' + apikey + '"}')


def on_message(ws, message):
    
    print("Response : " + message)
   
    # Authenticate : {"Complete":true,"Message":"Welcome!","MessageType":"AuthenticateResult"}
    allures = message.split(',')
    strComplete = allures[0].split(':')
    result = str(strComplete[1])
    # print('Response : ' + result)
    if result == "true":
        print('AUTHENTICATED!!!')
   
        
def on_error(ws, error):
    print("Error")


def on_close(ws):
    print("Reconnecting...")
    websocket.setdefaulttimeout(30)
    ws.connect(endpoint)


def on_open(ws):
    # print("Connected...")
    def run(*args):
        sleep(1)
        Authenticate(ws)

    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(endpoint,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
