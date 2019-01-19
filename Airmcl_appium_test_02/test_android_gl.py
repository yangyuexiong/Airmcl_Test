# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 下午5:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_android_gl.py
# @Software: PyCharm

from time import sleep
import myunit

vl = {
    '开始光疗': 'com.yunmei.aircml:id/start_light_cure',
    '结束光疗': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView[2]',
    '确认': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]',
    '1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.TextView',
    '2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.TextView',
    '3': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.TextView',
    '4': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[4]/android.widget.TextView',
}

mbss = {
    '1-1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout',
    '1-2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout',
    '1-3': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout',
    '1-4': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout',
}

mbss2 = {
    '2-1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout',
    '2-2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout',
    '2-3': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout',
}

mbss3 = {
    '3-1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout',
    '3-2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout',
    '3-3': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout',
}

mbss4 = {
    '4-1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout',
    '4-2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout',
    '4-3': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout',
}


def sanlianji(driver):
    driver.find_element_by_id(vl.get('开始光疗')).click()
    sleep(5)  # 加载
    driver.find_element_by_xpath(vl.get('结束光疗')).click()
    driver.find_element_by_xpath(vl.get('确认')).click()
    sleep(1)


def gl(driver):
    a = 0
    try:
        for k, v in mbss.items():
            driver.find_element_by_xpath(v).click()
            sanlianji(driver)
            print('finish:--->>>%s' % k)
            a = a + 1
        if a == 4:
            driver.find_element_by_xpath(vl.get('2')).click()
            print('start:祛黄淡斑')
            for k2, v2 in mbss2.items():
                driver.find_element_by_xpath(v2).click()
                sleep(1)
                sanlianji(driver)
                print('finish:--->>>%s' % k2)
                a = a + 1
                if a == 7:
                    driver.find_element_by_xpath(vl.get('3')).click()
                    print('start:祛痘祛印')
                    for k3, v3 in mbss3.items():
                        driver.find_element_by_xpath(v3).click()
                        sleep(1)
                        sanlianji(driver)
                        print('finish:--->>>%s' % k3)
                        a = a + 1
                        if a == 10:
                            driver.find_element_by_xpath(vl.get('4')).click()
                            print('start:镇静舒缓')
                            for k4, v4 in mbss4.items():
                                driver.find_element_by_xpath(v4).click()
                                sleep(1)
                                sanlianji(driver)
                                print('finish:--->>>%s' % k4)
                                a = a + 1
                                if a == 14:
                                    print('所有光疗模式完毕')
    except BaseException as e:
        print('出现异常', e)
    finally:
        print('所有光疗模式完毕')


class TestAnd(myunit.StartEnd):
    """ok"""

    def test_meibaisuoshui(self):
        driver = self.driver
        print('开始')
        sleep(3)  # 启动加载等待
        print('等待完毕')
        gl(driver)


if __name__ == '__main__':
    pass
