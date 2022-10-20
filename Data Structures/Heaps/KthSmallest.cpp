#include<bits/stdc++.h>
using namespace std;
    int kthsmallest(int arr[],int l,int r,int k){
       priority_queue<int> pq;
       for(int i=0;i<k;i++){
        pq.push(arr[i]);
       }
       for(int i=k;i<=r;i++){
        if(arr[i]<pq.top()){
        pq.pop();
        pq.push(arr[i]);
        }
       }
    int ans=pq.top();
    return ans;
    }
int main(){
    int n=5;
    int arr[5]={7,10,4,20,15};
    cout<<kthsmallest(arr,0,4,3);
    return 0;
}
