class Date:
    """
    Date(year, month, day): 创建一个 Date 实例并初始化成公历中的一天。西元前 1 年及之前的日期中的年部分用负数表示。
    year(): 返回该公历日期的年。
    month(): 返回该公历日期的月。
    day(): 返回该公历日期的日。
    monthName(): 返回该公历日期的月份名。
    dayOfWeek(): 返回星期数，值为 [0-6]，0 表示星期一，6 表示星期日。
    numDays(otherDate): 返回这两个日期间所差距的天数，是一个正整数。
    isLeapYear(): 布尔值，检测该日期是否在一个闰年中。
    advanceBy(days): 如果参数是正数，则返回的日期将增加这么多天，如果负数则减少，有必要的话，该日期将近似到西元前 4714 年的 12 月 24 日。
    comparable(otherDate): 实现逻辑运算，如 &lt;, &lt;=, &gt;, &gt;=, ==, !==。
    toString(): 返回 `yyyy-mm-dd` 形式的字符串表示。
    """

    def __init__(self, year, month, day):
        self._julianDay = 0
        assert self._isValidGregorian(year, month, day), "invalid Gregorian data."
        # Gredorian data --> julian day formula:
        # T = (M - 14) / 12
        # jday = D - 32075 + (1461 * (Y + 4800 + T) / 4) +
        #                    (367 * (M - 2 - T * 12) / 12) -
        #                    (3 * ((Y + 4900 + T) / 100) / 4)
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + \
                          (367 * (month - 2 + tmp * 12) // 12) - \
                          (3 * ((year + 4900 + tmp) // 100) // 4)

    # 一月（31天），二月（平年28天，闰年29天），三月（31天），
    # 四月（30天），五月（31 天），六月（30天），七月（31天），
    # 八月（31天），九月（30天），十月（31天），十一月（30天），
    # 十二月（31天）
    # 判断日期格式是否满足格雷高里历法
    def _isValidGregorian(self, year, month, day):
        if month > 12 or month < 1:
            print("Wrong format for month.")
            return False
        if day > 31 or day < 1:
            print("Wrong format for day.")
            return False
        # 天数为30的月份表
        month_30_days = [4, 6, 9, 11]
        if month in month_30_days and day > 30:
            print("Wrong format for day.")
            return False
        # 判断是否为闰月
        if month == 2:
            if self._leapYear(year):
                if day > 29:
                    print("Wrong format for day.")
                    return False
            else:
                if day > 28:
                    print("Wrong format for day.")
                    return False
        return True

    # 判断是否是闰年
    # 若是整百数，须被400整除；若非整百数，须被4整除
    def _isleapYear(self, year):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
        else:
            if (year % 4 == 0):
                return True
        return False

    def isLeapYear(self):
        return self._leapYear(self.year)

    # 抽取年、月、日
    def year(self):
        return (self._toGregorian())[0]

    def month(self):
        return (self._toGregorian())[1]

    def day(self):
        return (self._toGregorian())[2]

    # 返回Gregorian格式的日期三元组，(year,month,day)
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return year, month, day

    # 月份名称
    def monthName(self):
        months = ["Jan", "Feb", "Mar", "Apr", "may", "Jun",
                  "Jul", "Aug", "Sept", "Oct", "Nov", "Dec", ]
        return months[self.month()]

    # 星期几
    def dayOfWeek(self):
        day_in_week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        year, month, day = self._toGregorian()
        if month < 3:
            month += 12
            year -= 1
        num = ((13 * month + 3) // 5 + day + \
               year + year // 4 - year // 100 + year // 400) % 7
        return day_in_week[num]

    # 比较两个日期的天数之差
    def numDays(self, otherData):
        if self._julianDay > otherData._julianDay:
            return self._julianDay - otherData._julianDay
        else:
            return otherData._julianDay - self._julianDay

    # 日期变更
    def advanceBy(self, days):
        self._julianDay += days
        if self._julianDay < 0:
            self._julianDay = 0

    # 返回标准日期格式
    def __str__(self):
        year, month, day = self._toGregorian()
        return "%04d-%02d-%02d" % (year, month, day)

    # 将日期按格里高利历法格式返回
    def __repr__(self):
        return str(self)

    # 比价两个日期，依次为（相等、小于、小于等于）
    def __eq__(self, otherData):
        return self._julianDay == otherData._julianDay

    def __lt__(self, otherData):
        return self._julianDay < otherData._julianDay

    def __le__(self, otherData):
        return self._julianDay <= otherData._julianDay


if __name__ == "__main__":
    def promptAndExtractData():
        print("Enter a birth date.")
        year = int(input("year (0 to quit):"))
        if year == 0:
            return None
        else:
            month = int(input("month:"))
            day = int(input("day:"))
            return Date(year, month, day)


    bornBefore = Date(1984, 5, 2)
    date = promptAndExtractData()
    while date is not None:
        if date <= bornBefore:
            print("date:", date)
            print("borndata:", bornBefore)
            print("dayOfWeek:", date.dayOfWeek())
            print("compareDays:", date.numDays(bornBefore))
        date = promptAndExtractData()
