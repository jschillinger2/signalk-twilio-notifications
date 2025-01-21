import json
import websocket
import requests
from twilio.rest import Client


# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

SIGNAL_K_URL = config["signal_k_url"]
SIGNAL_K_PATH = config["signal_k_path"]

TWILIO_ACCOUNT_SID = config["twilio_account_sid"]
TWILIO_AUTH_TOKEN = config["twilio_auth_token"]
TWILIO_FROM_NUMBER = config["twilio_from_number"]
TWILIO_TO_NUMBER = config["twilio_to_number"]

def make_twilio_call(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=TWILIO_TO_NUMBER,
            from_=TWILIO_FROM_NUMBER
        )
        print(f"Call initiated with SID: {call.sid}")
    except Exception as e:
        print(f"Failed to make call: {e}")

def extract_single_path(data):
    """
    Extracts a single 'path' value from the given dictionary.

    Args:
        data (dict): The dictionary containing the data.

    Returns:
        str: The extracted path.

    Raises:
        ValueError: If no path or more than one path is found.
    """
    paths = []
    updates = data.get('updates', [])
    for update in updates:
        values = update.get('values', [])
        for value in values:
            path = value.get('path')
            if path:
                paths.append(path)
    
    if len(paths) == 1:
        return paths[0]
    elif len(paths) == 0:
        raise ValueError("No paths found in the data.")
    #else:
    #    raise ValueError(f"Multiple paths found: {paths}")

        
def on_message(ws, message):
    """Handle incoming Signal K messages."""
    try:
        data = json.loads(message)
        path = extract_single_path(data)
        #print("Extracted path:", path)
        #print("Search path:   ", SIGNAL_K_PATH)
        if path == SIGNAL_K_PATH:
            print("!!! Path Match")
            make_twilio_call(f"Alert {path}")
    except json.JSONDecodeError:
        print("Failed to decode message:", message)

def on_error(ws, error):
    """Handle WebSocket errors."""
    print("WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    """Handle WebSocket closure."""
    print("WebSocket closed.")

def on_open(ws):
    """Handle WebSocket connection."""
    print("Connected to Signal K.")

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(
        SIGNAL_K_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
