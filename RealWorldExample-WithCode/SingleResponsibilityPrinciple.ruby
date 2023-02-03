Single Responsibility Principle (SRP) - A class should have only one responsibility.
Example: A class that is responsible for sending email notifications.

class EmailNotifier:
    def __init__(self, email_config):
        self.email_config = email_config

    def send_email(self, recipient, subject, message):
        # code to send email using self.email_config
        pass
