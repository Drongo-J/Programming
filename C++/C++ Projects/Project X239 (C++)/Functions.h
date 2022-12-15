#pragma once

#include <iostream>
#include <conio.h>
#include "Structs.h" 
using namespace std;

void ShowEntrance()
{
	cout << "\n ========= Entrance ========= " << endl;
	cout << "\n  Sign In (1) || Sign Up (2) " << endl;
	cout << "\n ============================ " << endl;
}

void GetNewUser()
{
	const int text_size = 100;
	cout << "\n ========= Registration ========= " << endl;
	
	cout << "\n Enter your fullname : ";
	char* fullname = new char[text_size] {};
	cin.getline(fullname, text_size);

	cout << " Enter new gmail name : ";
	char* gmail_name = new char[text_size] {};
	cin.getline(gmail_name, text_size);

	cout << " Enter new password : ";
	char* password = new char[text_size] {};
	//cin.getline(password, text_size);

	int i = 0;
	while ((password[i] = _getch()) != '\r')
	{
		if (int(password[i]) == 8)
		{
			cout << "\b";
		}
		else if (int(password[i]) == 32)
		{
			continue;
		}
		else
		{
			cout << "*";
			i++;
		}
	}

	cout << endl;

	cout << " Confirm your password : ";
	char* confirm_password = new char[text_size] {};
	//cin.getline(confirm_password, text_size);

	int i2 = 0;
	while ((confirm_password[i2] = _getch()) != '\r')
	{
		if (int(confirm_password[i2]) == 8)
		{
			cout << "\b";
		}
		else if (int(confirm_password[i2]) == 32)
		{
			continue;
		}
		else
		{
			cout << "*";
			i2++;
		}
	}

	cout << password << endl;
	cout << confirm_password << endl;

}




void SignUp(AllMails& all_mails, char* mail )
{
	int count = all_mails.mail_quantity;
	Mail** new_mails = new Mail * [count + 1]{};

	for (int x = 0; x < count; x++)
	{
		new_mails[x] = all_mails.mails[x];
	}

	new_mails[count] = new Mail { mail };
	//all_mails = new_mails;
	new_mails = nullptr;
	all_mails.mail_quantity++;
}
