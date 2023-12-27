import requests
from bs4 import BeautifulSoup
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

url = 'https://gama.casino/ru'

slack_token = ''
slack_channel = ''

response = requests.get(url)

slack_client = WebClient(token=slack_token)


if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')

    element = soup.find(class_='ng-tns-c134-11')

    if element:
        print('Сайт доступен, страница отображается')
    else:
        erroe_message = 'Сайт доступен, страница НЕ отображается'
        print(erroe_message)
        try:
            response = slack_client.chat_postMessage(
                channel=slack_channel,
                text=erroe_message
            )
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")


else:
    erroe_message = f'Ошибка при запросе к сайту. HTTP-код состояния: {response.status_code}'
    print(erroe_message)
    try:
        response = slack_client.chat_postMessage(
            channel=slack_channel,
            text=erroe_message
        )
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")



    