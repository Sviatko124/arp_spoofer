# arp_spoofer

This tool takes advantage of the ARP protocol to route the internet traffic between the target computer and the router go through your computer first, effectively making you the man in the middle. This tool doesn't actually print the traffic, but that will come in the near future and I will update this readme when it comes out. 

Also, before using this tool, if you want the traffic to go through your computer and make you the man in the middle, run the following command beforehand:
echo 1 > /proc/sys/net/ipv4/ip_forward

However, you also have an option to completely block the victim's internet access by running this command before running the tool:
echo 0 > /proc/sys/net/ipv4/ip_forward\

Both options have their advantages, but for a man in the middle attack you will want to do the first option. Again, this tool will only fool the router and the target computer to make their communication go through your computer first, but this tool doesn't actually read the traffic. For that, you will want to use this tool and the packet sniffer that I will be writing in the near future, so stay tuned for that. 
