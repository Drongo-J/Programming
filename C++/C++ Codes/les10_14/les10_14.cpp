#include <iostream>
//#include <iomanip>
#include <conio.h>
using namespace std;

class Employee
{
private:
    string firstName;
    string lastName;
    double salary;

public:
    Employee(const string& firstName, const string& lastName, double salary)
        : firstName(firstName), lastName(lastName), salary(salary)
    {}

    void setFirstName(const string& firstName)
    {
        this->firstName = firstName;
    }

    string getFirstName() const
    {
        return firstName;
    }

    void setLastName(const string& lastName)
    {
        this->lastName = lastName;
    }

    string getLastName() const
    {
        return lastName;
    }

    virtual double calculateSalary() const = 0;

    virtual void display() const
    {
        cout << getFirstName() << " " << getLastName() <<
            ", month salary: " << calculateSalary() << endl;
    }
};

double Employee::calculateSalary() const
{
    return salary;
}

class Worker : public Employee
{
public:
    Worker(const string& firstName, const string& lastName, double salary)
        : Employee(firstName, lastName, salary)
    {
    }

    double calculateSalary() const override
    {
        return Employee::calculateSalary();
    }
};

int main()
{
    cout << "Pure virtual function with body." << endl;
    cout << endl;

    Employee* employee = new Worker("Kate", "Jordan", 2000);
    employee->display();
    delete employee;

    cout << endl;
    _getch();
    return 0;
}
