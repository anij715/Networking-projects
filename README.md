# Networking-projects

## http_server.py

It's a  web  server  that  handles  one  HTTP  request  at  a  time.  it accepts and parses the HTTP request, gets the requested file from the server’s file system, creates an HTTP response message consisting of the requested file preceded by header lines, and then sends the response directly to the client. In case the requested file is not present in the server, then it sends an HTTP “404 Not Found” message back to the client.

### Screenshots for http_server.py
##### With test file available at the server
![image](https://user-images.githubusercontent.com/35270511/117739963-68d2f580-b1cd-11eb-8b58-340f413a5484.png)

##### With test file not available at the server
![image](https://user-images.githubusercontent.com/35270511/117740095-b4859f00-b1cd-11eb-9d8a-25bcd1cd2f49.png)

## server_mailtry.py

It's a simple mail client that sends email to any recipient. For that, it first connects to a mail server, then dialogues with the mail server using the SMTP protocol, and sends an email message to the mail server.

### Screenshots for server_mailtry.py
![image](https://user-images.githubusercontent.com/35270511/117740141-d1ba6d80-b1cd-11eb-8d1f-7271b38ae76f.png)
![image](https://user-images.githubusercontent.com/35270511/117740220-f6aee080-b1cd-11eb-9523-aad06ffd7946.png)

## pinger1.py

It's a Ping application in Python which uses ICMP but not exactly follows the official specification in RFC 1739. It  sends  ping  requests  to  a  specified  host separated by approximately one second. Each message contains a payload of data that includes a  timestamp.  After  sending  each  packet,  the  application  waits  up  to  one  second  to  receive  a reply. If one second goes by without a reply from the server, then the client assumes that either the ping packet or the pong packet was lost in the network (or that the server is down).

### Screenshots for pinger1.py
![image](https://user-images.githubusercontent.com/35270511/117740269-0f1efb00-b1ce-11eb-9124-f17c69f42fdc.png)
