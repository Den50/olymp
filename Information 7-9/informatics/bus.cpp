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
	int child;
	int parents;
	int bus;
	cout << "Дети:";cin >> child;
	cout << "Взрослые:";cin >> parents;
	cout << "Вместимость автобуса:";cin >> bus;
	if (child <= 0 && parents < 2 || parents == 0) {
		cout << "Error";
	}
	else {
		if ((child + parents) % bus != 0) {
			cout << 0;
		}
		else {
			cout << ((child + parents) / bus);
		}
	}


	_getch();
	return 0;
}

