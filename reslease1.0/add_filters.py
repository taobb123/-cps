from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from moviepy.video.fx import all as vfx

def add_filter(input_video_path, output_video_path):
    # 加载视频剪辑
    #合成音频视频
    video_clip = VideoFileClip(input_video_path)
    filtered_clip = vfx.colorx(video_clip, factor=0.8)
    audio_clip = AudioFileClip("merged_audio.mp3")
    combined_video = filtered_clip.set_audio(audio_clip)
    combined_video.write_videofile(output_video_path)    

    # 应用滤镜效果
    #filtered_clip = vfx.colorx(video_clip, factor=0.8)  # 将滤镜效果的因子设置为0.5

    # 保存处理后的视频剪辑
    #filtered_clip.write_videofile(output_video_path)

    print('添加滤镜执行结束!')
    
    
