#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 锯齿迭代器类定义
class ZigzagIterator {
private:
    vector<int>::iterator it1, end1, it2, end2;
    int turn; // 用于交替选择向量

public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        it1 = v1.begin();
        end1 = v1.end();
        it2 = v2.begin();
        end2 = v2.end();
        turn = 0; // 从第一个向量开始
    }

    int next() {
        // 交替从两个向量中取元素
        if (it1 == end1) { // 如果v1已经迭代完成，直接从v2取
            return *it2++;
        } else if (it2 == end2) { // 如果v2已经迭代完成，直接从v1取
            return *it1++;
        } else {
            // 根据turn的值决定从哪个向量取元素，然后更新turn值
            if (turn % 2 == 0) {
                turn++;
                return *it1++;
            } else {
                turn++;
                return *it2++;
            }
        }
    }

    bool hasNext() {
        // 只要任一向量中还有元素，就返回true
        return it1 != end1 || it2 != end2;
    }
};

// 主函数，用于测试
int main() {
    vector<int> v1 = {1, 2};
    vector<int> v2 = {3, 4, 5, 6};
    ZigzagIterator zi(v1, v2);

    while (zi.hasNext()) {
        cout << zi.next() << " ";
    }

    return 0;
}