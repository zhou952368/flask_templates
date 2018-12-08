"""
对文件上传的文件重命名

"""
import datetime
import random

IMG_PREFIX_NAME = 'IMG'


def get_file_name(file_name: str):
    suffix_name = '.' + file_name.split('.')[-1]
    # 时间加上随机数
    new_name = IMG_PREFIX_NAME + \
               (datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + \
               (str(random.randint(100000, 999999)))
    return new_name + suffix_name
