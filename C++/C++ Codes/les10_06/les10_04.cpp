#include <iostream>
#include <conio.h>
#include "line.h"
using namespace std;

int main()
{
    cout << "Line Drawing" << endl;

    Line* line;

    line = new Line('-');
    line->draw(10);

    delete line;
    line = new Line('=');
    line->draw(5);

    delete line;
    line = new LineDown('*');
    line->draw(5);

    delete line;
    line = new LineColor('-', ConsoleColor::Red);
    line->draw(10);

    delete line;
    line = new LineColorDown('-', ConsoleColor::Green);
    line->draw(5);

    delete line;
    line = new Line('-');
    line->draw(10);

    delete line;
    cout << endl;
    _getch();
    return 0;
}

