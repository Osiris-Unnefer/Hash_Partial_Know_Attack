import hashlib
dictionnaires  = {0 : 'md5',1 : 'sha1',2 : 'sha256'}
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n   Created by Osiris_Unnefer \n\nhttps://github.com/Osiris-Unnefer\n")
mot_de_passe = input('\nenter the part of the hash (lowercase letters)-> ');c='0'


mode = input("modes available -> \n[0] md5 \n[1] sha1 \n[2] sha2-256\n\n")
hash_function = getattr(hashlib, dictionnaires[int(mode)])

while True :
    c = int(c);c= str(c+1)
    cc = hash_function(c.encode('utf-8')).hexdigest()
    if mot_de_passe in cc :
        print(f"similarité trouvée -> {c}  hash  -> {cc}")
        #coupage manuel obligatoire ctrl + c
