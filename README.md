# 长江雨课堂自动刷课脚本

该脚本使用Selenium自动完成长江雨课堂平台上的课程。它会导航到指定的课程页面，互动视频元素，并以两倍速播放视频来标记它们为已完成。

## 先决条件

在运行脚本之前，请确保已安装以下内容：

- Python 3.x
- 安装依赖（使用`pip install -r requirements.txt`安装）
- 用于您的首选浏览器的WebDriver（例如，Google Chrome的ChromeDriver）

## 配置

1. **课程URL:** 更新`url`变量为您要自动完成的具体课程页面URL：

   ```python
   url = "https://changjiang.yuketang.cn/v2/web/studentLog/16978956"
   ```

2. **Cookie:** 更新`cookie`字典为您的会话ID或其他必要的身份验证Cookie：

   ```python
   cookie = {'name': 'sessionid', 'value': 'catf5tpoi584n5k57ipgkcswn0nty4z'}
   ```

3. **并发数:** 更新`concurrent`变量为您想要处理的并发窗口数：

   ```python
   concurrent = 5
   ```

## 使用方法

1. **WebDriver设置:** 确保您拥有所选浏览器的WebDriver。例如，从ChromeDriver下载适用于Google Chrome的ChromeDriver，并将其放在系统的PATH中包含的目录中。

2. **运行脚本:** 使用Python执行脚本：

   ```shell
   python yuketang_auto_script.py
   ```

## 脚本功能

1. **初始化:**
   - 脚本初始化Selenium WebDriver并设置等待时间为10秒。
   - 打开指定的课程URL并添加身份验证Cookie。
2. **导航到课程页面:**
   - 脚本等待"成绩单"元素出现并点击它。
   - 然后它等待视频元素加载并获取页面上的所有视频元素。
3. **处理视频:**
   - 脚本遍历视频列表。
   - 对于每个未标记为"已完成 详情"的视频，它在新窗口中打开视频。
   - 静音视频，将播放速度设置为两倍速，并开始播放视频。
   - 脚本确保打开的窗口数不超过指定的并发数。
4. **完成:**
   - 脚本等待所有视频窗口关闭后再退出。

## 注意事项

- **浏览器兼容性:** 该脚本使用`webdriver.Chrome()`，但您可以通过更改WebDriver初始化来使用其他浏览器。
- **错误处理:** 确保脚本能够优雅地处理意外错误，例如网络问题或网站结构的变化。
- **法律和道德考虑:** 负责任地使用此脚本，并确保其符合雨课堂平台的服务条款。对网站的自动化交互应始终在道德和法律范围内进行。

## 许可证

该项目根据MIT许可证授权。有关详细信息，请参阅LICENSE文件。