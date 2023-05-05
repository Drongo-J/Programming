#include <iostream>
#include <windows.h>
#include "line.h"
using namespace std;

void drawLine(char c, int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << c;
    }
    cout << endl;
}

void drawLineDown(char c, int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << c;
        cout << endl;
    }
}

void drawLine(char c, int length, ConsoleColor color)
{
    ConsoleColor textColor = GetTextColor();
    ConsoleColor backColor = GetBackColor();

    SetColor(backColor, color);
    drawLine(c, length);
    SetColor(backColor, textColor);
}

void drawLineDown(char c, int length, ConsoleColor color)
{
    ConsoleColor textColor = GetTextColor();
    ConsoleColor backColor = GetBackColor();

    SetColor(backColor, color);
    drawLineDown(c, length);
    SetColor(backColor, textColor);
}
