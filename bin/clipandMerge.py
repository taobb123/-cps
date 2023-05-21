from moviepy.editor import VideoFileClip, concatenate_videoclips

def clip_and_merge_videos(video_paths, output_path, start_time, end_time):
    # 创建一个空的视频剪辑列表
    clips = []

    # 逐个打开并剪辑视频
    for path in video_paths:
        clip = VideoFileClip(path).subclip(start_time, end_time)
        clips.append(clip)

    # 将所有视频剪辑合并为一个
    final_clip = concatenate_videoclips(clips)

    # 保存最终视频剪辑为输出文件
    final_clip.write_videofile(output_path)

    # 释放资源
    final_clip.close()

clipList = ['EP01.mp4',
            'EP02.mp4',
            'EP03.mp4']
start = 3
end = 42

#clip_and_merge_videos(clipList, 'output.mp4', start, end)
