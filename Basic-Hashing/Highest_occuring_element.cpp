#include<iostream>
#include<unordered_map>
using namespace std;

int main()
{
    int arr[]={1,2,3,3,2,1,1,1};
    int n=8;

    unordered_map<int,int>freq;

    for(int i=0;i<n;i++)
    {
        freq[arr[i]]++;
    }

    int maxfreq=0;
    int  highestelement=0;

    for(auto x: freq)
    {
        if(x.second>maxfreq){
            maxfreq=x.second;
            highestelement=x.first;
        }
    }

    cout<<"Highest occuring element:"<<highestelement<<endl;
    cout<<"Frequency:"<<maxfreq<<endl;
}
