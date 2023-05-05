#include <iostream>
#include <conio.h>
using namespace std;

class Human
{
private:
    string name;
public:
    Human(string name) :name(name) {}
    virtual void show() const
    {
        cout << name << endl;
    }
};

class Employee : public Human
{
private:
    string position;
public:
    Employee(string name, string position) : Human(name), position(position) {}
    void show() const
    {
        Human::show();
        cout << position << endl;
    }
};

int main()
{
    cout << "Virtual Functions" << endl;
    cout << endl;

    cout << "Objects:" << endl;
    cout << "-------" << endl;

    Human human("Human");
    human.show();                           // Human
    cout << endl;

    Employee employee("Employee", "Positon");
    employee.show();                        // Employee Position
    cout << endl;

    cout << "Pointers:" << endl;
    cout << "---------" << endl;

    Human* phHuman = &human;
    phHuman->show();                        // Human
    cout << endl;

    Employee* peHuman = (Employee*)&human;
    //peHuman->show();                      // runtime error

    Human* phEmployee = &employee;
    phEmployee->show();                     // Employee
    cout << endl;

    Employee* peEmployee = &employee;
    peEmployee->show();                     // Employee Position
    cout << endl;

    _getch();
    return 0;
}
