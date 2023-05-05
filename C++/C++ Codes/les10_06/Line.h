#pragma once
#include "color.h"

class Line
{
protected:
    char c;
    virtual void drawLine(int length);
public:
    Line(char c) : c{ c } {}
    virtual void draw(int length);
};

class LineDown : public Line
{
protected:
    void drawLine(int length) override;
public:
    LineDown(char c) : Line(c) {}
};

class LineColor : public Line
{
protected:
    ConsoleColor color;
public:
    LineColor(char c, ConsoleColor color) 
        : Line(c), color{ color } {}
    void draw(int length) override;
};

class LineColorDown: public LineColor
{
protected:
public:
    LineColorDown(char c, ConsoleColor color)
        : LineColor(c, color) {}
    void drawLine(int length) override;
};
