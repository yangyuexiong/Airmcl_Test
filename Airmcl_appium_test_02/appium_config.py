#!/usr/bin/env python
# encoding: utf-8

from appium import webdriver


# sys.path.append("..")

# Read mobile deviceId
# device_id = get_serialno()

# Read mobile os Version
# os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()


def appium_android():
    config = {
        'platformName': 'Android',  # 平台
        'platformVersion': '6.0.1',  # 系统版本
        # 'deviceName': 'S25QBDPD22PLH',  # 测试设备ID S25QBDPD22PLH
        'deviceName': '3452a8f4',  # 测试设备ID 3452a8f4
        'appPackage': 'com.yunmei.aircml',
        'appActivity': '.modules.home.ui.AppStartActivity',
        'newCommandTimeout': 3600,
        'automationName': 'Appium',
        'unicodeKeyboard': True,  # 编码,可解决中文输入问题
        'resetKeyboard': True,
        'noReset': True  # 不重置应用状态
    }

    return webdriver.Remote('http://localhost:4723/wd/hub', config)


if __name__ == '__main__':
    appium_android()


    # driver.find_element_by_id("com.yunmei.aircml:id/pw_tel").send_keys("15013038819")
    # driver.find_element_by_id("com.yunmei.aircml:id/pw_login").click()
    # driver.find_element_by_id("android:id/statusBarBackground").send_keys("666666")
