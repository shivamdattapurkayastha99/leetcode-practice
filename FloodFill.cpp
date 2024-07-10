#include <iostream>
void flood_fill_rec(int arr[2][2],int x,int y,int new_col,int old_col){
    if (x<0||y<0||x>=10||y>=10)
    {
        return;
    }
    if (arr[x][y]!=old_col)
    {
        return;
    }
    arr[x][y]=new_col;
    flood_fill_rec(arr,x+1,y,new_col,old_col);
    flood_fill_rec(arr,x-1,y,new_col,old_col);
    flood_fill_rec(arr,x,y+1,new_col,old_col);
    flood_fill_rec(arr,x,y-1,new_col,old_col);
    
    
}

void flood_fill(int arr[2][2],int x,int y,int col){
    int old_color=arr[x][y];

    flood_fill_rec(arr,x,y,col,old_color);

    
}
int main(int argc, char const *argv[])
{
    int grid[2][2]={
        {0,0},
        {0,1}
        };
        flood_fill(grid,3,4,5);
        for (auto i = 0; i < 2; i++)
        {
            for (auto j = 0; j < 2; j++)
            {
                std::cout<<grid[i][j]<<" ";
                
            }
            std::cout<<std::endl;

            
        }
        
    return 0;
}
