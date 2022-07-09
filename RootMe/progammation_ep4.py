import sys, socket, ssl, time
import urllib, re, math
import base64, zlib
 
NICK = 'antoine42_bot'
IDENT = 'antoine42_bot'
REALNAME = 'antoine42_bot'
CHAN = '#Root-Me'
PASSWORD = ''
data = ''
start = 'Start to connect.'
connected = 'Connection estblished.'
 
# LOGIN IRC CHAT
 
print start
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('irc.root-me.org', 6697))
ircsock=ssl.wrap_socket(s)
ircsock.send("USER %s %s %s :%s\r\n" %(NICK, IDENT, REALNAME, NICK))
ircsock.send("NICK %s\r\n" % NICK)
print connected
 
while True:
    # STAY CONNECTED
    data = ircsock.recv(4096)
    print data
    if data.find('PING') != -1:
        ircsock.send('PONG ' + data.split() [ 1 ] + '\r\n')
        # JOIN CHANNEL and IDENTIFY PASSWORD
    if data.find('001') != -1:
        ircsock.send("JOIN %s\r\n" % CHAN)
        data = ircsock.recv(4096)
        print data
        ircsock.send('PRIVMSG NickServ : IDENTIFY %s\r\n' % PASSWORD)
        data = ircsock.recv (4096)
        print data
        ircsock.send('PRIVMSG Candy :!ep4\r\n')
    if data.find('KICK') != -1:
        ircsock.send('JOIN %s\r\n' % CHAN)
        data = ircsock.recv(4096)
        print data
        ircsock.send('PRIVMSG Candy :!ep4\r\n')
    if data.find('PRIVMSG') != -1:
        message = data.split(':')[2]
        print message
        result = zlib.decompress(base64.b64decode(message))
        ircsock.send('PRIVMSG Candy :!ep4 -rep ' + result + '\r\n')
