       


from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.modify'])

service = build('gmail', 'v1', credentials=creds)

# Define a mensagem de resposta automática
message = MIMEText ('Obrigado por entrar em contato. Sua mensagem foi recebida e será respondida em breve.')

# Loop por todas as mensagens na caixa de entrada
result = service.users().messages().list(userId='me', q='is:unread').execute()
messages = result.get('messages', [])
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    # Marca a mensagem como lida
    service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()
    # Envia a mensagem de resposta automática
    service.users().messages().send(userId='me', body={'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}).execute()
