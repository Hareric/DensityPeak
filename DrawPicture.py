# coding=utf-8
#         ┌─┐       ┌─┐
#      ┌──┘ ┴───────┘ ┴──┐
#      │                 │
#      │       ───       │
#      │  ─┬┘       └┬─  │
#      │                 │
#      │       ─┴─       │
#      │                 │
#      └───┐         ┌───┘
#          │         │             神兽保佑
#          │         │            代码无BUG!
#          │         │
#          │         └──────────────┐
#          │                        │
#          │                        ├─┐
#          │                        ┌─┘
#          │                        │
#          └─┐  ┐  ┌───────┬──┐  ┌──┘
#            │ ─┤ ─┤       │ ─┤ ─┤
#            └──┴──┘       └──┴──┘              
# author = 'Eric Chen'
# create_date = '2019/4/15'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np


def get_picture(x, y, save_path, title, color='blue', outlier_index=None):
    # 创建Figure
    fig = plt.figure()
    # 用来正常显示中文标签
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    matplotlib.rcParams['axes.unicode_minus'] = False

    plt.axis([np.min(x)-2, np.max(x)+2, np.min(y)-2, np.max(y)+2])
    plt.scatter(x=x, y=y, c=color, s=20)

    plt.title(title)

    # 标示outliers
    if outlier_index is not None:
        text_location_x = np.min(x)-1
        text_location_y = np.max(y)+1
        t = 0
        for i in outlier_index:
            plt.annotate(i, (x[i],y[i]), color='black',  fontsize=12,
                         xytext=(text_location_x, text_location_y-t),
                         arrowprops=dict(arrowstyle="->", color='gray', connectionstyle="angle,angleA=0,angleB=90,rad=10"),
                         bbox=dict(boxstyle="round", fc="0.8")
                         )
            t += 1

            # plt.annotate("outlier", xy=(x[i], y[i]),
            #              xytext=(text_location_x, text_location_y),
            #              arrowprops=dict(arrowstyle="->", color='gray', connectionstyle="arc3,rad=.1"))
            # plt.scatter(x=x[i], y=y[i], c='black', marker='*', s=80)

    plt.savefig(save_path, bbox_inches='tight',
                pad_inches=0)
    plt.close()



if __name__ == '__main__':
    import sklearn.datasets as ds
    X, y = ds.make_blobs(100, centers=3, cluster_std=1, n_features=2)
    get_picture(X[:, 0], X[:, 1], "./graph/test.png", "test", outlier_index=[0,1,2])