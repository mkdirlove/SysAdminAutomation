import subprocess
import sys

# Firewall rules
rules = [
    {'protocol': 'tcp', 'port': 80, 'action': 'accept'},
    {'protocol': 'tcp', 'port': 22, 'action': 'accept'},
    {'protocol': 'tcp', 'port': 443, 'action': 'accept'},
    {'protocol': 'udp', 'port': 53, 'action': 'accept'},
    {'protocol': 'icmp', 'port': '', 'action': 'accept'},
    {'protocol': '', 'port': '', 'action': 'drop'}
]

# Configure firewall
for rule in rules:
    protocol = rule['protocol']
    port = rule['port']
    action = rule['action']
    cmd = ['iptables', '-A', 'INPUT', '-p', protocol, '--dport', str(port), '-j', action] if protocol and port else ['iptables', '-A', 'INPUT', '-j', action]
    result = subprocess.run(cmd)
    if result.returncode == 0:
        print("Firewall rule added successfully:", cmd)
    else:
        sys.exit("Failed to add firewall rule:", cmd)
