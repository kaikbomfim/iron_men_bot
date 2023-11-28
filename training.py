from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSATIONS = [
    r"conversations\basic_info.json",
    "conversations\greetings.json"
]

def start():
    robot = ChatBot("IronBot")
    coach = ListTrainer(robot)

    return coach

def load_conversations():
    loaded, conversations = False, []

    for conversations_archive in CONVERSATIONS:
        try:
            with open(conversations_archive, "r", encoding="utf-8") as archive:
                training = json.load(archive)
                conversations.append(training["conversations"])
            loaded = True
        except Exception as e:
            print(e)
    
    return loaded, conversations

def trainRobot(coach, conversations):
    for conversation in conversations:
        for messages_replies in conversation:
            messages = messages_replies["messages"]
            replies = messages_replies["replies"]

            print(f"Treinando o robô. Mensagens: {messages}. Respostas: {replies}")

            for message in messages:
                coach.train([message, replies])

if __name__ == "__main__":
    coach = start()
    loaded, conversations = load_conversations()
    if loaded:
        trainRobot(coach, conversations)