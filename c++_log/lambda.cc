#include <iostream>
#include <algorithm>

using namespace std;


int main(int argc, char **argv) {
		
		cout << "Hello, World!" << endl;
		int idx = 10;
		int ret = [=] (const int &val) mutable -> int 
		{
				cout << "in lambda, val=" << val << ", idx=" << ++idx << endl;
				++idx; // if no mutable, compiler complain: "error: increment of read-only variable ‘idx’"
				cout << "before return, idx=" << idx << endl;
				return idx;
		}(idx);
		cout << "after lambda, idx=" << idx << endl;
		return 0;
}
