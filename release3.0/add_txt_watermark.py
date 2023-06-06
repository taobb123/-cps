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

# 调用函数为压缩后的视频添加文字水印
add_text_watermark('compressed.mp4', 'watermarked.mp4', 'Taobb')
