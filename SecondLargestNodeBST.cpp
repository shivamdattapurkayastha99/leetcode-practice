#include<iostream>


struct Node
{
    Node *left;
    Node *right;
    int data;
    Node(int val):left(nullptr),
    right(nullptr),
    data(val){}
};
Node *insertNode(Node *root,int val){
    if (!root)
    {
        return new Node(val);

    }
    if (val<root->data)
    {
        root->left=insertNode(root->left,val);

    }
    else if (val>root->data)
    {
        root->right=insertNode(root->right,val);

    }
    
    return root;
}
void reverseInOrder(Node *root){
    if (root==nullptr)
    {
        return;
    }
    reverseInOrder(root->right);
    std::cout<<root->data<<" ";
    reverseInOrder(root->left);

}
void secondLargest(Node *root){
    if (root==nullptr)
    {
        return;
    }
    static int count=0;


    secondLargest(root->right);
    count++;
    if (count==2)
    {
        std::cout<<root->data<<std::endl;
        return;

    }
    
    
    secondLargest(root->left);

}
int main(int argc, char const *argv[])
{
    Node root(30);
    insertNode(&root,20);
    insertNode(&root,50);
    insertNode(&root,40);
    insertNode(&root,10);
    insertNode(&root,25);

    secondLargest(&root);
    

    return 0;
}
