# -*- coding: utf-8 -*-















import socket















fdyzyXDJjzIFALlPtfhhthncExBMScHs = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,



514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]















def dWUvXWgjgMbqmUHgmrsEqhlXyUSUzJcv(ip):



    try:



        socket.inet_aton(ip)



    except socket.error:



        return 'Error: Invalid IP address.'







    JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = ''







    for FTgtdFTPVHSlXMuoAyFhwFOaagfVMYOI in fdyzyXDJjzIFALlPtfhhthncExBMScHs:



        zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



        DYvtTWSDvQfBNwbqoXNEzbmvICZBOkHO = zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.connect_ex((ip, FTgtdFTPVHSlXMuoAyFhwFOaagfVMYOI))



        socket.setdefaulttimeout(0.5)







        BAiArKjSTZSQrGAboyLVEUrGHzmJmxEt = 'open' if not DYvtTWSDvQfBNwbqoXNEzbmvICZBOkHO else 'closed'







        JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl += '{:>5}/tcp {:>7}\n'.format(FTgtdFTPVHSlXMuoAyFhwFOaagfVMYOI, BAiArKjSTZSQrGAboyLVEUrGHzmJmxEt)







    return JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl.rstrip()



