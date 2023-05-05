#include <iostream>
#include <conio.h>
#include "line.h"
using namespace std;

int main()
{
    cout << "Line Drawing" << endl;

    drawLine('-', 10);
    drawLine('=', 5);

    cout << endl;
    _getch();
    return 0;
}

