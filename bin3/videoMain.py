# videoMain.py
import subprocess
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from clipandMerge import clip_and_merge_videos
from addWatermark import add_watermark_effects
from blurSubtitles import blur_subtitles
from add_filters import add_filter
import time 

def main(clip_list, start, end, input_video, text, org, blur_video, output_video):
    
	#切割合并素材            
    clip_and_merge_videos(clip_list, input_video, start, end)
    
    #保存音频
    merged_audio = "merged_audio_2.mp3"
    video = VideoFileClip(input_video)
    audio = video.audio
    audio.write_audiofile(merged_audio, codec='mp3')    
   
    # 水印
    # 水印的起始位置坐标
    #剪辑完成的视频
    #添加水印
    add_watermark_effects(input_video, 'water_2.mp4', text, org)
    
    #遮挡字幕
    blur_subtitles('water_2.mp4', blur_video)    
    
    #合成音频视频
    blur_video = VideoFileClip(blur_video)
    merged_video = "merged_video_2.mp4"
    audio_clip = AudioFileClip(merged_audio)
    combined_video = blur_video.set_audio(audio_clip)
    combined_video.write_videofile(merged_video)
    
    #添加滤镜
    add_filter('blur_output_video.mp4',output_video)
														
if __name__ == "__main__":

    start_time = time.time()
    #设置参数
    clip_list = ['3.mp4', '5.mp4']
    start = 3
    end = 4
    input_video = 'input.mp4'
    text = 'Taobb'
    org = (10,20)
    blur_video = 'blur_output_video.mp4'
    output_video = 'output_filtered_video.mp4'
    
    #运行
    main(clip_list, start, end, input_video, text, org, blur_video, output_video)
    
    #运行时长
    end_time = time.time()
    runtime = end_time - start_time
    print("程序运行时间:{:.2f}秒".format(runtime))
    
