import requests
import BeautifulSoup as bs

if __name__ == '__main__':
	username = raw_input('username : ')
	password = raw_input('password : ')
	payload = {'username': username, 'password': password, 'submit': 'Login'}
	headers = {'User-Agent': 'Mozilla/5.0'}

	session = requests.Session()
	session.post('http://duty.nussucommit.com/login.php',headers=headers,data=payload)
	r = session.get('http://duty.nussucommit.com/grabduty.php')
	print r.text
