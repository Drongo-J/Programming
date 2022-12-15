#pragma once

struct CV {
	double salary;
	int experience;
	char* languages;
	char* about;
};

struct Notification {
	char* message;
	const char* date;
};

struct Worker {
	char* username;
	char* fullname;
	char* speciality;
	CV* cv;
	Notification** notifications;
	int count = 0;
};

//Advertisement
struct AD {
	int id = 0;
	char* title;
	double salary;
	Worker** appliers;
	int app_count = 0;
};
struct Employer {
	char* username;
	char* fullname;
	char* company;
	AD** ads;
	int count = 0;
};
