# DNACenterInventoryWebexIntegration
Updating Inventory using DNA-C with Chatbot Notification bot






| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |
## Contacts
* Eda Akturk 

## Solution Components
* Python 3.8
*  DNA-Center
*  Webex
*  MySql Database 8.0  

## Installation/Configuration

#### Clone the repo :
```$ git clone (repo)```

## Setup: 
1. Obtain the username, password and base url for your Cisco DNA Center environment.

2. Export the following information as environment variables so it is possible to connect to the API.
```
DNAC_URL = env_lab.DNA_CENTER["host"]
DNAC_USER = env_lab.DNA_CENTER["username"]
DNAC_PASS = env_lab.DNA_CENTER["password"]
```

3. Create a Webex Bot. Webex Bots can be created from Cisco Developer website. https://developer.webex.com/docs/bots). 

4. Add the access token to the Bot.
```
ACCESS_TOKEN = "ACCESS_TOKEN"
```

5. Fill the email address of a user or group to recieve the webex notification. 
```
to = ' EMAIL_ADDRESSS'
```

## Usage: 
Run the python script
```
    $ python inventory_update.py
```

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
