# Defect-Detection

## Introduction

Automated optical inspection (AOI) [1] is an automated visual inspection of printed circuit board (PCB) (or LCD,transistor) manufacture where a camera autonomously scans the device under test for both catastrophic failure (e.g. missing component) and quality defects (e.g. fillet size or shape or component skew). It is commonly used in the manufacturing process because it is a non-contact test method. It is implemented at many stages through the manufacturing process including bare board inspection, solder paste inspection (SPI), pre-reflow and post-reflow as well as other stages. The Institute of Electronics and Optoelectronics in Industrial Technology Research Institute(ITRI) has spent years on developing flexible displays, hoping to elevate the production quality with AOI technology during the pilot run. This time we have invited experts from different fields to join us, and focus on identifying defect classifications of AOI image data that are offered so as to elevate the identification efficiency of AOI through statistical science

## Evaluation Criteria

After classification models of defect prediction are offered by researchers participating in the issue, the back-end of the system would process them in bathces regularly to calculate the score. Evaluations are conducted by calculating the corresponding accuracy rate of the actual value.

![image](https://github.com/liam0504/Defect-Detection/blob/main/1636790981720.jpg)

## Data description
There are six categories included in image data that the issue offers (1 normal category + 5 defect categories)

The download data file (aoi_data.zip) includes:

- train_images.zip: image data for training (PNG format), 2,528 images in total.
- train.csv: includes 2 columns, ID and Label.
   - ID: the image filename
   - Label: defect classification category (0: normal, 1: void, 2: horizontal defect, 3: vertical defect, 4: edge defect, 5: particle)
- test_images.zip: image data for testing (PNG format), 10,142 images in total.
- test.csv: includes 2 columns, ID and Label.
   - ID: the image filename
   - Label: defect classification category (the value can be only one of the following numbers: 0, 1, 2, 3, 4, 5)


## Usage

1.	Download the training and test data from AOI website [link](https://aidea-web.tw/topic/a49e3f76-69c9-4a4a-bcfc-c882840b3f27)

2.	Run the sort.py to distribute the images into five files.

3. Implement the train.py to train the model.

4. Run the predict.py to present the outcome.

## Achievement


