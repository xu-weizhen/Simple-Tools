# PDF工具
用于对PDF文档进行分割、将PDF转换为文字、将PDF转换为图片和识别图片中的文字  

## 界面
<img width=353px height=300px src="https://github.com/xu-weizhen/Simple-Tools/blob/master/PDF-Tool/%E7%A4%BA%E4%BE%8B%E5%9B%BE%E7%89%87/%E7%A8%8B%E5%BA%8F%E7%95%8C%E9%9D%A2.jpg?raw=true" alt="程序界面" align=center />  
  
## 依赖  
PyQt5 >= 5.11.3  
PyPDF2 >= 1.26.0  
baidu-aip >= 2.1.0.0 
Pillow >= 5.3.0  
requests >= 2.22.0  
  
### 安装
pip install PyQt5  
pip install PyPDF2   
pip install baidu-aip  
pip install Pillow  
pip install requests  

## 说明
本程序只适用于Windows系统。程序生成的文件默认保存在与程序相同的路径之下，为了方便查找文件，建议为程序建立一个文件夹并将程序放入文件夹中。对于文字识别的秘钥，为方便下次使用，默认以明文方式存放在`key.dat`文件中，如有需要可在代码83行修改文件文件名及路径，亦可在每次使用后手动删除这一文件。  
  
## 操作说明
首先选择需要操作的PDF文档。选择文档后，选择页码框默认选择PDF文档的全部页面。  
  
通过`选择页码框`可输入需要进行操作的页面，输入只接受数字、“，”和“-”。通过“，”分隔多组输入，通过“-”选择多个页面，其中“-”左侧的数字应小于右侧的数字，输入中不要包含空格，例如：  
+ 1,2,3  
+ 1-5,8,9  
+ 1,3-5,7,9-12  
+ 1,2,3,3,2  
  
  
点击`分割PDF`，将**按照输入的页码顺序**，从原文档中分割出相应页面并生成新文档，生成的文档保存在当前程序所在路径下。 
  
  
点击`PDF转文字`，将**按照输入的页码顺序**，从原文档中相应页面提取文字并保存在文档中，生成的文档保存在当前程序所在路径下。  
  
  
点击`图片文件夹`，将打开保存图片的文件夹。若该文件夹不存在，则将参加这一文件夹并打开。  
  
  
点击`图片转文字`，对图片文件夹中的图片中的文字进行识别，识别结果保存在文档中，文档保存路径在当前程序路径下。  
本程序使用百度API，点击`图片转文字`前需填写`ID、KEY1、KEY2`，相应内容可在[百度智能云](https://cloud.baidu.com/product/ocr)免费申请。程序一次最多可识别1000张图片中的文字。图片文件夹中图片的命名如下图所示，应该为`1.jpg,2.jpg,3.jpg...`，识别时先识别`1.jpg`，然后识别`2.jpg`...图片命名编号可以有缺少，但缺少的编号应小于5，如`1.jpg,4.jpg,5.jpg...`，缺少编号超过5时，程序将停止继续识别并输出识别结果到文件中。  
<img width=93px height=100px src="https://github.com/xu-weizhen/Simple-Tools/blob/master/PDF-Tool/%E7%A4%BA%E4%BE%8B%E5%9B%BE%E7%89%87/%E5%9B%BE%E7%89%87%E5%91%BD%E5%90%8D.jpg?raw=true" alt="图片命名" align=center />  
  
  
程序输出的分割后PDF文件、PDF提取文字后的文件和图片文字识别结果文件等的文件名和文件路径在代码80-84行，如有需要可以进行修改。  
  

 
