#include <iostream>
#include <conio.h>
using namespace std;

class Employee
{
private:
    char* firstName = nullptr;
    char* lastName = nullptr;
    double salary;

public:
    Employee(const char* firstName, const char* lastName, double salary) : salary(salary)
    {
        this->firstName = new char[strlen(firstName) + 1];
        strcpy_s(this->firstName, strlen(firstName) + 1, firstName);
        this->lastName = new char[strlen(lastName) + 1];
        strcpy_s(this->lastName, strlen(lastName) + 1, lastName);
    }

    void setFirstName(const char* firstName)
    {
        if (this->firstName != nullptr)
        {
            delete[] this->firstName;
        }
        this->firstName = new char[strlen(firstName) + 1];
        strcpy_s(this->firstName, strlen(firstName) + 1, firstName);
    }

    char* getFirstName() const
    {
        return firstName;
    }

    void setLastName(const char* lastName)
    {
        if (this->lastName != nullptr)
        {
            delete[] this->lastName;
        }
        this->lastName = new char[strlen(lastName) + 1];
        strcpy_s(this->lastName, strlen(lastName) + 1, lastName);
    }

    char* getLastName() const
    {
        return lastName;
    }

    virtual double calculateSalary() const = 0;

    virtual void display() const
    {
        cout << getFirstName() << " " << getLastName() <<
            " month salary: " << calculateSalary() << endl;
    }

    ~Employee()
    {
        cout << "~Employee" << endl;
        delete[] firstName;
        delete[] lastName;
    }
};

double Employee::calculateSalary() const
{
    return salary;
}

class Worker : public Employee
{
private:
    char* position = nullptr;
public:
    Worker(const char* firstName, const char* lastName, const char* position, double salary)
        : Employee(firstName, lastName, salary)
    {
        this->position = new char[strlen(position) + 1];
        strcpy_s(this->position, strlen(position) + 1, position);
    }

    void setPosition(const char* position)
    {
        if (this->position != nullptr)
        {
            delete[] this->position;
        }
        this->position = new char[strlen(position) + 1];
        strcpy_s(this->position, strlen(position) + 1, position);
    }

    char* getPosition() const
    {
        return position;
    }

    double calculateSalary() const override
    {
        return Employee::calculateSalary();
    }

    virtual void display() const override
    {
        cout << getFirstName() << " " << getLastName() <<
            ", " << getPosition() <<
            ", month salary: " << calculateSalary() << endl;
    }

    ~Worker()
    {
        cout << "~Worker" << endl;
        delete[] position;
    }
};

int main()
{
    cout << "Using destructors." << endl;
    cout << endl;

    Employee* employee = new Worker("Kate", "Jordan", "Senior clerk", 2000);
    employee->display();
    delete employee;

    cout << endl;
    _getch();
    return 0;
}
