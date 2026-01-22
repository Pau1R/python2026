from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name):
        self.sender_name = sender_name

    @abstractmethod
    def send(recipient, message):
        pass

    def format_message(self, message):
        return f"[{self.sender_name}] {message}"

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name, sender_email):
        self.sender_name = sender_name
        self.sender_email = sender_email

    def send(self, recipient, message):
        text = super().format_message(message)
        print(f'EMAIL to {recipient}: {text} (from {self.sender_email})')

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name, sender_phone):
        self.sender_name = sender_name
        self.sender_phone = sender_phone

    def send(self, recipient, message):
        text = super().format_message(message)
        print(f'SMS to {recipient}: {text} (from {self.sender_phone})')

class NotificationService:
    def __init__(self, channels):
        self.channels = channels

    def notify_all(self, recipient, message):
        for channel in self.channels:
            channel.send(recipient, message)

emailChannel = EmailChannel('Иван Петрович', 'petrovich@gmail.com')
sMSChannel = SMSChannel('Светлана Иванова', '98712345675')

notificator = NotificationService([emailChannel, sMSChannel])
notificator.notify_all('Иван', 'Хватит заниматься, пошли домой!!!')
notificator.notify_all('Иван', 'Хочу учиться!!!')
