from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

incoming_msg = request.values.get('Body', '').lower()

response = MessagingResponse()
msg = response.message()
msg.body("c'est une réponse de l'assistant virtuel.")


def bot():

    user_msg = request.values.get('Body', '').lower()

    response = MessagingResponse()

    q = user_msg + "akambinabil@outlook.com"

    result = []

