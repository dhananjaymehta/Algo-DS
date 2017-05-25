def rotate_image(img):
    n=len(img)
    # step 1: swap elements across diagonal symmerty
    for i in range(n):
        for j in range(i,n):
            img[i][j], img[j][i] =img[j][i], img[i][j]

    # step 2: reverse each row:
    for i in range(n):
        img[i]=img[i][::-1]

    return img

image = [[1,2,3],[4,5,6],[7,8,9]]
rotate_image(img=image)