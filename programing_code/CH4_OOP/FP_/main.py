alphabet = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# lọc nguyên âm
# viết bởi Quantrimang.com


def filterNguyenam(alphabet):
    nguyenam = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in nguyenam):
        return True
    else:
        return False

filterNguyenam = filter(filterNguyenam, alphabet)

print('Các nguyên âm được lọc là:')
for nguyenam in filterNguyenam:
    print(nguyenam)
