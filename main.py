from PIL import Image
import os

json='''{
  "images" : [
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "icon-20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "icon-20@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "icon-29.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "icon-29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "icon-29@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "icon-40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "icon-60@2x.png",
      "scale" : "3x"
    },
    {
      "size" : "57x57",
      "idiom" : "iphone",
      "filename" : "icon.png",
      "scale" : "1x"
    },
    {
      "size" : "57x57",
      "idiom" : "iphone",
      "filename" : "icon@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "icon-60@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "icon-60@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "20x20",
      "idiom" : "ipad",
      "filename" : "icon-20.png",
      "scale" : "1x"
    },
    {
      "size" : "20x20",
      "idiom" : "ipad",
      "filename" : "icon-20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "icon-29.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "icon-29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "icon-40.png",
      "scale" : "1x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "icon-40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "50x50",
      "idiom" : "ipad",
      "filename" : "icon-50.png",
      "scale" : "1x"
    },
    {
      "size" : "50x50",
      "idiom" : "ipad",
      "filename" : "icon-50@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "72x72",
      "idiom" : "ipad",
      "filename" : "icon-72.png",
      "scale" : "1x"
    },
    {
      "size" : "72x72",
      "idiom" : "ipad",
      "filename" : "icon-72@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "icon-76.png",
      "scale" : "1x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "icon-76@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "83.5x83.5",
      "idiom" : "ipad",
      "filename" : "icon-83.5@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "1024x1024",
      "idiom" : "ios-marketing",
      "filename" : "icon-1024.png",
      "scale" : "1x"
    },
    {
      "size" : "24x24",
      "idiom" : "watch",
      "filename" : "icon-24@2x.png",
      "scale" : "2x",
      "role" : "notificationCenter",
      "subtype" : "38mm"
    },
    {
      "size" : "27.5x27.5",
      "idiom" : "watch",
      "filename" : "icon-27.5@2x.png",
      "scale" : "2x",
      "role" : "notificationCenter",
      "subtype" : "42mm"
    },
    {
      "size" : "29x29",
      "idiom" : "watch",
      "filename" : "icon-29@2x.png",
      "role" : "companionSettings",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "watch",
      "filename" : "icon-29@3x.png",
      "role" : "companionSettings",
      "scale" : "3x"
    },
    {
      "size" : "40x40",
      "idiom" : "watch",
      "filename" : "icon-40@2x.png",
      "scale" : "2x",
      "role" : "appLauncher",
      "subtype" : "38mm"
    },
    {
      "size" : "44x44",
      "idiom" : "watch",
      "filename" : "icon-44@2x.png",
      "scale" : "2x",
      "role" : "appLauncher",
      "subtype" : "40mm"
    },
    {
      "size" : "50x50",
      "idiom" : "watch",
      "filename" : "icon-50@2x.png",
      "scale" : "2x",
      "role" : "appLauncher",
      "subtype" : "44mm"
    },
    {
      "size" : "86x86",
      "idiom" : "watch",
      "filename" : "icon-86@2x.png",
      "scale" : "2x",
      "role" : "quickLook",
      "subtype" : "38mm"
    },
    {
      "size" : "98x98",
      "idiom" : "watch",
      "filename" : "icon-98@2x.png",
      "scale" : "2x",
      "role" : "quickLook",
      "subtype" : "42mm"
    },
    {
      "size" : "108x108",
      "idiom" : "watch",
      "scale" : "2x",
      "filename" : "icon-108@2x.png",
      "role" : "quickLook",
      "subtype" : "44mm"
    },
    {
      "size" : "1024x1024",
      "idiom" : "watch-marketing",
      "filename" : "icon-1024.png",
      "scale" : "1x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}'''

#input image
image_name=input("Name of your icon in this directory = ")
input_image=Image.open(image_name)
dir="AppIcon.appiconset"
os.mkdir(dir)
os.chdir(dir)
contents = open("Contents.json", "w")
contents.write(json)



icon_20=input_image.resize((20,20))
icon_20.save("icon-20.png","PNG")
print("Created icon-20.png")

icon_20_2x=input_image.resize((40,40))
icon_20_2x.save("icon-20@2x.png","PNG")
print("Created icon-20@2x.png")

icon_20_3x=input_image.resize((60,60))
icon_20_3x.save("icon-20@3x.png","PNG")
print("Created icon-20@3x.png")

icon_24_2x=input_image.resize((48,48))
icon_24_2x.save("icon-24@2x.png","PNG")
print("Created icon-24@2x.png")

icon_27_5_2x=input_image.resize((55,55))
icon_27_5_2x.save("icon-27.5@2x.png","PNG")
print("Created icon-27.5@2x.png")

icon_29=input_image.resize((29,29))
icon_29.save("icon-29.png","PNG")
print("Created icon-29.png")

icon_29_2x=input_image.resize((58,58))
icon_29_2x.save("icon-29@2x.png","PNG")
print("Created icon-29@2x.png")

icon_29_3x=input_image.resize((87,87))
icon_29_3x.save("icon-29@3x.png","PNG")
print("Created icon-29@3x.png")

icon_40=input_image.resize((40,40))
icon_40.save("icon-40.png","PNG")
print("Created icon-40.png")

icon_40_2x=input_image.resize((80,80))
icon_40_2x.save("icon-40@2x.png","PNG")
print("Created icon-40@2x.png")

icon_44_2x=input_image.resize((88,88))
icon_44_2x.save("icon-44@2x.png","PNG")
print("Created icon-44@2x.png")

icon_50=input_image.resize((50,50))
icon_50.save("icon-50.png","PNG")
print("Created icon-50.png")

icon_50_2x=input_image.resize((100,100))
icon_50_2x.save("icon-50@2x.png","PNG")
print("Created icon-50@2x.png")

icon_108_2x=input_image.resize((216,216))
icon_108_2x.save("icon-108@2x.png","PNG")
print("Created icon-108@2x.png")

icon_60_2x=input_image.resize((120,120))
icon_60_2x.save("icon-60@2x.png","PNG")
print("Created icon-60@2x.png")

icon_60_3x=input_image.resize((180,180))
icon_60_3x.save("icon-60@3x.png","PNG")
print("Created icon-60@3x.png")

icon_72=input_image.resize((72,72))
icon_72.save("icon-72.png","PNG")
print("Created icon-72.png")

icon_72_2x=input_image.resize((144,144))
icon_72_2x.save("icon-72@2x.png","PNG")
print("Created icon-72@2x.png")

icon_76=input_image.resize((76,76))
icon_76.save("icon-76.png","PNG")
print("Created icon-76.png")

icon_76_2x=input_image.resize((152,152))
icon_76_2x.save("icon-76@2x.png","PNG")
print("Created icon-76@2x.png")

icon_83_5_2x=input_image.resize((167,167))
icon_83_5_2x.save("icon-83.5@2x.png","PNG")
print("Created icon-83.5@2x.png")

icon_86_2x=input_image.resize((172,172))
icon_86_2x.save("icon-86@2x.png","PNG")
print("Created icon-86@2x.png")

icon_98_2x=input_image.resize((196,196))
icon_98_2x.save("icon-98@2x.png","PNG")
print("Created icon-98@2x.png")

icon_1024=input_image.resize((1024,1024))
icon_1024.save("icon-1024.png","PNG")
print("Created icon-1024.png")

icon=input_image.resize((57,57))
icon.save("icon.png","PNG")
print("Created icon.png")

icon_2x=input_image.resize((114,114))
icon_2x.save("icon@2x.png","PNG")
print("Created icon@2x.png")



os.chdir('..')
os.mkdir('For Android')
os.chdir('For Android')

android=input_image.resize((512,512))
android.save("icon.png")
print("For android Created")



a = input('Press a key to exit')
if a:
    exit(0)






