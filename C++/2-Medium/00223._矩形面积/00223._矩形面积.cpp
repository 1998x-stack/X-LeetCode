#include<iostream>
using namespace std;

// 函数：计算矩形面积
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    // 计算两个矩形的面积
    int areaOfSqrA = (C-A) * (D-B);
    int areaOfSqrB = (G-E) * (H-F);
    
    // 检查矩形是否重叠
    int left = max(A, E);
    int right = min(C, G);
    int bottom = max(B, F);
    int top = min(D, H);
    
    // 计算重叠部分的面积
    int overlap = 0;
    if (right > left && top > bottom) {
        overlap = (right - left) * (top - bottom);
    }
    
    // 返回总面积
    return areaOfSqrA + areaOfSqrB - overlap;
}

int main() {
    // 示例：矩形坐标
    int A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2;
    
    // 计算并输出面积
    cout << "Total Area: " << computeArea(A, B, C, D, E, F, G, H) << endl;
    return 0;
}