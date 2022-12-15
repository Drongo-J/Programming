#pragma once

struct Human {
	char* name;
	char* phonenumber;
	const char* createdDate;
	const char* createdTime;
};

struct Contact {
	Human** humans;
	int count = 0;
};



