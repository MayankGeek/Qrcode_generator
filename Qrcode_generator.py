#Simple python script that generates qrcode when provided with a url/link
import qrcode
url=input("Enter a url/link to generate qrcode: ")
img=qrcode.make(url)
img.save("Qrcode.png","PNG")  
print("Qrcode generated")
