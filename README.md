## 短剧cps
## chatGpt调试程序实现自动化工作
` 对一个需求的描述尽量简洁,单一, 可以通过对一个复杂需求的拆解、组合,快速实现部分需求的完成.然后在一个简单版本之上完善,避免时间过多浪费在不懂且容易掉坑的地方.也就是不去有坑的地方.保持每个动作尽量有效,不做无用功. `
##  反思
+ 用chatGpt生产代码,做到加水印和遮挡字幕.
- 字幕遮挡生成的视频很模糊.
- 发现加水印视频不会模糊,通过对比找出两者的差异,然后粘贴**差异的代码问chatGpt解决方法**,之后了解到应该使用加权平均算法,接着让chatGpt修改原来的加法为加权平均算法的代码,替换了这部分,程序执行得到了清晰的结果,问题解决. 

### 今日结合chatGpt,写出方便视频操作的程序,对不懂的参数重复询问chatGpt,通过对具体参数的不停调试,完成了对视频字幕遮罩的自动处理.
 >* 创建遮罩图像 blurSubtitles.py
 >        cv2.fillPoly(mask, [np.array([[40, 1260], [1000, 1260], [1000, 1360], [40, 1360]], np.int32)], (255, 255, 0))


The background color is `#ffffff` for light mode and `#000000` for dark mode.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
</picture>

1. James Madison
2. James Monroe
3. John Quincy Adam


1. First list item
   - First nested list item
     - Second nested list item

