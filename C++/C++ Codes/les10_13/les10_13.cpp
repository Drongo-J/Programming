#include <iostream>
#include <conio.h>
using namespace std;

class Employee
{
private:
    string firstName;
    string lastName;
public:
    Employee(const string& firstName, const string& lastName) 
        : firstName(firstName), lastName(lastName)
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
            " month salary: " << calculateSalary() << endl;
    }
};

class Manager : public Employee
{
private:
    double salary;
    double bonus;
public:
    Manager(const string& firstName, const string& lastName,
        double salary, double bonus) : Employee(firstName, lastName)
    {
        setSalary(salary);
        setBonus(bonus);
    }

    void setSalary(double salary)
    {
        this->salary = salary < 0.0 ? 0.0 : salary;
    }

    double getSalary() const
    {
        return salary;
    }

    void setBonus(double bonus)
    {
        this->bonus = bonus < 0.0 ? 0.0 : bonus;
    }

    double getBonus() const
    {
        return bonus;
    }

    double calculateSalary() const override
    {
        return getSalary() + getBonus();
    }
};

class Worker : public Employee
{
private:
    double hourlyRate;
    double  hoursNumber;
public:
    Worker(const string& firstName, const string& lastName,
        double hourlyRate, double hoursNumber) : Employee(firstName, lastName)
    {
        setHourlyRate(hourlyRate);
        setHoursNumber(hoursNumber);
    }

    void setHourlyRate(double hourlyRate)
    {
        this->hourlyRate = hourlyRate < 0.0 ? 0.0 : hourlyRate;
    }

    double getHourlyRate() const
    {
        return hourlyRate;
    }

    void setHoursNumber(double hoursNumber)
    {
        this->hoursNumber = hoursNumber < 0.0 ? 0.0 : hoursNumber;
    }

    double getHoursNumber() const
    {
        return hoursNumber;
    }

    double calculateSalary() const override
    {
        return getHourlyRate() * getHoursNumber();
    }
};

class Agent : public Employee
{
private:
    double sales;
    double percent;
public:
    Agent(const string& firstName, const string lastName,
        double sales, double percent) : Employee(firstName, lastName)
    {
        setSales(sales);
        setPercent(percent);
    }

    void setSales(double sales)
    {
        this->sales = sales < 0.0 ? 0.0 : sales;
    }

    double getSales() const
    {
        return sales;
    }

    void setPercent(double percent)
    {
        this->percent = percent < 0.0 ? 0.0 : percent;
    }

    double getPercent() const
    {
        return percent;
    }

    double calculateSalary() const override
    {
        return getSales() * getPercent() / 100.0;
    }

    virtual void display() const override
    {
        cout << getFirstName() << " " << getLastName() <<
            " sales: " << sales <<
            " month salary: " << calculateSalary() << endl;
    }
};

int main()
{
    cout << "Abstract class. Pure virtual functions." << endl;
    cout << endl;

    Employee* employees[3];
    employees[0] = new Manager("Bob", "Smith", 1500, 500);
    employees[1] = new Worker("Kate", "Jordan", 140, 8);
    employees[2] = new Agent("Jack", "Peterson", 30000, 5);

    for (auto item : employees)
    {
        item->display();
    }

    for (auto item : employees)
    {
        delete item;
    }

    cout << endl;
    _getch();
    return 0;
}
