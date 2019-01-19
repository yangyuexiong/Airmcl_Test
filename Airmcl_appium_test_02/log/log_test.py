# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 下午7:43
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : log_test.py
# @Software: PyCharm


# CON_LOG = 'log.conf'
# logging.config.fileConfig(CON_LOG)
# logging = logging.getLogger()


import logging.config

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


# logging.basicConfig(
#     filename='log.log',
#     level=logging.DEBUG,
#     format='%(asctime)s ->%(filename)s[line:%(lineno)d] -%(levelname)s- %(message)s'
# )
logging.info('okc')
