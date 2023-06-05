import os

def batch_cut_videos(video_folder, output_folder, start_time, end_time):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历视频文件夹中的所有视频文件
    for filename in os.listdir(video_folder):
        # 检查文件扩展名是否为视频格式
        if filename.endswith((".mp4", ".avi", ".mkv")):
            # 构造输入和输出路径
            input_path = os.path.join(video_folder, filename)
            output_path = os.path.join(output_folder, f"cut_{filename}")

            # 构造FFmpeg命令
            command = f'ffmpeg -ss {start_time} -i "{input_path}" -to {end_time} -c copy -y "{output_path}"'

            # 执行FFmpeg命令
            os.system(command)
    # 构造文件列表
    file_list_path = os.path.join(output_folder, "file.txt")
    with open(file_list_path, "w") as file:
        for filename in os.listdir(output_folder):
            if filename.startswith("cut_"):
                file.write(f"file '{filename}'\n")
                
    #构造FFmpeg命令
                
    merge_command = f'ffmpeg -f concat -i "{file_list_path}" -c copy -y output.mp4'

    # 执行FFmpeg命令
    os.system(merge_command)
    
    compression_command = f'ffmpeg -y -i output.mp4 -c:a copy -c:v libx264 -profile:v high -r 30 -crf 18 -s 608x1080 -movflags +faststart 123123.mp4'
    os.system(compression_command)
    print("视频批量剪辑完成")

"""
# 示例用法
video_folder = "videos"
output_folder = "output"
start_time = "00:00:00"
end_time = "00:00:05"
batch_cut_videos(video_folder, output_folder, start_time, end_time)
"""
