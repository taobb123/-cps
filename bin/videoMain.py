# videoMain.py
import subprocess
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
from clipandMerge import clip_and_merge_videos
from addWatermark import add_watermark_effects
from blurSubtitles import blur_subtitles

def main():
	#切割合并素材
    clipList = ['EP01.mp4','EP02.mp4','EP03.mp4']
    start = 3
    end = 42               
    clip_and_merge_videos(clipList, 'input.mp4', start, end)

	
    # 水印
    text = "Hello Taobb!" 
    org = (50, 250)  # 水印的起始位置坐标
    #剪辑完成的视频
    input_video = 'input.mp4'
    #添加水印
    add_watermark_effects(input_video, 'temp.mp4', text, org)
    
    #遮挡字幕
    outVideo = 'complete_output.mp4'
    blur_subtitles('temp.mp4', outVideo) 
    
    

if __name__ == "__main__":
    main()
