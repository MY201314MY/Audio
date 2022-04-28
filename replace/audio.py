import sys
import json
import requests

TEXT = "欢迎使用百度语音合成"

# 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
# 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美
PER = 0
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 9
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 6

FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[6]

CUID = "123456PYTHON"

TTS_URL = 'http://tsn.baidu.com/text2audio'

if __name__ == '__main__':
    params = {'tok': "24.a671539d2032634324957a49f5c889b5.2592000.1652335174.282335-15876292",
              'tex': TEXT, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE,
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

    result = requests.get(url=TTS_URL, params=params)

    print(result.headers)

    with open("m.wav", 'wb') as of:
        of.write(result.content)

    print("music saved")