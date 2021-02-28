#include<iostream>
using namespace std;
void hanoi(int n,char a,char b,char c);
int main()
{
	int n;
	char A,B,C;
	A='A';B='B';C='C';
	cin>>n;
	hanoi(n,A,B,C);
	return 0;
}
void hanoi(int n,char a,char b,char c)
{
	if(n==1)
	  cout<<a<<"--->"<<c<<endl;
	else 
	  { hanoi(n-1,a,c,b);
	    cout<<a<<"--->"<<c<<endl;
	    hanoi(n-1,c,a,b);} 
} 

