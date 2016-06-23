/*
 * 2016-06-19
 * qucik sort algorithm
 */

#include <stdio.h> // for printf

static void 
print_array (int *array, int size)
{
		int idx = 0;
		printf ("array size:[%d]-->", size);
		for (idx = 0; idx < size; ++idx)
		{
				printf ("[%d]%d ", idx, array[idx]);
		}
		printf ("\n");
}

static void
quick_sort (int *array, int size)
{
		int i = 0, j = size;
		// 选取首个元素为 key
		int key = array[0];
		int round_cnt = 0; //调试, 记录快排趟数
		
		// size limit
		if (size == 1) return;
		print_array(array, size);
		printf ("key is:[%d]\n", key);

		// 一趟快排
		while (i < j)
		{
				++round_cnt;
				printf ("\n第%d次快排, i=[%d], j=[%d]\n", round_cnt, i, j);

				// j 初始化为 size - 1; 开始向前查找首个小于key的值
				for (--j; array[j] > key && j > i; --j);
				printf ("第%d次快排, 从后向前首次查找结束, j=[%d], array[%d]=[%d], i=[%d]\n",
						round_cnt, j, j, array[j], i);
				if (i == j) break;
				// 交换
				array[i] = array[j];
				array[j] = key;
				print_array(array, size);

				// i 初始化为 0 + 1; 开始向后查找首个大于key的值
				for (++i; array[i] < key && i < j; ++i);
				printf ("第%d次快排, 从前向后首次查找结束, i=[%d], array[%d]=[%d], j=[%d]\n",
						round_cnt, i, i, array[i], j);
				if (i == j) break;
				// 交换
				array[j] = array[i];
				array[i] = key;

				print_array(array, size);
		}

		if (i == j)
		{   
				//quick_sort (array, i);
				//quick_sort (&array[i+1], size - i - 1);
				return;
		}
}

int 
main (int argc, char **argv) 
{
		int array[] = {49,38,65,97,76,13,27};
		int a[10];
		printf ("sizeof array:%ld, sizeof a[10]:%ld\n", sizeof(array), sizeof(a));
		quick_sort (array, sizeof(array)/sizeof(int));

		return 0;
}
