import requests
user_id = 12345
url = "https://www.flo-joe.co.uk/fce/students/wordbank/pverb.htm"
headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
      }
r = requests.get(url, headers=headers)
with open('test15.html', 'w') as output_file:
  output_file.write(r.text)