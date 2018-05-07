import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg '
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
#with open('example.ini', 'w') as configfile:
#    config.write(configfile)

import hashlib

m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.digest())
m.update(b"It's been a long time since last time we ...")

print(m.digest())  # 2进制格式hash
print((m.hexdigest()))  # 16进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash

import hmac
h = hmac.new(b'天王盖地虎', b'宝塔镇河妖')
print(h.hexdigest())