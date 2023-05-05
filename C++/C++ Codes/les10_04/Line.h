#pragma once

class Line
{
protected:
    char c;
    virtual void drawLine(int length);

public:
    Line(char c) : c{ c } {}

    virtual void draw(int length);
};

