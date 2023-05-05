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
