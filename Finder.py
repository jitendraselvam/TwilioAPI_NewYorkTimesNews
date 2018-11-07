from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from newsAPI import getNews

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():

    resp = MessagingResponse()
    resp.message(getNews())

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)