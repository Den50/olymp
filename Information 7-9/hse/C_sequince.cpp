#include "stdafx.h"
#include <iostream>
#include <conio.h>
#include "hello.h"
#include <string>

using namespace std;
//using std::cout;
//using std::cin;
//using std::endl;


int main()
{
	int n, m;
	float summ = 0.0;
	string str;
	cout << "n: ";cin >> n;
	cout << "m: ";cin >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> str;
		for (int j = 0; j < str.length(); j++){
			if (str[j] == '/' || str[j] == '\\') {
				if (str[j + 1] == '.' && (str[j + 2] == '\\' || str[j + 2] == '/')) {
					summ += 2;
					j += 3;
				}
				else if (str[j + 1] == '.' && str[j + 2] == '.' && (str[j + 3] == '\\' || str[j + 3] == '/')) {
					summ += 3;
					j += 4;
				}
				else {
					summ += 0.5;
				}
				
			}
		}
	}
	PRINT(summ);
	//../\..../\/\
	//012345678910
	//./..\...\../
	//.\/\/....\/.


	system("PAUSE");
	return 0;
}

