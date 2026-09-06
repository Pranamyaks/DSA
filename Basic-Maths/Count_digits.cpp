#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter a Number:";
    cin>>n;

    n=abs(n); //Converts number into non-negative value

    if(n==0){
        cout<<1;
        return 0;
    }

    int count=0;
    while(n>0){
        count++;
        n=n/10;
    }

    cout<<"Total Digits are:"<<count;

    return 0;
}
