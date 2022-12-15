#pragma once

struct CV {
	double salary;
	char* experience;
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
	int notification_count = 0;
};

//Advertisement
struct AD {
	int id = 0;
	char* title;
	double salary;
	Worker** appliers;
	int applier_count = 0;
};
struct Employer {
	char* username;
	char* fullname;
	char* company;
	AD** ads;
	int ads_count = 0;
};