#imported flask and chatBot
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#configured app
app = Flask(__name__)
#initialized chatbot
toy_bot = ChatBot("Amina's ChatBot")
#ListTrainer Allows a chat bot to be trained using a list of strings where the list represents a conversation
trainer_Amina = ListTrainer(toy_bot)
trainer_Amina.train(["Hey",
                "Hi there!",
                "Hi",
                "Hi!",
                "How are you doing?",
                "I'm doing great.",
                "That is good to hear",
                "Thank you.",
                "You're welcome.",
                "what do you sell? ", "We sell exciting toys",
                "Can you recommend me any toy?",
                "Sure, first told me that if you have a daughter or son?",
                "son", "you can have a car toy, boys love playing with cars"
                "daughter", "you can have a doll toy, girls love playing with dolls",
                "Thank you.",
                "You're welcome.",
                "can you tell the price of a car toy?", "Sure sir/maam it's 10 DKK"
                "Thank you.",
                "You're welcome.",
                "can you tell the price of a doll toy?", "Sure sir/maam it's 12 DKK",
                "Thank you.",
                "You're welcome.",
                "from where i can buy it?", "There is a dropdown 'Toy Stores' on navigation bar you can check from there"
                "Sure i will,Thank you.",
                "You're welcome.",
                "What is your name?", "My name is toy ChatBot",
                "Who created you?", "Amina",
                "Tell me about yourself",
                "My name is Amina malik. I am a Computer engineer",
                "Contact",
                "Email : amina1000hashi@hotmail.com, Location : Denmark",
                "",
                ])

#route for home page will open index.html
@app.route("/")
def home():
    return render_template("index.html")

#route for getting the user input
@app.route("/get")
def chatbot_response():
    userText = request.args.get('msg')
    return str(toy_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
