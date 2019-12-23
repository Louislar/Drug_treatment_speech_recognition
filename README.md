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

## 2019/12/01
- 執行成功
- 成功圖片：![img03](https://raw.githubusercontent.com/Louislar/Drug_treatment_speech_recognition/master/Screenshot%20from%202019-12-01%2017-48-48.png)
- 完成使用python執行的程式了
- 注意： lm跟dic檔案格式要改成跟原本的一樣才能正常預測。不能直接用網站上轉好的。


## 2019/12/03
- 嘗試將python部份轉成exe可執行檔，用pyinstaller，再到windows上新開process call，傳輸部份用socket取代讀寫檔案I/O。


## 2019/12/10

- 發現python 2.7無法順利包裝成exe，所以改用socket連線送。
- 目前順利寫出可連線的socket（python2.7），檔案為/home/wmlab/Downloads/Socket_programming/python-TCP/TCP-server-python27.py
- 剩下在ubuntu的工作為將辨識的python碼與tcp的python碼結合。
- 目前已經完成5樓連線測試
- 接下來的任務為，整合server的python code讓他能夠，接到unity端的確認tcp後，回傳辨識結果。


## 2019/12/23

- 解決了之前編譯成exe後會報錯的問題。
- 問題描述：直接使用pyinstaller編譯完後，在ubuntu上用以下方式在command line上執行會報錯
```
./pythonspeechrecog
```
- 錯誤碼：
```
ImportError: /tmp/_MEIIG7r7r/pocketsphinx.so: cannot open shared object file: No such file or directory
[12438] Failed to execute script speechrecogserver
```
- 參考網站：
- 1. https://blog.xuite.net/o1o1o1o1o/blog/396404852-Pyinstaller%E5%B0%87python%E7%A8%8B%E5%BC%8F%E6%89%93%E5%8C%85%E7%82%BA%E4%B8%80%E5%80%8B%E5%8F%AF%E5%9F%B7%E8%A1%8C%E6%AA%94
- (狀況D：Runtime執行時少了某library)
- 2. https://stackoverflow.com/questions/49085970/no-such-file-or-directory-error-using-pyinstaller-and-scrapy
- 3. https://pythonhosted.org/PyInstaller/spec-files.html

- 缺少的兩個.so檔案，從原本下載的安裝包找，直接搜尋名子找會比較快(sphinxpocket.so, sphinxbase.so) 

- 解法：依照參考網站1的方式修改.spec檔案，注意！一定要依照參考網站3的格式做修改。