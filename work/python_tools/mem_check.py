import os, re, time
from pyecharts import Line

"""
配置游戏包名和名字
"""
package_name = "com.dashenyx.jzpml"  # 配置测试包名
game_name = "九州缥缈录"
#com.game.sgz.a360  com.dashenyx.jzpml


class Phone():
    def __init__(self):
        self.mem = os.popen("adb shell dumpsys meminfo %s" % package_name)
        for i in self.mem.readlines():
            if "MEMINFO" in i:
                self.pid_info = i
                break
        self.mem.close()
        try:
            self.pid = int(self.pid_info.split(" ")[4])
            print ("pid:", self.pid)
        except:
            raise IOError("检查adb连接并启动游戏")

    def total_test(self, test_time, duration):
        """
        测试pss和cpu
        :param test_time: 测试时间，单位s
        :param duration: 测试刷新间隔
        :return: 时间list， psstotal数据， cpu数据的list
        """
        i = 0
        time_init = int(time.time())
        time_end = time_init + test_time
        current_time = int(time.time())
        psslist, time_list = [], []
        while current_time < time_end:
            t = os.popen("adb shell dumpsys meminfo %s" % self.pid)
            content = t.readlines()
            t.close()
            for item in content:
                if "TOTAL" in item:
                    pss_info = item
                    break

            pss = float(re.findall("\d+\d|\d", pss_info)[0]) / 1000
            psstotal = float("%.2f" % pss)
            current_time = int(time.time())
            # print ("测试倒计时:%s秒"%(current_time-time_init))
            time_test = time.strftime("%H:%M:%S")
            # time_test = time.strftime("%Y-%m-%d %H:%M:%S")
            print(time_test, ("PssTotal="), psstotal)
            psslist.append(psstotal)
            time_list.append(time_test)
            time.sleep(duration)
            i += 1
        maxlist = sorted(psslist, reverse=True)
        average_pss = sum(psslist) / i
        print ("平均PssTotal", average_pss)
        print ("最高PssTotal", maxlist[0])
        print ("最低PSSTotal", maxlist[-1])
        return [psslist, time_list]

    def graphic(self, test_time=600, duration=2):
        """
        作图，调用测试
        :param test_time:测试时间，单位s
        :param duration: 刷新间隔
        :return:
        """
        pss_list = self.total_test(test_time=test_time, duration=duration)
        attr = pss_list[1]
        v1 = pss_list[0]
        v2 = pss_list[2]
        line = Line(game_name)
        line.add("PSS_total(M)", attr, v1, mark_point=["max"])
        line.render()


p = Phone()
p.graphic(60, 1)