from moviepy.editor import *
import os


import douyin



#   douyin.get_url("https://aweme.snssdk.com/aweme/v1/hotsearch/aweme/billboard/")
# 定义一个数组
L = []


time =0
# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk("./video"):
    # 按文件名排序
    files.sort()
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            video = VideoFileClip(filePath)
            video=video.set_start(time).crossfadein(1)
            time =time + int(video.duration)
            video=video.set_pos("center")
            # 添加到数组
            L.append(video)
            
        if os.path.splitext(file)[1] == '.mkv':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            video = VideoFileClip(filePath)
            video=video.set_start(0).crossfadein(1)
            video=video.set_pos("center")
            time= int(video.duration)
            # 添加到数组
            L.append(video)


# 拼接视频
final_clip = CompositeVideoClip(L)

# 生成目标视频文件
final_clip.to_videofile("./target.mp4", fps=24, remove_temp=False)