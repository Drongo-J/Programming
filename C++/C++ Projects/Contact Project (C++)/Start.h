#pragma once

#include <iostream>
#include <windows.h>
#include <conio.h>
#include "Entities.h"
#include "Functions.h"
using namespace std;

void Start()
{
	Human* h1 = new Human{
		new char[] {"Chevonne Lew"},
		new char[] {"+44 4232 959154"},
		__DATE__,
		__TIME__
	};

	Human* h2 = new Human{
		new char[] {"Madelina Lanford"},
		new char[] {"+44 7361 497981"},
		__DATE__,
		__TIME__
	};

	Human* h3 = new Human{
		new char[] {"Norton Ermintrude"},
		new char[] {"+44 1911 854437"},
		__DATE__,
		__TIME__
	};

	Human* h4 = new Human{
		new char[] {"Felecia Gerry"},
		new char[] {"+44 8911 820111"},
		__DATE__,
		__TIME__
	};

	Human* h5 = new Human{
		new char[] {"Kevin Fletcher"},
		new char[] {"+44 8457 586732"},
		__DATE__,
		__TIME__
	};

	Human* h6 = new Human{
		new char[] {"David Morrison"},
		new char[] {"+44 9911 800183"},
		__DATE__,
		__TIME__
	};

	Human* h7 = new Human{
		new char[] {"Jane Platt"},
		new char[] {"+44 7178 152771"},
		__DATE__,
		__TIME__
	};

	Human* h8 = new Human{
		new char[] {"Andrew Young"},
		new char[] {"+44 5457 039187"},
		__DATE__,
		__TIME__
	};

	Human* h9 = new Human{
		new char[] {"Raymond Babb"},
		new char[] {"+44 4654 347825"},
		__DATE__,
		__TIME__
	};

	Human* h10 = new Human{
		new char[] {"Brendan Caden"},
		new char[] {"+44 7368 147242"},
		__DATE__,
		__TIME__
	};

	Human* h11 = new Human{
		new char[] {"Glenys Horton"},
		new char[] {"+44 0246 287237"},
		__DATE__,
		__TIME__
	};

	Human* h12 = new Human{
		new char[] {"Evafe Moore"},
		new char[] {"+44 2236 684425"},
		__DATE__,
		__TIME__
	};

	Human* h13 = new Human{
		new char[] {"Suzanne Lock"},
		new char[] {"+44 4585 746332"},
		__DATE__,
		__TIME__
	};

	Human* h14 = new Human{
		new char[] {"Mark Llewellyn"},
		new char[] {"+44 3333 435432"},
		__DATE__,
		__TIME__
	};

	Human* h15 = new Human{
		new char[] {"Timose Rothwell"},
		new char[] {"+44 2545 325774"},
		__DATE__,
		__TIME__
	};

	Human* h16 = new Human{
		new char[] {"Timothy Moss"},
		new char[] {"+44 2562 234578"},
		__DATE__,
		__TIME__
	};

	Human* h17 = new Human{
		new char[] {"Evans David"},
		new char[] {"+44 3787 324492"},
		__DATE__,
		__TIME__
	};

	Human* h18 = new Human{
		new char[] {"Nicholas Holmes"},
		new char[] {"+44 4523 345443"},
		__DATE__,
		__TIME__
	};

	Human* h19 = new Human{
		new char[] {"Mary Potts"},
		new char[] {"+44 0246 256244"},
		__DATE__,
		__TIME__
	};

	Human* h20 = new Human{
		new char[] {"Billy Skinner"},
		new char[] {"+44 2236 342353"},
		__DATE__,
		__TIME__
	};

	Human* h21 = new Human{
		new char[] {"Charles Turner"},
		new char[] {"+44 4382 265174"},
		__DATE__,
		__TIME__
	};

	Human* h22 = new Human{
		new char[] {"Tracey Bradshaw"},
		new char[] {"+44 2568 527554"},
		__DATE__,
		__TIME__
	};

	Human* h23 = new Human{
		new char[] {"Lena Cameron"},
		new char[] {"+44 5729 257357"},
		__DATE__,
		__TIME__
	};

	Human* h24 = new Human{
		new char[] {"Billy Moss"},
		new char[] {"+44 6252 457292"},
		__DATE__,
		__TIME__
	};

	Human* h25 = new Human{
		new char[] {"Suresh Jones"},
		new char[] {"+44 3452 346753"},
		__DATE__,
		__TIME__
	};

	Human* h26 = new Human{
		new char[] {"Mariam Cape"},
		new char[] {"+44 3653 463634"},
		__DATE__,
		__TIME__
	};

	auto humans = new Human * [] {h1, h2, h3, h4, h5, h6,
		h7, h8, h9, h10, h11, h12,
		h13, h14, h15, h16, h17, h18,
		h19, h20, h21, h22, h23, h24,
		h25, h26};
	Contact* contact = new Contact{ humans,26 };

	char selection = ' ';
	ShowMenu();
	while (true)
	{
		selection = 0;
		cout << "\n Enter your choice : ";
		cin >> selection;
		system("cls");
		if (selection == '1')
		{
			ShowAll(*contact);
			GoBackToMenu();
		}
		else if (selection == '2')
		{
			cout << "\n =========== SORTED A TO Z (A-Z) =========== " << endl;
			SortAToZ(*contact);
			ShowAll(*contact);
			GoBackToMenu();
		}
		else if (selection == '3')
		{
			cout << "\n =========== SORTED Z TO A (Z-A) =========== " << endl;
			SortAToZ(*contact, true);
			ShowAll(*contact);
			GoBackToMenu();
		}
		else if (selection == '4')
		{
			auto newhuman = GetNewHuman(*contact);
			if (newhuman != 0)
			{
				AddNewHuman(*contact, *newhuman);
				SortAToZ(*contact);
				Sleep(2000);
				system("cls");
				ShowMenu();
			}
			else
			{
				Sleep(2000);
				system("cls");
				ShowMenu();
			}
		}
		else if (selection == '5')
		{
			if (contact->count != 0)
			{
				cout << "\n How do you want to delete the contact ? " << endl;
				cout << " By Name (n) | By Phone Number (p) - ";
				char choice = ' ';
				cin >> choice;

				system("cls");
				cout << "\n =========== DELETING A CONTACT ============" << endl;
				if (choice == 'n' || choice == 'N')
				{
					ShowAll(*contact);
					cin.ignore();
					cin.clear();
					char* name = new char[100]{};
					cout << "\n Enter the name of the contact : ";
					cin.getline(name, 100);
					DeleteByName(*contact, name);
				}
				else if (choice == 'p' || choice == 'P')
				{
					ShowAll(*contact);
					cin.ignore();
					cin.clear();
					char* phonenumber = new char[100]{};
					cout << "\n Enter the phone number of the contact : ";
					cin.getline(phonenumber, 100);
					DeleteByPhoneNumber(*contact, phonenumber);
				}
				else
				{
					system("cls");
					ColorTextRed();
					cout << "\n Incorrect Input!" << endl;
					Sleep(1500);
					system("cls");
					ShowMenu();
				}
			}
			else
			{
				cout << "\n There is no one in the contact." << endl;
			}
		}
		else if (selection == '6')
		{
			SearchEngine(*contact);
		}
		else if (selection > 54 || selection < 49)
		{
			system("cls");
			ColorTextRed();
			cout << "\n Incorrect Input!" << endl;
			Sleep(1500);
			system("cls");
			ShowMenu();
		}
	}
}



