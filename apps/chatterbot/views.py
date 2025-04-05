from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create your views here.

# Initialize the chatbot
chatbot = ChatBot(
    'DjangoBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
    ],
    database_uri='sqlite:///chatterbot.sqlite3',
)

# Train the chatbot on the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

def chat_view(request):
    user_message = ''
    bot_response = ''

    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = chatbot.get_response(user_message)

    return render(request, 'chatterbot/chat.html', {
        'user_message': user_message,
        'bot_response': bot_response
    })