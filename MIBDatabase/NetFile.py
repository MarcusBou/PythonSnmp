from netmiko import ConnectHandler


class NetmikoConfCon:
    def __init__(self):
        self.net_connect = ConnectHandler(**{'device_type': 'cisco_ios', 'host': '192.168.1.1', 'username': 'admin', 'password': 'Kode1234!', 'secret': 'kode'})
        self.net_connect.enable()
