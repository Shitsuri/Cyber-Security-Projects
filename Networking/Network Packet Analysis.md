 Key Concepts
1. What is a Network Packet?
 A network packet is a small unit of data transmitted over a network.
 It consists of three parts:

   It Contains metadata, such as source/destination IP addresses, protocol, and port numbers.
   Payload: The actual data being transmitted.
   Trailer: Optional; often used for error detection.

 2. Why Analyze Packets?

    Troubleshooting: To identify connectivity or latency issues in a network.
    Security: Detect suspicious or malicious activities like intrusions or data breaches.
    Performance: Optimize network bandwidth and application behavior.


 4. Packet Analysis Tools

   Common tools include:

       Wireshark: A widely used GUI-based tool for detailed packet inspection.
       tcpdump: A command-line tool for capturing network packets.
       ngrep: A utility for analyzing packets with pattern matching.
       Snort/Suricata: Intrusion detection systems (IDS) that analyze packet data for security threats.

Process of Packet Analysis

1. Packet Capture

The first thing, I did was to capture network traffic using Wireshark. I specifically focused on capturing TCP packets. To do this, I started, Wireshark and selected the network interface to monitor. I applied a simple capture filter (tcp) to ensure I only captured TCP traffic and then let Wireshark run to gather the packets. Once I had captured all the data I needed, I saved the capture as a .pcap file for further analysis.

2. Packet Inspection

       Examine headers for IP addresses, protocols (TCP/UDP/ICMP), and port numbers.
       Analyze payloads for application data (e.g., HTTP, DNS).

5. Pattern Identification

       Look for anomalies, such as unusual traffic spikes, failed connections, or odd payload sizes.

6. Filtering

       Apply filters to focus on specific traffic (e.g., ip.addr == 192.168.1.1 in Wireshark).

Logging and Reporting

       Record findings and generate actionable reports.

Key Protocols in Analysis

      TCP (Transmission Control Protocol): Ensures reliable data transfer.
      UDP (User Datagram Protocol): Facilitates fast, connectionless communication.
      HTTP/HTTPS: Analyze web traffic and encrypted content.
      DNS (Domain Name System): Look for unusual queries or potential exfiltration.
      ICMP (Internet Control Message Protocol): Monitor ping or traceroute behavior.

