#include<iostream>
using namespace std;

int main()
{
    //int n,arr[n];

    int arr[]={67,89,34,56,21};
    int n=5;

    //cout<<"Enter the size of the array:";
    //cin>>n;

    //cout<<"Enter the array elements:";
    //for(int i=0;i<n;i++)
    //{
        //cin>>arr[i];
    //}

    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                swap(arr[j],arr[j+1]);
            }
        }
    }

    cout<<"Sorted Array";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

}
