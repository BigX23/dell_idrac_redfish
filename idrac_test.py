import getpass
import requests
from pprint import pprint


def get_BIOS_Settings(hostname, user, cred):
    biosHead = {'content-type': 'application/json'}
    GETURL = f"https://{hostname}/redfish/v1/Systems/System.Embedded.1/Bios"

    response = requests.get(url=GETURL, auth=(user, cred), verify=False, headers=biosHead)

    data = response.json()

    return data



if __name__ == "__main__":

    idrac_host = input("Enter iDRAC FQDN: ")
    idrac_user = getpass.getpass(prompt='Enter iDRAC username: ', stream=None)
    print(f"Running as {idrac_user}")
    idrac_pass = getpass.getpass(prompt='Enter iDRAC password: ', stream=None)

    return_data = get_BIOS_Settings(idrac_host, idrac_user, idrac_pass)
    
    ServiceTag = return_data['Attributes']['SystemServiceTag']

    pprint(return_data)

    print(f"\nService Tag: {ServiceTag}\n")

