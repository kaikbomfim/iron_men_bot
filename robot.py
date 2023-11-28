from chatterbot import ChatBot

MINIMUM_TRUST = 0.75

def start():
    robot = ChatBot("IronBot", read_only = True, logic_adapters = [
        {
            "import_path": "chatterbot.logic.BestMatch"
        }
    ])

    return True, robot

def run_robot(robot):
    while True:
        message = input("Digite alguma coisa...\n")
        if(message == ""):
            pass
        else:
            replies = robot.get_response(message.lower())
            if replies.confidence >= MINIMUM_TRUST:
                print(f"IronBot >> {replies.text}")
            else:
                print(f"Me desculpe, mas ainda não tenho respostas para essa pergunta.")
                print("Pergunte outra coisa.")

if __name__ == "__main__":
    started, robot = start()
    if started:
        run_robot(robot)