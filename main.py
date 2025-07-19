from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# 🧠 Simple Q&A database
tech_faq = {
    "dhcp": "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses to devices on a network.",
    "wifi slow": "Try restarting your router, reducing interference, or switching to a less crowded channel.",
    "ip address": "An IP address is a unique identifier for a device on a network.",
    "ping": "Ping is a command used to test connectivity between two devices.",
    "dns": "DNS (Domain Name System) translates domain names into IP addresses.",
    "blue screen": "Windows needs to be reinstalled. Please log a request on http://elmaramerica.co.za for collection."
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # 🧠 Match keywords
    reply = "Sorry, I don't have info on that. Try asking about DHCP, DNS, or IP addresses."
    for keyword in tech_faq:
        if keyword in incoming_msg:
            reply = tech_faq[keyword]
            break

    msg.body(reply)
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)