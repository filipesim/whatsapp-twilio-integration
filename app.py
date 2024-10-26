import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter credenciais da Twilio das variáveis de ambiente
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

app = Flask(__name__)

# Dicionário para armazenar o estado atual de cada usuário
user_state = {}

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
  """Responder a mensagens recebidas no WhatsApp."""
  incoming_msg = request.values.get('Body', '').lower()
  from_number = request.values.get('From', '')
  resp = MessagingResponse()
  msg = resp.message()

  # Verificar o estado atual do usuário
  state = user_state.get(from_number, 'initial')

  if state == 'initial':
    response = "Olá! O que você gostaria de fazer? \n1. Falar com a Camila \n2. Agendar um horário"
    user_state[from_number] = 'awaiting_choice'
  elif state == 'awaiting_choice':
    if '1' in incoming_msg:
      response = "Aguarde um instante."
      user_state[from_number] = 'initial'  # Resetar estado
    elif '2' in incoming_msg:
      response = "Escolha um serviço: \n1. Limpeza de pele \n2. Design de sobrancelhas"
      user_state[from_number] = 'awaiting_service'
    else:
      response = "Desculpe, não entendi. Por favor, escolha uma opção: \n1. Falar com a Camila \n2. Agendar um horário"
  elif state == 'awaiting_service':
    if '1' in incoming_msg:
      response = "Ainda tenho disponível os horários de 10h e 15h. Qual deles você prefere?"
      user_state[from_number] = 'awaiting_time'
    elif '2' in incoming_msg:
      response = "Ainda tenho disponível os horários de 11h e 16h. Qual deles você prefere?"
      user_state[from_number] = 'awaiting_time'
    else:
      response = "Desculpe, não entendi. Por favor, escolha um serviço: \n1. Limpeza de pele \n2. Design de sobrancelhas"
  elif state == 'awaiting_time':
    if '10' in incoming_msg or '15' in incoming_msg or '11' in incoming_msg or '16' in incoming_msg:
      response = f"Seu horário foi agendado para {incoming_msg}h. Obrigado!"
      user_state[from_number] = 'initial'  # Resetar estado
    else:
      response = "Desculpe, não entendi. Por favor, escolha um horário disponível."

  msg.body(response)
  return str(resp)

if __name__ == "__main__":
  app.run(debug=True)