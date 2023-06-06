import os
import subprocess

def merge_videos(input_folder, output_file):
    # 获取输入文件夹中的视频文件列表
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    # 生成要合并的视频文件列表文件
    list_file = 'filelist.txt'
    with open(list_file, 'w') as f:
        for video_file in video_files:
            file_path = os.path.join(input_folder, video_file)
            f.write(f"file '{file_path}'\n")

    # 执行合并操作
    command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', list_file,
        '-c', 'copy',
        output_file
    ]
    subprocess.run(command)

    # 删除临时生成的文件列表文件
    os.remove(list_file)

# 调用函数进行视频合并
merge_videos('output', 'merged.mp4')
