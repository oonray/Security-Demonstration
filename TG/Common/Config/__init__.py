import pickle
from sys import argv

path="Common/Config/_config.pk"
std_config ={
'th0': '192.168.15.35',
'Network': '10.0.0.0/24',
'Subnet': '255.255.255.0',
'OldRootPasswd':'jV6XjQDVhGVYsp',
'NewRootPasswd': 'SuperSecretPassword@!NordoffTG2016',
'Users': 'joe,anderson',
'Passwrds': 'Joe@TG2016,Anderson@TG2016',
'ApachePath': '/usr/local/apache2/'
}
config ={
'th0': '192.168.15.35',
'Network': '10.0.0.0/24',
'Subnet': '255.255.255.0',
'OldRootPasswd':'jV6XjQDVhGVYsp',
'NewRootPasswd': 'SuperSecretPassword@!NordoffTG2016',
'Users': 'joe,anderson',
'Passwrds': 'Joe@TG2016,Anderson@TG2016',
'ApachePath': '/usr/local/apache2/'
}

def dump(): pickle.dump(config,open(path))

def load(): config = pickle.load(open(path))

def get(field=""):
   if field != "": return config[field]
   else: return config

def get_std(field=""):
   if field != "": return std_config[field]
   else: return std_config

def change(field=(""),value=("")):
    for i in field: config[field[i]] = value[i]

if __name__=="__main__":
    if len(argv)<3:
        print("Changes Fields in the Config\nUsage: {} <Field> <Value>".format(argv[0]))
        change(argv[1],argv[2])