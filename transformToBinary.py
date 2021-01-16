def getBinaryValue(values):
    if 1 in values:
        return 1
    else:
        return 0

def transformToBinary(data,dT):
    l = len(data)
    dif = l%dT
    first = 0
    matrix = []
    for i in range(0,l-dif):
        last = i+1
        if last%dT == 0:
            print(data[first:last])
            matrix.append(getBinaryValue(data[first:last]))
            first = last
    print(data[first:l])
    matrix.append(getBinaryValue(data[first:l]))
    return matrix
