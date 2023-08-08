import ssl
import socket

hostname = 'prod.ds.interqual.com'
port = 443  # HTTPS port

# Create a socket and wrap it with SSL/TLS
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(sock)

# Connect to the server
ssl_sock.connect((hostname, port))

# Get the certificate from the server
cert = ssl_sock.getpeercert()

# Validate the certificate
subject = dict(x[0] for x in cert['subject'])
issuer = dict(x[0] for x in cert['issuer'])
cert_valid_from = cert['notBefore']
cert_valid_to = cert['notAfter']

print("Subject:", subject)
print("Issuer:", issuer)
print("Valid from:", cert_valid_from)
print("Valid to:", cert_valid_to)

# Close the SSL/TLS connection
ssl_sock.close()
