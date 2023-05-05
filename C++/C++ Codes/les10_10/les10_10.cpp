#include <iostream>
#include <iomanip>
#include <sstream>
#include <conio.h>
using namespace std;

class BaseAccount
{
protected:
    int sum;
    int period;
    double percent;

public:
    BaseAccount(int sum, int period, double percent)
        : sum(sum), period(period), percent(percent)
    {}

    BaseAccount() : BaseAccount(0,0,0)
    {}

    virtual int income() const
    {
        int newSum = sum;
        for (int i = 0; i < period; i++)
        {
            int newIncome = round(newSum * percent / 100);
            newSum += newIncome;
        }
        return newSum - sum;
    }

    virtual string toString() const
    {
        stringstream result;
        result << fixed << setprecision(2)
            << "sum:" << sum << ", "
            << "period:" << period << ", "
            << "percent:" << percent;
        return result.str();
    }

    friend ostream& operator<< (ostream& output, const BaseAccount& account)
    {
        output << account.toString();
        return output;
    }
};

class LongAccount : public BaseAccount
{
protected:
    int startPeriod;

public:
    LongAccount(int sum, int period, double percent, int startPeriod)
        : BaseAccount(sum, period, percent), startPeriod(startPeriod)
    {}

    int income() const
    {
        int newSum = sum;
        for (int i = startPeriod; i < period; i++)
        {
            int newIncome = round(newSum * percent / 100);
            newSum += newIncome;
        }
        return newSum - sum;
    }

    string toString() const
    {
        return BaseAccount::toString()
            + ", startPeriod:" + to_string(startPeriod);
    }

    friend ostream& operator<< (ostream& output, const LongAccount& account)
    {
        output << account.toString();
        return output;
    }
};

class SpecialAccount : public BaseAccount
{
protected:
    double increment;

public:
    SpecialAccount(int sum, int period, double percent, double increment)
        : BaseAccount(sum, period, percent), increment(increment)
    {}

    virtual int income() const
    {
        int newSum = sum;
        double newPercent = percent;
        for (int i = 0; i < period; i++)
        {
            int newIncome = round(newSum * newPercent / 100);
            newSum += newIncome;
            newPercent += increment;
        }
        return newSum - sum;
    }

    string toString() const
    {
        stringstream result;
        result << fixed << setprecision(2)
            << ", increment:" << increment;
        return BaseAccount::toString() + result.str();
    }

    friend ostream& operator<< (ostream& output, const SpecialAccount& account)
    {
        output << account.toString();
        return output;
    }
};

int main()
{
    cout << "Virtual Functions for Accounts" << endl;
    cout << endl;

    BaseAccount* accounts[3];
    accounts[0] = new BaseAccount(1000, 12, 5);
    accounts[1] = new LongAccount(1000, 12, 10, 6);
    accounts[2] = new SpecialAccount(1000, 12, 2, 0.6);
    for (auto item : accounts)
    {
        cout << item->toString() << endl
            << "income:" << item->income() << endl;
    }

    for (auto item : accounts)
    {
        delete item;
    }
    cout << endl;
    _getch();
    return 0;
}
