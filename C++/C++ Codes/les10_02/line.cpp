#include <iostream>
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
