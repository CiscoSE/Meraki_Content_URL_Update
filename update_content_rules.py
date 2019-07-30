#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) {{current_year}} Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from __future__ import absolute_import, division, print_function

__author__ = "Aaron Davis <aarodavi@cisco.com>"
__contributors__ = [
    "Jeffry Handal <jehandal@cisco.com>"
]
__version__ = "0.1.0"
__copyright__ = "Copyright (c) {{current_year}} Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

"""
Add the following environment variables to the machine that will
run this script:

Variable: "MERAKI_API"
Value:  Your Meraki Dashboard API key

Variable:  "MERAKI_NET"
Value:  The network ID for the network that will have rules updated

To determine the Meraki network ID, goto http://postman.meraki.com
"""

import os
import sys
import json
import requests
import click

from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.models.update_network_content_filtering_model import UpdateNetworkContentFilteringModel
from meraki_sdk.exceptions.api_exception import APIException
from meraki_sdk.exceptions.api_exception import APIException

MERAKI_API = os.environ.get('MERAKI_API')
x_cisco_meraki_api_key = MERAKI_API
MERAKI_NET = os.environ.get('MERAKI_NET')

client = MerakiSdkClient(x_cisco_meraki_api_key)

network_id = MERAKI_NET

# Get Network Content Filtering

content_filtering_rules_controller = client.content_filtering_rules
try:
    print("Reading current settings from Meraki Dashboard...\n")
    result = content_filtering_rules_controller.get_network_content_filtering(network_id)
    response = json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    try:
        print("Backing up current settings to local file...\n")
        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(response, outfile)
    finally:
        outfile.close()
except APIException as e:
    print(e)

print("Reading local file...\n")
with open('data.json', 'r', encoding='utf-8') as f:
    jsonData = json.load(f)

jsonDataS = json.loads(jsonData)

json_allowedUrlPatterns = jsonDataS["allowedUrlPatterns"]
json_blockedUrlCategories = jsonDataS["blockedUrlCategories"]
json_blockedUrlPatterns = jsonDataS["blockedUrlPatterns"]
json_urlCategoryListSize = jsonDataS["urlCategoryListSize"]

print("Current content filtering configuration settings: ")
print("Allowed Url Patterns: %s" % json_allowedUrlPatterns)
print("Blocked Url Categories: \n")
for id in json_blockedUrlCategories:
    print(json.dumps(id['name']))
print('\n')
print("Blocked Url Patterns: %s" % json_blockedUrlPatterns)
print("Url Category List Size: %s" % json_urlCategoryListSize)
print('\n')

# Put the list of Categories into a List to maintain existing configuration

Category_List = []

for id in json_blockedUrlCategories:
    Filter_id = (id['id'])
    Category_List.append(Filter_id)

# Prompt for new URL to block

addBlockedUrlPattern = input("Enter the URL to add to the blocked list: ")
print('\n')

confirmUrlPattern = input("Are you sure %s should be added to the blocked list? (Y or N) " % addBlockedUrlPattern)
print('\n')

if confirmUrlPattern == "Y" or confirmUrlPattern == "y":
    print("Ok. Adding %s to the blocked list" % addBlockedUrlPattern)
    print('\n')

    new_add_blockedUrlPatterns = []
    new_add_blockedUrlPatterns.append(addBlockedUrlPattern)
    updated_blockedUrlPatterns = json_blockedUrlPatterns + new_add_blockedUrlPatterns
    print("The new blocked list will be: ")
    print(updated_blockedUrlPatterns)
    print('\n')

else:
    print("Not adding %s to the blocked list!" % addBlockedUrlPattern)
    sys.exit("Exiting...")

# Change Network Content Filtering rules

content_filtering_rules_controller = client.content_filtering_rules
collect = {}
collect['network_id'] = network_id

update_network_content_filtering = UpdateNetworkContentFilteringModel()
update_network_content_filtering.allowed_url_patterns = json_allowedUrlPatterns
update_network_content_filtering.blocked_url_patterns = updated_blockedUrlPatterns
update_network_content_filtering.blocked_url_categories = Category_List

# Although not documented, the following line must exist, or the update fails.
# The option can be 'fullList', or 'topSites'
update_network_content_filtering.url_category_list_size = json_urlCategoryListSize
collect['update_network_content_filtering'] = update_network_content_filtering

try:
    result = content_filtering_rules_controller.update_network_content_filtering(collect)
    print("Update completed...")
except APIException as e:
    print(e)
