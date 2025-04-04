from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "bye": "Goodbye! Have a nice day!",
    "default": "I'm sorry, I didn't understand that. Can you please try again?",
    "what is your name?": "I am a simple QA chatbot. How can I assist you today?",
    "what can you do?": "I can help answer your questions and provide information. What do you need help with?",
    "how are you?": "I'm doing great, thank you for asking! How are you?",
    "where are you from?": "I don't have a physical location, but I am here to assist you anytime!",
    "what do you know?": "I know a lot of things! What would you like to know more about?",
    "good morning!": "Good morning! What can I help you with today?",
    "hey!": "Hey! How's it going? What can I do for you?",
    "hi, how are you?": "Hello! I'm doing well, thank you! How about you?",
    "greetings!": "Greetings! How can I help you today?",
    "can you help me?": "Of course! What do you need help with?",
    "i need assistance.": "Sure, what do you need help with?",
    "i'm stuck with something.": "Tell me more, and I'll help you out!",
    "can you give me some tips?": "Sure! What kind of tips are you looking for?",
    "how do I get started?": "Let me guide you! What are you trying to get started with?",
    "goodbye!": "Goodbye! Have a wonderful day!",
    "see you later!": "Take care! See you next time!",
    "i'm done, thanks.": "You're welcome! Don't hesitate to return if you need anything else.",
    "catch you later!": "See you! Have a great day!",
    "blah blah blah": "Sorry, I didn't understand that. Can you try asking something else?",
    "what's going on?": "I'm not sure what you mean. Could you rephrase that?",
    "hmm, I don't know": "I see! Maybe I can help if you give me more details.",
    "i don't get it.": "Can you clarify? I'll do my best to help.",
    "just wondering.": "Curiosity is great! Let me know how I can assist you.",
    "what's the weather like?": "I don't have weather updates, but you can check your local weather app for details.",
}

def index(request):
    return render(request, 'simplechat/index.html')

def get_response(request):
    user_message = request.GET.get('message', '').lower()
    response = responses.get(user_message, responses["default"])
    return JsonResponse({'response': response})