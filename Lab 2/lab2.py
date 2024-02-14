import os
import csv
import random
from PIL import Image

def choose_image():
    file = random.choice(os.listdir(r"images/"))
    image = Image.open(f"images/{file}", "r")
    image.show()
    return file

amount=int(input("How many images would you like to see? (Please enter an integer)\n"))

def rorschach(num):
    image_num = 0
    csv_file = open("csv_for_loop_ex.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Name", "Image", "Input"])
    while num!=0:
        image_num+=1
        print("\nImage "+str(image_num)+"\n-----------")
        name = input("What is your name?\n")
        filename = choose_image()
        description = input("Describe what you see in this image\n")
        csv_writer.writerow([name, filename, description])
        num-=1
    csv_file.close()
    print('\nThanks for playing!')
    (Image.open(f"thanks.png", "r")).show()
rorschach(amount)




