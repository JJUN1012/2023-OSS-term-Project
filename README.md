# Show Me The Highway

This is a mini project leveraging OpenCV for real-time analysis of highway traffic conditions using data provided by the National Transport Information Center.

## Main Goal

+ Retrieve API data from the National Transport Information Center's CCTV system.
    + [API Manual](https://www.its.go.kr/opendata/)
+ Analyze the number of vehicles in CCTV videos using OpenCV.
+ Transmit the analyzed information to a mobile app and visualize both the video stream and density of detected vehicles.

## How to Use

If you wish to use this program, you must obtain an API key. Follow these steps to apply for the CCTV image API key [here](https://www.its.go.kr/user/issueAuthKey?service=OPD_00000003).

You can also use 'test' as a placeholder for the API key during testing.

<details>
<summary>How to Apply for API?</summary>

You can obtain the API key by specifying the purpose, usage, and desired services.

![Check the CCTV image](images/api_tutorial_1.png)

**Purpose Options:**
![Purpose options](images/api_tutorial_2.png)
</details>

After obtaining the API key, create an "apiKey.txt" file in the `datafiles` folder and paste the API key into the text file.

## Project Details

Our project aims to enhance the convenience of accessing real-time highway traffic information provided by the Korea Expressway Corporation. By obtaining free data on highway conditions through an approved API key, we use OpenCV to analyze images from CCTV cameras placed along the highways. The program then provides user-friendly responses such as "Currently experiencing highway congestion" or "Traffic is smooth, proceed at a moderate speed."

Feel free to contribute to the project or use the code for your own applications!
