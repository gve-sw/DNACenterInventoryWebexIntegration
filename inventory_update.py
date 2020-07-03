import requests
import mysql.connector
import datetime

from requests.auth import HTTPBasicAuth
from webexteamssdk import WebexTeamsAPI

# Connection to the database
db = mysql.connector.connect(
    host='',
    username='',
    password='',
    database='',
)

cursor = db.cursor(buffered=True)
sqlFormula = "INSERT INTO test_device (hostname, ip, serial, platformId, version, role, uptime, createDate, updateDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s) " \
             "ON DUPLICATE KEY UPDATE updateDate=%s"
cursor.execute('SHOW TABLES')

# Connection to the DNA-C environment
DNAC_URL = ""
DNAC_USER = ""
DNAC_PASS = ""

def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://{}/dna/system/api/v1/auth/token'.format(DNAC_URL)  # Endpoint URL
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS))  # Make the POST Request
    token = resp.json()['Token']  # Retrieve the Token from the returned JSON
    return token  # Create a return statement to send the token back for later use

def get_device_list():
    """ 
    Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint
    """
    token = get_auth_token()  # Get Token
    url = "https://{}/api/v1/network-device/1/10".format(DNAC_URL)
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    resp = requests.get(url, headers=hdr)  # Make the Get Request
    device_list = resp.json()
    message = update_db(device_list)
    return message

def update_db(device_json):
    """ 
    Format the data and add to the database
    """    
    message = 'The database was updated with the following serial ids: '
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            date = datetime.datetime.now()
            today = date.strftime('%H:%M %m-%d-%Y')
            str = (device['hostname'],
                   device['managementIpAddress'],
                   serialNumber,
                   platformId,
                   device['softwareVersion'],
                   device['role'], uptime, today, today, today)           
            message = message + serialNumber + '\n, '
            if serialNumber:
                cursor.execute(sqlFormula, str)
                db.commit()
    message = message[:-2]
    return message

ACCESS_TOKEN ="" #Access token for the Database Update Bot in Webex
api = WebexTeamsAPI(access_token=ACCESS_TOKEN) #Connection to the webex bot via the access token

if __name__ == "__main__":
    message = get_device_list()
    to = ""
    api.messages.create(toPersonEmail=to, markdown=message) #Send a webex notification once the update is made
