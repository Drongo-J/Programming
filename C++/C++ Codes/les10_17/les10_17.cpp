#include <iostream>
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

    virtual double calculateSalary() const
    {
        return salary;
    }

    virtual void display() const
    {
        cout << getFirstName() << " " << getLastName() <<
            ", month salary: " << calculateSalary() << endl;
    }

    virtual ~Employee() = 0;
};

Employee::~Employee()
{
    cout << "~Employee" << endl;
}


class Worker : public Employee
{
private:
    char* position = nullptr;
public:
    Worker(const string& firstName, const string& lastName, double salary,
        const char* position)
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

    virtual void display() const override
    {
        cout << getFirstName() << " " << getLastName() <<
            ", " << getPosition() <<
            ", month salary: " << calculateSalary() << endl;
    }

    ~Worker() override
    {
        cout << "~Worker" << endl;
        delete[] position;
    }
};

int main()
{
    cout << "Using pure virtual destructor." << endl;
    cout << endl;

    Employee* employee = new Worker("Kate", "Jordan", 2000, "Senior clerk");
    employee->display();
    delete employee;

    cout << endl;
    _getch();
    return 0;
}
