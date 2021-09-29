import json
import requests

slack_webhook_url = "YOUR_SLACK_WEBHOOK_URL"


def slack_notifications(message):
    slack_data = {'text': "Subdomain Takeover Possible: {}".format(message)}
    response = requests.post(slack_webhook_url, data=json.dumps(slack_data))
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


filepath = 'subzyresults.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       result = line.find('VULNERABLE')
       if result == 8:
           slack_notifications(line)
       line = fp.readline()
       cnt += 1




