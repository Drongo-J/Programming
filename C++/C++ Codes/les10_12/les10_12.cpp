#include <iostream>
#include <conio.h>
using namespace std;

void printNumber(int number)
{
    cout << "number line:" << number << endl;
}

void printDoubleNumber(int number)
{
    cout << number << ":line:" << number << endl;
}

class Line
{
protected:
    int number;
public:
    Line(int number) : number{ number } {}
    virtual void print()
    {
        cout << "number line:" << number << endl;
    }
};

class DoubleLine : public Line
{
public:
    DoubleLine(int number) : Line(number) {}
    void print() override
    {
        cout << number << ":line:" << number << endl;
    }
};

int main()
{
    cout << "Late binding" << endl;
    cout << endl;

    srand(time(0));
    for (int i = 0; i < 8; i++)
    {
        int choice = rand();
        void (*print)(int) = choice % 2 == 0 ? printNumber : printDoubleNumber;
        print(1000);
    }
    cout << endl;

    for (int i = 0; i < 8; i++)
    {
        int choice = rand();
        Line* line = choice % 2 == 0 ? new Line(1000) : new DoubleLine(1000);
        line->print();
        delete line;
    }

    cout << endl;
    _getch();
    return 0;
}
