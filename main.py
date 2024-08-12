from flask import Flask, request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse

incoming_msg = request.values.get('Body', '').lower()

response = MessagingResponse()
msg = response.message()
msg.body("c'est une réponse de l'assistant virtuel.")


def bot():

    user_msg = request.values.get('Body', '').lower()

    response = MessagingResponse()

    q = user_msg + "geeksforgeeks.org"

    result = []

    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        result.append(i)


    msg = response.message(f"--- Results for '{user_msg}' ---")
    for result in search_results:
        msg = response.message(result)

    return str(response)

