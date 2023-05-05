#include <windows.h>
#include "color.h"

void SetColor(ConsoleColor backColor,
    ConsoleColor textColor)
{
    HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hStdOut,
        (WORD)backColor << 4 | (WORD)textColor);
}

ConsoleColor GetBackColor()
{
    HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO  console;
    GetConsoleScreenBufferInfo(hStdOut, &console);
    return (ConsoleColor)(console.wAttributes >> 4);
}

ConsoleColor GetTextColor()
{
    HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO  console;
    GetConsoleScreenBufferInfo(hStdOut, &console);
    int mask = 15;
    int color = console.wAttributes & mask;
    return (ConsoleColor)color;
}
