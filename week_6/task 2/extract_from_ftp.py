from ftplib import FTP

def download_file_from_ftp():
    ftp = FTP()
    ftp.connect("127.0.0.1", 2121)
    ftp.login("user", "12345")

    filename = "sample_file.csv"
    with open(filename, "wb") as f:
        ftp.retrbinary(f"RETR {filename}", f.write)

    print(f"✅ Downloaded '{filename}' from FTP server.")
    ftp.quit()

if __name__ == "__main__":
    download_file_from_ftp()
