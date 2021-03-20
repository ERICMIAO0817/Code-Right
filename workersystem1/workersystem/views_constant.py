import hashlib
from workersystem.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail
from django.template import loader
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt

MALE = 0
FEMALE = 1


def hax_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


def send_email(username, recive, token):
    subject = '你好,%s' % username
    message = 'Hello'
    recipient_list = [recive]
    data = {
        'username': username,
        'active_url': 'http://localhost:8000/user/active/?u_token={}'.format(token)
    }
    html_message = loader.get_template('active.html').render(data)
    send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER, recipient_list=recipient_list,
              html_message=html_message)


def get_join(join1, join2, join3, join4):
    return (join1 + join2 + join3 + join4) / 4


def get_conclude(A, B, C):
    return A / (A + B + C)


def KPI(list,name):
    x = []
    for i in range(0, len(list)):
        x.append(i)
    plt = pyplot
    plt.figure()
    plt.plot(x, list, marker='o', color='r', label='KPI_data')
    plt.legend()
    plt.xlabel('季度')
    plt.ylabel('KPI')
    plt.savefig('static/uploads/KPI/'+name+'_KPI.png')
    plt.show()

def conclude(list,name):
    # 用于正常显示中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 用于正常显示符号
    plt.rcParams['axes.unicode_minus'] = False
    # 使用ggplot的绘图风格，这个类似于美化了，可以通过plt.style.available查看可选值，你会发现其它的风格真的丑。。。
    plt.style.use('ggplot')
    # 构造数据
    values = list
    feature = ['个人能力', 'QC知识', '解决问题能力', '服务质量意识', '团队精神']
    # 设置每个数据点的显示位置，在雷达图上用角度表示
    angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)
    # 拼接数据首尾，使图形中线条封闭
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    # 绘图
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)  # 设置为极坐标格式
    ax.plot(angles, values, 'o-', linewidth=2)  # 绘制折线图
    ax.fill(angles, values, alpha=0.25)  # 填充颜色
    # 设置图标上的角度划分刻度，为每个数据点处添加标签
    # ax.set_thetagrids(angles * 180 / np.pi, feature)
    ax.set_ylim(0, 5)  # 设置雷达图的范围
    plt.title('综合个人能力')
    ax.grid(True)  # 添加网格线
    plt.savefig('static/uploads/conclude/'+name+'_con.png')
    plt.show()

def join(list,name):
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.style.use('ggplot')
    labels = 'A', 'B', 'C', 'D'
    fraces = list
    explode = [0.1, 0, 0, 0]
    plt.axes(aspect=1)
    plt.pie(x=fraces, labels=labels, autopct='%0f%%', explode=explode, shadow=True)
    plt.title('项目综合评分')
    plt.savefig('static/uploads/join/'+name+'_join.png')
    plt.show()

