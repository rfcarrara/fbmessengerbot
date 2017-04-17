import json, requests

class FbMessenger(object):

    def __init__(self, token):
        self.token = token
        self.uri_send_message = 'https://graph.facebook.com/v2.6/me/messages'

    def send_message(self, recipient_id, message_text):
    	payload = {
            "recipient": {
                "id": recipient_id
            }, 
            "message": {
                "text": message_text
            }
        }
    	# payload = {"recipient":{"id":recipient_id},"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"Aniversário no CT do Corinthians? Primeiro pedaço de bolo é de Kazim","subtitle":"De volta após perder um mês de jogos por conta de um problema no joelho, gringo será opção contra o São Paulo. Contratado este ano, atacante virou tema de uma brincadeira interna do time","item_url":"http://globoesporte.globo.com/futebol/times/corinthians/noticia/aniversario-no-ct-do-corinthians-primeiro-pedaco-de-bolo-e-de-kazim.ghtml","image_url":"http://s2.glbimg.com/RAHSPAxYDkRmBX_2SPiV_suMH9Y=/540x304/top/smart/http://s.glbimg.com/es/ge/f/original/2017/04/14/a3396f116415.jpg"}]}}}}

    	return json.dumps(
    			requests.post(
    				self.uri_send_message, 
    				params={'access_token': self.token}, 
    				json=payload
    			).json()
    		)

    def send_link_message(self, recipient_id, params):

        payload = {
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                        {
                            "title": params['title'],
                            "subtitle": params['subtitle'],
                            "item_url": params['item_url'],
                            "image_url": params['image_url']
                        }]
                    }
                }
            }
        }

        return json.dumps(
                requests.post(
                    self.uri_send_message, 
                    params={'access_token': self.token}, 
                    json=payload
                ).json()
            )


