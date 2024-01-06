import re
import random

def get_response(user_input):
     split_message = re.split(r'\s|[,:;.?!-_]\s*',user_input.lower())
     return check_all_messages(split_message)

def message_probability(user_message,recognized_words,single_response = False, required_word=[]):
     message_certainty = 0
     has_required_words = True
     for word in user_message:
          if word in recognized_words:
               message_certainty += 1
     percentage = float(message_certainty) / float (len(recognized_words))
     for word in required_word:
          if word not in user_message:
               has_required_words = False
               break
     if has_required_words or single_response:
          return int(percentage*100)
     else:
          return 0
     
def check_all_messages(message):
     highest_prob = {}
     def response(bot_response,list_of_words,single_response = False, required_word = []):
          nonlocal highest_prob
          highest_prob[bot_response] = message_probability(message,list_of_words,single_response,required_word)

     response("Hola",['hola','klk','saludos','buenas'],single_response=True)
     response("Estoy bien, ¿y tú?",['como','estas','va','vas','sientes'],required_word=['como'])
     response("Siempre a la orden",['gracias','te lo agradezco','thanks'],single_response=True)
     print(highest_prob)

     best_match = max(highest_prob, key=highest_prob.get)
     return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
     return ["¿Puedes decirlo de nuevo?","No estoy seguro de lo que quieres","Búscalo en Google a ver que tal"][random.randrange(3)]

while(True):
     print("Bot:" + get_response(input("You:" )))



     