#include<iostream>
using namespace std;

int main()
{
    int n;

    cout<<"Enter a number";
    cin>>n;

    bool is_prime=true;

    if(n<=1){
        is_prime=false;
    }

    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            is_prime=false;
            break;
        }
    }

    if(is_prime){
        cout<<"Number is Prime";
    }
    else{
        cout<<"Is not prime";
    }
}
