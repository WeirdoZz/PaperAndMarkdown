# Seaborn使用教学

## Line Chart

可以直接调用dataframe来绘制其中所有的数据折线图 必须是数字

```py
plt.figure(figsize=(20,10))
plt.title('Weirdo_lineplot')
sns.lineplot(data=Weirdo_dataframe)
```

![picture 1](images/0d910345846a176294281495380d4f2072fd887a3725ffef1da06fef6343d437.png)  


也可以通过读取dataframe的某一列，来单独对这一列进行绘制

```py
sns.lineplot(data=weirdo_dataframe[column_1],label='column_1')
plt.xlabel('anything')
```

![picture 2](images/b9d2c7fd003c7f671a0fed1afe1c8e85da1bfd0c8e076ef68ecf8040f30efae3.png)  


## barcharts

对dataframe中的某一列数据做跟随索引变化的柱状图 必须是数字

```py
sns.barplot(x=Weirdo_data.index, y=Weirdo_data['column_1'])
plt.ylabel('column_1')
```

![picture 3](images/0952bc508d593ca3802b1e51ce6318415e188f9c7d5183b5baf84bd9b533bf81.png)  

## heapmap

对整张表格进行颜色深浅关联数据大小的图的绘制

annot是设置图中的方块里是否显示数据的值

```py
sns.heatmap(data=Weirdo_data,annot=True)
```

![picture 4](images/29c4e613fc008b8f18c2b290d108a9e9b602199c5b597e8c12302246dd8f17d7.png)  

## scatterplot

### 普通scatterplot

做两列连续数据的相对关系的变化图

```py
sns.scatterplot(x=Weirdo_data['column_1'],y=Weirdo_data['column_2'])
```

![picture 5](images/8eb849b7c84cb9d03ee5c42e7b43f83861fa9528dbdf4b2760e790efb8136e94.png)  

### 带回归线的regeplot

可以在其中加入其对应的回归线

```py
sns.regplot(x=Weirdo_data['column_1'],y=Weirdo_data['column_2'])
```

![picture 6](images/169bcfc7db07aa0623d9c84808ff5f4990cf695e7eec2d4ad761a0cef7513913.png)  

### 对点做分类的scatterplot

可以增加一个参数hue，将某个只有有限值的比如0，1的列赋给它

```py
sns.scatterplot(x=Weirdo_data['column_1'],y=Weirdo_data['column_2'],hue=Weirdo_data('column_3'))
```

![picture 7](images/51993a252d61f06213b9964810bc17c2b11ee10970f2a3130a37dbeb698f5a95.png)  

在该类图像中也可以加入回归线 lmplot

```py
sns.lmplot(x=Weirdo_data['column_1'],y=Weirdo_data['column_2'],hue=Weirdo_data('column_3'))
```

![picture 8](images/4987882a4455eab0c551606b9c4acf20c64387aedaf0b235c1e346c122818b67.png)  

### 将某一列的分布根据某一列分为两份，观察其总体范围的swarmplot

```py
sns.swarmplot(x=Weirdo_data['column_1'],y=Weirdo_data['column_2'])
```

![picture 9](images/55262b5b644a1ae95aa907000dc0279abc6fcdf5037b16e51a43948374e0b6d2.png)  

## distributions

### 直方图 distplot

可以观察某一列出现的值对应的频率变化，其中kde表示是否用曲线

```py
sns.displot(data=Weirdo_data['column_1'],kde=False)
```

![picture 10](images/c9b0cf6e81ea24cfb1e0db4dbeeeb6beaff21313454d9c54be6e9d94e25aa035.png)  


### 曲线形式的直方图 kdeplot

其中参数表示是否对线的下方填色

```py
sns.kdeplot(data=Weirdo_data['column_1'],shade=True)
```

![picture 11](images/afc920b80540473f79b6e3ef1ff87b6be1f3a4e2033ef78e4e36604cda350a5d.png)  


### 2d的kdeplot jointplot

```py
sns.jointplot(x=Weirdo_data['column_1'],y=Weirdo_data['column_2'],kind='kde')
```

![picture 12](images/762e0ae324ca4f6dc23b3a472ce8c80ec2aedc26f208ba76d1dc97ae320a8424.png)  


### 不同列的直方图  

可以在直方图中设置不同的列并设置它们的label来显示它们的legend,这样不同的列的信息就可以出现在同一张直方图中了

```py
sns.distplot(data=Weirdo_data['column_1'],
label="Iris-setosa", kde=False)
sns.distplot(data=Weirdo_data['Petal Length (cm)'],label="Iris-versicolor", kde=False)
sns.distplot(data=Weirdo_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

plt.legend()
```
kdeplot也是同理

![picture 13](images/3e1173be18f328bfc744149cf03db6b5e502769d467913a10687dc97aa02f670.png)  

