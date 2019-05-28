密度峰值算法（Clustering by fast search and find of density peaks）由Alex Rodriguez和Alessandro Laio于2014年提出，并将论文发表在Science上。Science上的这篇文章《Clustering by fast search and find of density peaks》主要讲的是一种基于密度的聚类方法，基于密度的聚类方法的主要思想是寻找被低密度区域分离的高密度区域。

密度峰值算法(DPCA)也基于这样的假设：

（1）类簇中心点的密度大于周围邻居点的密度；

（2）类簇中心点与更高密度点之间的距离相对较大。因此，DPCA主要有两个需要计算的量：第一，局部密度![](https://latex.codecogs.com/png.latex?%5Crho%20_%7Bi%7D)；第二，与高密度点之间的距离![](https://latex.codecogs.com/png.latex?\delta&space;_{i})。
