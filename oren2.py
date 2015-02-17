import requests
from bs4 import BeautifulSoup as soup
from time import strftime
import getpass

if __name__ == '__main__':
	response = raw_input('So i heard you wanna be rich huh ? (Y/n) ')
	print ''
	if response != 'Y': 
		print 'bye bye'
		exit()
	print('Welcome to duty2 grabber')
	while True:
		username = raw_input('username: ')
		password = getpass.getpass('password: ')
		payload = {'user_name': username, 'password': password, 'submit': ''}
		headers = {'User-Agent': 'Mozilla/5.0'}
		session = requests.Session()
		res = session.post('http://duty2.nussucommit.com/login',headers=headers,data=payload)

		if username in res.text:
			print 'Successful login'
		else:
			print 'Invalid username or password.. try again'
			continue
		print ''
		print 'waiting for duty release... (do not stop this script)\n'

		while True:
			html = session.get('http://duty2.nussucommit.com/grablist').text
			doc = soup(html)
			table = doc.table
			if not table:
				continue
			availableDuty = []
			for form in table.find_all('form'):
				common = {'submit':''}
				for param in form.find_all('input', recursive=False):
					common[param.get('name')] = param.get('value');
				for opt in form.find_all('div'):
					req = common.copy()
					req[opt.input.get('name')] = 'on'
					req['time'] = opt.getText().strip()
					availableDuty.append(req);
			if availableDuty:
				print strftime("%d-%m-%Y %H:%M:%S")
			for duty in availableDuty:
				print '  grabbed >  '+("%02d"%int(duty['date']))+'-'+("%02d"%int(duty['month']))+'-'+duty['year']+' '+duty['time']+' on '+duty['venue'] 
				session.post('http://duty2.nussucommit.com/grablist.php', data=duty)
			print ''
			if availableDuty:
				print 'waiting for duty release...\n'
