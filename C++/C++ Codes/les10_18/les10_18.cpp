#define _USE_MATH_DEFINES

#include <iostream>
#include <iomanip>
#include <sstream>
#include <conio.h>
using namespace std;

string toString(double number, int precision = 0)
{
    stringstream result;
    result << fixed << setprecision(precision) << number;
    return result.str();
}

class Shape
{
public:
    virtual double getPerimeter() const = 0;
    virtual double getArea() const = 0;
    virtual string toString() const
    {
        return "Perimeter: " + ::toString(getPerimeter(), 2) +
            ", Area: " + ::toString(getArea(), 2) + "\n";
    }
};

class Rectangle : public Shape
{
protected:
    double a;
    double b;
public:
    Rectangle() : Rectangle(0, 0)
    {}
    Rectangle(double a, double b)
        : a{ a }, b{ b }
    {}
    double getPerimeter() const override
    {
        return (a + b) * 2;
    }
    double getArea() const override
    {
        return a * b;
    }
    string toString() const override
    {
        return "Rectangle: " + ::toString(a) + ", " + 
            ::toString(b) + "\n\t" +
            Shape::toString();
    }
};

class Triangle : public Shape
{
protected:
    double a;
    double b;
    double c;
public:
    Triangle() :Triangle(0, 0, 0)
    {}
    Triangle(double a, double b, double c)
        : a{ a }, b{ b }, c{ c }
    {}
    double getPerimeter() const override
    {
        return (a + b + c);
    }
    double getArea() const override
    {
        double p = getPerimeter() / 2;
        return sqrt(p * (p - a) * (p - b) * (p - c));
    }
    string toString() const override
    {
        return "Triangle: " + ::toString(a) + ", " + ::toString(b) + 
            ", " + ::toString(c) + "\n\t" +
            Shape::toString();
    }
};

class Circle : public Shape
{
protected:
    double r;
public:
    Circle() : Circle(0)
    {}
    Circle(double r) : r{ r }
    {}
    double getPerimeter() const override
    {
        return 2 * M_PI * r;
    }
    double getArea() const override
    {
        return M_PI * r * r;
    }
    string toString() const override
    {
        return "Circle: " + ::toString(r) + "\n\t" +
            Shape::toString();
    }
};

class Square : public Rectangle
{
public:
    Square() : Square(0)
    {}
    Square(double a) : Rectangle(a, a)
    {}
    string toString() const override
    {
        return "Square: " + ::toString(a) + "\n\t" +
            Shape::toString();
    }
};

class Ring : public Circle
{
protected:
    double inR;
public:
    Ring() : Ring(0, 0)
    {}
    Ring(double r, double inR) : Circle(r), inR(inR)
    {
    }
    double getPerimeter() const override
    {
        return Circle::getPerimeter() + Circle(inR).getPerimeter();
    }
    double getArea() const override
    {
        return Circle::getArea() - Circle(inR).getArea();
    }
    string toString() const override
    {
        return "Ring: " + ::toString(Circle::r) + ", " 
            + ::toString(inR) +"\n\t" +
            Shape::toString();
    }
};

int main()
{
    cout << "Virtual functions" << endl;
    cout << endl;

    Shape* shapes[5];
    shapes[0] = new Rectangle(10, 5);
    shapes[1] = new Triangle(3, 4, 5);
    shapes[2] = new Circle(5);
    shapes[3] = new Square(5);
    shapes[4] = new Ring(5, 1);
    for (auto shape : shapes)
    {
        cout << shape->toString() << endl;
    }

    for (auto shape : shapes)
    {
        delete shape;
    }
    cout << endl;
    _getch();
    return 0;
}
