import os
import sys

try:
    import ffmpy
except:
    path = '"' + os.path.dirname(sys.executable) + '\\scripts\\pip" install ffmpy'
    os.system(path)
    import ffmpy

import tkinter
import tkinter.filedialog
import tkinter.messagebox  # 要使用messagebox先要导入模块


class Transcoder:
    def checkbox1(self):
        var_qsv = ' '
        if (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 0):
            l.config(text='QSV_H264加速已开启')
            var_qsv = "-c:v h264_qsv"
        elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0):
            l.config(text='hevc_qsv加速已开启')
            var_qsv = "-c:v hevc_qsv"
        elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0):
            l.config(text='mpeg2_qsv加速已开启')
            var_qsv = "mpeg2_qsv"
        elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1):
            l.config(text='vp9_qsv加速已开启')
            var_qsv = "vp9_qsv"
        elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 0):
            l.config(text='硬件加速已关闭')
            var_qsv = " "
        else:
            l.config(text='你无法选择两种及以上硬件加速器,将关闭硬件加速')
            var_qsv = " "

    def checkbox2(self):
        global resolution
        if var_r.get() == "AUDIO TRANSCODE":
            l.config(text='音频转码模式')
            resolution = ' '
        else:
            l.config(text='输出分辨率是:' + var_r.get())
            resolution = var_r.get()

    def checkbox3(self):
        l.config(text='输出音频码率是:' + Transcoder.rb2(self).var_a.get())
        global audio
        audio = Transcoder.rb2(self).var_a.get()

    def xz(self):  # 点击选择按钮后的弹窗
        global filename
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            l.config(text="您选择的文件是：\n" + filename)
        else:
            l.config(text="您没有选择任何文件")

    def sc(self):  # 输出
        outname = e1.get()
        if var_r.get() == "AUDIO TRANSCODE":
            bitbytes = ' '
        else:
            bitbytes = " -b:v " + e2.get()
        videoname = filename
        ff = ffmpy.FFmpeg(
            inputs={videoname: None},
            outputs={outname: Transcoder.checkbox1(self).var_qsv + bitbytes + " -b:a " + audio + resolution}
        )
        print(ff.cmd)
        ff.run()
        tkinter.messagebox.showinfo(message="转码成功！")

    def rb1(self):
        global var_r
        fm = tkinter.Frame()
        fm.pack(side='left', fill='y', expand='YES')
        var_r = tkinter.StringVar()
        tkinter.Label(fm, text='分辨率选择').pack(side='top', fill='y', expand='YES')
        r1 = tkinter.Radiobutton(fm, text='4096x2160',
                                 variable=var_r, value=' -s 4096x2160',
                                 command=Transcoder.checkbox2)
        r1.pack(side='top', fill='y', expand='YES')
        r2 = tkinter.Radiobutton(fm, text='2560x1440',
                                 variable=var_r, value=' -s 2560x1440',
                                 command=Transcoder.checkbox2)
        r2.pack(side='top', fill='y', expand='YES')
        r3 = tkinter.Radiobutton(fm, text='1920x1080',
                                 variable=var_r, value=' -s 1920x1080',
                                 command=Transcoder.checkbox2)
        r3.pack(side='top', fill='y', expand='YES')
        r4 = tkinter.Radiobutton(fm, text='1280x720',
                                 variable=var_r, value=' -s 1280x720',
                                 command=Transcoder.checkbox2)
        r4.pack(side='top', fill='y', expand='YES')
        r5 = tkinter.Radiobutton(fm, text='640x480',
                                 variable=var_r, value=' -s 640x480',
                                 command=Transcoder.checkbox2)
        r5.pack(side='top', fill='y', expand='YES')
        r6 = tkinter.Radiobutton(fm, text='音频转码',
                                 variable=var_r, value='AUDIO TRANSCODE',
                                 command=Transcoder.checkbox2)
        r6.pack(side='top', fill='y', expand='YES')

    def rb2(self):
        fm = tkinter.Frame()
        fm.pack(side='right', fill='y', expand='YES')
        var_a = tkinter.StringVar()
        tkinter.Label(fm, text='音频码率选择').pack(side='top', fill='y', expand='YES')
        r1 = tkinter.Radiobutton(fm, text='960kbps',
                                 variable=var_a, value='960k',
                                 command=Transcoder.checkbox3)
        r1.pack(side='top', fill='y', expand='YES')
        r2 = tkinter.Radiobutton(fm, text='640kbps',
                                 variable=var_a, value='640k',
                                 command=Transcoder.checkbox3)
        r2.pack(side='top', fill='y', expand='YES')
        r3 = tkinter.Radiobutton(fm, text='320kbps',
                                 variable=var_a, value='320k',
                                 command=Transcoder.checkbox3)
        r3.pack(side='top', fill='y', expand='YES')
        r4 = tkinter.Radiobutton(fm, text='256kbps',
                                 variable=var_a, value='256k',
                                 command=Transcoder.checkbox3)
        r4.pack(side='top', fill='y', expand='YES')
        r5 = tkinter.Radiobutton(fm, text='128kbps',
                                 variable=var_a, value='128k',
                                 command=Transcoder.checkbox3)
        r5.pack(side='top', fill='y', expand='YES')

    def cb1(self):
        fm = tkinter.Frame()
        fm.pack(side='top', fill='y', expand='YES')
        global var1, var2, var3, var4
        var1 = tkinter.IntVar()
        var2 = tkinter.IntVar()
        var3 = tkinter.IntVar()
        var4 = tkinter.IntVar()
        c1 = tkinter.Checkbutton(fm, text='qsv_h264硬件加速',
                                 variable=var1, onvalue=1, offvalue=0, command=Transcoder.checkbox1)
        c1.pack()
        c2 = tkinter.Checkbutton(fm, text='hevc_qsv硬件加速',
                                 variable=var2, onvalue=1, offvalue=0, command=Transcoder.checkbox1)
        c2.pack()
        c3 = tkinter.Checkbutton(fm, text='mpeg2_qsv硬件加速',
                                 variable=var3, onvalue=1, offvalue=0, command=Transcoder.checkbox1)
        c3.pack()
        c4 = tkinter.Checkbutton(fm, text='vp9_qsv硬件加速',
                                 variable=var4, onvalue=1, offvalue=0, command=Transcoder.checkbox1)
        c4.pack()


window = tkinter.Tk()
window.title("FFMPEG TRANSCODER")
window.geometry('480x300')
l = tkinter.Label(window, bg='yellow', width=80, height=2, text='POWERED BY ZYX')
l.pack()
T = Transcoder()
T.rb1()
T.rb2()
T.cb1()
btn = tkinter.Button(text="选择文件", command=T.xz)
btn.pack()
tkinter.Label(window, text='输出名称(如XXX.mov)').pack()
entry_var1 = tkinter.StringVar()
entry_var2 = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=entry_var1)  # 视频输出名称框口
e1.pack()  # 放置第一个输入文本框
tkinter.Label(window, text='比特率(如2000k)').pack()
e2 = tkinter.Entry(window, textvariable=entry_var2)  # 视频输出比特率框口
e2.pack()
button_outstream = tkinter.Button(text="输出", command=T.sc)  # 输出按钮
button_outstream.pack()
window.mainloop()  # 窗口主循环
