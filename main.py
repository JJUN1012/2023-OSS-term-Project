import get_cctv_lists_image as gcli
import get_cctv_lists_video as gclv
import get_traffic_status as gts
import open_video as ov
import os
import asciiart as aa

minX = 127.0
maxX = 127.4
minY = 37.3
maxY = 37.6

aa.aaprint();
try:
    fp = open("datafiles/apiKey.txt", 'r')
    print("api key file found")
    api_key = fp.readline()
    result = gcli.get_cctv_lists(minX, maxX, minY, maxY)
    if(result == -2):
        print("invalid api key")
        os.remove("datafiles/apiKey.txt")
        fp.close()
        exit()
    print("Please wait a moment...")
    gclv.get_cctv_video_list(minX, maxX, minY, maxY)
    print("Get cctv lists success")
    fp.close()
except:
    print("api key file not found")
    fp = open("datafiles/apiKey.txt", 'w', encoding= "UTF-8")
    api_key = input("input api key: ")
    fp.write(api_key)
    fp.close()
    result = gcli.get_cctv_lists(minX, maxX, minY, maxY)
    if(result == -2):
        print("invalid api key")
        os.remove("datafiles/apiKey.txt")
        exit()
    print("Please wait a moment...")
    gclv.get_cctv_video_list(minX, maxX, minY, maxY)
    print("Get cctv lists success")

fp = open("datafiles/cctv_lists.txt", 'r', encoding= "UTF-8")
cctv_lists = fp.readlines()
fp.close()
fp = open("datafiles/cctv_lists_video.txt", 'r', encoding= "UTF-8")
cctv_lists_video = fp.readlines()
fp.close()
for index, data in enumerate(cctv_lists):
    name = cctv_lists[index].split(',')[0][2:-1]
    print(f"{index}: {name}")

selected_cctv = int(input("\nPlease enter the number of the CCTV you want: "))
try:
    selected_cctv_name = cctv_lists[selected_cctv].split(',')[0][2:-1]
except:
    print("It's a CCTV number that doesn't exist.")
    exit()
selected_cctv_url = cctv_lists[selected_cctv].split(',')[3][2:-3]
selected_cctv_video_url = cctv_lists_video[selected_cctv].split(',')[3][2:-3]
print(f"selected cctv: {selected_cctv_name}")
gts.get_traffic_status(selected_cctv_url)
ov.open_video(selected_cctv_video_url)