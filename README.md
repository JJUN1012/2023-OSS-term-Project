Show Me The Highway
===================
This is a mini project with OpenCV.

### Main Goal
+ Get API of National Transport Information Center's CCTV info.
    + API Manual  
    https://www.its.go.kr/opendata/
+ Analyze the number of vehicles in CCTV videos using OpenCV
+ Transmit the analyzed inforamtion to a mobile app and visualize both the video stream and density of detected vehicles.

### How to use?
If you want to use these program, you have to make a api key txt file.  
You need to apply for the CCTV image API. You can get API from [here](https://www.its.go.kr/user/issueAuthKey?service=OPD_00000003)  
You also can use just 'test' instead real API key for testing.

<details>
<summary>How to apply API?</summary>
You can get API with entering the purpose, usage, desired services.
<img src="images/api_tutorial_1.png" alt="Check the CCTV image">

Purpose options
<img src="images/api_tutorial_2.png" alt="Purpose options">
</details>

Then make a "apiKey.txt" file in datafiles folder, and paste the api key in the text file.