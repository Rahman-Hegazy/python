'''
Created on Aug 7, 2011

@author: Agassi


'''

#_*_encoding:utf-8_*_
from lxml import html
import cookielib
import os
import urllib2


class douban_robot:
#	login_path = 'https://www.douban.com/accounts/login'
	download_dir='albums'
	album_dir=''
	
	def __init__(self):
		self.cj =cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		urllib2.install_opener(self.opener)
		self.opener.addheaders = [('User-agent','Opera/9.23')]
		
		if not os.path.isdir(self.download_dir):
			os.mkdir(self.download_dir)

#	def login(self):
#		post_data = urllib.urlencode({
#			'form_email':self.email,
#			'form_password':self.password,
#			'remeber':'on',
#			})
#		request = urllib2.Request(self.login_path,post_data)
#		html = self.opener.open(request).read()
#		print re.findall('<h1>(.*)</h1>',html,re.S)[0].decode('utf8') 
#		get_url = self.opener.open(request).geturl()
#		if get_url == 'http://www.douban.com/':
#			self.cj.save('douban.cookie')
#			print 'Login success !'
#			return True
#		else:
#			print get_url
#			print 'Login error'
#			return False

	def do_get(self,url):
		return self.opener.open(url).read()
		
	def get_album_page_url(self,url):
		
		print 'Analyzing album pages',url
		
		page_urls=[]
		
		page_urls.append(url)
		
		album_page=self.do_get(url)
		doc=html.document_fromstring(album_page)
		
		paginator=doc.xpath('//div[@class="paginator"]/a//@href')
		album_title=doc.xpath('/html/head/title/text()')[0].replace('\n','').replace(' ','')
		
		self.album_dir=os.path.join(self.download_dir,album_title)
		
		
		
		if not os.path.isdir(self.album_dir):os.mkdir(self.album_dir)
		
		page_urls.extend(paginator)
		
		return page_urls
	
	def get_img_page_urls(self,urls):
		
		print "Analyzing image pages"
		
		image_page_urls=[]
		
		for url in urls:
			album_page=self.do_get(url)
			doc=html.document_fromstring(album_page)
			
			urls_in_single_page=doc.xpath('//div[@class="photolst clearfix"]/div/a/@href')
			
			image_page_urls.extend(urls_in_single_page)
			
		return image_page_urls
	
	def get_image_urls(self,img_page_urls):
		print "Analyzing large image urls..."
		
		image_urls=[]
		
		for url in img_page_urls:
			image_page=self.do_get(url)
			
			doc=html.document_fromstring(image_page)
			
			img_url=doc.xpath('//a[@class="mainphoto"]/img/@src')
			
			image_urls.append(img_url[0])
			
		return image_urls
	
	def save_image(self,url):
		filename=url.split('/')[-1]
		
		f=file(os.path.join(self.album_dir,filename),'wb')
		
		f.write(self.do_get(url))
		f.close()
		
if __name__=='__main__':
	douban=douban_robot()
	url=raw_input("input url:>>>")
	album_pages = douban.get_album_page_url(url)
	img_pages=douban.get_img_page_urls(album_pages)
	img_urls=douban.get_image_urls(img_pages)
	
	i=0
	for x in img_urls:
		i=i+1
		print "(%d/%d)>>>%s" % (i,len(img_urls),x)
		
		try:
			douban.save_image(x)
			print "saved"
		except:
			print 'failed'
			
	print 'all downloads completed.'
			
