# 系统部署说明

##### 开发服务器

1. `git clone git@github.com:suoigwg/PetHospital.git`
2. 切换到项目根目录下
3. `pip install -r requirement.txt`
4. `pip install git+git://github.com/sshwsfc/xadmin.git@django2`
5. `python3 manage.py collectstatic`
6. `python3 manage.py runserver`




##### 使用Nginx&uswgi(Ubuntu)

1. `sudo apt-get install nginx`
2. `pip install uswgi`
3. 切换到项目根目录下
4. `python3 manage.py collectstatic`
5. 将nginx的upstream server设置为uwsgi
6. `nohup uwsgi --http :8000 --wsgi-file PetHospital/wsgi.py --logto ./log.txt &`
7. `disown`



##### API 参考文档

`localhost:8000/docs/`



##### 管理后台

`localhost:8000`

默认账号:admin 密码:qwertyuiop