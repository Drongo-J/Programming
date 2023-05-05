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

class LineDown : public Line
{
protected:
    void drawLine(int length) override;

public:
    LineDown(char c) : Line(c) {}

};


