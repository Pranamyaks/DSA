#include<iostream>
using namespace std;

int main()
{
    int n,rev=0,digit;

    cout<<"Enter a Number:";
    cin>>n;

    int temp=n;

    while(n!=0){
        digit=n%10;
        rev=rev*10+digit;
        n=n/10;
    }

    if(rev==temp){
        cout<<"Number is palindrome";
    }

    else{
        cout<<"Number is not palindrome";
    }

   
    return 0;

}
