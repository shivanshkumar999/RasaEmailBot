from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ActionMailSent(Action):

    def name(self) -> Text:
        return "action_mail_sent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("email")
         
        SendEmail(
        email, "Sample rasa email bot testing","Hello, this email is a testing bot for rasa email bot. Powered by DataXL solutions."
        )
        dispatcher.utter_message(text=f"Your mail was sent to {email}!")
        return []

def SendEmail(toaddr,subject,message):
    fromaddr = "666anonymailer999@gmail.com"
    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = subject

    body = message

    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()


    try:
        s.login(fromaddr, "kxwapeedoljoghol")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)
    except:
        print("An Error occured while sending email.")
    finally:
        s.quit()

