#include <iostream>
void subarray_sum(int arr[],int n,int sum){
    int curr_sum=arr[0];
    int start=0;
    int end=1;
    while (end<=n)
    {
        if (curr_sum==sum)
        {
            std::cout<<"Range ["<<start<<", "<<end-1<<"]"<<std::endl;
            return;
        }
        if (curr_sum>sum&&start<end)
        {
            curr_sum-=arr[start++];

        }
        else if (curr_sum<sum&&end<n)
        {
            curr_sum+=arr[end++];

        }
        
        
    }
    
}
int main(int argc, char const *argv[])
{
    int arr[]={10,3,5,8,6,12,20,15,31};
    subarray_sum(arr,sizeof(arr)/sizeof(arr[0]),31);
    return 0;
}
