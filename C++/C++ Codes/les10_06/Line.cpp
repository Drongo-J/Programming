#include <iostream>
#include "Line.h"
using namespace std;

void Line::draw(int length)
{
    drawLine(length);
}

void Line::drawLine(int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << c;
    }
    cout << endl;
}

void LineDown::drawLine(int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << c;
        cout << endl;
    }
}

void LineColor::draw(int length)
{
    ConsoleColor textColor = GetTextColor();
    ConsoleColor backColor = GetBackColor();
    SetColor(backColor, color);

    drawLine(length);

    SetColor(backColor, textColor);
}

void LineColorDown::drawLine(int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << c;
        cout << endl;
    }
}

