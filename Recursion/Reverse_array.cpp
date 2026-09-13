#include<iostream>
using namespace std;

int reversearray(int arr[],int i,int n)
{
    if(i>=n/2){
        return 0;
    }

    swap(arr[i],arr[n-i-1]);

    reversearray(arr,i+1,n);
}

int main()
{
    int arr[]={1,2,3,4,5};
    int n=5;

    reversearray(arr,0,5);

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

}
