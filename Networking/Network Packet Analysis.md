 Network Packet Analysis Guide
Core Concepts
1. Network Packet Structure

A network packet is the fundamental unit of data transmission across networks, consisting of:
Component	Description
Header	Contains metadata (source/destination IP, protocol, ports, TTL, checksums)
Payload	The actual data being transmitted (e.g., HTTP requests, DNS queries)
Trailer	Optional footer for error detection (e.g., Frame Check Sequence in Ethernet)
2. Purpose of Packet Analysis
Use Case	Application Example
Troubleshooting	Diagnosing dropped VoIP calls by analyzing RTP/RTCP packet loss
Security	Detecting port scanning (e.g., SYN floods) or malware C2 traffic
Performance	Identifying bandwidth hogs via throughput analysis (e.g., Netflix vs. Zoom traffic)
Tools Comparison
Tool	Type	Best For	Example Command
Wireshark	GUI	Deep protocol analysis	Filter: tcp.port == 443 && http
tcpdump	CLI	High-speed capture	tcpdump -i eth0 'port 53' -w dns.pcap
Zeek	IDS	Behavioral analysis	Generates conn.log with flow data
Analysis Workflow
1. Capture

    Method: Use Wireshark (GUI) or tcpdump (CLI)

    Best Practices:
    bash

    # Capture only HTTP traffic on port 80
    tcpdump -i eth0 'tcp port 80' -w http_traffic.pcap

        Limit captures to 100MB to avoid overload: -C 100

2. Inspection

    Key Headers:

        Ethernet: Source/dest MAC addresses

        IP: TTL, fragmentation flags

        TCP: Sequence numbers, window size

    Payload Tricks:
    wireshark

    Follow TCP Stream > Analyze HTTP cookies
    Right-click > Export Objects > Extract files from FTP

3. Pattern Detection
Anomaly	Indicator	Wireshark Filter
Port Scan	Repeated SYN to closed ports	tcp.flags.syn==1 && tcp.flags.ack==0
DNS Tunneling	Long TXT records or high frequency	dns.qry.type == 16
4. Filtering
wireshark

# Show only traffic between two IPs
ip.addr == 192.168.1.100 && ip.addr == 10.0.0.5

# Find failed connections
tcp.flags.reset == 1

5. Reporting

    Essential Metrics:
    text

Top Talkers: Conversations > IPv4 Statistics
Round-Trip Time: Statistics > TCP Stream Graph

Automation:
bash

    tshark -r capture.pcap -q -z io,phs > protocol_hierarchy.txt

Protocol Cheat Sheet
Protocol	Key Fields	Security Risks
TCP	SEQ/ACK numbers, Window	SYN floods, session hijacking
DNS	Query type (A/AAAA/TXT)	Cache poisoning, exfiltration
HTTP	User-Agent, Cookies	Credential stuffing, XSS
Practical Example: Detecting SSH Brute Force

    Capture:
    bash

tcpdump -i eth0 'port 22' -w ssh.pcap

Analyze:
wireshark

# Filter rapid connection attempts
ssh && frame.time_delta < 1.0

Report:
text

    Alert: 50+ failed SSH logins from 45.33.21.7
    Recommended Action: Block IP in firewall

Pro Tips

    Optimize Captures:
    bash

# Drop privileges for security
tcpdump -Z nobody -i eth0 -w capture.pcap

Cloud Analysis:

    Upload PCAPs to CloudShark for team collaboration
