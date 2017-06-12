# -*- coding:utf-8 -*-
import itchat
import math
import PIL.Image as Image
import os
import shutil
class weChat(object):
    def __init__(self):
        self.path = 'C:\Users\Administrator\Desktop\image'
        try:
            shutil.rmtree(self.path)
        except Exception as e:
            pass
        itchat.auto_login()
    def getImage(self):
        friends = itchat.get_friends(update=True)[0:]
        num = 0
        os.mkdir(self.path)
        for i in friends:
            img = itchat.get_head_img(userName=i["UserName"])
            fileImage = open(self.path + "\\" + str(num) + ".jpg", 'wb')
            fileImage.write(img)
            fileImage.close()
            num += 1
        self.pilImage()
    def pilImage(self):
        ls = os.listdir(self.path)
        each_size = int(math.sqrt(float(640 * 640) / len(ls)))
        lines = int(640 / each_size)
        image = Image.new('RGBA', (640, 640))
        x = 0
        y = 0
        for i in range(0, len(ls) + 1):
            try:
                img = Image.open(self.path + "\\" + str(i) + ".jpg")
            except IOError:
                print("Error")
            else:
                img = img.resize((each_size, each_size), Image.ANTIALIAS)
                image.paste(img, (x * each_size, y * each_size))
                x += 1
                if x == lines:
                    x = 0
                    y += 1
        image.save(self.path + "\\" + "all.jpg")
        itchat.send_image(self.path + "\\" + "all.jpg", 'filehelper')
        itchat.logout()

if __name__ == "__main__":
    test = weChat()
    test.getImage()
