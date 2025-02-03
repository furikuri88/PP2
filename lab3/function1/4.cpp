#include <iostream>
#include <vector>
using namespace std;

bool prime(int x){
    bool b=1;
    for(int i=2;i<x;i++){
        if(x%i==0){
            b=false;
        }
    }
    if(b==1){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int n;
    vector<int> v;
    while (cin.peek()!='\n')
    {
        cin>>n;
        v.push_back(n);
    }
    for(int i=0;i<v.size();i++){
        if(prime(v[i]) && v[i]!=1 && v[i]!=0){
            cout<<v[i]<<" ";
        }
    }

}