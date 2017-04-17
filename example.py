import requests, json, configparser
from fbmessenger import FbMessenger
from flask import Flask
from flask import request

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
token = config['FACEBOOK']['FacebookToken']
fb = FbMessenger(token)

@app.route("/webhook", methods=['GET', 'POST'])
def fb_webhook():
	if request.method == 'POST':
		data = request.json

		for entry in data['entry']:
			recipient_id = data['entry']['messaging'][0]['sender']['id']
			received_text = data['entry']['messaging'][0]['message']['text']

		if received_text == '/hnews':
			message_params = {
				'title': 'Hacker News',
				'subtitle': 'Hacker News Website',
				'item_url': 'https://news.ycombinator.com/',
				'image_url': ''
			}
			return fb.send_link_message(recipient_id, message_params)
		else:
			return fb.send_message(recipient_id, 'Would like to receive a random Hacker News? (Type: /hnews)')

	else:
		return request.args.get('hub.challenge')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)
