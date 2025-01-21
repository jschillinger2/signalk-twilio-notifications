
# Signal K Alert System

This project monitors a Signal K server for specific notifications and triggers an alert via a Twilio call when a match is found.

## Features

- Connects to a Signal K server via WebSocket.
- Monitors for a specific `path` defined in the configuration.
- Sends a Twilio call with a custom alert message when the specified `path` is detected.

## Prerequisites

- Python 3.8 or later.
- A Signal K server instance.
- A Twilio account with API credentials.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/signal-k-alert.git
   cd signal-k-alert
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the project:
   - Edit `config.json` with your Signal K server URL, path to monitor, and Twilio account credentials.

## Configuration

The `config.json` file should include the following:

```json
{
    "signal_k_url": "ws://your-signal-k-server:port/signalk/v1/stream",
    "signal_k_path": "path_to_monitor",
    "twilio_account_sid": "your_twilio_account_sid",
    "twilio_auth_token": "your_twilio_auth_token",
    "twilio_from_number": "+1234567890",
    "twilio_to_number": "+0987654321",
    "alert_message": "Your custom alert message here!"
}
```

## Usage

Run the application:

```bash
python app.py
```

The application will:
1. Connect to the Signal K server.
2. Monitor incoming messages for the specified path.
3. Trigger a Twilio call when the path matches.

## File Descriptions

- `app.py`: Main application script. Handles WebSocket communication and Twilio integration.
- `config.json`: Configuration file for Signal K server and Twilio settings.
- `requirements.txt`: Python dependencies for the project.

## Dependencies

- `websocket-client==1.5.2`
- `twilio==7.16.0`

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

- [Signal K](https://signalk.org/)
- [Twilio](https://www.twilio.com/)

## Disclaimer

This software is provided "as is", without warranty of any kind, express or implied. I take no responsibility for its use or the outcomes of its operation. It is considered experimental and should be used with caution.