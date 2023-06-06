import subprocess

def compress_video(input_file, output_file, crf=28):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',
        '-crf', str(crf),
        '-preset', 'medium',
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(command)

# 调用函数进行视频压缩
compress_video('merged.mp4', 'compressed.mp4', crf=28)
