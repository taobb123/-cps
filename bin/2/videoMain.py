# videoMain.py
import subprocess
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from clipandMerge import clip_and_merge_videos
from addWatermark import add_watermark_effects
from blurSubtitles import blur_subtitles
import time 

def main():
    
	#切割合并素材
    clipList = ['EP1.mp4','EP2.mp4','EP3.mp4','EP4.mp4','EP5.mp4']
    start = 45
    end = 90
    input_video = "input.mp4"               
    clip_and_merge_videos(clipList, input_video, start, end)
    
    #保存音频
    input_video = "input.mp4"
    merged_audio = "merged_audio.mp3"
    video = VideoFileClip(input_video)
    audio = video.audio
    audio.write_audiofile(merged_audio, codec='mp3')    
   
    # 水印
    text = "Taobb" 
    org = (10, 20)  # 水印的起始位置坐标
    #剪辑完成的视频
    #添加水印
    add_watermark_effects(input_video, 'water.mp4', text, org)
    
    #遮挡字幕
    blur_video = 'blur_output.mp4'
    blur_subtitles('water.mp4', blur_video)    
    
    #合成音频视频
    blur_video = VideoFileClip(blur_video)
    merged_video = "merged_video.mp4"
    audio_clip = AudioFileClip(merged_audio)
    combined_video = blur_video.set_audio(audio_clip)
    combined_video.write_videofile(merged_video)
														

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    runtime = end_time - start_time
    print("程序运行时间:{:.2f}秒".format(runtime))
    
