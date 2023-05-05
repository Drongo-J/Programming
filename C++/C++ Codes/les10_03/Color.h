#pragma once
enum class ConsoleColor
{
    Black,
    Blue,
    Green,
    Aqua,
    Red,
    Purple,
    Yellow,
    White,
    Gray,
    LightBlue,
    LightGreen,
    LightAqua,
    LightRed,
    LightPurple,
    LightYellow,
    BrightWhite
};
void SetColor(ConsoleColor backColor, ConsoleColor textColor);
ConsoleColor GetBackColor();
ConsoleColor GetTextColor();
