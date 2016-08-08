# 快速排序 (quick sort)
快速排序是对冒泡排序的改进, 将原序列分成左右两个, 使左边子序列小于右边子序列, 再对左右子序列分别进行快速排序.  (递归实现)
一般选择首个/末尾元素作为左右分组的因子.

快排的时间复杂度是 O(n*logN), 最坏是 O(n^2), 空间复杂度 O(n*logN)

## 快排一趟的算法为
1: 设置两个索引`i`, `j`, 开始时`i = 0`, `j = n - 1`<br>
2: 以第一个元素作为因子, 赋值给`key`, `key = A[i]`<br>
3: 从`j`开始向前搜索, 找到首个元素小于`key`, 索引记作`J`, 与`key`进行交换, `A[i] = A[J]; A[J] = key`<br>
4: 从`i`开始向后搜索, 找到首个元素大于`key`, 索引记作`I`, 与`key`进行交换, `A[J] = A[I]; A[I] = key`<br>
5: 重复`3`, `4` 直到`I == J`, 则一趟快排完成, 此时以`I`或`J`为中轴,`A[0:I-1] <= key`, `A[I+1:n-1] >= key`<br>
6: 分别对`A[0: I-1]` 及 `A[I+1: n-1]` 序列调用快速排序<br>

``` c
static void
quick_sort (int *array, int size)
{
	int i = 0, j = size;
    // 选取首个元素为 key
    int key = array[0];

	// 一趟快排
	while (i < j)
	{
		// j 初始化为 size - 1; 开始向前查找首个小于key的值
		for (--j; array[j] > key && j > i; --j);
		// 交换
		array[i] = array[j];
		array[j] = key;
		// i 初始化为 0 + 1; 开始向后查找首个大于key的值
		for (++i; array[i] < key && i < j; ++i);
		// 交换
		array[j] = array[i];
		array[i] = key;
	}
	if (i == j)
	{
		quick_sort (array, i);
        quick_sort (&array[i+1], size - i - 1);
        return;
	}
}
```
