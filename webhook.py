# Import the necessary library
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_to_discord_webhook(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Retrieve the webhook URL from the environment variables
        webhook_url = os.getenv('webhook_url')

        # Check if the webhook URL is not found
        if webhook_url is None:
            print("Webhook URL not found in the .env file. Please set it in the .env file.")
            return

        # Prepare the payload to be sent to the Discord webhook
        payload = {
            'content': content
        }

        # Send the payload to the webhook URL
        response = requests.post(webhook_url, json=payload)

        # Check if the request was successful
        if response.status_code == 204:
            pass
        else:
            print("Failed to send content to Discord. Status code:", response.status_code)

    except FileNotFoundError:
        print("File not found. Please check the file path.")

#THIS IS TO CONFIGURE THE WEBHOOK
if __name__ == "__main__":
    file_path = "house.txt"  # Update the file path accordingly
#-CONFIG END-

send_to_discord_webhook(file_path)
