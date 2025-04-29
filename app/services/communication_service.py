from azure.communication.email import EmailClient
from azure.identity import DefaultAzureCredential
from app.models.communication_models import SendEmailModel  # Assuming SendEmailModel is in the same directory
from dotenv import load_dotenv
import os
from typing import Any


load_dotenv()

class EmailService:
    def __init__(self):
        connection_string = os.getenv("AZURE_COMMUNICATION_CONN_STR")
        endpoint = os.getenv("AZURE_COMMUNICATION_ENDPOINT")
        """
        Initializes the EmailService.

        Args:
            connection_string (str, optional): The connection string for Azure Communication Services. Defaults to None.
            endpoint (str, optional): The endpoint for Azure Communication Services. Defaults to None.
        
        Note: Either connection_string or endpoint is required. If both are provided, connection_string will be used.
        """
        if connection_string:
            self.client = EmailClient.from_connection_string(connection_string)
        elif endpoint:
            credential = DefaultAzureCredential()
            self.client = EmailClient(endpoint, credential)
        else:
            raise ValueError("Either connection_string or endpoint must be provided.")

    def send_email(self, email_model: SendEmailModel) -> Any:
        """
        Sends an email using Azure Communication Services.

        Args:
            email_model (SendEmailModel): The email details.

        Returns:
            str: The operation ID of the sent email.

        Raises:
            Exception: If there is an error sending the email.
        """
        try:
            # Prepare the email message
            message = {
                "senderAddress": email_model.fromAddress,
                "content": {
                    "subject": email_model.subject,
                    "html": email_model.body,  # Assuming body is HTML, can be changed to text if needed
                },
                "recipients": {
                    "to": [{"address": email_model.toAddress}]
                },
            }

            # Send the email
            poller = self.client.begin_send(message)
            result = poller.result()
            return result  # Return the message ID of the sent email
        except Exception as e:
            raise Exception(f"Error sending email: {e}")
