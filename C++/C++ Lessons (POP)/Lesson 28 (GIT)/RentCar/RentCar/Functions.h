#pragma once
#include<iostream>
#include "Entities.h"
#include "FileHelper.h"
using namespace std;
int car_count = 3;
Car** cars = new Car * [car_count] {
	new Car{ 1,new char[] {"Bentley Continental"},false,350,Date{0,0,0},Date{0,0,0} },
		new Car{ 2,new char[] {"Mercedes 63 AMG"},true,280,Date{0,0,0},Date{0,0,0} },
		new Car{ 3,new char[] {"Rolls Royce Ghost"},false,550,Date{0,0,0},Date{0,0,0} },
};

int user_count = 1;
User** users = new User * [1]{
		new User{2,new char[] {"Rafiq Rafiqli"},new char[] {"Mercedes 63 AMG"},__DATE__}
};


Car** LoadData() {
	Car** car_s = nullptr;
	if (isExist("cars.bin")) {
		car_s = ReadFromFile();
	}
	else {
		WriteCarsToFile(cars, 3);
		car_s = ReadFromFile();
	}
	return car_s;
}

User** LoadUsers() {
	User** user_s = nullptr;
	if (isExist("users.bin")) {
		user_s = ReadUsersFromFile();
	}
	else {
		WriteUsersToFile(users, 1);
		user_s = ReadUsersFromFile();
	}
	return user_s;
}

bool isAdmin(const char* username, const char* pass) {
	if (strcmp(username, "admin") == 0) {

		if (strcmp(pass, "admin") == 0) {
			return true;
		}
		else {
			cout << "Password is incorrect" << endl;
			return false;
		}
	}
	else {
		cout << "Username is incorrect" << endl;
		return false;
	}
}


void ShowCar(const Car* car) {
	cout << "=========CAR INFO==========" << endl;
	cout << "ID : " << car->id << endl;
	cout << "MODEL : " << car->model << endl;
	cout << "Rented : ";
	if (car->isFull) {
		cout << "YES" << endl;
	}
	else {
		cout << "NO" << endl;
	}
	cout << "Price per day : " << car->pricePerDay << "$ " << endl;
	cout << "Date start : " << car->start.day << "/" << car->start.month << "/" << car->start.year << endl;
	cout << "Date end : " << car->end.day << "/" << car->end.month << "/" << car->end.year << endl;
}

void ShowAllCars(Car** cars, int count) {
	for (size_t i = 0; i < count; i++)
	{
		ShowCar(cars[i]);
	}
}

void ShowUser(const User*user) {
	cout << "RENT INFO : " << user->fullname << "  " << user->car_id << "  " << user->car_model << "  " << user->takeCarDate << endl;
}

void ShowAllUsers(User** users, int count) {
	for (size_t i = 0; i < count; i++)
	{
		ShowUser(users[i]);
	}
}

Car* getCarById(Car** cars, const int& count, const int& id) {
	for (size_t i = 0; i < count; i++)
	{
		if (cars[i]->id == id) {
			return cars[i];
		}
	}
	return  nullptr;
}
User* getUserByFullname(User** users, const int& count, const char*fullname) {
	for (size_t i = 0; i < count; i++)
	{
		if (strcmp(users[i]->fullname,fullname)==0) {
			return users[i];
		}
	}
	return  nullptr;
}


User** AddUser(User** users, int& count, User* newuser) {
	auto newusers = new User * [count + 1]{};
	for (size_t i = 0; i < count; i++)
	{
		newusers[i] = users[i];
	}
	newusers[count] = newuser;

	users = newusers;
	newusers = nullptr;
	count++;
	return users;
}