#include<iostream>
using namespace std;

bool ispalindrome(string s,int i,int n)
{
    if(i>=n/2) 
      return true;

    if(s[i]!=s[n-i-1])
      return false;
      
    return ispalindrome(s,i+1,n);  
}

int main()
{
    string s = "madam";

    if(ispalindrome(s,0,s.length())){
        cout<<"is palindrome";
    }

    else{
        cout<<"Not a Palindrome";
    }
}
