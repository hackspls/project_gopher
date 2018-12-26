import requests, base64, pprint, json

def headers():
    auth = base64.b64encode("<apiusername>:<password>".encode())
    headers = {"Authorization": "Basic " + auth.decode(),
               "Content-Type": "application/json"}
    return headers

url = "https://api.upcloud.com/1.2/"
ssh = "<sshkey>"
user_data = "#!/bin/bash\nyum updrade\nyum install -y vim epel-release\nyum update\nyum install -y git python python-devel python-pip openssl ansible\nsed -i '22s/#//' /etc/ansible/ansible.cfg\nsed -i '14s/#//' /etc/ansible/ansible.cfg"

zone = input("where will you deploy master_node: ")
def payload():
    payload = {
      "server": {
        "zone": f"{zone}",
        "title": "centos-swarm00-master",
        "hostname": "centos.swarm00.master",
        "plan": "4xCPU-8GB",
        #"avoid_host": "7653311107",
        "storage_devices": {
          "storage_device": [
            {
              "action": "clone",
              "storage": "01000000-0000-4000-8000-000050010300",
              "size": 50,
              "title": "centos-swarm00-master-vda",
              "tier": "maxiops"
            },
          ]
        },
        "login_user": {
          "username": "root",
          "ssh_keys": {
            "ssh_key": [
              f"{ssh}",
            ]
           }
        },
        "user_data": f"{user_data}"
      }
    }
    return payload

def get_templates(headers, url):
    r = requests.get(f"{url}storage/template/", headers=headers())
    server_list = r.json()
    pprint.pprint(server_list)

def create_server_master(payload, headers, url):
    #zone = input("where will you deploy master_node: ")
    #user_data = "#!/bin/bash\nyum updrade\nyum install -y vim epel-release\nyum update\nyum install -y git python python-devel python-pip openssl ansible\nsed -i '22s/#//' /etc/ansible/ansible.cfg\nsed -i '14s/#//' /etc/ansible/ansible.cfg"
    r = requests.post(f"{url}server/", data=json.dumps(payload()), headers=headers())
    pprint.pprint(r.json())


def create_swarm(headers, url):
    ssh = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8Ag+afN9Ppcz1Wxxy91UBHt5BOh6lqRokSJZXlvduNcTvKCz1JmGKoFt3rgPLdZON2aTrQjVAwOIwajVw8FbR2uwt5rYnWlyB3qUj1Y6b62t7y3m5Cv0cwMHBcUHkGiXVi0LrqQTBgfuBtvBB62hkortyvgNrbKTnK+Y84eUVrZHmArjZPDPyD4rA/gZ3FK3KntLEKsovemmPLjI2TISc9BKGmT/pthMvlvjOXUqF9f9rrvwHrU7FqO6HKEr1agAK87US6wCzKVK+eFS9hITCWP53+FoFBQO2zZMtLYEBFEx6Dc36lmXImUjdREsMqXjEcjv6ud4sKBrsdoqJ/yQF ronnieturner@Ronnies-MacBook-Pro-2.local"
    user_data = "#!/bin/bash\nyum updrade\n"
    zone = "nl-ams1"
    payload = {
      "server": {
        "zone": f"{zone}",
        "title": "centos-swarm01-ams",
        "hostname": "centos.swarm01.ams",
        "plan": "4xCPU-8GB",
        #"avoid_host": "7653311107",
        "storage_devices": {
          "storage_device": [
            {
              "action": "clone",
              "storage": "01000000-0000-4000-8000-000050010300",
              "size": 50,
              "title": "centos-swarm01-ams-vda",
              "tier": "maxiops"
            },
          ]
        },
        "login_user": {
          "username": "root",
          "ssh_keys": {
            "ssh_key": [
              f"{ssh}",
            ]
           }
        },
        "user_data": f"{user_data}"
      }
    }
    r = requests.post(f"{url}server/", data=json.dumps(payload), headers=headers())
    pprint.pprint(r.json())

    user_data = "#!/bin/bash\nyum updrade\n"
    zone = "uk-lon1"
    payload = {
      "server": {
        "zone": f"{zone}",
        "title": "centos-swarm01-lon",
        "hostname": "centos.swarm01.lon",
        "plan": "4xCPU-8GB",
        #"avoid_host": "7653311107",
        "storage_devices": {
          "storage_device": [
            {
              "action": "clone",
              "storage": "01000000-0000-4000-8000-000050010300",
              "size": 50,
              "title": "centos-swarm01-lon-vda",
              "tier": "maxiops"
            },
          ]
        },
        "login_user": {
          "username": "root",
          "ssh_keys": {
            "ssh_key": [
              f"{ssh}",
            ]
           }
        },
        "user_data": f"{user_data}"
      }
    }
    r = requests.post(f"{url}server/", data=json.dumps(payload), headers=headers)
    pprint.pprint(r.json())

#create_server_master(payload, headers, url)

#get_templates(headers, url)

create_swarm(headers, url)
