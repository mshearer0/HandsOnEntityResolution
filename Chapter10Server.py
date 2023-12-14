import private_set_intersection.python as psi
from flask import Flask, request
from pandas import read_csv

# Server Setup Values
fpr = 0.01
num_client_inputs = 100

# Get Server datasource
df_m = read_csv('basic_clean.csv',keep_default_na=False)

server_items = ['ABLY RESOURCES G2 1PB','ADVANCE GLOBAL RECRUITMENT EH7 4HG']
#server_items = (df_m['CompanyName']+' '+ df_m['Postcode']).to_list()

app = Flask(__name__)

# Setup psi class to hold server key created at every match
class psikey(object):
    def __init__(self):
        self.key = None

    def set_key(self, newkey):
        self.key = newkey
        return self.key

    def get_key(self):
        return self.key
pkey = psikey()    

# In response to POST to /match, generate new key and encrypt payload elements and return

@app.route('/match', methods=['POST'])
def match():
    s =  pkey.set_key(psi.server.CreateWithNewKey(True))
    psirequest = psi.Request()
    psirequest.ParseFromString(request.data)
    return s.ProcessRequest(psirequest).SerializeToString()   

# Return the setup using current key. This means re-encrypting whole data set at every ask and returning either raw or compressed (gcs or bloom) to client.

@app.route('/gcssetup', methods=['GET'])
def gcssetup():
    s = pkey.get_key()
    return s.CreateSetupMessage(fpr, num_client_inputs, server_items, psi.DataStructure.GCS).SerializeToString()

@app.route('/rawsetup', methods=['GET'])
def rawsetup():
    s = pkey.get_key()
    return s.CreateSetupMessage(fpr, num_client_inputs, server_items, psi.DataStructure.RAW).SerializeToString()

@app.route('/bloomsetup', methods=['GET'])
def bloomsetup():
    s = pkey.get_key()
    return s.CreateSetupMessage(fpr, num_client_inputs, server_items, psi.DataStructure.BLOOM_FILTER).SerializeToString()
