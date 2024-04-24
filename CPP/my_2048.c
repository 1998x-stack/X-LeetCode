// 2048游戏的C语言实现

#include<stdio.h>
/*
    - 作用：`stdio.h`是C语言的一个标准输入输出库，提供了一系列的函数用于数据的输入输出。
    - 常用函数：`printf()`，`scanf()`，`fgets()`，`fputs()`，`fread()`，`fwrite()`等。
*/
#include<string.h>
/*
    - 作用：`string.h`提供了多种操作字符串的函数。
    - 常用函数：`strlen()`用于获取字符串长度，`strcpy()`和`strncpy()`用于复制字符串，`strcat()`用于连接字符串，`strcmp()`和`strncmp()`用于比较字符串等。
*/
#include<stdlib.h>
/*
    - 作用：`stdlib.h`包含了进行内存分配、控制程序执行、生成随机数等多种操作的函数。
    - 常用函数：`malloc()`和`free()`用于动态内存分配和释放，`exit()`用于退出程序，`atoi()`和`atof()`用于将字符串转换为整数和浮点数，`rand()`和`srand()`用于生成随机数等。
*/
#include<time.h>
/*
    - 作用：`time.h`提供了日期和时间处理的函数。
    - 常用函数：`time()`用于获取当前时间，`ctime()`将时间转换为本地时间字符串格式，`difftime()`用于计算两个时间差，`mktime()`用于将结构体转换为时间戳等。
*/
#ifdef _WIN32
#include<windows.h>
/*
     - 作用：`windows.h`是Windows操作系统的主要开发库，提供了大量的API函数调用，涉及窗口管理、系统服务等。
*/
#include<conio.h>
/*
     - 作用：`conio.h`用于进行控制台输入输出操作，这是一个比较旧的C标准库，主要用于MS-DOS和Windows系统。
     - 常用函数：`getch()`用于获取按键输入，但不回显在控制台。
*/
#else
#include<termios.h>
/*
`termios.h`用于UNIX系统中终端I/O接口的设置，可以控制异步通信端口
*/
#include<unistd.h>
/*
     - 作用：`unistd.h`定义了POSIX操作系统API，提供对操作系统POSIX兼容接口的访问。
     - 常用函数：`read()`，`write()`，`close()`，`usleep()`等用于低级I/O操作和其他系统调用。
*/
#endif

#define IS_UP_DOWN(d) (!((d)>>1))
/*
    - 定义：`#define IS_UP_DOWN(d) (!((d)>>1))`
    - 作用：此宏是一个简单的逻辑函数，用于判断一个给定的方向`d`是否是“上”或“下”。这里使用了位右移运算符`>>`，将`d`右移一位后，再取逻辑非`!`。如果`d`的值是0（上）或1（下），则`d >> 1`的结果为0，逻辑非后结果为1（true），否则为false。
    - 示例：如果`d`为0或1，`IS_UP_DOWN(d)`返回true；如果为2或更高，返回false。
*/
#define IS_UP_LEFT(d) (!((d)&1))
/*
    - 定义：`#define IS_UP_LEFT(d) (!((d)&1))`
    - 作用：此宏用来检测一个方向`d`是否是“上”或“左”。通过与运算符`&`和数字1，它检查`d`的最低位是否为0。如果为0（即`d`是偶数），则表示方向是“上”或“左”，返回true；如果为1（即`d`是奇数），则表示方向是“下”或“右”，返回false。
    - 示例：对于`d`值0或2（上或左），`IS_UP_LEFT(d)`返回true；对于1或3（下或右），返回false。
*/
#define WIN_NUMBER 2048
/*
   - 定义：`#define WIN_NUMBER 2048`
   - 作用：定义了一个游戏胜利的条件数字2048。在2048游戏中，当玩家在棋盘上合成出2048这个数字时，玩家胜利。
*/
#define true 1
#define false 0

#define RESET "\033[0m"
#define BOLD "\033[1m"
#define BASE "\033["
#define PADDING "        "
/*
   - 定义：
     - `#define RESET "\033[0m"`：重置所有属性到默认状态。
     - `#define BOLD "\033[1m"`：将文本设置为粗体。
     - `#define BASE "\033["`：ANSI转义序列的基础，用于控制终端的文本格式。
     - `#define PADDING "        "`：定义了一个由八个空格组成的填充字符串。
   - 作用：这些宏主要用于格式化输出到终端的文本。使用ANSI转义码来控制文本的属性（如粗体、颜色等）。例如，`BOLD`可以让随后的文本加粗显示，`RESET`用于清除之前设置的所有格式，使文本回到默认状态。`PADDING`提供了一种简单的方式来添加空白字符，用于美化输出格式。
*/

typedef _Bool bool; // 定义一个布尔类型
typedef int NUMTYPE; // 定义一个整数类型
typedef enum _direction {UP,DOWN,LEFT,RIGHT,NONE} DIRECTION; // 定义一个枚举类型，表示方向
typedef enum _colorCode{
    FG_BLACK = 30,
    FG_BLUE = 34,
    FG_CYAN = 36,
    FG_DARK_GRAY = 90,
    FG_DEFAULT = 39,
    FG_GREEN = 32,
    FG_LIGHT_BLUE = 94,
    FG_LIGHT_CYAN = 96,
    FG_LIGHT_GRAY = 37,
    FG_LIGHT_GREEN = 92,
    FG_LIGHT_MAGENTA = 95,
    FG_LIGHT_RED = 91,
    FG_LIGHT_YELLOW = 93,
    FG_MAGENTA = 35,
    FG_RED = 31,
    FG_WHITE = 97,
    FG_YELLOW = 33,
} COLOR_CODE; // 定义一个枚举类型，表示颜色代码
const COLOR_CODE COLOR[11] = {
    FG_BLACK,
    FG_RED,
    FG_GREEN,
    FG_YELLOW,
    FG_BLUE,
    FG_MAGENTA,
    FG_CYAN,
    FG_LIGHT_GRAY,
    FG_DARK_GRAY,
    FG_LIGHT_RED,
    FG_LIGHT_GREEN
}; // 定义一个颜色数组，用于设置不同数字的颜色
int BEST_SCORE = 0;

// 以下是游戏界面函数
void clearScreen(); // 清空屏幕
void setConsoleCursorPosition(); // 设置控制台光标位置
void showConsoleCursor(bool); // 显示或隐藏控制台光标
void printTitle(); // 打印游戏标题
void printTable(NUMTYPE*, int, int, int); // 打印游戏棋盘
void randGenerate(NUMTYPE*, int); // 生成随机数
void printColoredNumber(NUMTYPE); // 打印带颜色的数字
int Log2(NUMTYPE); // 计算一个数的对数
int moveTable(DIRECTION, NUMTYPE*, int); // 移动棋盘
int getPos(DIRECTION, int, int, int); // 获取指定方向的位置

// 以下是游戏逻辑函数
bool startGame(NUMTYPE*, int); // 开始游戏
bool cmpTable(NUMTYPE*, NUMTYPE*, int); // 比较两个棋盘是否相同
bool getConfirm(NUMTYPE*, int, int, int); // 获取确认
bool confirmQuit(NUMTYPE*, int, int, int); // 确认退出
bool confirmRestart(NUMTYPE*, int, int, int); // 确认重开
bool confirmWinQuit(NUMTYPE*, int, int, int); // 确认胜利退出
bool checkWin(NUMTYPE*, int); // 检查胜利
bool checkGameOver(NUMTYPE*, int); // 检查游戏结束
char getCh(); // 获取按键输入
DIRECTION directionMap(char); // 方向映射


int main(){
    srand(time(NULL)); // 设置随机数种子
    int size = 4; // 棋盘大小
    printTitle(); // 打印游戏标题
    scanf("%d", &size); // 输入棋盘大小
    if(size <= 1)
        size = 4; // 如果输入的大小小于等于1，则设置为默认大小4
    int n = size * size; // 棋盘格子数
    NUMTYPE *table = (NUMTYPE*)malloc(n * sizeof(NUMTYPE)); // 申请棋盘内存
    while(true){
        memset(table, 0, n * sizeof(NUMTYPE)); // 初始化棋盘
        if(!startGame(table, size)) // 开始游戏
            break; // 如果游戏失败，退出游戏
    }
    #ifdef _WIN32
    system("pause"); // Windows系统下暂停
    #else
    getchar(); // UNIX系统下暂停
    #endif
    return 0;
}

void init(NUMTYPE *table, int size){
    randGenerate(table, size);// 初始化棋盘
    randGenerate(table, size);// 初始化棋盘
}

bool startGame(NUMTYPE* table, int size){
    int n = size * size; // 棋盘格子数
    int score = 0; // 分数
    int moves = 0; // 移动次数

    NUMTYPE *before = (NUMTYPE*)malloc(n * sizeof(NUMTYPE)); // 申请内存保存上一步棋盘
    bool isWin = false; // 是否胜利
    bool isRestart = false; // 是否重开
    init(table, size); // 初始化棋盘
    printTable(table, size, score, moves); // 打印棋盘
    while(true){
        char input = getCh();
        if(input == 'q' && confirmQuit(table, size, score, moves)) // 退出游戏
            break;
        if(input == 'r' && confirmRestart(table, size, score, moves)) // 重开游戏
        {
            isRestart = true;
            break;
        }

        DIRECTION direction  = directionMap(input); // 获取方向
        if(direction == NONE) // 如果方向不合法
            continue; // 继续输入

        memcpy(before, table, n * sizeof(NUMTYPE)); // 保存当前棋盘
        score += moveTable(direction, table, size); // 移动棋盘
        if(score > BEST_SCORE) // 更新最高分
            BEST_SCORE = score;
        
        if(!cmpTable(before, table, n)) // 如果棋盘改变且生成新数字
        {
            randGenerate(table, size); // 生成新数字
            moves++; // 移动次数加一
        }

        printTable(table, size, score, moves); // 打印棋盘

        if(!isWin && checkWin(table, n)) // 检查胜利
        {
            printf("\nYou are win!! Congratulations!\n");
            isWin = true;
            if(confirmWinQuit(table, size, score, moves)) // 确认胜利退出
            {
                if(confirmRestart(table, size, score, moves)) // 确认重开
                {
                    isRestart = true;
                }
                break;
            }
        }

        if(checkGameOver(table, size)){
            printf("\nGame Over!\n");
            if(confirmRestart(table, size, score, moves)) // 确认重开
            {
                isRestart = true;
            }
            break;
        }
    }

    free(before);
    return isRestart;
}

void randGenerate(NUMTYPE *table, int size){
    int n = size * size; // 棋盘格子数
    int pos = rand() % n; // 随机位置
    while(table[pos]) // 如果位置已有数字
        pos = rand() % n; // 重新生成位置
    NUMTYPE val = 1 << (((rand() % 10) / 9) + 1); // 随机生成数字
    table[pos] = val; // 在位置上放置数字
}


bool getConfirm(NUMTYPE *table, int size, int score, int moves){
    // 获取确认, 是否继续游戏
    while(true)
    {
        char c = getCh(); // 获取按键输入
        if(c == 'Y' || c == 'y') // 如果输入为Y或y
            return true;
        if(c == 'N' || c == 'n') // 如果输入为N或n
        {
            // 清空屏幕
            showConsoleCursor(false);
            // 设置控制台光标位置
            clearScreen();
            // 打印游戏标题
            printTable(table, size, score, moves);
            return false;
        }
    }
}

bool confirmQuit(NUMTYPE *table, int size, int score, int moves){
    showConsoleCursor(true); // 显示控制台光标
    printf("\nDo you want to quit the game? (Y/N)\n"); // 提示是否退出游戏
    return getConfirm(table, size, score, moves); // 获取确认
}

bool confirmRestart(NUMTYPE *table, int size, int score, int moves){
    showConsoleCursor(true); // 显示控制台光标
    printf("\nDo you want to restart the game? (Y/N)\n"); // 提示是否重开游戏
    return getConfirm(table, size, score, moves); // 获取确认
}

bool confirmWinQuit(NUMTYPE *table, int size, int score, int moves){
    showConsoleCursor(true); // 显示控制台光标
    printf("Continue playing current game? [Y/n] "); // 提示是否退出游戏
    return getConfirm(table, size, score, moves); // 获取确认
}

bool checkWin(NUMTYPE *table, int len){
    // 检查胜利
    for (int i = 0; i < len; i++)
    {
        if(table[i] == WIN_NUMBER) // 如果有数字等于2048
            return true; // 返回胜利
    }
}

bool checkGameOver(NUMTYPE *table, int size){
    // 检查游戏结束
    int n = size * size; // 棋盘格子数
    for(int i = 0; i < n; i++){
        if(!table[i]) // 如果有空格
            return false; // 返回游戏未结束
    }

    // 申请内存保存测试棋盘 便于测试是否可以移动
    NUMTYPE *testTable = (NUMTYPE*)malloc(n * sizeof(NUMTYPE) / sizeof(char));
    for(int i = 0; i < 4; i++){
        memcpy(testTable, table, n * sizeof(NUMTYPE) / sizeof(char)); // 保存当前棋盘
        if(moveTable(i, testTable, size)) // 如果可以移动
        {
            free(testTable); // 释放内存
            return false; // 返回游戏未结束
        }
    }
    free(testTable); // 释放内存
    return true; // 返回游戏结束
}

bool cmpTable(NUMTYPE *table1, NUMTYPE *table2, int len){
    // 比较两个棋盘是否相同
    for(int i = 0; i < len; i++){
        if(table1[i] != table2[i]) // 如果有不同
            return false; // 返回不相同
    }
    return true; // 返回相同
}

int Log2(NUMTYPE x){
    int ans = 0;
    while(x >>= 1)
        ++ans;
    return ans;
}

void printColoredNumber(NUMTYPE num){
    // 打印带颜色的数字
    if(!num)
        printf("│      ");
    else{
        int y = Log2(num) - 1;
        int index = y < 12 ? y - 1 : y % 12 - 1;
        printf("│ %s%s%dm%4d%s ", BOLD, BASE, (int)COLOR[index], num, RESET);

    }
}


void printTable(NUMTYPE *t, int size, int score, int moves)
{
    setConsoleCursorPosition(); // 设置控制台光标位置
    printf("┌───────────────────────────┐\n"); // 打印上边框
    printf("│ %sSCORE: %18d%s │\n", BOLD, score, RESET); // 打印分数
    printf("│ %sBEST SCORE: %13d%s │\n", BOLD, BEST_SCORE, RESET); // 打印最高分
    printf("│ %sMOVES: %18d%s │\n", BOLD, moves, RESET); // 打印移动次数
    printf("└───────────────────────────┘\n"); // 打印下边框
    printf("┌"); // 打印左上角
    for(int i = 0; i < size - 1; i++) printf("──────┬"); // 打印上边框
    printf("──────┐\n"); // 打印右上角
    for(int i = 0; i < size; i++) // 打印每一行
    {
        for(int j = 0; j < size; j++)
        {
            int pos = i * size + j;
            printColoredNumber(t[pos]); // 打印带颜色的数字
        }
        printf("│\n"); // 打印竖线
        if(i == size - 1) break;
        printf("├"); // 打印左边框
        for(int i = 0; i < size - 1; i++) printf("──────┼"); // 打印中间分割线
        printf("──────┤\n"); // 打印右边框
    }
    printf("└"); // 打印左下角
    for(int i = 0; i < size - 1; i++) printf("──────┴"); // 打印下边框
    printf("──────┘\n"); // 打印右下角
}

DIRECTION directionMap(char c){
    // 方向映射
    switch(c){
        case 'w':
        case 'W':
            return UP;
        case 's':
        case 'S':
            return DOWN;
        case 'a':
        case 'A':
            return LEFT;
        case 'd':
        case 'D':
            return RIGHT;
        default:
            return NONE;
    }
}

int getPos(DIRECTION d, int x, int y, int size){
    // 获取指定方向的位置
    switch(d){
        case UP:
            return x * size + y;
        case DOWN:
            return x * size + y;
        case LEFT:
            return y * size + x;
        case RIGHT:
            return y * size + x;
        default:
            return -1;
    }
}

// /**
//  * UP   = 00, DOWN  = 01, >> 1 = 0 -> (j, i)
//  * LEFT = 10, RIGHT = 11, >> 1 = 1 -> (i, j)
//  */
// inline int getPos(DIRECTION direction, int i, int j, int size)
// {
//     if(IS_UP_DOWN(direction)) return j * size + i;
//     else return i * size + j;
// }


int moveTable(DIRECTION direction, NUMTYPE *table, int size){
    int start, end, step; // 起始位置，结束位置，步长
    int score = 0; // 分数

    if(IS_UP_LEFT(direction)){ // 如果是上或左
        start = 0; // 起始位置
        end = size; // 结束位置
        step = 1; // 步长
    }
    else{ // 如果是下或右
        start = size - 1;
        end = -1;
        step = -1;
    }

    for(int i = 0; i < size; i++){
        int p = start;
        for(int j = p + step; step > 0 ? j <= end : j >= end; j += step){
            int pos = getPos(direction, i, j, size); // 获取位置
            if(!table[pos]) // 如果位置为空
                continue; // 继续下一个位置
            int next = getPos(direction, i, p, size); // 获取下一个位置
            if(table[next] && (table[next] ^ table[pos]))
            {
                // 如果下一个位置不为空且不相等
                p += step; // 移动到下一个位置
                table[getPos(direction, i, p, size)] = table[pos]; // 移动数字
                if(p ^ j) // 如果位置改变
                    table[pos] = 0; // 清空原位置
            }
            else
            {
                if(!table[next])
                {
                    // 如果下一个位置为空
                    table[next] = table[pos]; // 移动数字
                }
                else
                {
                    table[next] <<= 1; // 合并数字
                    score += table[next]; // 更新分数
                    p += step; // 移动到下一个位置
                }
                table[pos] = 0; // 清空原位置
            }
        }
    }
    return score; // 返回分数
}


void printTitle()
{
    #ifdef _WIN32
    system("chcp 65001"); // UTF-8
    #endif
    clearScreen();
    printf(PADDING"-----------------------------------\n%s%dm", BASE, (int)FG_LIGHT_GREEN);
    printf(PADDING" █████    █████      ███    █████  \n");
    printf(PADDING"██   ██  ██   ██    ████   ██  ██  \n");
    printf(PADDING"█     █  █    ██    █ ██   ██   ██ \n");
    printf(PADDING"█     █  █     █   ██ ██   ██   ██ \n");
    printf(PADDING"██   ██  █     █   █  ██    █████  \n");
    printf(PADDING"███ ██   █     █  ██  ██   ███████ \n");
    printf(PADDING"   ██    █     █ ██   ██   █    ██ \n");
    printf(PADDING"  ██     █     █ ████████ ██     █ \n");
    printf(PADDING"███      █    ██      ██  ██     █ \n");
    printf(PADDING"███      ███ ███      ██   ██   ██ \n");
    printf(PADDING"███████   █████       ██    █████  %s\n", RESET);
    printf(PADDING"-------- By: SpaceSkyNet ----------\n\n");
    printf("Join the numbers and get to the %s%dm2048%s tile!\n", BASE, (int)FG_LIGHT_GREEN, RESET);
    printf("You can press %s%dm`q`%s to quit and press %s%dm`r`%s to restart!\n", BASE, (int)FG_LIGHT_RED, RESET, BASE, (int)FG_LIGHT_RED, RESET);
    printf("You can use %s%dm`WASD`%s to move in playing!\n", BASE, (int)FG_LIGHT_RED, RESET);
    printf("Now, please input the size of the game: ");
}


#ifndef _WIN32 // UNIX系统下实现控制台光标隐藏和按键输入
void setBufferedInput(bool enable) // 设置是否启用缓冲输入
{
	static bool enabled = true; // 是否启用
	static struct termios OLD; // 旧的终端设置
	struct termios NEW; // 新的终端设置

	if (enable && !enabled) // 如果启用且未启用
    {
		// restore the former settings
        // 恢复以前的设置
		tcsetattr(STDIN_FILENO, TCSANOW, &OLD);
		// set the new state
        // 设置新状态
		enabled = true;
	}
    else if (!enable && enabled) 
    {
		// get the terminal settings for standard input
        // 获取标准输入的终端设置
		tcgetattr(STDIN_FILENO, &NEW);
		// we want to keep the old setting to restore them at the end
        // 我们希望保留旧的设置，以便在最后恢复它们
		OLD = NEW;
		// disable canonical mode (buffered i/o) and local echo
        // 禁用规范模式（缓冲输入/输出）和本地回显
		NEW.c_lflag &= (~ICANON & ~ECHO);
		// set the new settings immediately
        // 立即设置新设置
		tcsetattr(STDIN_FILENO, TCSANOW, &NEW);
		// set the new state
        // 设置新状态
		enabled = false;
	}
}
#endif
char getCh()
{
#ifdef _WIN32
    return getch(); // 获取按键输入
#else
    setBufferedInput(false); // 设置不启用缓冲输入
    char c = getchar(); // 获取按键输入
    setBufferedInput(true); // 设置启用缓冲输入
    return c;
#endif
}
void showConsoleCursor(bool show)
{
#ifdef _WIN32
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE); // 获取控制台句柄
    CONSOLE_CURSOR_INFO cci; // 控制台光标信息
    GetConsoleCursorInfo(consoleHandle, &cci); // 获取控制台光标信息
    cci.bVisible = show; // show/hide cursor // 显示/隐藏光标
    SetConsoleCursorInfo(consoleHandle, &cci); // 设置控制台光标信息
#else
    printf(show ? "\033[?25h" : "\033[?25l"); // show/hide cursor // 显示/隐藏光标
#endif
}
void clearScreen()
{
#ifdef _WIN32
    system("cls"); // Windows系统下清空屏幕
#else
    system("clear"); // UNIX系统下清空屏幕
#endif    
}
void setConsoleCursorPosition()
{
#ifdef _WIN32
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE); // 获取控制台句柄
    COORD cur = {0, 0}; // 控制台光标位置
    showConsoleCursor(false); // 隐藏控制台光标
    SetConsoleCursorPosition(consoleHandle, cur); // 设置控制台光标位置
#else
    printf("\033[0m\033[2J\033c"); // 设置控制台光标位置
#endif
}