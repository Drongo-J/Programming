#pragma once
#include<iostream>
#include "Entities.h"
using namespace std;

bool isExist(const char* filename) {
	FILE* file;
	fopen_s(&file, filename, "rb");
	if (file != nullptr) {
		fclose(file);
		return true;
	}
	return false;
}

//3
// 1
// 5 - model data
// bool
//double
// 10 12 2022
// 12 12 2022


void WriteCarsToFile(Car** cars,int car_count) {
	FILE* file;
	fopen_s(&file, "cars.bin", "wb");

	fwrite(&car_count, sizeof(int), 1, file);//car count

	for (size_t i = 0; i < car_count; i++)
	{
		fwrite(&cars[i]->id, sizeof(int), 1, file);// car id
		int l = strlen(cars[i]->model); 
		fwrite(&l, sizeof(int), 1, file); //model length 
		fwrite(cars[i]->model, sizeof(char), l, file);
		//bool
		fwrite(&cars[i]->isFull, sizeof(bool), 1, file);
		//double
		fwrite(&cars[i]->pricePerDay, sizeof(double), 1, file);

		//start
		fwrite(&cars[i]->start.day, sizeof(int), 1, file);
		fwrite(&cars[i]->start.month, sizeof(int), 1, file);
		fwrite(&cars[i]->start.year, sizeof(int), 1, file);

		//end
		fwrite(&cars[i]->end.day, sizeof(int), 1, file);
		fwrite(&cars[i]->end.month, sizeof(int), 1, file);
		fwrite(&cars[i]->end.year, sizeof(int), 1, file);
	}
	fclose(file);
}
int global_car_count = 0;
Car** ReadFromFile() {
	int count = 0;
	FILE* file;
	fopen_s(&file, "cars.bin", "rb");
	fread_s(&count, sizeof(int), sizeof(int), 1, file);

	global_car_count = count;

	auto cars = new Car * [count] {};
	for (size_t i = 0; i < count; i++)
	{
		int id = 0;
		fread_s(&id, sizeof(int), sizeof(int), 1, file);

		int l = 0;
		fread_s(&l, sizeof(int), sizeof(int), 1, file);

		char* model = new char[l + 1]{};
		fread_s(model, l, sizeof(char), l, file);

		bool isFull = false;
		fread_s(&isFull, sizeof(bool), sizeof(bool), 1, file);

		double pricePerDay = 0;
		fread_s(&pricePerDay, sizeof(double), sizeof(double), 1, file);

		Date start;
		fread_s(&start.day, sizeof(int), sizeof(int), 1, file);
		fread_s(&start.month, sizeof(int), sizeof(int), 1, file);
		fread_s(&start.year, sizeof(int), sizeof(int), 1, file);

		Date end;
		fread_s(&end.day, sizeof(int), sizeof(int), 1, file);
		fread_s(&end.month, sizeof(int), sizeof(int), 1, file);
		fread_s(&end.year, sizeof(int), sizeof(int), 1, file);

		cars[i] = new Car{ id,model,isFull,pricePerDay,start,end };
	}
	fclose(file);
	return cars;
}


int global_user_count = 0;


User** ReadUsersFromFile() {
	int count = 0;
	FILE* file;
	fopen_s(&file, "users.bin", "rb");
	fread_s(&count, sizeof(int), sizeof(int), 1, file);

	global_user_count = count;

	auto users = new User * [count] {};
	for (size_t i = 0; i < count; i++)
	{
		int id = 0;
		fread_s(&id, sizeof(int), sizeof(int), 1, file);

		int l1 = 0;
		fread_s(&l1, sizeof(int), sizeof(int), 1, file);

		char* fullname = new char[l1 + 1]{};
		fread_s(fullname, l1, sizeof(char), l1, file);

		int l2 = 0;
		fread_s(&l2, sizeof(int), sizeof(int), 1, file);

		char* model = new char[l2 + 1]{};
		fread_s(model, l2, sizeof(char), l2, file);

		int l3 = 0;
		fread_s(&l3, sizeof(int), sizeof(int), 1, file);

		char* date = new char[l3 + 1]{};
		fread_s(date, l3, sizeof(char), l3, file);

		

		users[i] = new User{id,fullname,model,date};
	}
	fclose(file);
	return users;
}


void WriteUsersToFile(User** users, int user_count) {
	FILE* file;
	fopen_s(&file, "users.bin", "wb");

	fwrite(&user_count, sizeof(int), 1, file);

	for (size_t i = 0; i < user_count; i++)
	{
		fwrite(&users[i]->car_id, sizeof(int), 1, file);

		int l1 = strlen(users[i]->fullname);
		fwrite(&l1, sizeof(int), 1, file);
		fwrite(users[i]->fullname, sizeof(char), l1, file);

		int l2 = strlen(users[i]->car_model);
		fwrite(&l2, sizeof(int), 1, file);
		fwrite(users[i]->car_model, sizeof(char), l2, file);

		int l3 = strlen(users[i]->takeCarDate);
		fwrite(&l3, sizeof(int), 1, file);
		fwrite(users[i]->takeCarDate, sizeof(char), l3, file);
	}
	fclose(file);
}