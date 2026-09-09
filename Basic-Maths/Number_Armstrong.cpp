#include<iostream>
using namespace std;

int main()
{
    int n;

    cin>>n;

    int original=n;
    int digits=0;
    int temp=n;

    while(temp>0){
        digits++;
        temp=temp/10;
    }

    int sum=0;
    temp=n;
    
    while(temp>0){
       int digit = temp % 10;

       int power=1;

       for(int i=1;i<=digits;i++)
       {
        power=power*digit;
       }

       sum=sum+power;
       temp=temp/10;
       

      
    }

    //cout<<"digits:"<<digits<<endl;
    //cout<<"sum:"<<sum<<endl;

    if(sum==original){
        cout<<"Number is Armstrong:";
    }

    else{
        cout<<"Not a Armstrong";
    }
}
