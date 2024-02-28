// 假设 API read4 已经被定义
int read4(char *buf4);

class Solution {
public:
    /**
     * @brief 从文件中读取 n 个字符
     * 
     * @param buf 目标缓冲区
     * @param n 请求读取的字符数
     * @return 实际读取的字符数
     */
    int read(char *buf, int n) {
        int buffer4Count = 0; // read4 返回的字符数
        int buffer4Index = 0; // buffer4 中当前的位置
        char buffer4[4]; // read4 的缓冲区
        
        int readBytes = 0; // 实际读取的字符数
        
        while (n > 0) {
            // 当 buffer4 消费完，调用 read4 读取更多
            if (buffer4Index == buffer4Count) {
                buffer4Count = read4(buffer4);
                buffer4Index = 0;
                // 如果没有读取到字符，结束循环
                if (buffer4Count == 0) break;
            }
            
            // 从 buffer4 复制字符到 buf
            while (n > 0 && buffer4Index < buffer4Count) {
                buf[readBytes++] = buffer4[buffer4Index++];
                n--;
            }
        }
        
        return readBytes;
    }
};