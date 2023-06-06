import os
import subprocess

def split_videos(input_folder, output_folder, start_time, duration):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 获取输入文件夹中的视频文件列表
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    for video_file in video_files:
        input_file = os.path.join(input_folder, video_file)
        output_file = os.path.join(output_folder, video_file)

        # 切割视频
        command = [
            'ffmpeg',
            '-i', input_file,
            '-ss', start_time,
            '-t', duration,
            '-c', 'copy',
            output_file
        ]
        subprocess.run(command)

# 调用函数进行批量视频切割
split_videos('videos', 'output', '00:00:05', '00:00:10')
