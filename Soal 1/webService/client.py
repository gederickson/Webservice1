from suds.client import Client

clientMd5 = Client('http://localhost:8080/Hash/soap/description')
clientHash = Client('http://localhost:8080/hashSha/soap/description')

while True:
    print "\nALGORITMA HASHING"
    print "1. md5"
    print "2. sha1"
    print "3. sha224"
    print "4. sha256"
    print "5. sha384"
    print "6. sha512"
    print "Selain no diatas, dianggap keluar "
    jenisHash = raw_input("Silakan pilih no untuk jenis algoritma hash : ")
    inputKata = raw_input("Input kata          : ")
    if(jenisHash == '1'):
        print clientMd5.service.md5(inputKata)
    elif(jenisHash == '2'):
        print clientHash.service.sha1(inputKata)
    elif(jenisHash == '3'):
        print clientHash.service.sha224(inputKata)
    elif(jenisHash == '4'):
        print clientHash.service.sha256(inputKata)
    elif(jenisHash == '5'):
        print clientHash.service.sha384(inputKata)
    elif(jenisHash == '6'):
        print clientHash.service.sha512(inputKata)
    else:
        break