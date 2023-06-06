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
            '-c', 'copy','-y',
            output_file
        ]
        subprocess.run(command)

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
        '-c', 'copy','-y',
        output_file
    ]
    subprocess.run(command)

    # 删除临时生成的文件列表文件
    os.remove(list_file)

def compress_video(input_file, output_file, crf=28):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',
        '-crf', str(crf),
        '-preset', 'medium',
        '-c:a', 'copy','-y',
        output_file
    ]
    subprocess.run(command)
    
import subprocess

def add_text_watermark(input_file, output_file, text):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f"drawtext=text='{text}':x=10:y=10:fontsize=24:fontcolor=gray",
        '-c:a', 'copy','-y',
        output_file
    ]
    subprocess.run(command)

def main():
    input_folder = 'videos'
    output_folder = 'output'
    start_time = '00:00:03'
    duration = '00:00:35'
    merged_file = 'merged.mp4'
    compressed_file = 'compressed.mp4'

    # 切割视频
    split_videos(input_folder, output_folder, start_time, duration)

    # 合并视频
    merge_videos(output_folder, merged_file)

    # 压缩视频
    compress_video(merged_file, compressed_file)
    
    # 调用函数为压缩后的视频添加文字水印
    add_text_watermark('compressed.mp4', 'watermarked.mp4', 'Taobb')

# 调用主函数
main()
