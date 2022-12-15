#pragma once

// Go Back To Main Menu (Worker - 5) (Employer - 3)

#include<iostream>
#include "Entities.h"
#include "Functions.h"
#include<Windows.h>
using namespace std;

int global_id = 0;
int adv_count = 0;

void ColorTextRed()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 12);
}

void ColorTextGreen()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 10);
}

void ColorTextYellow()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 14);
}

void ShowMenu()
{
	ColorTextYellow();
	system("cls");
	cout << "\n ======== MAIN MENU ======== " << endl;
	cout << "\n   Worker(w) | Employer(e)" << endl;
	cout << "\n =========================== " << endl;

}

void IncorrectInput()
{
	ColorTextRed();
	system("cls");
	cout << "\n Incorrect Input!" << endl;
	Sleep(1000);
	ShowMenu();
}

Worker** workers = new Worker * [] {
	new Worker{ new char[] {"elvin123"},new char[] {"Elvin"},new char[] {"Programmer"},
	NULL ,NULL },
	new Worker{ new char[] {"john26"},new char[] {"John"},new char[] {"Designer"},
	NULL ,NULL },
};

Employer** employers = new Employer * [] {
	new Employer{ new char[] {"rafiq123"},new char[] {"Rafiq Eliyev"},new char[] {"Rafiq\'s MMC"},NULL,0 }
};

void ShowIntro();
void Start() {
	while (true)
	{
		ShowIntro();
		system("cls");
	}
}

Worker* isWorkerExist(Worker** workers, int count, const char* username) {
	for (size_t i = 0; i < count; i++)
	{
		if (strcmp(workers[i]->username, username) == 0) {
			return workers[i];
		}
	}
	return nullptr;
}

void ShowWorkerMenu(const Worker* worker) {
	ColorTextYellow();
	cout << "\n ======== WORKER MENU ======== " << endl;
	cout << "\n  Advertisements            1  " << endl;
	cout << "  Create your own CV        2  " << endl;
	cout << "  Notifications (" << worker->notification_count << ")         3  " << endl;
	cout << "  Observe your cv           4  " << endl;
	cout << "\n ============================= " << endl;
}

void ShowNotifications(const Worker* worker) {
	if (worker->notification_count == 0) {
		system("cls");
		ColorTextRed();
		cout << "\n You do not have any notifications." << endl;
		cout << endl;
		Sleep(2000);
	}
	else {
		for (size_t i = 0; i < worker->notification_count; i++)
		{
			ColorTextYellow();
			cout << "\n Notification content : " << worker->notifications[i]->message << endl;
			cout << " Date : " << worker->notifications[i]->date << endl;
			system("pause");
		}
		cout << endl;
	}
}

void ShowCV(const CV* cv) {
	if (cv != nullptr)
	{
		ColorTextYellow();
		cout << "\n ========== CV INFO ==========" << endl;
		cout << "\n Experience : " << cv->experience << endl;
		cout << " Salary requirement : " << cv->salary << endl;
		cout << " Languages : " << cv->languages << endl;
		cout << " About YOU : " << cv->about << endl;
		cout << "\n =============================" << endl;
	}
	else
	{
		cout << "\n No cv." << endl;
	}
}
CV* getNewCV() {
	system("cls");
	ColorTextYellow();
	cout << "\n =========== CREATING A CV ===========" << endl;
	cout << "\n Enter salary requirement : ";
	double salary = 0;
	cin >> salary;
	cin.ignore();
	cin.clear();
	cout << " Enter your experience : ";
	char* experience = new char[100] {};
	cin.getline(experience,100);
	cout << " Enter languages skills : ";
	char* languages = new char[200]{};
	cin.getline(languages, 200);
	cout << " Enter about you : ";
	char* about = new char[250]{};
	cin.getline(about, 250);
	auto cv = new CV{ salary,experience,languages,about };
	cout << "\n =====================================" << endl;
	return cv;
}

Employer* isEmployerExist(const char* username, int count) {
	for (size_t i = 0; i < count; i++)
	{
		if (strcmp(employers[i]->username, username) == 0) {
			return employers[i];
		}
	}
	return nullptr;
}

AD* getNewAD() {
	ColorTextYellow();
	cout << "\n ============== CREATING NEW ADVERTISEMENT ==============" << endl;
	cin.ignore();
	cin.clear();
	cout << "\n Enter advertisement title : ";
	char* title = new char[100]{};
	cin.getline(title, 100);
	cout << " Enter max salary : ";
	double salary = 0;
	cin >> salary;
	cout << "\n ========================================================" << endl; 
	++global_id;
	adv_count++;
	AD* ad = new AD{ global_id,title,salary };
	return ad;
}

void AddADToEmployer(Employer* employer, AD* ad) {
	auto newads = new AD * [employer->ads_count + 1]{};
	for (size_t i = 0; i < employer->ads_count; i++)
	{
		newads[i] = employer->ads[i];
	}
	newads[employer->ads_count] = ad;
	employer->ads = newads;
	newads = nullptr;
	employer->ads_count++;
	ColorTextGreen();
	cout << "\n New advertisement was successfully created!" << endl;
	Sleep(1500);
}


void ShowEmployerMenu() {
	ColorTextYellow();
	cout << "\n ========= EMPLOYER MENU =========" << endl;
	cout << "\n  Add advertisement             1  " << endl;
	cout << "  Show appliers                 2  " << endl;
	cout << "\n =================================" << endl;
}

void ShowEmployerAds(Employer* employer) {
	ColorTextYellow();
	cout << "\n =========== ADS ===========" << endl;
	for (size_t i = 0; i < employer->ads_count; i++)
	{
		cout << "\n =========================== ID : " << employer->ads[i]->id << endl;
		cout << "\n Title : " << employer->ads[i]->title << endl;
		cout << " Salary : " << employer->ads[i]->salary << endl;
	}
}

void ShowAllADS(Employer** employers, int e_count) {
	for (size_t i = 0; i < e_count; i++)
	{
		ShowEmployerAds(employers[i]);
	}
}

AD* getADSById(Employer** employers, int e_count, int id) {
	for (size_t i = 0; i < e_count; i++)
	{
		for (size_t k = 0; k < employers[i]->ads_count; k++)
		{
			if (employers[i]->ads[k]->id == id) {
				return employers[i]->ads[k];
			}
		}
	}
	return nullptr;
}

void addApplierToAds(AD* ads, Worker* worker) {
	auto newappliers = new Worker * [ads->applier_count + 1]{};
	for (size_t i = 0; i < ads->applier_count; i++)
	{
		newappliers[i] = ads->appliers[i];
	}
	newappliers[ads->applier_count] = worker;
	ads->appliers = newappliers;
	newappliers = nullptr;
	ads->applier_count++;
}

void BidToAds(Employer** employers, int count, Worker* worker, int id) {
	auto ads = getADSById(employers, count, id);
	if (ads != nullptr) {
		addApplierToAds(ads, worker);
		ColorTextGreen();
		cout << "\n Your BID was added successfully!" << endl;
	}
	else {
		system("cls");
		ColorTextRed();
		cout << "\n Incorrect input" << endl;
		Sleep(2000);
	}
}

void ShowWorker(const Worker* worker) {
	ColorTextYellow();
	cout << "\n ========= Worker INFO =========" << endl;
	cout << "\n Full name : " << worker->fullname << endl;
	cout << " Speciality : " << worker->speciality << endl;
	ShowCV(worker->cv);
	cout << endl;
}

bool ThereIsApplier(Employer* employer)
{
	for (size_t i = 0; i < employer->ads_count; i++)
	{
		if (employer->ads[i]->applier_count > 0)
		{
			return true;
		}
	}
	return false;
}

void ShowAds(Employer* employer,const int ads_no)
{
	cout << "\n ============= ADS ============== " << endl;;
	cout << "\n Advertisement title : " << employer->ads[ads_no]->title << endl;
	cout << " Max salary : " << employer->ads[ads_no]->salary << endl;
	cout << "\n ================================ " << endl;
}

void ShowAllAppliers(Employer* employer) 
{
	for (int x = 0; x < employer->ads_count; x++)
	{
		if (employer->ads[x] != nullptr)
		{
			if (employer->ads[x]->applier_count != 0)
			{
				cout << "\n ================ Advertisement ID : " << employer->ads[x]->id << " ==================" << endl;
				ShowAds(employer, x);
				for (int y = 0; y < employer->ads[x]->applier_count; y++)
				{
					ShowWorker(employer->ads[x]->appliers[y]);
				}
			}
		}
	}
}

void AddNewMessage(Worker* worker, char* message)
{
	int c = worker->notification_count;
	Notification** newNotifications = new Notification * [c + 1]{};

	for (int x = 0; x < c; x++)
	{
		newNotifications[x] = worker->notifications[x];
	}
	Notification* newNotification = new Notification{message,__DATE__};
	newNotifications[c] = newNotification;
	worker->notifications = newNotifications;
	newNotifications = nullptr;
	worker->notification_count++;
}

int GetIndexOfAdsByID(Employer* employer, const int id_of_advertisement)
{
	for (int x = 0; x < employer->ads_count; x++)
	{
		if (employer->ads[x]->id == id_of_advertisement)
		{
			return true;
		}
	}
	return false;
}


void DeleteAdvertisementById(Employer* employer, const int id_of_advertisement)
{
	int l = employer->ads_count - 1;
	AD** newads = new AD * [l - 1]{};
	int index = GetIndexOfAdsByID(employer, id_of_advertisement);
	for (int x = 0; x < index; x++)
	{
		newads[x] = employer->ads[x];
	}
	for (int y = index+1; y < l; y++)
	{
		newads[y-1] = employer->ads[y];
	}
	employer->ads = newads;
	newads = nullptr;
	employer->ads_count--;
}


void HireApplier(Employer* employer,const char* name_of_applier,const int id_of_advertisement,const char* message)
{
	bool exists = false;
	for (int x = 0; x < employer->ads_count; x++)
	{
		if (employer->ads[x]->applier_count != 0)
		{
			for (int z = 0; z < employer->ads[x]->applier_count; z++)
			{
				if (employer->ads[x]->id == id_of_advertisement && strcmp(employer->ads[x]->appliers[z]->fullname, name_of_applier) == 0)
				{
					// Send Notification 
					int l = strlen(message);
					char* newMessage = new char[l + 1]{};
					strcpy_s(newMessage, l + 1, message);

					AddNewMessage(employer->ads[x]->appliers[z], newMessage);
					newMessage = nullptr;

					// Delete advertisement
					DeleteAdvertisementById(employer, id_of_advertisement);
				
					exists = true;
					break;
				}
			}
		}
		if (exists)
		{
			break;
		}
	}
	if (exists)
	{
		cout << "\n Your message was sent to " << name_of_applier << endl;
		Sleep(2000);
	}
	else
	{
		cout << "\n Incorrect ID of advertisement or name!" << endl;
		Sleep(2000);
	}
}