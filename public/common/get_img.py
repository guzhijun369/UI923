# -*-coding:utf-8 -*-
import os
import unittest
from datetime import datetime
from functools import wraps
from config.basic_config import ConfigInit
from config import globalparam
from loguru import logger
from requests import request
import uuid
from qiniu import Auth, put_file, etag
import qiniu.config

access_key = ConfigInit.AccessKey
secret_key = ConfigInit.SecretKey

"""
此模块用于屏幕截图
"""
# 获取截截图保存的路径
img_base_path = os.path.join(globalparam.img_path)
# case 断言失败截图装饰器
def screenshot_about_case(func):
    # 保持传入的case的名称不被装饰器所改变
    @wraps(func)
    # t = func
    def get_screenshot_about_case(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            # 获取case_name的名称
            case_name = '{}'.format(unittest.TestCase.id(self) )
            # 截屏的路径
            screenshotPath = os.path.join(img_base_path, case_name)
            # 获得现在的时间戳
            time_now = datetime.now().strftime('%Y%m%d%H%M%S')
            # 名字的一部分
            screen_shot_name = ".png"
            # 组装图片需要传入的路径和推片名称
            screen_img = screenshotPath + '_' + time_now + '_' + screen_shot_name
            img_name = case_name + '_' + time_now + screen_shot_name
            logger.info(img_name)
            # 截图并保存到相应的名称的路径
            self.dr.take_screenshot(screen_img)
            img_url = upload_img(screen_img, img_name)
            print('screenshot:', img_url)
            raise e
    return get_screenshot_about_case

def upload_img(screenshotpath, img_name):
    q = Auth(access_key, secret_key)
    bucket_name = ConfigInit.qiniu_house
    # 上传后保存的文件名
    uu = uuid.uuid4()
    key = str(uu).replace('-', '')
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, expires=3600)
    # 要上传文件的本地路径
    localfile = screenshotpath
    try:
        r = put_file(token, key, localfile)
        logger.info('上传图片成功---')
        return ConfigInit.qiniu_domain + key
    except Exception as e:
        logger.debug('上传图片失败:{}'.format(e))
