
def check_ip_v4(ip4):
    ipnums = ip4.split('.')
    
    for num in ipnums:
        if len(num) == 0 or len(num) > 3:
            return 'Neither'
        
        if(len(num) !=2 and num[0] == '0') or not num.isdigit() or int(num) >255:
            return 'Neither'

    return 'IPv4'

import string

def check_ip_v6(ipv6):
    ipnums = ipv6.split(':')
    for num in ipnums:
        if len(num) == 0 or len(num) >4 or not all( c in string.hexdigits for c in num):
            return 'Neither'
    return 'IPv6'

def validIpAddress(IP):
    if IP.count('.') == 3:
        return check_ip_v4(IP)
    elif IP.count(':') == 7 :
        return check_ip_v6(IP)
    else:
        return 'Neither'
    
    
print(validIpAddress('123.123.123.123'))