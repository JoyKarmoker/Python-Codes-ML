def main():
    dic = {"Joe":12345, "Trump": 2022, "Obama":2018}

    print(dic["Joe"])

    print(dic)

    del dic["Joe"]

    print(dic)

    for key in dic:
        print("Key:", key, "Value: ", dic[key])

    for k, v in dic.items():
        print("Key: ", k, "Value: ", v)

    print ("Obama" in dic)
    print("Joy" in dic)

    dic.clear()

    point = (5, 9)
    print(point[0])
    print(point[1])

if  __name__ == "__main__":
    main()
main