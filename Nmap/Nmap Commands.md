Here are 10 essential Nmap commands, along with detailed explanations for each:

1. Scan a single host:
`nmap <host>`
This command scans a single host specified by its IP address or hostname. By default, Nmap scans the 1000 most common ports.

2. Scan a range of IP addresses:
`nmap <start IP>-<end IP>`
This command scans a range of IP addresses, from the start IP to the end IP. For example, nmap 192.168.1.1-10 will scan IPs from 192.168.1.1 to 192.168.1.10.

3. Scan a subnet:
`nmap <subnet>`
This command scans an entire subnet, defined by the IP address and subnet mask. For example, nmap 192.168.1.0/24 will scan all IP addresses in the 192.168.1.0 subnet.

4. Scan a list of hosts:
`nmap -iL <list>`
This command scans a list of hosts specified in a text file, where each line contains an IP address or hostname. For example, nmap -iL targets.txt scans all hosts listed in targets.txt.

5. Perform a fast scan:
`nmap -F <host>`
This command performs a quick scan on a host, checking only the 100 most common ports. It’s useful for a rapid assessment of open ports and potential vulnerabilities.

6. Perform a more detailed scan:
`nmap -sS <host>`
This command performs a more in-depth scan using the TCP SYN scan method. It’s faster and less detectable than the standard TCP connect scan.

7. Perform a TCP SYN scan:
`nmap -sS <host>`
This scan uses the TCP SYN method, sending SYN packets to each port and awaiting a response. It’s a stealthy approach that can often bypass firewalls and intrusion detection systems.

8. Perform a UDP scan:
`nmap -sU <host>`
This command scans using the UDP protocol, commonly used for services like DNS and DHCP. UDP scans can be slower and less reliable than TCP scans, but they may reveal additional open ports.

9. Scan for specific ports:
`nmap -p <port(s)> <host>`
This command scans specific ports, which can be listed as a comma-separated list of port numbers or ranges. For example, nmap -p 80,443,8080 192.168.1.1 checks ports 80, 443, and 8080 on the host 192.168.1.1.

10. Scan all ports:
`nmap -p- <host>`
This command scans all ports (1-65535) on a host. While it may take longer to complete, it can uncover hidden or obscure services.
