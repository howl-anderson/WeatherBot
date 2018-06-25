# WeatherBot

## 依赖
### python 版本
python 3

### python 依赖
```console
pip install requirements.txt
```

## 下载数据和模型
* `data/total_word_feature_extractor.dat`: 从 [https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz) 下载，解压缩后放置到对应位置
* `models/default/current`：通过运行 `train_NLU.bash` 生成
* `models/dialogue`：通过运行 `train_CORE.bash` 生成
