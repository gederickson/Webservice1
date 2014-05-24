from ladon.ladonizer import ladonize
import hashlib


class Hash(object):

    @ladonize(str,rtype=str)
    def md5(self,str):
        return "Hasil hash md5      : " + hashlib.md5(str).hexdigest()

class hashSha(object):

    @ladonize(str,rtype=str)
    def sha1(self,str):
        return "Hasil hash sha1     : " + hashlib.sha1(str).hexdigest()

    @ladonize(str,rtype=str)
    def sha224(self,str):
        return "Hasil hash sha224   : " + hashlib.sha224(str).hexdigest()

    @ladonize(str,rtype=str)
    def sha256(self,str):
        return "Hasil hash sha256   : " + hashlib.sha256(str).hexdigest()

    @ladonize(str,rtype=str)
    def sha384(self,str):
        return "Hasil hash sha384   : " + hashlib.sha384(str).hexdigest()

    @ladonize(str,rtype=str)
    def sha512(self,str):
        return "Hasil hash sha512   : " + hashlib.sha512(str).hexdigest()