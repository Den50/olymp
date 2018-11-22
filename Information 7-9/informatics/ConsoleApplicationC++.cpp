// ConsoleApplicationC++.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <conio.h>
#include <cmath>

using std::cout;
using std::cin;
using std::endl;


int main()
{	
	setlocale(LC_ALL, "Russian");
	int KIndex;
	int lenles = 50,
		data;
	cout << "кол-во уроков";
	cin >> data;
	if (data > 15) {
		cout << "Eror" << endl;
	}
	else {
		int minutes = (8 * 60 + lenles * data);
		cout << round(minutes / 60) << ":" << (minutes % 60);
	}
	
	//cout << data << endl;

	_getch();
    return 0;
}

