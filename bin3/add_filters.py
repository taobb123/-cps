from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx

def add_filter(input_video_path, output_video_path):
    # 加载视频剪辑
    video_clip = VideoFileClip(input_video_path)

    # 应用滤镜效果
    filtered_clip = vfx.colorx(video_clip, factor=0.7)  # 将滤镜效果的因子设置为0.5

    # 保存处理后的视频剪辑
    filtered_clip.write_videofile(output_video_path)

    print('添加滤镜执行结束!')
    
    
