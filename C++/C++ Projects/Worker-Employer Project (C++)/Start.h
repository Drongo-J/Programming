#pragma once

#include<iostream>
#include "Entities.h"
#include "Functions.h"
#include<Windows.h>
using namespace std;

void ShowIntro() {
	ShowMenu();
	while (true)
	{
		cout << "\n Enter your choice : ";
		char select = ' ';
		cin >> select;
		if (select == 'w' || select == 'W') {
			system("cls");
			cin.ignore();
			cin.clear();
			cout << "\n ======== REGISTRATION ======== " << endl;
			cout << "\n Enter your username : ";
			char* username = new char[100]{};
			cin.getline(username, 100);

			auto worker = isWorkerExist(workers, 2, username);
			if (worker != nullptr) 
			{
				while (true)
				{
					system("cls");
					cout << "\n  Worker : " << worker->fullname << endl;
					ShowWorkerMenu(worker);
					cout << "\n Enter your choice (To go back to main menu, press 0) : ";
					int select = 0;
					cin >> select;
					if (select == 0)
					{
						ShowMenu();
						break;
					}
					else if (select == 1)
					{
						if (adv_count == 0)
						{
							system("cls");
							ColorTextRed();
							cout << "\n There is no advertisement." << endl;
							Sleep(2000);
							ShowWorkerMenu(worker);
						}
						else
						{
							system("cls");
							ShowAllADS(employers, 1);
							cout << "\n ===========================" << endl;
							cout << "\n Select advertisement ID for BID : ";
							int id = 0;
							cin >> id;
							BidToAds(employers, 1, worker, id);
							Sleep(2000);
							ShowWorkerMenu(worker);
						}
					}
					else if (select == 2) {
						auto cv = getNewCV();
						worker->cv = cv;
						ColorTextGreen();
						cout << "\n Your CV was successfully created!" << endl;
						Sleep(2000);
						ShowWorkerMenu(worker);;
					}
					else if (select == 3) {
						ShowNotifications(worker);
						ShowWorkerMenu(worker);
					}
					else if (select == 4) {
						if (worker->cv != nullptr)
						{
							ShowCV(worker->cv);
							cout << endl;
							system("pause");
							ShowWorkerMenu(worker);
						}
						else
						{
							system("cls");
							ColorTextRed();
							cout << "\n You have not created a CV yet." << endl;
							Sleep(2000);
							ShowWorkerMenu(worker);
						}
					}
					else
					{
						IncorrectInput();
						break;
					}
				}
			}
			else 
			{
				system("cls");
				ColorTextRed();
				cout << "\n This user does not exist!" << endl;
				Sleep(2000);
				ShowMenu();
			}
		}
		else if (select == 'e' || select == 'E') {
			system("cls");
			cin.ignore();
			cin.clear();

			cout << "\n ======== REGISTRATION ======== " << endl;
			cout << "\n Enter your username : ";
			char* username = new char[100]{};
			cin.getline(username, 100);

			auto employer = isEmployerExist(username, 1);
			if (employer != nullptr) {
				while (true)
				{
					system("cls");
					cout << "\n  Employer : " << employer->fullname << endl;
					ShowEmployerMenu();
					cout << "\n Enter your choice (To go back to main menu, press 0) : ";
					int select = 0;
					cin >> select;
					if (select == 0)
					{
						ShowMenu();
						break;
					}
					else if (select == 1) 
					{
						system("cls");
						auto ads = getNewAD();
						AddADToEmployer(employer, ads);
						ShowEmployerMenu();
					}
					else if (select == 2) 
					{
						
						if (ThereIsApplier(employer))
						{
							ShowAllAppliers(employer);
							cout << "\n Who do you hire ? " << endl;

							cout << " Enter id of the advertisement : ";
							int id_of_advertisement = 0;
							cin >> id_of_advertisement;

							cin.ignore();
							cin.clear();
							cout << " Enter full name of the applier : ";
							char* name_of_applier = new char[100] {};
							cin.getline(name_of_applier,100);

							cout << " Enter your message to applier : ";
							char* message = new char[100]{};
							cin.getline(message, 100);

							HireApplier(employer, name_of_applier, id_of_advertisement, message);
							ShowEmployerMenu();
						}
						else
						{
							system("cls");
							ColorTextRed();
							cout << "\n There is not an applier yet." << endl;
							Sleep(2000);
							ShowEmployerMenu();
						}
					}
					else
					{
						IncorrectInput();
						break;
					}
				}
			}
			else {
				system("cls");
				ColorTextRed();
				cout << "\n This employer does not exist!" << endl;
				Sleep(2000);
				ShowMenu();
			}
		}
		else 
		{
			IncorrectInput();
		}
	}
}