#!/usr/bin/env python2
# coding=utf8

import os,sys,pexpect

current_user = os.getenv('USER')
home_path = os.getenv('HOME')
pub_key_path =  home_path + '/.ssh/id_rsa.pub'
hostname = 'xenconsole.cm5'

file_cmd = 'file ' + pub_key_path
scp_cmd = '/usr/bin/ssh-copy-id -i' + pub_key_path

#print current_user,home_path,pub_key_path
#print file_cmd,scp_cmd

## XXX 执行速度非常慢
#(output,exit_status)=pexpect.run(file_cmd,withexitstatus=1)
#print (output,exit_status)

script_path = os.path.dirname(os.path.realpath(__file__))
hostname_path = script_path + '/hostname.txt'
#print os.path.realpath(__file__)
#print script_path,hostname_path

## $ ssh app.broom.cm4
## The authenticity of host 'app.broom.cm4 (172.24.102.132)' can't be established.
## DSA key fingerprint is 93:d0:b7:1a:09:ce:e8:c6:bb:b3:aa:17:b0:13:45:91.
## Are you sure you want to continue connecting (yes/no)? 

## # ssh-copy-id -i ~/.ssh/id_rsa.pub xenconsole.cm5
## Warning: Permanently added 'xenconsole.cm5,172.25.89.230' (DSA) to the list of known hosts.
## root@xenconsole.cm5's password:
passwd = 'hello_world'

def ssh_copy_id(pub_key_path,current_user,hostname):
	print '/usr/bin/ssh-copy-id -i %s %s@%s' %(pub_key_path,current_user,hostname)
	child = pexpect.spawn('/usr/bin/ssh-copy-id -i %s %s@%s' %(pub_key_path,current_user,hostname))
	try:
		#index = child.expect(['continue','password:',pexpect.EOF],timeout=8)
		index = child.expect(['continue connecting \(yes/no\)','\'s password:',pexpect.EOF],timeout=8)
		print index
		if index == 0:
			child.sendline('yes')
			#index = child.expect(['continue connecting (yes/no)','\'s password:',pexpect.EOF],timeout=8)
			print child.after,child.before
		if index == 1:
			child.sendline(passwd)
			## 若密码错误，一直尝试输入，直至退出
			child.expect('password:')
			child.sendline(passwd)
			print child.after,child.before
		if index == 2:
			print '[ failed ]'
			print child.after,child.before
			child.close()
	except pexpect.TIMEOUT:
		#print 'pexpect.TIMEOUT'
		print child.after,child.before
		child.close()
	else:
		print '若没有异常发生，会匹配该行'

key_exist = os.system(file_cmd)
#print exit_status

if key_exist == 0:

	hostname_file = open(hostname_path)

	for hostname in hostname_file.readlines():
		hostname = hostname.strip('\n')
        # 判断是否是空行或注释行
		if not len(hostname) or hostname.startswith('#'):
		        continue

		### 'ssh-copy-id -i' + pub_key_path + current_user + '@' + hostname
		#scp_argv_list = [ '-i', pub_key_path, current_user, '@', hostname ]
		#print scp_argv_list 

		#print hostname

		ssh_copy_id(pub_key_path,current_user,hostname)

	hostname_file.close()

else:
	print "[ error ] id_rsa.pub 公钥不存在"





