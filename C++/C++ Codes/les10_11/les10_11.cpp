#include <iostream>
#include <conio.h>
using namespace std;

void printLineNumber(int number)
{
    cout << "number line:" << number << endl;
}

void printLineString(string word)
{
    cout << "word line:\"" << word << "\"" << endl;
}

void printLine(int number)
{
    cout << "line:" << number << endl;
}

void printLine(string word)
{
    cout << "line:\"" << word << "\"" << endl;
}

template <class T>
void print(T item)
{
    cout << typeid(item).name() << " line:" << item << endl;
}

int main()
{
    cout << "Early binding" << endl;
    cout << endl;

    printLineNumber(1000);
    printLineString("1000");
    printLine(1000);
    printLine("1000");
    print(1000);
    print("1000");

    cout << endl;
    _getch();
    return 0;
}
