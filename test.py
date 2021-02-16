
def fun(data):
    return [i**2 for i in data ]

if __name__ == '__main__':
    data = [1,2,3,4,5]
    res = []
    res.append(fun(data))
    print(res)