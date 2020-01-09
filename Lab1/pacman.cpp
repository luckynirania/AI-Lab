#include <iostream>
#include <string>
#include <vector>
#include <queue> 

using namespace std;
struct node{
    int data;
    bool visited;
    node() {
        visited = false;
    }
};

struct adj{
    vector<node*> arr;
    void disp() {
        for(int i = 0;i < arr.size();i++) {
            cout << arr[i]->data << " ";
        }
        cout << endl;
    }
};

int main() {
    int algo;
    // cin >> algo;
    vector<string> input;
    string temp;
    while(getline(cin, temp) && temp != ""){
        input.push_back(temp);
    }
    int m = input.size();
    int n = input[0].length();
    cout << m << " " << n << endl;
    adj adj_list[99999];
    node graph[99999];
    for(int i = 1;i < m - 1;i++) {
        cout << input[i] << endl;
        for(int j = 1;j < n - 1;j++) {
            if(input[i][j] == ' ') {
                adj temp;
                if(input[i-1][j] == ' ') {
                    node* tmp = &graph[n*(i-1) + j];
                    tmp->data = n*(i-1) + j;
                    temp.arr.push_back(tmp);
                }
                if(input[i+1][j] == ' ') {
                    node *tmp = &graph[n*(i+1) + j];
                    tmp->data = n*(i+1) + j;
                    temp.arr.push_back(tmp);
                }
                if(input[i][j-1] == ' ') {
                    node* tmp = &graph[n*i + (j-1)];
                    tmp->data = n*i + (j-1);
                    temp.arr.push_back(tmp);
                }
                if(input[i][j+1] == ' ') {
                    node* tmp = &graph[n*i + (j+1)];
                    tmp->data = n*i + (j+1);
                    temp.arr.push_back(tmp);
                }
                adj_list[n*i + j] = temp;
            }
        }
    }
    for(int i = 0;i < n*m;i++) {
        cout << i << "\t";
        adj_list[i].disp();
    }
    int source = n + 1;
    int dest = n*(m - 1) - 2;

    vector<int> path;
    queue<int> que;

    return 0;
}