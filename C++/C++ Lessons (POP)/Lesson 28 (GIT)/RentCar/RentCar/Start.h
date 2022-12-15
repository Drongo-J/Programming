#pragma once
#include<iostream>
#include "Functions.h"
#include "FileHelper.h"
using namespace std;


void Menu() {
	cout << "=====================" << endl;
	cout << "ADMIN 1" << endl;
	cout << "GUEST 2" << endl;
}
void Start() {
	Menu();
	int select = 0;
	cin >> select;
	if (select == 1) {
		cin.ignore();
		cin.clear();
		char* username = new char[100]{};
		cout << "Enter username : " << endl;
		cin.getline(username, 100);
		char* pass = new char[100]{};
		cout << "Enter password : " << endl;
		cin.getline(pass, 100);
		if (isAdmin(username, pass)) {
			system("cls");
			cout << "CARS     1 : " << endl;
			cout << "RENTS    2 : " << endl;
			cout << "ADD CARS 3 : " << endl;
			int s = 0;
			cin >> s;
			if (s == 1) {
				auto cars = LoadData();
				ShowAllCars(cars, global_car_count);
			}
			else if (s == 2) {
				auto users = LoadUsers();
				ShowAllUsers(users, global_user_count);
			}
		}
	}
	else if (select == 2) {
		auto cars = LoadData();
		ShowAllCars(cars, global_car_count);
		cout << "ENTER Car ID : " << endl;
		int id = 0;
		cin >> id;
		auto car = getCarById(cars, global_car_count, id);
		system("cls");
		if (car->isFull) {
			cout << "You Can not select this car" << endl;
			return;
		}
		else {
			ShowCar(car);
			cout << "Enter start date" << endl;
			int start_day = 0;
			cin >> start_day;

			int start_month = 0;
			cin >> start_month;

			int start_year = 0;
			cin >> start_year;
			cout << "Enter end date " << endl;
			int end_day = 0;
			cin >> end_day;

			int end_month = 0;
			cin >> end_month;

			int end_year = 0;
			cin >> end_year;
			cin.ignore();
			cin.clear();

			int total_days = end_day - start_day;
			cout << "Total Payments : " << total_days * car->pricePerDay << "$" << endl;

			cout << "ENTER your own info" << endl;
			cout << "Enter name and surname : " << endl;
			char* fullname = new char[100]{};
			cin.getline(fullname, 100);
			User* user = new User{ car->id,fullname,car->model,__DATE__ };
			car->isFull = true;
			cout << "Your rent process completed successfully" << endl;
			WriteCarsToFile(cars, global_car_count);


			auto users = LoadUsers();
			users=AddUser(users, global_user_count, user);
			WriteUsersToFile(users, global_user_count);

		}

	}

}
