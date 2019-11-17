# 戒毒語音辨識-使用CMU Sphinx
- 參考教學：https://github.com/orochiZhang/CMUsphinx-Demo

## 2019/11/11
- 使用python版本： 2.7
- 情況：安裝Sphinx base
- 遇到報錯：![image](https://raw.githubusercontent.com/Louislar/Drug_treatment_speech_recognition/master/Screenshot%20from%202019-11-11%2016-43-52.png)
- 解釋：ubuntu預設內部就有一個python2.7，圖片上的路徑是ubuntu內部的python2.7的路徑，但是我現在執行的python是anaconda上的，所以必須將Sphinx-base安裝到anaconda裡的那個python
- 參考：
    - 要改路徑：https://stackoverflow.com/questions/14983730/installing-setuptools-with-root-getting-a-pythonpath-error
    - 找到anacond那個env的路徑：https://www.zhihu.com/question/41974592
    - Sphinx base的configure command要加入--prefix指令：https://github.com/cmusphinx/sphinxbase
- 解法：輸入指令：./configure --prefix=/home/wmlab/.conda/envs/python27_CMUSphinx
- 注意：每次改configure，都要輸入一次make clean，再make會比較不會報錯。

## 2019/11/11_2
- 情況：安裝pocketsphinx
- 作法：按照教學做，但是兩行export函數改成：
```
 export LD_LIBRARY_PATH=/home/wmlab/.conda/envs/python27_CMUSphinx/lib
 export PKG_CONFIG_PATH=/home/wmlab/.conda/envs/python27_CMUSphinx/lib/pkgconfig
```
- 補充解釋：教學文裡面提的/usr/local/bin，在我這邊因為用anaconda，所以改成/home/wmlab/.conda/envs/python27_CMUSphinx/bin

## 2019/11/11_3
- 目前尚未解決的報錯
- 發生情況：輸入指令：
```
./pocketsphinx_continuous -hmm /home/wmlab/CMU_try/cmusphinx-zh-cn-5.2 -lm /home/wmlab/CMU_try/CMUsphinx-Demo-master/0506.lm -dict /home/wmlab/CMU_try/CMUsphinx-Demo-master/0506.dic
```
- 問題圖片：![img02](https://raw.githubusercontent.com/Louislar/Drug_treatment_speech_recognition/master/Screenshot%20from%202019-11-11%2019-26-41.png)

## 2019/11/17
- 確認使用英文辨識指令可以運作（有接麥克風的情況下）
- 指令：
```
./pocketsphinx_continuous
```