import socket
import sys
import argparse


class check_smtp_user:
    def __init__(self, args: list):
        self._parse_args(args)

    def _parse_args(self, args: list):
        parser = argparse.ArgumentParser(
            description='Simple script to check if'
                        'a given user exists in SMTP.')
        parser.add_argument('-u', '--username', help='Username to check if exists.', required=True)
        parser.add_argument('-i', '--ip', help='IP of the SMTP server.', required=True)
        parser.add_argument('-p', '--port', help='port of the SMTP server.', default=25,
                            type=int)

        args = parser.parse_args(args)
        self.ip = args.ip
        self.port = args.port
        self.username = args.username

    def check_if_exits(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
        except ConnectionError:
            print("[-] Connection Error.")
            print('[-] Exiting...')
            sys.exit(0)
        banner = s.recv(1024)
        print(banner)
        s.send('VRFY ' + self.username + '\r\n')
        result = s.recv(1024)
        print(result)
        s.close()


check_smtp_user(sys.argv[1:]).check_if_exits()
