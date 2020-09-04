# DNA Center-Inventory-Webex Integration
Updating Inventory using DNA-C with Chatbot Notification bot






| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |
## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
* Python 3.8
*  DNA-Center
*  Webex
*  MySql Database 8.0  

## Installation/Configuration

#### Clone the repo :
```$ git clone https://github.com/gve-sw/DNACenterInventoryWebexIntegration.git```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

Now you have your virtual environment setup and ready

#### Install the libraries :

```$ pip install requirements.txt```


## Setup: 
*Cisco DNA Center Connection*
1. Obtain the username, password and base url for your Cisco DNA Center environment.

2. Export the following information as environment variables so it is possible to connect to the Cisco DNA Center API.
```
DNAC_URL = env_lab.DNA_CENTER["host"]
DNAC_USER = env_lab.DNA_CENTER["username"]
DNAC_PASS = env_lab.DNA_CENTER["password"]
```
*Cisco Webex Bot*

3. Create a Webex Bot. Webex Bots can be created from the Cisco Developer website. https://developer.webex.com/docs/bots 

4. Add the access token for the Webex Bot.
```
ACCESS_TOKEN = "ACCESS_TOKEN"
```
5. Fill the email address of a user or group to recieve the webex notification. 
```
to = ' EMAIL_ADDRESSS'
```
*Database Connection*

6. Download and Install MySQL. 

7. Create a table in MySQL database with the following script. You can run the script from MySQL Workbench.  
```
CREATE TABLE `allDeviceDetails` (
  `hostname` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `serial` varchar(255) NOT NULL,
  `platformId` varchar(255) DEFAULT NULL,
  `version` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `uptime` varchar(255) DEFAULT NULL,
  `createDate` varchar(255) DEFAULT NULL,
  `updateDate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`serial`)
) 
```
Now you have completed the setup and are ready to run the script. 

## Usage: 
Run the python script
```
    $ python inventory_update.py
```
The Webex Bot will send the list of Network devices which have been updated in the database:
![Sample Database Update Message](/IMAGES/DatabaseUpdateMessage.PNG)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
