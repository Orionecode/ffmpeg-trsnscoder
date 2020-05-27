#!/usr/bin/python
# coding:utf-8
import os
# import ctypes 此处的ctype为支持高DPI缩放
import time
import tkinter.font as tkFont

try:
    import ffmpy
except ImportError:
    path = "python -m pip install ffmpy"
    os.system(path)
    import ffmpy

    print("ffmpy is now installed")
import tkinter
from tkinter import ttk
import tkinter.filedialog
import tkinter.messagebox  # 要使用messagebox先要导入模块


def checkbox1(*args):
    # "请选择", "INTEL H264_QSV", "INTEL HEVC_QSV", "NVIDIA H264_NVENC", "NVDIA HEVC_NVENC", "关闭硬件加速"
    encoder = var_encoder.get()
    if encoder == "INTEL H264_QSV":
        l.config(text='INTEL H264硬件加速已开启')
        var_qsv = "-c:v h264_qsv"
    elif encoder == "INTEL HEVC_QSV":
        l.config(text='INTEL HEVC硬件加速已开启')
        var_qsv = "-c:v hevc_qsv"
    elif encoder == "NVIDIA H264_NVENC":
        l.config(text='NVIDIA H264硬件加速已开启')
        var_qsv = "-c:v h264_nvenc"
    elif encoder == "NVDIA HEVC_NVENC":
        l.config(text='NVDIA HEVC硬件加速已开启')
        var_qsv = "-c:v hevc_nvenc"
    elif (encoder == "关闭硬件加速") or (encoder == "请选择"):
        l.config(text='硬件加速已关闭')
        var_qsv = " "
    else:
        var_qsv = " "
    return var_qsv


def checkbox2(*args):
    global resolution
    if var_r.get() == "AUDIO TRANSCODE" or var_r.get() == "请选择":
        l.config(text='音频转码模式')
        resolution = ' '
        # "请选择"," -s 4096x2160", " -s 2560x1440", " -s 1920x1080", " -s 1280x720", " -s 640x480"
        # "请选择", "High Quality 2160p 4K", "QHD 1440p 2K", "FHD 1080p", "HD 720p", "SHD 480P",
    elif var_r.get() == "High Quality 2160p 4K":
        resolution = ' -s 4096x2160 '
        l.config(text='输出分辨率是:' + resolution)
    elif var_r.get() == "QHD 1440p 2K":
        resolution = ' -s 2560x1440 '
        l.config(text='输出分辨率是:' + resolution)
    elif var_r.get() == "FHD 1080p":
        resolution = ' -s 1920x1080 '
        l.config(text='输出分辨率是:' + resolution)
    elif var_r.get() == "HD 720p":
        resolution = ' -s 1280x720 '
        l.config(text='输出分辨率是:' + resolution)
    elif var_r.get() == "SHD 480P":
        resolution = ' -s 640x480 '
        l.config(text='输出分辨率是:' + resolution)


def checkbox3(*args):
    global audio
    if var_a.get() == "请选择":
        audio = ' 320k '
    else:
        l.config(text='输出音频码率是:' + var_a.get())
        audio = var_a.get()


def checkbox4(*args):
    global fps
    if var_f.get() == "保持原视频帧数" or var_f.get() == "请选择":
        l.config(text="自动识别原视频帧数")
        fps = ' '
    else:
        l.config(text="输出的帧数是:" + var_f.get())
        fps = var_f.get()


def xz():  # 点击选择按钮后的弹窗
    global filename
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        l.config(text="您选择的文件是：\n" + filename)
    else:
        l.config(text="您没有选择任何文件")


def sc():  # 输出
    outname = e1.get()
    if var_r.get() == "AUDIO TRANSCODE":
        bitbytes = ' '
        var_qsv = ' '
    else:
        bitbytes = " -b:v " + e2.get() + "k"
        var_qsv = checkbox1()
    videoname = filename
    ff = ffmpy.FFmpeg(
        inputs={videoname: None},
        outputs={outname: var_qsv + bitbytes + " -b:a " + audio + fps + resolution}
    )
    print(ff.cmd)
    t1 = time.time()
    ff.run()
    t2 = time.time()
    time_spend = t2 - t1
    tkinter.messagebox.showinfo(title='转码成功', message="转码耗时：" + format(time_spend, '.2f') + "秒")


def rb1():
    global var_r
    global var_a
    global var_encoder
    global var_f
    var_r = tkinter.StringVar()
    var_a = tkinter.StringVar()
    var_encoder = tkinter.StringVar()
    var_f = tkinter.StringVar()
    fm = tkinter.Frame()
    fm.pack(side='top', fill='y', expand='YES')
    # 分辨率选择
    tkinter.Label(fm, text='分辨率选择', font=font1).pack(side='top', fill='y', expand='YES')
    comboxlist = ttk.Combobox(fm, textvariable=var_r, width=28)
    comboxlist["values"] = (
        "请选择", "High Quality 2160p 4K", "QHD 1440p 2K", "FHD 1080p", "HD 720p", "SHD 480P",
        "AUDIO TRANSCODE")
    comboxlist.current(0)
    comboxlist.bind("<<ComboboxSelected>>", checkbox2)
    comboxlist.pack(side='top', fill='y', expand='YES')
    # 音频码率选择
    tkinter.Label(fm, text='音频码率选择', font=font1).pack(side='top', fill='y', expand='YES')
    comboxlist = ttk.Combobox(fm, textvariable=var_a, width=28)
    comboxlist["values"] = (
        "请选择", "1536k", "960k", "640k", "320k", "256k", "128k", "64k", "32k"
    )
    comboxlist.current(0)
    comboxlist.bind("<<ComboboxSelected>>", checkbox3)
    comboxlist.pack(side='top', fill='y', expand='YES')
    # 编码器选择
    tkinter.Label(fm, text='GPU加速选择', font=font1).pack(side='top', fill='y', expand='YES')
    comboxlist = ttk.Combobox(fm, textvariable=var_encoder, width=28)
    comboxlist["values"] = (
        "请选择", "INTEL H264_QSV", "INTEL HEVC_QSV", "NVIDIA H264_NVENC", "NVDIA HEVC_NVENC", "关闭硬件加速"
    )
    comboxlist.current(0)
    comboxlist.bind("<<ComboboxSelected>>", checkbox1)
    comboxlist.pack(side='top', fill='y', expand='YES')
    # 帧数选择
    tkinter.Label(fm, text='帧数选择', font=font1).pack(side='top', fill='y', expand='YES')
    comboxlist = ttk.Combobox(fm, textvariable=var_f, width=28)
    comboxlist["values"] = (
        "请选择", "保持原视频帧数", " -r 240 ", " -r 120 ", " -r 90 ", " -r 60 ", " -r 30 ", " -r 25 "
    )
    comboxlist.current(0)
    comboxlist.bind("<<ComboboxSelected>>", checkbox4)
    comboxlist.pack(side='top', fill='y', expand='YES')


window = tkinter.Tk()
# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# window.tk.call('tk', 'scaling', ScaleFactor / 75)
window.title("FFMPEG TRANSCODER")
window.geometry('360x576')
font1 = tkFont.Font(family='microsoft yahei', size=10, weight=tkFont.NORMAL)
font2 = tkFont.Font(family='microsoft yahei', size=10)
l = tkinter.Label(window, bg='yellow', width=100, height=3, text='POWERED BY ZENGYIXIAO IN 2020/5')
l.pack(side='top', fill='y', expand='NO')
fm = tkinter.Frame()
fm.pack(side='top', fill='y', expand='YES')
tkinter.Button(fm, text="选择文件", command=xz, width=27, height=1, font=font2, relief="groove").pack(side='top', fill='y',
                                                                                                  pady=10,
                                                                                                  expand='YES')
rb1()  # 分辨率选择 音频码率选择 编解码器选择
tkinter.Label(fm, text='输出名称(如XXX.mov)', font=font1).pack(side='top', fill='y', expand='YES')
entry_var1 = tkinter.StringVar()
entry_var2 = tkinter.StringVar()
e1 = tkinter.Entry(fm, textvariable=entry_var1, width=30)  # 视频输出名称框口
e1.pack(side='top', fill='y', expand='YES')  # 放置第一个输入文本框
tkinter.Label(fm, text='比特率(如2000,单位为kbps)', font=font1).pack(side='top', fill='y', expand='YES')
e2 = tkinter.Entry(fm, textvariable=entry_var2, width=30)  # 视频输出比特率框口
e2.pack(side='top', fill='y', expand='YES')
tkinter.Button(text="一键输出视频", command=sc, width=27, height=2, font=font2, relief="groove").pack(side='bottom', fill='y',
                                                                                                pady=18,
                                                                                                expand='NO')  # 输出按钮
window.mainloop()  # 窗口主循环
