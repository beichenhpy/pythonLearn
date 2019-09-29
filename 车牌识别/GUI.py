import tkinter as tk
import tkinter.filedialog as tkFD
import pymysql
import demo
import traceback
import datetime
import sum
from tkinter import ttk


class Gui(ttk.Frame):
    viewhigh = 600
    viewwide = 600
    def __init__(self,win):
        ttk.Frame.__init__(self,win)
        frame_right=ttk.Frame(self)
        frame_left=ttk.Frame(self)
        win.title("停车场管理系统")
        win.state("zoomed")
        self.pack(fill=tk.BOTH, expand=tk.YES, padx="10", pady="10")
        frame_right.pack(side='top', expand=1, fill=tk.Y)
        frame_left.pack(side='left', expand=1, fill='both')
        self.scan1=ttk.Button(frame_right,text='扫描入场',width=15,height=3,command=self.scan)
        self.scan1.pack(side=tk.LEFT)
        self.out1=ttk.Button(frame_right,text='结账出场',command=self.out)
        self.out1.pack(side=tk.RIGHT)

    def scan(self):
        fileName =tkFD.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("python",".py")])
        image_path = fileName
        number = demo.get_license_plate(image_path)
        print(number)
        now_time = datetime.datetime.now()
        print(now_time)
        # 打开数据库连接
        db = pymysql.connect("207.148.104.108", "root", "123456", "car")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 插入语句
        sql = "INSERT INTO carinfo (carnumber,intime) VALUES (\"%s\",\"%s\")" % (str(number),str(now_time))

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            frame = tk.Frame(win)
            frame.pack()
            self.callback=ttk.Label(frame,text=number+'进场成功记录')
            self.callback.pack()
        except Exception:
            traceback.print_exc()  # 如果发生错误则回滚
            db.rollback()

        # 关闭数据库连接
        db.close()
    def out(self):
        fileName = tkFD.askopenfilename(filetypes=[("PNG", ".png"), ("GPF", ".gpf"), ("JPG", ".jpg"), ("python", ".py")])
        image_path = fileName
        number = demo.get_license_plate(image_path)
        print(number)
        now_time = datetime.datetime.now()
        print(now_time)
        db = pymysql.connect("207.148.104.108", "root", "123456", "car")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql0="UPDATE carinfo SET outtime = (\"%s\") where carnumber=(\"%s\")" % (str(now_time),str(number))
        sql1 = "SELECT intime from carinfo WHERE carnumber = (\"%s\")" % (str(number))
        sql2 = "SELECT outtime from carinfo WHERE carnumber = (\"%s\")" % (str(number))
        try:
            # 执行sql语句
            cursor.execute(sql0)
            # 提交到数据库执行
            db.commit()
            print("插入语句执行成功")
        except Exception:
            traceback.print_exc()  # 如果发生错误则回滚
            db.rollback()
        try:
            cursor.execute(sql1)
            intime = cursor.fetchall()
            for row in intime:
                row1=row[0]
            intime=row1
            print(intime)
        except Exception:
            traceback.print_exc()  # 如果发生错误则回滚
            db.rollback()
        try:
            cursor.execute(sql2)
            outtime = cursor.fetchall()
            for row in outtime:
                row1 = row[0]
            outtime=row1
            print(outtime)
        except Exception:
            traceback.print_exc()  # 如果发生错误则回滚
            db.rollback()
        db.close()
        park_fee = sum.check_fee(intime, outtime)
        frame = ttk.Frame(win)
        frame.pack()
        self.callback = ttk.Label(frame, text="请交款 "+str(park_fee)+" 元")
        self.callback.pack()
if __name__ == '__main__':
    win = tk.Tk()
    gui = Gui(win)
    win.mainloop()