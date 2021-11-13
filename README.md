# Defect-Detection

## Introduction

Automated optical inspection (AOI) [1] is an automated visual inspection of printed circuit board (PCB) (or LCD,transistor) manufacture where a camera autonomously scans the device under test for both catastrophic failure (e.g. missing component) and quality defects (e.g. fillet size or shape or component skew). It is commonly used in the manufacturing process because it is a non-contact test method. It is implemented at many stages through the manufacturing process including bare board inspection, solder paste inspection (SPI), pre-reflow and post-reflow as well as other stages. The Institute of Electronics and Optoelectronics in Industrial Technology Research Institute(ITRI) has spent years on developing flexible displays, hoping to elevate the production quality with AOI technology during the pilot run. This time we have invited experts from different fields to join us, and focus on identifying defect classifications of AOI image data that are offered so as to elevate the identification efficiency of AOI through statistical science

## Evaluation Criteria

After classification models of defect prediction are offered by researchers participating in the issue, the back-end of the system would process them in bathces regularly to calculate the score. Evaluations are conducted by calculating the corresponding accuracy rate of the actual value.

![image](https://github.com/liam0504/Defect-Detection/blob/main/1636790981720.jpg)

## Goal
參與AIdea網站的AOI自動光學檢測競賽


## 使用方式
1.	至AIdea網站下載訓練用資料 [link](https://aidea-web.tw/topic/a49e3f76-69c9-4a4a-bcfc-c882840b3f27)

2.	資料集整理
    *  至train_images資料夾內，新增三個資料夾test、train、valid，並在此三個資料夾內分別新增名字為0、1、2、3、4、5的資料夾
    * 執行 `python initial.py` 將圖片按照7:1.5:1.5的比例分配至test、train、valid三個資料夾內，並且按照圖片的分類放置0、1、2、3、4、5的資料夾內

3.	程式執行
執行 `python final.py`，來運行模型訓練，最終會印出使用train_images/test內測試資料進行測試的結果，倘若結果不錯可使用下一步驟產生AIdea需要的csv檔案上傳評分。

4.	輸出AIdea要求的csv檔
執行 `python predict.py`，除了再次印出使用測試資料進行測試的結果外，也會在資料夾內產生output.csv的檔案，倘若此檔已存在即立刻複寫。
