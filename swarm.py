import requests, base64, pprint, json

def headers():
    auth = base64.b64encode("<apiusername>:<password>".encode())
    headers = {"Authorization": "Basic " + auth.decode(),
               "Content-Type": "application/json"}
    return headers

url = "https://api.upcloud.com/1.2/"
ssh = "<sshkey>"
user_data = "#!/bin/bash\nyum updrade -y\nyum install -y vim epel-release\nyum update -y\nyum install -y git python python-devel python-pip openssl ansible\nsed -i '22s/#//' /etc/ansible/ansible.cfg\nsed -i '14s/#//' /etc/ansible/ansible.cfg"

zone = input("where will you deploy master_node: ")
def payload(zone, title, hostname, vda_title, user_data):
    payload = {
      "server": {
        "zone": f"{zone}",
        "title": f"{title}",
        "hostname": f"{hostname}",
        "plan": "4xCPU-8GB",
        #"avoid_host": "7653311107",
        "storage_devices": {
          "storage_device": [
            {
              "action": "clone",
              "storage": "01000000-0000-4000-8000-000050010300",
              "size": 50,
              "title": f"{vda_title}",
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

def get_server_info(headers, url, uuid):
    r = requests.get(f"{url}server/{uuid}", headers=headers())
    server_info = r.json()
    pprint.pprint(server_info)

def create_server_master(payload, headers, url):
    '''with open('master_udata.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')'''
    title = f"swarm00_master_node_{zone}"
    hostname = f"swarm00.master.{zone}"
    vda_title = f"swarm00-master-{zone}"
    user_data = "#!/bin/bash\nyum updrade\nyum install -y vim epel-release\nyum update\nyum install -y git python python-devel python-pip openssl ansible\nsed -i '22s/#//' /etc/ansible/ansible.cfg\nsed -i '14s/#//' /etc/ansible/ansible.cfg"
    #user_data = myfile
    r = requests.post(f"{url}server/", data=json.dumps(payload(
        zone, title, hostname, vda_title, user_data)), headers=headers())
    pprint.pprint(r.json())
    server_data = r.json()
    return server_data


def create_swarm_ams1(payload, headers, url, zone):
    if zone != "nl-ams1":
        zone = "nl-ams1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_lon1(payload, headers, url, zone):
    if zone != "uk-lon1":
        zone = "uk-lon1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_fra1(payload, headers, url, zone):
    if zone != "de-fra1":
        zone = "de-fra1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_sin1(payload, headers, url, zone):
    if zone != "sg-sin1":
        zone = "sg-sin1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        uuid = server_data["server"]["uuid"]
        return server_data
    else:
        pass

def create_swarm_sjo1(payload, headers, url, zone):
    if zone != "us-sjo1":
        zone = "us-sjo1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_chi1(payload, headers, url, zone):
    if zone != "us-chi1":
        zone = "us-chi1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_hel1(payload, headers, url, zone):
    if zone != "fi-hel1":
        zone = "fi-hel1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_hel2(payload, headers, url, zone):
    if zone != "fi-hel2":
        zone = "fi-hel2"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

master_server_data = create_server_master(payload, headers, url)
lon1_server_data = create_swarm_lon1(payload, headers, url, zone)
ams1_server_data = create_swarm_ams1(payload, headers, url, zone)
fra1_server_data = create_swarm_fra1(payload, headers, url, zone)
sin1_server_data = create_swarm_sin1(payload, headers, url, zone)
sjo1_server_data = create_swarm_sjo1(payload, headers, url, zone)
chi1_server_data = create_swarm_chi1(payload, headers, url, zone)
hel1_server_data = create_swarm_hel1(payload, headers, url, zone)
hel2_server_data = create_swarm_hel2(payload, headers, url, zone)
#uuid = server_data["server"]["uuid"]
