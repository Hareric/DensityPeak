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
# create_date = '2019/3/30'


from Tkinter import *
import ttk
import PIL.Image
import PIL.ImageTk
from DensityPeak import *
from DrawPicture import get_picture
import Kmeans
import sklearn.datasets as ds

def generate_blob_data():
    """
    For button “blob data”
    Generate and display isotropic Gaussian blobs for clustering
    :return:
    """
    global X
    X, y = ds.make_blobs(int(points_number.get()), centers=int(center_num.get()), cluster_std=1, n_features=2)

    get_picture(X[:, 0], X[:, 1], "./graph/origin.png", "origin data")
    refresh_photo('./graph/origin.png')


def generate_arrow_data():
    """
    For button “arrow data”
    Generate and display arrow shape data for clustering
    :return:
    """
    global X
    centers = int(center_num.get())
    points = int(points_number.get())

    center_array = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [1, -1], [2, -2], [3, -3], [4, -4]])
    sample_nums = np.array([10, 9, 8, 7, 6, 9, 8, 7, 6])
    sample_nums *= (points / centers / 70)

    sample_nums = np.tile(sample_nums, centers)
    t = center_array.copy()
    for i in xrange(centers - 1):
        t[:, 0] += 5
        center_array = np.concatenate((center_array, t), axis=0)
    X, y = ds.make_blobs(n_samples=sample_nums, centers=center_array, cluster_std=0.5, n_features=2)

    get_picture(X[:, 0], X[:, 1], "./graph/origin.png", "origin data")
    refresh_photo('./graph/origin.png')


def load_iris_data():
    """
    For button “iris data”
    Load and display iris data sets for cluster analysis
    :return:
    """
    global X
    iris = ds.load_iris()
    X = iris.data[:, [combo_x.current(), combo_y.current()]]
    # y = iris.target
    get_picture(X[:, 0], X[:, 1], "./graph/origin.png", "origin data")
    refresh_photo('./graph/origin.png')


def density_peak_decision_graph():
    """
    For button “decision graph”
    Analyze the generated or loaded data, generate a decision graph and display
    :return:
    """
    global X, dp
    dp = DensityPeak(X, float(r.get()))
    dp.get_decision_graph(float(zscore_threshold.get()))
    outliers_index.set(dp.outliers_index_list.__str__()[1:-1])
    refresh_photo('./graph/origin_with_outliers.png', './graph/decision_graph.png')


def density_peak_clustering():
    """
    For button “DensityPeak”
    After the user selects the appropriate cluster center (outlier point),
    start doing cluster analysis and display the clustering result.
    :return:
    """
    global dp
    dp.clustering(np.fromstring(outliers_index.get(), dtype=int, sep=' '))
    refresh_photo('./graph/clustering.png', './graph/decision_graph.png')


def kmeans_clustering():
    """
    For button “Kmeans”
    Use the Kmeans algorithm to docluster analysis on generated or
    loaded data and display the clustering results
    :return:
    """
    global X
    Kmeans.run_given_data(X, int(k.get()))
    refresh_photo('./graph/origin.png', './graph/clustering.png')


def refresh_photo(left_path=None, right_path=None):
    """
    刷新图片
    :param left_path: 左边图片的文件路径，若为None，则使用空白图片
    :param right_path: 右边图片的文件路径，若为None，则使用空白图片
    :return:
    """
    global im_right, photo_right, im_left, photo_left

    if left_path is None:
        im_left = PIL.Image.open(u"graph/white.png")
        photo_left = PIL.ImageTk.PhotoImage(im_left)
        picture_label_left.configure(image=photo_left)
    else:
        im_left = PIL.Image.open(unicode(left_path))
        photo_left = PIL.ImageTk.PhotoImage(im_left)
        picture_label_left.configure(image=photo_left)

    if right_path is None:
        im_right = PIL.Image.open(u"graph/white.png")
        photo_right = PIL.ImageTk.PhotoImage(im_right)
        picture_label_right.configure(image=photo_right)
    else:
        im_right = PIL.Image.open(unicode(right_path))
        photo_right = PIL.ImageTk.PhotoImage(im_right)
        picture_label_right.configure(image=photo_right)


root = Tk()
root.title("Density Peak  And  Kmeans")
mainframe = ttk.Frame(root, padding="0 0 0 0")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

im_left = PIL.Image.open(u"graph/white.png")
photo_left = PIL.ImageTk.PhotoImage(im_left)
picture_label_left = ttk.Label(mainframe, image=photo_left)
picture_label_left.grid(column=0, row=0, columnspan=5, rowspan=40, sticky=W)

im_right = PIL.Image.open(u"graph/white.png")
photo_right = PIL.ImageTk.PhotoImage(im_right)
picture_label_right = ttk.Label(mainframe, image=photo_right)
picture_label_right.grid(column=5, row=0, columnspan=5, rowspan=40, sticky=E)

X = None

# 设置输入框和按钮
r = StringVar()  # cutoff distance
points_number = StringVar()  # 随机点个数
center_num = StringVar()  # 随机点的簇的个数
file_path = StringVar()
k = StringVar()  # kmeans 的k值
zscore_threshold = StringVar()
outliers_index = StringVar()

'------------------------------------------------------------------------------------------------'
ttk.Label(mainframe, text="points number").grid(column=10, row=2, sticky=W)
points_number_entry = ttk.Entry(mainframe, width=10, textvariable=points_number)
points_number.set('300')
points_number_entry.grid(column=10, row=3, sticky=W)
points_number_entry.focus()

ttk.Label(mainframe, text="clusters number").grid(column=10, row=4, sticky=W)
center_num_entry = ttk.Entry(mainframe, width=10, textvariable=center_num)
center_num.set('3')
center_num_entry.grid(column=10, row=5, sticky=W)
center_num_entry.focus()

ttk.Button(mainframe, text="blob data", command=generate_blob_data).grid(column=10, row=6, sticky=W)
ttk.Button(mainframe, text="arrow data", command=generate_arrow_data).grid(column=10, row=7, sticky=W)
'------------------------------------------------------------------------------------------------'

combo_x_label = ttk.Label(mainframe, text="choose x")
combo_x_label.grid(column=10, row=20, sticky=W)
combo_x = ttk.Combobox(mainframe, width=10, values=["sepal length", "sepal width", "petal length", "petal width"])
combo_x.grid(column=10, row=21, sticky=W)
combo_x.current(0)

combo_y_label = ttk.Label(mainframe, text="choose y")
combo_y_label.grid(column=10, row=22, sticky=W)
combo_y = ttk.Combobox(mainframe, width=10, values=["sepal length", "sepal width", "petal length", "petal width"])
combo_y.grid(column=10, row=23, sticky=W)
combo_y.current(1)

ttk.Button(mainframe, width=10, text="iris data", command=load_iris_data).grid(column=10, row=24, sticky=W)
'------------------------------------------------------------------------------------------------'

ttk.Label(mainframe, text="cutoff distance").grid(column=0, row=40, sticky=E)
r_entry = ttk.Entry(mainframe, width=10, textvariable=r)
r.set('1')
r_entry.grid(column=1, row=40, sticky=W)
r_entry.focus()

ttk.Label(mainframe, text="z-score threshold").grid(column=2, row=40, sticky=E)
zscore_threshold_entry = ttk.Entry(mainframe, width=10, textvariable=zscore_threshold)
zscore_threshold.set('2')
zscore_threshold_entry.grid(column=3, row=40, sticky=W)
zscore_threshold_entry.focus()

ttk.Button(mainframe, width=10, text="decision graph", command=density_peak_decision_graph). \
    grid(column=4, row=40, sticky=E)

ttk.Label(mainframe, text="outliers index").grid(column=0, row=41, sticky=E)
outliers_index_entry = ttk.Entry(mainframe, width=40, textvariable=outliers_index)
outliers_index_entry.grid(column=1, row=41, columnspan=3, sticky=W)
outliers_index_entry.focus()

ttk.Button(mainframe, width=10, text="DensityPeak", command=density_peak_clustering) \
    .grid(column=4, row=41, sticky=E)
'------------------------------------------------------------------------------------------------'

ttk.Label(mainframe, text="k number").grid(column=6, row=40, sticky=E)
k_entry = ttk.Entry(mainframe, width=10, textvariable=k)
k.set('3')
k_entry.grid(column=7, row=40, sticky=W)
k_entry.focus()

ttk.Button(mainframe, width=10, text="Kmeans", command=kmeans_clustering). \
    grid(column=8, row=40, sticky=E)

root.mainloop()
