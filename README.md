# -cps
# chatGpt学习程序自动处理视频
今日结合chatGpt,写出方便视频操作的程序,对不懂的参数重复询问chatGpt
通过对具体参数的不停调试,完成了对视频字幕遮罩的自动处理.
 * 创建遮罩图像 blurSubtitles.py
         cv2.fillPoly(mask, [np.array([[40, 1260], [1000, 1260], [1000, 1360], [40, 1360]], np.int32)], (255, 255, 0))
