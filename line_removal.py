def main():
    from PIL import Image
    img = Image.open('0de39a03b.jpg')
    pixelMap = img.load()
    new_img = Image.new( img.mode, img.size)
    pixelsNew = new_img.load()
    length, height = new_img.size
    colors = dict()
    maxcount = 0
    maxline = 0
    for i in range(height):
        count = 0
        for j in range(length):
            pixelsNew[j,i] = pixelMap[j,i]
            #ignoring boundries
            if(i>4 and i<height-4 and j>4 and j<length-4):
                #get red pixel count
                r,g,b = pixelMap[j,i]
                if(r>g+40 and r>b+40):
                    count += 1
        if(count>maxcount):
            maxline = i
            maxcount = count
    for j in range(length):
        ru,gu,bu = pixelMap[j,maxline-1]
        rd,gd,bd = pixelMap[j,maxline+1]
        pixelsNew[j,maxline] = (int(ru+rd)//2,int(gu+gd)//2,int(bu+bd)//2)
    img.close()
    new_img.show()       
    new_img.save("out.tif") 
    new_img.close()
 
if __name__ == '__main__':
    main()