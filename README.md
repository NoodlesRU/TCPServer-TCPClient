# TCPServer-TCPClient
#Your client should accept an integer between 1 and 100 from the keyboard and validate user input, open a TCP socket to your server and send a message containing 
#i.	a string containing your name (e.g., “Client: Name”)
#ii.	the entered integer value and then wait for a sever reply.

#Your server will create a string containing its name (e.g., “Server: Name”) and then begin accepting connections from clients.  On receipt of a client message, your server should
#i.	print (display) the client’s name (extracted from the received message) and the server’s name 
#ii.	itself randomly pick an integer between 1 and 100 and display the client’s number, its number, and the sum of those numbers
#iii.	send its name string and the server-chosen integer value back to the client

#Your client should read the message sent by the server and display its name, the server’s name, its integer value, and the server’s integer value, and then compute the sum.  The client then terminates after releasing any created sockets. As an aside (and as a check that you #are doing things correctly, you should make sure for yourself that the values and the sums are correct)
