#pragma once
#include<iostream>
using namespace std;

struct Date {
	int year;
	int month;
	int day;
};


struct Car {
	int id;
	char* model;
	bool isFull=false;
	double pricePerDay;
	Date start;
	Date end;
};

struct User {
	int car_id;
	char* fullname;
	char* car_model;
	const char* takeCarDate;
};
