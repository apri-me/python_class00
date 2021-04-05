
cls = ['mohsen', 'radmeht', 'mahdi', 'alireza']

def minimum_number(li):
    m = li[0]
    for i in range(1, len(li)):
        if li[i] < m:
            m = li[i]
    return m

print( minimum_number ( cls ) )
