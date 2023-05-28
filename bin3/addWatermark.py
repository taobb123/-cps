#addWartemark.py

import cv2
import time
from moviepy.editor import *

def add_watermark_effects(input_video_path, output_video_path, watermark_text, org_text):
    # 打开视频文件
    video_capture = cv2.VideoCapture(input_video_path)

    # 获取视频的基本信息
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # 创建视频写入对象
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

    # 循环读取视频帧并添加水印和特效
    while video_capture.isOpened():
        ret, frame = video_capture.read()

        if not ret:
            break

        # 添加水印文本
        cv2.putText(frame, watermark_text, org_text, cv2.FONT_HERSHEY_SIMPLEX, 1, (173, 216, 230), 2, cv2.LINE_AA)

        # 添加特效（这里只是示例，你可以根据需要进行修改）
        #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        inverted_frame = cv2.bitwise_not(gray_frame)
        
        #frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        #frame = cv2.cvtColor( gray_frame, cv2.COLOR_HSV2BGR)
        frame = cv2.cvtColor( gray_frame, cv2.COLOR_LAB2BGR)
        

        # 写入处理后的帧到输出视频文件
        video_writer.write(frame)
    # 释放资源
    video_capture.release()
    video_writer.release()
 
"""   
text = "Taobb" 
org = (10, 20)  # 水印的起始位置坐标
starttime = time.time()

add_watermark_effects('s.mp4', 'output.mp4', text, org)
endtime = time.time()
clip = VideoFileClip("output.mp4")
clip.save_frame("f.jpeg")
runtime = endtime - starttime
print("程序运行时间:{:.2f}".format(runtime))
"""
