import cv2
import numpy as np

def blur_subtitles(input_video_path, output_video_path):
    # 打开视频文件
    video_capture = cv2.VideoCapture(input_video_path)

    # 获取视频的基本信息
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # 创建视频写入对象
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

    # 循环读取视频帧并进行处理
    while video_capture.isOpened():
        ret, frame = video_capture.read()

        if not ret:
            break

        # 创建遮罩图像
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
       # cv2.fillPoly(mask, [np.array(subtitle_coordinates, dtype=np.int32)], (255, 255, 0))
        cv2.fillPoly(mask, [np.array([[40, 1260], [1000, 1260], [1000, 1360], [40, 1360]], dtype=np.int32)], (255, 255, 0))

        # 对遮罩区域进行模糊处理
        blurred_frame = cv2.GaussianBlur(frame, (33, 33), 0)
        frame = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
        alpha = 0.4  # 加权平均的权重
        # 将帧转换为浮点型，以便进行加权平均操作
        frame = frame.astype(float)
        blurred_frame = blurred_frame.astype(float)
        # 对帧进行加权平均
        weighted_frame = cv2.addWeighted(frame, 1 - alpha, blurred_frame, alpha, 0.0)
        # 将加权平均后的帧转换回整数类型
        frame = weighted_frame.astype(np.uint8)
        
       

        # 写入处理后的帧到输出视频文件
        video_writer.write(frame)

    # 释放资源
    video_capture.release()
    video_writer.release()
    print('finish!')
    
#blur_subtitles('input.mp4', 'blurf_output.mp4')
