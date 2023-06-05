from clip_merge_compression import batch_cut_videos
from addWatermark import add_watermark_effects
import time 

def main(video_folder, output_folder, start, end, text, org):    
	#切割素材            
    batch_cut_videos(video_folder, output_folder, start, end)
    
    #音频分离 
    #添加水印
    #合并音频
    add_watermark_effects('123123.mp4', 'watermark_output.mp4', text, org)
       
    
														
if __name__ == "__main__":

    start_time = time.time()
    video_folder = 'videos'
    output_folder = 'output'
    star = 0
    end = 5
    text = 'Taobb'
    org = (10,20)
    
    #运行
    main(video_folder, output_folder, star, end, text, org)
    
    #运行时长
    end_time = time.time()
    runtime = (end_time - start_time)/60
    print("程序运行时间:{:.2f}分".format(runtime))
    
