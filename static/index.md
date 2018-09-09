# Demo for 天气预报查询机器人

## 源代码地址
https://github.com/howl-anderson/WeatherBot

## 功能
这个机器人可以根据你提供的城市（北京、上海等）和日期（明天、后天等），查询出相应的天气预报。

## 特性
使用 Frame-based 对话管理方案，如果上述两个 Slot (既城市和天气)，有任意一个用户未提供，对话管理系统会负责让你澄清相关 Slot 的值。

## 能力范围
* 受限于天气数据提供方的能力，这个机器人只能查询 **中国大陆地区市级城市** 三天以内 **（今天，明天，后天）** 的气象数据，**不能查询过去**（昨天，前天）等历史数据。
* 受限于开发时间，这个机器人 **不提供** 诸如 **这个星期五、下个星期一** 这种需要计算才能得到日期给定方式。也 **不能提供** 诸如 **绝对日期：三月一号、六一儿童节日** 这种日期的查询能力。
* 因为使用的是免费的天气查询接口，所以 **会有配额限制**，可能会因为 **超出调用次数** ，而在一个小时内不能用。同时网络查询接口可能存在不稳定因素，导致 **没有结果返回或者出现异常**，**尝试多次重新发送请求可解决问题**。

## 在线演示
见页面右下方的聊天widget ![chat_button](chat_button.png)，点击即可使用

## 作者

Xiaoquan Kong @ https://github.com/howl-anderson

## Copyrights

<div>Robot icon in web-chat interface made by <a href="https://www.flaticon.com/authors/good-ware" title="Robotic">Robotic</a> from <a href="https://www.flaticon.com/"     title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/"     title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
