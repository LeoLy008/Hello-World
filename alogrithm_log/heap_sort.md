# 堆排序
堆排序首先构建一个二叉树, 大堆根节点最大, 小堆根节点最小 (对左右子节点大小顺序无要求)<br>
用数组表示堆排序二叉树的关系是:<br> 
+ 假设元素的索引为`idx`, 则
+ 根节点的索引为`(idx - 1) / 2`, 
+ 左右子节点的索引为`idx * 2 + 1`和`idx * 2 + 2`
堆排序满足任意节点的根节点都应大于/小于他子节点的值

堆排序:<br>
+ 构建好堆后, 首个元素即为最大/最小元素
+ 从第二个元素开始, 重建堆, 则第二个元素为剩余元素的最值
+ 依次直至倒数第二的元素
+ 排序完成