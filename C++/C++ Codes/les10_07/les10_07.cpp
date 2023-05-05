#include <iostream>
#include <conio.h>
using namespace std;

class Human
{
private:
    string name;
public:
    Human(string name):name(name){}
    void showName() const
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
    void showPosition() const
    {
        cout << position << endl;
    }
};

int main()
{
    cout << "Pointer and References to Base Class" << endl;
    cout << endl;

    cout << "Objects:" << endl;
    cout << "-------" << endl;

    Human human("Human");
    human.showName();                       // Human
    //human.showPositon();                  // compilation error
    //((Employee)human).showPositon();      // compilation error

    Employee employee("Employee", "Positon");
    employee.showName();                    // Employee
    employee.showPosition();                // Positon
    cout << endl;

    cout << "Pointers:" << endl;
    cout << "---------" << endl;

    Human* phHuman = &human;
    phHuman->showName();                    // Human
    //phHuman->showPosition();              // compilation error
    ((Employee*)phHuman)->showName();       // Human
    //((Employee*)phHuman)->showPosition(); // runtime error

    //Employee* peHuman = &human;           // ompilation error
    Employee* peHuman = (Employee*)&human;
    peHuman->showName();                    // Human
    //peHuman->showPosition();              // runtime error
    cout << endl;

    Human* phEmployee = &employee;
    phEmployee->showName();                 // Employee                                                              `
    //phEmployee->showPosition();           // compilation error
    ((Employee*)phEmployee)->showPosition();// Positon

    Employee* peEmployee = &employee;
    peEmployee->showName();                 // Employee
    peEmployee->showPosition();             // Positon
    cout << endl;

    cout << "References:" << endl;
    cout << "-----------" << endl;

    Human& rhHuman = human;
    rhHuman.showName();                     // Human
    //rhHuman.showPosition();               // compilation error
    //((Employee&)phHuman).showPosition();  // runtime error

    //Employee& reHuman = human;            // compilation error
    Employee& reHuman = (Employee&)human;
    reHuman.showName();                     // Human
    //reHuman.showPosition();               // runtime error
    cout << endl;

    Human& rhEmployee = employee;
    rhEmployee.showName();                  // Employee
    //rhEmployee.showPosition();            // compilation error
    ((Employee&)rhEmployee).showPosition(); // Positon
    
    Employee& reEmployee = employee;
    reEmployee.showName();                  // Employee
    reEmployee.showPosition();              // Positon
    cout << endl;

    _getch();
    return 0;
}
