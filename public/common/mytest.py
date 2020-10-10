#coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam
from config.basic_config import ConfigInit
from loguru import logger
from public.pages.LoginPage import Login


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser,globalparam.headless)
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))


    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')


class MyAutologinTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     MongoModel().delete_customer('13800138011')

    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser,globalparam.headless)
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))
        self.workbench = Login(self.dr).login('admin','jimi123', '业务平台')

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')
