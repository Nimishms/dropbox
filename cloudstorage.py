import dropbox
class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main ():
    access_token = 'sl.BJv111HGbAQR8_4y01X3teonFHioFqA60bz7J2PSjcTExnDyUEzuIYC2h3K-uDqRmQarGtTbsfeA6P5E2vttHLtzoscTyWihKnqag8RlomuEz_GC6_Mkfw6jNtYtWVtakkc0toI'
    transferdata = Transferdata(access_token)
    file_from = input('Please enter file path to transfer: ')
    file_to = input('Please enter the full path to upload to dropbox')
    transferdata.upload_files(file_from,file_to)

    print('file has been moved')
main()