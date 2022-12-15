#pragma once

struct Mail 
{
	char* fullname;
	char* gmail_name;
	char* password;
	const char* creating_date;
	const char* creating_time;
};

struct AllMails 
{
	Mail** mails;
	int mail_quantity = 0;	
};