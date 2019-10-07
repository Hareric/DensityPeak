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
# create_date = '2019/4/20'


from sklearn.cluster import KMeans
from DrawPicture import *


def run_given_data(X, k):
    y_predict = KMeans(n_clusters=k, random_state=9).fit_predict(X)
    get_picture(X[:, 0], X[:, 1], save_path='graph/clustering.png', title="clustering result",
                color=y_predict)


if __name__ == '__main__':
    X, y = ds.make_blobs(300, centers=3, cluster_std=1, n_features=2)
    get_picture(X[:, 0], X[:, 1], "./graph/origin.png", "origin data")
    run_given_data(X, 3)
