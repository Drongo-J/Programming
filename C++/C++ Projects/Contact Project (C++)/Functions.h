#pragma once

#include <conio.h>
#include <iostream>
#include "Entities.h"

using namespace std;

void ColorTextRed()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 12);
}

void ColorTextGreen()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 10);
}

void ColorTextLightBlue()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 11);
}

void ColorTextPink()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 13);
}

void ColorTextYellow()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 14);
}

void ColorTextBlue()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 9);
}

void ShowMenu()
{
	ColorTextYellow();
	cout << "\n ======== MAIN MENU ========" << endl;
	cout << "\n    Show All Contacts   1" << endl;
	cout << "    Show Contacts A-Z   2 " << endl;
	cout << "    Show Contacts Z-A   3 " << endl;
	cout << "    Add New Contact     4 " << endl;
	cout << "    Delete Contact      5 " << endl;
	cout << "    Search Contact      6 " << endl;
	cout << "\n ===========================" << endl;
}

void GoBackToMenu()
{
	cout << "\n";
	system("pause");
	system("cls");
	ShowMenu();
}

void ShowHuman(const Human& human) {
	cout << " Name : " << human.name << endl;
	cout << " Mobile Phone Number : " << human.phonenumber << endl;
	cout << " Date of creation : " << human.createdDate << " " << human.createdTime << endl;
}

void ShowAll(const Contact& contact) {
	ColorTextYellow();
	if (contact.count != 0)
	{
		cout << "\n ================ CONTACTS =================" << endl;
		cout << "\n";
		for (size_t i = 0; i < contact.count; i++)
		{
			cout << " -------------------------------------------" << endl;
			ShowHuman(*contact.humans[i]);
		}
		cout << " -------------------------------------------" << endl;
		cout << "\n ===========================================" << endl;
	}
	else
	{
		ColorTextRed();
		cout << "\n There is no one in the contact." << endl;
	}
}

void GoToRowColumn(int row_position, int col_position)
{
	HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
	int x_position = col_position, y_position = row_position;
	COORD screen;
	HANDLE hOutput = GetStdHandle(STD_OUTPUT_HANDLE);
	screen.X = x_position;
	screen.Y = y_position;
	SetConsoleCursorPosition(hOutput, screen);
}

char* LowerCase(char* str)
{
	int l = strlen(str);
	char* newstr = new char[l + 1]{};
	for (int x = 0; x < l; x++)
	{
		if (str[x] >= 65 && str[x] <= 90)
		{
			newstr[x] = str[x] + 32;
		}
		else
		{
			newstr[x] = str[x];
		}
	}
	newstr[l + 1] = '\0';
	return newstr;
}

char* UpperCase(char* str)
{
	int l = strlen(str);
	char* newstr = new char[l + 1]{};
	for (int x = 0; x < l; x++)
	{
		if (str[x] >= 97 && str[x] <= 122)
		{
			newstr[x] = str[x] - 32;
		}
		else
		{
			newstr[x] = str[x];
		}
	}
	newstr[l + 1] = '\0';
	return newstr;
}


bool IsSuffix(char* name, char* word)
{
	int l_name = strlen(name);
	int l_word = strlen(word);
	int counter = 0;
	name = LowerCase(name);
	word = LowerCase(word);
	counter = 0;
	for (int x = 0; x < l_name; x++)
	{
		counter = 0;
		for (int y = 0; y < l_word; y++)
		{
			if (name[x + y] == word[y])
			{
				counter++;
			}
		}
		if (counter == l_word)
		{
			return true;
		}
	}
	return false;
}

bool IsPrefixLetter(char* name, char* word)
{
	int l = strlen(word);
	char* name_lowercase = LowerCase(name);
	char* word_lowercase = LowerCase(word);
	for (int x = 0; x < l; x++)
	{
		if (name_lowercase[x] != word_lowercase[x])
		{
			return false;
		}
	}
	return true;
}

bool ExistInArray(int* arr, int size, int number)
{
	for (int x = 0; x < size; x++)
	{
		if (arr[x] == number)
		{
			return true;
		}
	}
	return false;
}

char* AddPlusIfNeeded(char* phone_number);
void ShowAllForGetch(Contact& contact, char* word)
{
	cout << endl;
	int l = 0;
	int counter = 0;
	int index = 0;
	int* arr = new int[index] {};
	// First displaying contacts which begins with searched word
	for (int x = 0; x < contact.count; x++)
	{
		l = strlen(contact.humans[x]->name);
		for (int y = 0; y < l; y++)
		{
			if (IsPrefixLetter(contact.humans[x]->name, word) || IsPrefixLetter(contact.humans[x]->phonenumber, word))
			{
				ColorTextYellow();
				counter++;
				cout << "\n -------------------------------------------" << endl;
				ShowHuman(*contact.humans[x]);
				arr[index] = x;
				index++;
				cout << " -------------------------------------------" << endl;
				break;
			}
		}
	}
	// Then showing the rest of them
	for (int x = 0; x < contact.count; x++)
	{
		l = strlen(contact.humans[x]->name);
		for (int y = 0; y < l; y++)
		{
			if (IsSuffix(contact.humans[x]->name, word) || IsSuffix(contact.humans[x]->phonenumber, word))
			{
				// Not to show the same person again
				if (!ExistInArray(arr, index, x))
				{
					ColorTextYellow();
					counter++;
					cout << "\n -------------------------------------------" << endl;
					ShowHuman(*contact.humans[x]);
					cout << " -------------------------------------------" << endl;
					break;
				}
			}
		}
	}
	if (counter == 0)
	{
		ColorTextRed();
		cout << "\n No results match your search :(" << endl;
	}
}

void SearchEngine(Contact& contact)
{
	ColorTextYellow();
	cout << "\n - - Press ENTER to finish the search - -" << endl;
	cout << "\n Search someone : ";
	char* word = new char[100]{};
	int i = 0;
	cin.ignore();
	cin.clear();

	while (ShowCursor(false) >= 0);
	ShowCursor(false);

	while ((word[i] = _getch()) != '\r')
	{
		GoToRowColumn(3, i + 18);
		if (int(word[i]) == 8) // Backspace
		{
			if (i > 0)
			{
				word[i] = NULL;
				word[i - 1] = NULL;
				cout << "\b \b";
				i--;
				if (i == 0)
				{
					ColorTextYellow();
					system("cls");
					cout << "\n - - Press ENTER to finish the search - -" << endl;
					cout << "\n Search someone : ";
				}
				else
				{
					ShowAllForGetch(contact, word);
					GoToRowColumn(3, i + 18);
				}
			}
			GoToRowColumn(3, i + 18);
		}
		else
		{
			ColorTextYellow();
			system("cls");
			cout << "\n - - Press ENTER to finish the search - -" << endl;
			cout << "\n Search someone : ";
			int no = word[i];
			i++;
			for (int x = 0; x < i; x++)
			{
				cout << word[x];
			}
			ShowAllForGetch(contact, word);
			GoToRowColumn(3, i + 18);
		}
	}
	Sleep(300);
	system("cls");
	ShowMenu();
}


inline bool isDigit(char ch)
{
	if ((int)ch > 57 || (int)ch < 48)
	{
		return false;
	}
	return true;
}

bool isFormatted(char* phone_number)
{
	if (phone_number[0] != '+')
		return false;
	for (int x = 1; x < 3; x++)
	{
		if (!isDigit(phone_number[x]))
			return false;
	}
	if (phone_number[3] != ' ')
		return false;
	for (int x = 4; x < 8; x++)
	{
		if (!isDigit(phone_number[x]))
			return false;
	}
	if (phone_number[8] != ' ')
		return false;
	for (int x = 9; x < 15; x++)
	{
		if (!isDigit(phone_number[x]))
			return false;
	}
	return true;
}

bool is12Digited(char* phone_number)
{
	int l = strlen(phone_number);
	int counter = 0;
	for (int x = 0; x < l; x++)
	{
		if (isDigit(phone_number[x]))
			counter++;
	}

	if (counter == 12)
		return true;
	return false;
}

char* AddPlusIfNeeded(char* phone_number)
{
	if (phone_number[0] != '+')
	{
		int l = strlen(phone_number);
		char* newNumber = new char[l + 2];
		newNumber[0] = '+';
		for (int x = 1; x < l + 2; x++)
		{
			newNumber[x] = phone_number[x - 1];
		}
		newNumber[l + 2] = '\0';
		phone_number = newNumber;
		newNumber = nullptr;
		return phone_number;
	}
	return phone_number;
}

int numberOfSpaces(const char* phone_number)
{
	int counter = 0;
	int l = strlen(phone_number);
	for (int x = 0; x < l; x++)
	{
		if (phone_number[x] == ' ')
		{
			counter++;
		}
	}
	return counter;
}

char* RemoveSpacesFromNumber(char* phone_number)
{
	int numberOfSpacesV = numberOfSpaces(phone_number);
	int l = strlen(phone_number);
	char* newPhoneNumber = new char[l - numberOfSpacesV + 1]{};
	int index = 0;
	for (int x = 0; x < l + 1; x++)
	{
		if (phone_number[x] != 32)
		{
			newPhoneNumber[index] = phone_number[x];
			index++;
		}
	}
	newPhoneNumber[l - numberOfSpacesV + 1] = '\0';
	phone_number = newPhoneNumber;
	newPhoneNumber = nullptr;
	return phone_number;
}

char* FormatNumber(char* phone_number)
{
	phone_number = AddPlusIfNeeded(phone_number);
	phone_number = RemoveSpacesFromNumber(phone_number);

	char* newPhoneNumber = new char[16]{};
	for (int x = 0; x < 4; x++)
	{
		newPhoneNumber[x] = phone_number[x];
	}
	newPhoneNumber[3] = ' ';
	for (int y = 4; y < 8; y++)
	{
		newPhoneNumber[y] = phone_number[y - 1];
	}
	newPhoneNumber[8] = ' ';
	for (int z = 9; z < 15; z++)
	{
		newPhoneNumber[z] = phone_number[z - 2];
	}
	newPhoneNumber[15] = '\0';
	phone_number = newPhoneNumber;
	newPhoneNumber = nullptr;
	return phone_number;
}

bool UniqueName(Contact& contact, const char* name)
{
	for (int x = 0; x < contact.count; x++)
	{
		if (strcmp(contact.humans[x]->name, name) == 0)
		{
			return false;
		}
	}
	return true;
}

bool UniquePhoneNumber(Contact& contact, const char* phone_number)
{
	for (int x = 0; x < contact.count; x++)
	{
		if (strcmp(contact.humans[x]->phonenumber, phone_number) == 0)
		{
			return false;
		}
	}
	return true;
}

Human* GetNewHuman(Contact& contact)
{
	cout << "\n ================= CREATING A NEW CONTACT ==================" << endl;
	cin.ignore();
	cin.clear();

	char* name = new char[100]{};
	cout << "\n Enter name of contanct : ";
	cin.getline(name, 100);

	char* phonenumber = new char[100]{};
	cout << " Enter phone number of contanct (12 digit) : ";
	cin.getline(phonenumber, 100);
	cout << "\n ===========================================================" << endl;

	phonenumber = FormatNumber(phonenumber);
	if (!is12Digited(phonenumber))
	{
		ColorTextRed();
		cout << "\n The phone number should be 12-digits." << endl;
		cout << " New contact was not created!" << endl;
		return 0;
	}
	else if (!UniqueName(contact, name))
	{
		ColorTextRed();
		cout << "\n There is a contact with this name." << endl;
		cout << " New contact was not created!" << endl;
		return 0;
	}
	else if (!UniquePhoneNumber(contact, phonenumber))
	{
		ColorTextRed();
		cout << "\n There is a contact with this phone number." << endl;
		cout << " New contact was not created!" << endl;
		return 0;
	}
	else
	{
		Human* human = new Human{ name,phonenumber,__DATE__,__TIME__ };
		return human;
	}
}

void AddNewHuman(Contact& contact, Human& human)
{
	if (!isFormatted(human.phonenumber))
	{
		human.phonenumber = FormatNumber(human.phonenumber);
	}

	int count = contact.count;
	auto newhumans = new Human * [count + 1]{};
	for (size_t i = 0; i < count; i++)
	{
		newhumans[i] = contact.humans[i];
	}
	newhumans[count] = new Human{ human };
	contact.humans = newhumans;
	newhumans = NULL;
	contact.count++;
	ColorTextGreen();
	cout << "\n New contact was added successfully!";
}

void SortAToZ(Contact& contact, bool reverse = false) {
	int data = 1;
	if (reverse)
	{
		data = -1;
	}
	for (size_t i = 0; i < contact.count - 1; i++)
	{
		for (size_t k = 0; k < contact.count - i - 1; k++)
		{
			if (strcmp(contact.humans[k]->name, contact.humans[k + 1]->name) == data) {
				auto temp = contact.humans[k];
				contact.humans[k] = contact.humans[k + 1];
				contact.humans[k + 1] = temp;
			}
		}
	}
}

int GetHumanIndexName(Contact& contact, char* name)
{
	int count = contact.count;
	name = LowerCase(name);
	int l = strlen(contact.humans[0]->name);
	char* newName = new char[l + 1]{};
	for (int x = 0; x < count; x++)
	{
		newName = LowerCase(contact.humans[x]->name);
		if (strcmp(newName, name) == 0)
		{
			return x;
		}
	}
	return -1;
}

void DeleteByName(Contact& contact, char* name)
{
	int count = contact.count;
	auto newhumans = new Human * [count - 1]{};
	int indexOFHuman = GetHumanIndexName(contact, name);
	if (indexOFHuman >= 0)
	{
		ColorTextGreen();
		cout << "\n \'" << contact.humans[indexOFHuman]->name << "\' was deleted successfully!" << endl;
		int index = 0;
		for (int x = 0; x < indexOFHuman; x++)
		{
			newhumans[index] = contact.humans[x];
			index++;
		}
		for (int y = indexOFHuman + 1; y < count; y++)
		{
			newhumans[index] = contact.humans[y];
			index++;
		}
		contact.humans = newhumans;
		newhumans = NULL;
		contact.count--;
		Sleep(2000);
		system("cls");
		ShowAll(contact);
		GoBackToMenu();
	}
	else
	{
		ColorTextRed();
		cout << "\n There is no one with this name in the contact." << endl;
		Sleep(2000);
		system("cls");
		ShowMenu();
	}
}

int GetHumanIndexNumber(Contact& contact, const char* phonenumber)
{
	int count = contact.count;
	for (int x = 0; x < count; x++)
	{
		if (strcmp(contact.humans[x]->phonenumber, phonenumber) == 0)
		{
			return x;
		}
	}
	return -1;
}

void DeleteByPhoneNumber(Contact& contact, char* phonenumber)
{

	if (!isFormatted(phonenumber))
	{
		phonenumber = FormatNumber(phonenumber);
	}
	int count = contact.count;
	auto newhumans = new Human * [count - 1]{};
	int indexOFHuman = GetHumanIndexNumber(contact, phonenumber);

	if (indexOFHuman >= 0)
	{
		ColorTextGreen();
		cout << "\n \'" << contact.humans[indexOFHuman]->name << "\' was deleted successfully!" << endl;
		int index = 0;
		for (int x = 0; x < indexOFHuman; x++)
		{
			newhumans[index] = contact.humans[x];
			index++;
		}
		for (int y = indexOFHuman + 1; y < count; y++)
		{
			newhumans[index] = contact.humans[y];
			index++;
		}
		contact.humans = newhumans;
		newhumans = NULL;
		contact.count--;
		Sleep(2000);
		system("cls");
		ShowAll(contact);
		GoBackToMenu();
	}
	else
	{
		ColorTextRed();
		cout << "\n There is no one with this phone number in the contact." << endl;
		Sleep(2000);
		system("cls");
		ShowMenu();
	}
}



