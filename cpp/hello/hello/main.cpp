#include <stdio.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	printf("hello world\n");
	
	int age;
	//age = getchar();
	cin >> age;
	int times5 = age * 5;
	cout << times5;
	//char c = (char)times5;
	//putchar( c );
	
	//putchar("test");
	cout << "\ntype exit to quit\n>";
	char a;
	cin >> a;
	
	//age = getchar();
	
	return 0;
}
