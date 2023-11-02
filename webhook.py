#THIS FILE SENDS THE HOUSE.TXT FILE CONTENT TO THE WEBHOOK
import requests

def send_to_discord_webhook(webhook_url, file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Retrieve the webhook URL from the secret
        webhook_url = os.environ.get('HOOK')

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
    # webhook_url = "INPUT YOUR WEBHOOK HERE"
    file_path = "house.txt"  # Update the file path accordingly
#-CONFIG END-

    send_to_discord_webhook(webhook_url, file_path)
