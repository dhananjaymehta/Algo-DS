def remove_item_inplace(array, value):
    #array.sort()  #sort the elements
    try:
        while True:
            array.remove(value)
    except:
        return len(array)

array = [0,4,4,0,0,2,4,4]
value = 4
print(remove_item_inplace(array, value))