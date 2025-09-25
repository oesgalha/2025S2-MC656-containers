import smtplib
from email.message import EmailMessage

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Email(BaseModel):
    subject: str
    sender: str
    receiver: str
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/mail")
async def send_mail(email: Email):
    msg = EmailMessage()
    msg.set_content(email.content)
    msg['Subject'] = email.subject
    msg['From'] = email.sender
    msg['To'] = email.receiver

    s = smtplib.SMTP('maildev', 1025)
    s.send_message(msg)
    s.quit()

    return {"Message": "Mail sent!"}
