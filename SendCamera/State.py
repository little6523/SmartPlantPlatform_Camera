import cv2
import math

def get_color(file_name) :
    img = cv2.imread(file_name) # 이미지 전처리(배경제거)된 이미지 호출
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    pixel_cnt = [0, 0, 0] # [Good, Not Bad, Bad] pixel loop counter

# https://manuscriptlink-society-file.s3-ap-northeast-1.amazonaws.com/kics/conference/koreaai2021/presentation/G-3-2.pdf => 경계값 참고

    for row in img_hsv :
        for pixel in row : # 순서대로 초록색 계열, 노란색 계열 추출, 갈색 계열(h : 0~179)
            if (pixel[0] >= 34 and pixel[0] <= 91) and (pixel[1] >= 50 and pixel[1] <= 255) and (pixel[2] >= 60 and pixel[2] <= 255) :
                pixel_cnt[0] += 1

            elif (pixel[0] >= 21 and pixel[0] <= 33) and (pixel[1] >= 50 and pixel[1] <= 255) and (pixel[2] >= 50 and pixel[2] <= 255) :
                pixel_cnt[1] += 1

#            elif (pixel[0] >= 170 or pixel[0] <= 5) and (pixel[1] >= 20 and pixel[1] <= 255) and (pixel[2] >= 20 and pixel[2] <= 255) :
            elif (pixel[0] >= 4 and pixel[0] <= 20) and (pixel[2] <= 140) :
                pixel_cnt[2] += 1

    print(pixel_cnt)

    return pixel_cnt

def get_state(file_name) :
    # pixel_cnt = get_color(file_name)
    pixel_cnt = get_color("dying_plant2.jpg")
    max_color = max(pixel_cnt)
    avg_color = pixel_cnt.index(max_color)

    if avg_color == 0 :
        plant_state = "Good"
    elif avg_color == 1 :
        plant_state = "Not Bad"
    else :
        plant_state = "Bad"

    return plant_state, avg_color