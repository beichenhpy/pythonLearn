# coding=UTF-8
import time
import datetime
import math


# 把字符串转成datetime
def string_toDatetime(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())


def Fee(time1, time2):
    times = time2 - time1
    days = times.days
    hours = days * 24 + times.seconds / 3600.00
    fee_hours = int(math.ceil(hours))
    # 如果flag = 1 表示第二日时间段，没有免费15分钟。

    d_fee = 0
    n_fee = 0
    time_i = time1
    while time_i < time2:
        hour_i = time_i.hour
        if hour_i >= 7 and hour_i < 22:
            d_fee = d_fee + 4
        if hour_i < 7 or hour_i >= 22:
            n_fee = n_fee + 4
        time_i = time_i + datetime.timedelta(hours=1)

    if n_fee > 8:
        n_fee = 8
    fee = d_fee + n_fee

    print(" %s-%s 停车%s小时，收费%d小时，日间%d元， 夜间%d元， 停车费：%d元" % (time1, time2, hours, fee_hours, d_fee, n_fee, fee))

    return fee


def check_fee(time1, time2):
    timei = time1
    if (timei < time2):
        # 以7点为节点，递归计算
        timei_next = string_toDatetime((timei + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + " 07:00:00")
        if timei_next < time2:
            park_fee = Fee(time1, timei_next + datetime.timedelta(seconds=-1)) + check_fee(timei_next, time2)
        else:
            park_fee = Fee(time1, time2)

        return park_fee
    else:
        return 0


time_in = "2018-01-02 16:20:00"
time_out = "2018-01-02 18:30:00"
time1 = string_toDatetime(time_in)
time2 = string_toDatetime(time_out)

# 递归计算车费
park_fee = check_fee(time1, time2)

print("停车费总计：%d元" % park_fee)