from robot import *
from flask import Flask, jsonify

_, robot = start()
service = Flask("IronBot")

@service.get("/info")
def get_info():
    return jsonify(
        description = "Serviço de robô da academia Iron Men",
        version = "1.0"
    )

@service.get("/replies/<message>")
def get_replies(message):
    feedback = jsonify(
        replies = "não sei responder a essa pergunta"
    )

    replies = robot.get_response(message)
    if replies.confidence >= MINIMUM_TRUST:
        feedback = jsonify(
            replies = replies.text
        )
    
    return feedback

if __name__ == "__main__":
    service.run(host="0.0.0.0", debug=True)
