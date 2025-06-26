from fastapi import FastAPI, Depends
from typing import Annotated

app= FastAPI()

class Email_service:
    def send_email(self, recipient: str, message: str):
        print(f"Sending email to {recipient}: {message}")
        
def get_email():
    return Email_service()

email_dependency= Annotated[Email_service, Depends(get_email)]
    
@app.get("/service")
def send_email(recipient: str, message: str, email_service: email_dependency):
    return email_service.send_email(recipient, message)