import psutil

tcp_connections = psutil.net_connections(kind='tcp')

for conn in tcp_connections:
    if conn.status == psutil.CONN_ESTABLISHED:
        print(f"Local address: {conn.laddr.ip}:{conn.laddr.port} "
              f"Remote address: {conn.raddr.ip}:{conn.raddr.port}")

