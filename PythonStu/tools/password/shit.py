import requests,fileinput

headers ={
	'Accept': 'image/gif, image/jpeg, image/pjpeg, image/pjpeg,*/*',
	'Referer': 'http://www.onlinehashcrack.com/',
	'Accept-Language': 'zh-cn',
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;.NET CLR 2.0.50727)',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept-Encoding': 'gzip, deflate',
	'Host': 'www.onlinehashcrack.com',
	'Content-Length': '85'
	}
url = 'http://www.onlinehashcrack.com/multi-hash-cracking.php'
def password(hash):
	data ={
		'hashVIP':hash,
		'emailVIP':'xxxxxxxxxx@qq.com',
		'submitVIP':'Send+%21'
		}
	r = requests.post(url, data=data, headers=headers)

with open('1.txt') as f:
	for line in f:  
		password(line)

