# Twilio WhatsApp Integration

Este projeto demonstra como integrar o Twilio com o WhatsApp usando Python. O objetivo é criar um chatbot simples que pode responder a mensagens recebidas no WhatsApp e gerenciar interações básicas com os usuários.

## Funcionalidades

- Responder a mensagens recebidas no WhatsApp.
- Oferecer opções de interação ao usuário.
- Gerenciar estados de conversação para fornecer respostas contextuais.
- Agendar horários para serviços específicos.

## Configuração

### Pré-requisitos

- Python 3.6 ou superior
- Conta no [Twilio](https://www.twilio.com/)
- [ngrok](https://ngrok.com/) para expor o servidor local para a internet

### Passos para Configuração

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/twilio-whatsapp-integration.git
   cd twilio-whatsapp-integration
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No macOS/Linux
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure suas credenciais da Twilio:
   - Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
     ```plaintext
     TWILIO_ACCOUNT_SID=your_account_sid
     TWILIO_AUTH_TOKEN=your_auth_token
     ```

5. Inicie o servidor Flask:
   ```sh
   python app.py
   ```

6. Exponha o servidor local para a internet usando ngrok:
   ```sh
   ngrok http 5000
   ```
   - Copie o URL gerado pelo ngrok (por exemplo, `http://<ngrok-id>.ngrok.io`).

7. Configure o webhook no Twilio:
   - Acesse o [Console da Twilio](https://www.twilio.com/console).
   - Vá para a seção "Phone Numbers" e selecione o número do WhatsApp que você configurou.
   - Na seção "Messaging", configure o campo "A MESSAGE COMES IN" para apontar para o URL gerado pelo ngrok, seguido pelo endpoint `/whatsapp` (por exemplo, `http://<ngrok-id>.ngrok.io/whatsapp`).

## Uso

1. Envie uma mensagem para o número do WhatsApp da Twilio.
2. O chatbot responderá com uma mensagem padrão perguntando o que você gostaria de fazer.
3. Siga as instruções para interagir com o chatbot.

## Estrutura do Projeto

```
twilio-whatsapp-integration/
├── venv/
├── .gitignore
├── requirements.txt
├── README.md
├── .env
├── main.py
├── app.py
└── tests/
    └── test_main.py
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/fooBar`).
3. Commit suas mudanças (`git commit -am 'Add some fooBar'`).
4. Faça um push para a branch (`git push origin feature/fooBar`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato

- Nome: Filipe Simon
- Email: filipesimon@live.com
- GitHub: [filipesim](https://github.com/filipesim)
```