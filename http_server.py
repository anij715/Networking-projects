#import socket module
import socket
HOST,PORT = '127.0.0.1',8082
# serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serverSocket.bind((HOST,PORT))
serverSocket.listen(1)
 
print('the web server is up on port:', PORT)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()    
    req = connectionSocket.recv(1024).decode('utf-8')
    string_list = req.split(' ') 
    method = string_list[0]
    requesting_file = string_list[1]
    print('Client request ',requesting_file)
 
    myfile = requesting_file.split('?')[0] # After the "?" symbol not relevent here
    myfile = myfile.lstrip('/')
    if(myfile == ''):
        myfile = 'index.html'    # Load index file as default
 
    try:
        file = open(myfile,'rb') # open file , r => read , b => byte format
        response = file.read()
        file.close()
 
        header = 'HTTP/1.1 200 OK\n'
 
        mimetype = 'text/html'
 
        header += 'Content-Type: '+str(mimetype)+'\n\n'
 
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
 
    final_response = header.encode('utf-8')
    final_response += response
    connectionSocket.send(final_response)
    connectionSocket.close()