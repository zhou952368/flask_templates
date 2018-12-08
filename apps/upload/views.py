from flask import Blueprint, request, render_template

from apps.ext import img_set, db, doc_set
from apps.upload import helper
from apps.upload.models import Image

upload = Blueprint('upload', __name__, template_folder='templates')
"""
怎么避免文件上传是重名
1 对文件名字重命名
2 对文件的目录尽量细
"""


@upload.route('/upload/', methods=['get', 'post', 'put'])
def upload_image():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        image_file = request.files['img']
        # 通过UploadSet对象
        image_name = helper.get_file_name(image_file.filename)
        file_name = img_set.save(image_file, folder='user/1/', name=image_name)
        # 生成访问路径
        img_url = img_set.url(file_name)
        try:
            img = Image(path=img_url, type=1, uid=1)
            db.session.add(img)
            db.session.commit()
        except:
            db.session.rollback()
        return render_template('image.html', img_url=img_url)


@upload.route('/save/', methods=['get', 'post', 'put'])
def upload_files():
    if request.method == 'GET':
        return render_template('doc.html')
    else:
        file_str = request.files['doc']
        doc_name = doc_set.save(file_str)
        url = doc_set.url(doc_name)
        return '上传成功!!!'
