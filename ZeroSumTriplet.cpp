#include<iostream>
#include<algorithm>

void zero_sum_triplets(int arr[],int n){

    std::sort(arr,arr+n);
    for (auto i = 0; i < n-2; i++)
    {
        auto l=i+1;
        auto r=n-1;
        while (l<r)
        {
            int val=-arr[i];
            if (arr[l]+arr[r]>val)
            {
                r--;

            }
            else if (arr[l]+arr[r]<val)
            {
                l++;

            }
            else
            {
                std::cout<<arr[i]<<", "<<arr[l]<<", "<<arr[r]<<std::endl;
                l++;
                r--;

            }
            
        }
        
    }
    
}

int main(int argc, char const *argv[])
{
    int arr[]={0,-2,7,2,4,-6};
    zero_sum_triplets(arr,sizeof(arr)/sizeof(arr[0]));
    
    return 0;
}
