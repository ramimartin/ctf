message = "5a6f7c643d5f72653d6e787e686f7469643d7c737c71646e746e3d6d6f726b7479786e3d7c3d7b6871713d6e646e6978703d74736e6d787e69747273313d7b6f72703d7f7269753d6975783d79786b7871726d786f3d6d786f6e6d787e69746b783d7c73793d7c3d6f787c713d707c71747e7472686e3d757c7e76786f3d6d786f6e6d787e69746b78"

for x in range(0, 256):
    print(str(chr(x)))

    decoded = ''
    for (he, xa) in zip(message[0::2], message[1::2]):
        int_value = int(he+xa,16)
        decoded = decoded + chr(int_value ^ x)

    print(decoded)


    ##decoded = ''
    ##for c in message:
    ##    decoded = decoded + chr(ord(c) ^ x)

    ##print(decoded)