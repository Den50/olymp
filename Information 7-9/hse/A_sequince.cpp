// olympic.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include "printcout.h"

int main()
{
	int n, m, k, l, minSumm, subtraction;
	PRINT("n: ");cin >> n;
	PRINT("m: ");cin >> m;
	PRINT("k: ");cin >> k;
	PRINT("l: ");cin >> l;

	minSumm = 0;

	subtraction = (m - n) % 4;

	if ((m - n) / 4 > 0 && ((m - n) * k > (m - n) / 4 * l)) {
		minSumm += (m - n) / 4 * l;
	}
	else if ((m - n) / 4 > 0 && ((m - n) * k < (m - n) / 4 * l)){
		minSumm += (m - n) * k;
	}
	if (subtraction > 0 && (subtraction * k < l)) {
		minSumm += subtraction * k;
	}
	if(subtraction > 0 && (subtraction * k > l)){
		minSumm += l;
	}
	else if (subtraction > 0 && (subtraction * k == l)) {
		minSumm += subtraction * k;
	}

	PRINT(minSumm);





	
	system("PAUSE");
    return 0;
	
}

