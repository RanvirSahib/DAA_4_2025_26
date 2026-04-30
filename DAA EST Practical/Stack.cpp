#include<iostream>
using namespace std;

class Node{
public:
    int val;
    Node* next;
    Node(int val){
        this->val = val;
        next = NULL;
    }
};

class Stack{
private:
    Node* Head;
    Node* Tail;
    int count;

public:
    Stack(){
        Head = NULL;
        Tail = NULL;
        count = 0;
    }

    void push(int val){
        Node* newNode = new Node(val);
        if(Head == NULL){
            Head = newNode;
            Tail = newNode;
        }
        else{
            Tail->next = newNode;
            Tail = newNode;
        }
        count++;
    }

    void pop(){
        if(Head == NULL) return;
        if(Head == Tail){
            delete Head;
            Head = NULL;
            Tail = NULL;
        }
        else{
            Node* temp = Head;
            while(temp->next != Tail){
                temp = temp->next;
            }
            delete Tail;
            Tail = temp;
            Tail->next = NULL;
        }
        count--;
    }

    void display(){
        Node* temp = Head;
        while(temp != NULL){
            cout << temp->val;
            if(temp->next != NULL) cout << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    void size(){
        int count = 0;
        Node* temp = Head;
        while(temp != NULL){
            temp = temp->next;
            count++;
        }
        cout<<count<<endl;
    }

    void isEmpty(){
        if(Head == NULL) cout<<true;
        else cout<<false;
        cout<<endl;
    }
};

int main(){
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.display();
    s.pop();
    s.display();
    s.size();
    s.isEmpty();
    return 0;
}