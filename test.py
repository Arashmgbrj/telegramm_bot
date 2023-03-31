import requests
for i in (1,200):
    requests.get(f'https://api.telegram.org/bot5750144758:AAH1CvSZ0NJIIzROH3WB1ruWSxi0etz6D1U/deleteMessage?chat_id=2078475433&message_id={i}')