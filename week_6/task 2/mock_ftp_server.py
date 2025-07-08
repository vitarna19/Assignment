from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", "C:/python codes/Celebal Intership/week 6 assignment/task 2/ftp_files", perm="elradfmwMT")  # full permissions
    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("127.0.0.1", 2121), handler)
    print("FTP server running at ftp://127.0.0.1:2121")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
