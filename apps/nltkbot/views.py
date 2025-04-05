from django.shortcuts import render
import nltk
from nltk.chat.util import Chat, reflections

# Create your views here.
# Define a set of patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Greetings!']),
    (r'how are you?', ['I am fine, thank you!', 'Doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by NLTK.']),
    (r'bye|exit', ['Goodbye!', 'See you later!']),
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(patterns, reflections)

def chat_view(request):
    user_message = ''
    bot_response = ''

    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = chatbot.respond(user_message)

    return render(request, 'nltkbot/chat.html', {
        'user_message': user_message,
        'bot_response': bot_response
    })