from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token='YOUR_SLACK_API_TOKEN')

def send_message(channel, text):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
