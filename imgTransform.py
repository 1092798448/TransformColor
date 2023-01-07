# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 15:09:00 2022

@author: Administrator
"""

import tkinter as tk
import os
import cv2
from tkinter.filedialog import *

class ImgTransform:
    def __init__(self):
        self.ori_img = ''
        self.trans_img = ''
        #创建主窗口对象
        root = tk.Tk()
        #设置标题
        root.title('UI界面')
        root.minsize(200,200)
        #创建按钮
        btn_open_file = tk.Button(root,text='选择图片',command=self.open_file)
        btn_to_gray = tk.Button(root,text='转成灰度图片',command=lambda:self.transform_color('1'))
        btn_to_BGRA = tk.Button(root,text='转成BGRA图片',command=lambda:self.transform_color('2'))
        btn_to_XYZ = tk.Button(root,text='转成XYZ图片',command=lambda:self.transform_color('3'))
        btn_to_YCrCb = tk.Button(root,text='转成YCrCb图片',command=lambda:self.transform_color('4'))
        btn_to_HSV = tk.Button(root,text='转成HSV图片',command=lambda:self.transform_color('5'))
        btn_to_Lab = tk.Button(root,text='转成Lab图片',command=lambda:self.transform_color('6'))
        btn_to_Luv = tk.Button(root,text='转成Luv图片',command=lambda:self.transform_color('7'))
        btn_to_HLS = tk.Button(root,text='转成HLS图片',command=lambda:self.transform_color('8'))
        btn_save_file = tk.Button(root,text='保存转换后图片',command=self.save_file)
        btn_open_file.pack()
        btn_to_gray.pack()
        btn_to_BGRA.pack()
        btn_to_XYZ.pack()
        btn_to_YCrCb.pack()
        btn_to_HSV.pack()
        btn_to_Lab.pack()
        btn_to_Luv.pack()
        btn_to_HLS.pack()
        btn_save_file.pack()
        #加入消息循环
        root.mainloop()


    def open_file(self):
        img_path = askopenfilename(title="选择识别图片", filetypes=[("jpg图片", "*.jpg")])
        if len(img_path.strip()) == 0:
            return
        cv2.namedWindow('ori_image')
        self.ori_img = cv2.imread(img_path)
        cv2.imshow("ori_image", self.ori_img)
        #cv2.waitKey(0)
        
    def save_file(self):
        if len(self.trans_img) == 0:
            self.show_warning('没有转换图片')
            return
        file_path = asksaveasfilename(title='保存文件',defaultextension='jpg',initialfile='result',
                                      filetypes=[("jpg图片", "*.jpg")])
        if len(file_path.strip()) > 0:       
            cv2.imwrite(file_path,self.trans_img)
        
        
    def transform_color(self,type):        
        if cv2.getWindowProperty('trans_image', cv2.WND_PROP_VISIBLE):
            cv2.destroyWindow('trans_image')
        if len(self.ori_img) == 0:
            self.show_warning('请先选择图片')
            self.open_file()
            return
        cv2.namedWindow('trans_image')
        if type == '1':
            code = cv2.COLOR_BGR2GRAY
        elif type == '2':
            code = cv2.COLOR_RGB2BGRA
        elif type == '3':
            code = cv2.COLOR_RGB2XYZ
        elif type == '4':
            code = cv2.COLOR_RGB2YCrCb
        elif type == '5':
            code = cv2.COLOR_RGB2HSV
        elif type == '6':
            code = cv2.COLOR_RGB2Lab  
        elif type == '7':
            code = cv2.COLOR_RGB2Luv
        elif type == '8':
            code = cv2.COLOR_RGB2HLS
        self.trans_img = cv2.cvtColor(self.ori_img, code)  
        cv2.imshow("trans_image", self.trans_img)
        #cv2.waitKey(0)
        
    def show_warning(self,msg):
        tk.messagebox.showwarning('提示',msg)
        
if __name__ == '__main__':
    imgTransform = ImgTransform()





    