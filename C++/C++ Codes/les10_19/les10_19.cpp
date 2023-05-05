#include <iostream>
#include <conio.h>
using namespace std;

class A
{
public:
    virtual void show(string name, int count) const
    {
        cout << name << " , " << count << endl;
    }
};

class B : public A
{
public:
    virtual void show(string name, int count) const override //final
    {
        cout << name << " : " << count << endl;
    }
};

class C : public B
{
public:
    virtual void show(string name, int count) const override
    {
        cout << name << " => " << count << endl;
    }
};

int main()
{
    cout << "Virtual Functions" << endl;
    cout << endl;

    A* c = new C;
    c->show("a", 1);

    _getch();
    return 0;
}
