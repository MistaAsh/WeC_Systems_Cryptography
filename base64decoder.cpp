#include <bits/stdc++.h>

using namespace std;

char* base64decoder(char* str, int n)
{
    
}

int main()
{
    char str[1000];
    cout<<"Enter the encoded string: ";
    cin>> str;

    cout<<"\n\nDecoded string: "<<base64decoder(str, strlen(str));
    return 0;
}