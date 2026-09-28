from abc import ABC, abstractmethod


class NotificationSender(ABC):
   
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

#definir a regra de construçao    
    
class EmailNotificationSender(NotificationSender):
    
    def send_notification(self, message : str) -> None:
        print(f" email message - {message}")


class SMSNotificationSender(NotificationSender):
    
    def send_notification(self, message : str) -> None:
        print(f" SMS message - {message}")
        

class Notification:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender
        
    def send(self, message: str)-> None:
        #validation
        self.__notification_sender.send_notification(message)
              
        
obj = Notification(SMSNotificationSender())
obj.send('ola mundo')