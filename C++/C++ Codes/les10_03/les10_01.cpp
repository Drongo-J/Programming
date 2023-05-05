#include <iostream>
#include <conio.h>
#include "line.h"
using namespace std;

int main()
{
    cout << "Line Drawing" << endl;

    drawLine('-', 10);
    drawLine('=', 5);

    drawLineDown('*', 5);

    drawLine('-', 10, ConsoleColor::Red);
    drawLineDown('=', 5, ConsoleColor::Green);
    drawLine('-', 10);

    cout << endl;
    _getch();
    return 0;
}

