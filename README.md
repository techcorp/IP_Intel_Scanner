# IP Intel Scanner

## Overview
IP Intel Scanner is an advanced IP lookup tool that provides detailed information about any given IP address. It retrieves data such as geolocation, ISP details, proxy/vpn status, threat intelligence, and even reverse DNS lookup. This tool is ideal for cybersecurity professionals, ethical hackers, and IT specialists who need accurate IP intelligence.

## Features
- Fetch IP geolocation data (Country, City, Region, Zip Code, Timezone)
- Reverse DNS lookup
- Proxy/VPN detection
- Threat intelligence check
- ISP and organization details
- Google Maps link for IP location visualization
- Colorful and user-friendly terminal interface

## Installation

### Prerequisites
Ensure you have Python installed (version 3.x recommended). You can check your Python version using:
```sh
python --version
```

### Step 1: Clone the Repository
```sh
git clone https://github.com/techcorp/IP_Intel_Scanner
cd Ip_Intel_Scanner
```

### Step 2: Install Dependencies
Install the required Python libraries using:
```sh
pip install -r requirements.txt
```

## Usage
Run the tool using:
```sh
python iplookup.py
```
Then, enter the IP address you want to lookup when prompted.

### Example Output
```
        Status       : Valid
        Country      : United States (US)
        Region       : California
        City        : Los Angeles
        Latitude    : 34.0522
        Longitude   : -118.2437
        Timezone    : America/Los_Angeles
        ISP         : Google LLC
        Organization: Google
        ASN         : AS15169 Google LLC
        Zip Code    : 90001
        Reverse DNS : google.com
        Proxy/VPN   : No
        Threat Check: Safe
        Google Maps : https://www.google.com/maps?q=34.0522,-118.2437
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests to improve the tool.

## Author
Developed by **Muhammad Anas** - Technical Corp

---
Happy Hacking! 🚀
