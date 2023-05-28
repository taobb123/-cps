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

def main(clip_list, start, end, output_video, text, org):
    
	#切割合并素材            
    clip_and_merge_videos(clip_list, output_video, start, end)
    
    #保存音频
    merged_audio = "merged_audio.mp3"
    video = VideoFileClip(output_video)
    audio = video.audio
    audio.write_audiofile(merged_audio, codec='mp3')    
   
    # 水印
    # 水印的起始位置坐标
    #剪辑完成的视频
    #添加水印
    add_watermark_effects(output_video, 'water.mp4', text, org)
       
    """
    #合成音频视频
    blur_video = VideoFileClip('water.mp4')
    merged_video = "merged_video.mp4"
    audio_clip = AudioFileClip(merged_audio)
    combined_video = blur_video.set_audio(audio_clip)
    combined_video.write_videofile(merged_video)
    """
    
    #添加滤镜
    add_filter('water.mp4','output_filter_video.mp4')
														
if __name__ == "__main__":

    start_time = time.time()
    #设置参数
    clip_list = ['2.mp4','3.mp4', '6.mp4','8.mp4','14.mp4','15.mp4']
    #clip_list = ['2.mp4','3.mp4']
    start = 0
    end = 38
    output_video = 'input.mp4'
    text = 'Taobb'
    org = (10,20)
    
    #运行
    main(clip_list, start, end, output_video, text, org)
    
    #运行时长
    end_time = time.time()
    runtime = end_time - start_time
    print("程序运行时间:{:.2f}秒".format(runtime))
    
