from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


# Create your views here.

bot = ChatBot('chatbot', read_only=False,
              logic_adapters=[{
                  'import_path': 'chatterbot.logic.BestMatch',
                #   'default_response': 'Sorry, I don\'t know what that means!',
                #   'maximum_similarity_threshold': 0.90
                  }])

list_to_train = [
    "hi",
    "hi, there",
    "What's your name?",
    "I'm just a chatbot",
    "what's your fav food?",
    "I like pasta"
]

chatter_bot_corpus_trainer = ChatterBotCorpusTrainer(bot)

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

chatter_bot_corpus_trainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'blog/index.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)