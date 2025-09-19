# arp_spoofer

This tool takes advantage of the ARP protocol to route the internet traffic between the target computer and the router go through your computer first, making you the man in the middle. 

Also, before using this tool, if you want the traffic to go through your computer and let you intercept traffic, run the following command beforehand:
echo 1 > /proc/sys/net/ipv4/ip_forward

However, you also have an option to completely block the victim's internet access by running this command before running the tool:
echo 0 > /proc/sys/net/ipv4/ip_forward

IMPORTANT! This tool is only for educational purposes only and is to be used with consent. Misuse of this tool can get you into serious trouble and I do not encourage illegal activities. Thank you. 
