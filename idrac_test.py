"""
This script will collect iDRAC details via input from the user and then connect to the
 edfish API endpoint of an iDRAC, query the BIOS settings, and return the BIOS data in json format.

This script requires the following modules:
    getpass
    requests
    pprint

This file contains the following function:
    * get_BIOS_Settings - returns the BIOS settings of the iDRAC in json format

This file contains the following if __name__ == "__main__" block:
    * Inputs the iDRAC FQDN, username, and password
    * Prints the BIOS settings of the iDRAC in json format
    * Prints the Service Tag of the iDRAC
"""
import getpass
import requests
from pprint import pprint


def get_BIOS_Settings(hostname, user, cred):
    """
    This function will connect to the Redfish API endpoint of an iDRAC and query the BIOS settings
    and return the BIOS data in json format.

    Parameters:
    hostname (str): The FQDN of the iDRAC
    user (str): The username of the iDRAC
    cred (str): The password of the iDRAC

    Returns:
    data (dict): The BIOS settings of the iDRAC in json format
    """
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

