#include<iostream>
using namespace std;

void mergee(int arr[],int low,int mid,int high)
{
    int i=low;
    int j=mid+1;
    int k=low;

    int temp[100];

    while(i<=mid && j<=high)
    {
        if(arr[i]<=arr[j])
        {
            temp[k]=arr[i];
            i++;
        }
        else{
            temp[k]=arr[j];
            j++;
        }
        k++;
    }
    while(i<=mid)
    {
        temp[k]=arr[i];
        i++;
        k++;
    }

    while(j<=high)
    {
        temp[k]=arr[j];
        j++;
        k++;
    }

    for(int x=low;x<=high;x++)
    {
        arr[x]=temp[x];
    }
}
void mergesort(int arr[],int low,int high)
{
    if(low<high)
    {
        int mid=(low+high)/2;

        mergesort(arr,low,mid);
        mergesort(arr,mid+1,high);

        mergee(arr,low,mid,high);
    }
}

int main()
{
    int arr[]={4,3,6,8,19,23,9,56};
    int n=8;

    mergesort(arr,0,n-1);

    cout<<"Sorted Array";

    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

}
