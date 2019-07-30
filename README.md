# Meraki_Content_URL_Update

*Add new URL blocking rule to Meraki content filter policy*

---

**ToDo's:**

- [ ] Consider writing your README first.  Doing so helps you clarify your intent, focuses your project, and it is much more fun to write documentation at the beginning of a project than at the end of one, see:
    - [Readme Driven Development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
    - [GitHub Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [ ] Ensure you put the [license and copyright header](./HEADER) at the top of all your source code files.
- [ ] Be mindful of the third-party materials you use and ensure you follow Cisco's policies for creating and sharing Cisco Sample Code.

---

## Motivation

I wanted to make it easy to add a new "Blocked URL pattern" to a Meraki network Content Filtering policy.

## Show Me!

I'm working on the visual.

## Features

This script does the following actions:

- Connect to your Meraki network ID, and obtain the current settings of the Content Filter policy.
- Prompt for the URL for a new site to be added to the policy.
- Modify the URL blocking policy, without changing the other policy settings.

## Technologies & Frameworks Used

This is Cisco Sample Code!  What Cisco and third-party technologies are you working with?  Are you using a coding framework or software stack?  A simple list will set the context for your project.

**Cisco Products & Services:**

- Meraki SDK
- Service

**Third-Party Products & Services:**

- os
- sys
- json
- requests
- click

## Usage

Run the script, and follow the prompts to add a new URL to the Meraki Content Filter policy.

## Installation

Add the following environment variables to the machine that will run this script:

Variable: "MERAKI_API"
Value:  Your Meraki Dashboard API key

Variable:  "MERAKI_NET"
Value:  The network ID for the network that will have rules updated

To determine the Meraki network ID, goto http://postman.meraki.com

## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Aaron Davis <aarodavi@cisco.com>
- Jeffry Handal <jehandal@cisco.com>

## Credits

Jeffry challenged me to create this for a customer.  He gets the credit for the inspiration.  Hopefully, he will help me update it with additional functionality.

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
