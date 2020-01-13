#include <iostream>
#include <string>
#include <vector>
#include <queue> 
#include <stack>
#include <fstream>

using namespace std;

struct position {
    int data;
    position* parent;
    bool visited;
    position() {
        parent = NULL;
        visited = false;
    }
};

struct adj {
    vector<position*> arr;
    void disp() {
        for(int i = 0;i < arr.size();i++) {
            cout << arr[i]->data << " ";
        }
        cout << endl;
    }
};

int main() {
    ifstream inp;
    inp.open("input.txt");
    vector<string> input;
    string temp;
    getline(inp,temp);
    int algo = stoi(temp);
    while(getline(inp,temp)) {
        input.push_back(temp);
    }

    int m = input.size();
    int n = input[0].length();

    int source = 0;
    int dest;

    position node[99999];
    adj adj_list[99999];

    for(int i = 0;i < input.size();i++) {
        for(int j = 0;j < input[i].size();j++) {
            int pos = n*i + j;
            node[pos].data = pos;
            if(input[i][j] == '*') dest = pos;
            if(input[i][j] == ' ' or ( i == 0 && j == 0)) {
                if(i < m && (input[i+1][j] == ' ' or input[i+1][j] == '*')) adj_list[pos].arr.push_back(&node[pos + n]);
                if(i > 0 && (input[i-1][j] == ' ' or input[i-1][j] == '*')) adj_list[pos].arr.push_back(&node[pos - n]);
                if(j < n && (input[i][j+1] == ' ' or input[i][j+1] == '*')) adj_list[pos].arr.push_back(&node[pos + 1]);
                if(j > 0 && (input[i][j-1] == ' ' or input[i][j-1] == '*')) adj_list[pos].arr.push_back(&node[pos - 1]);
            }
        }
    }
    int states = 1;
    int length = 1;

    //BFS
    if(algo == 0) {
        queue<position*> que;
        que.push(&node[source]);
        
        while(!que.empty()) {
            int que_front_index = que.front()->data;
            for(int i = 0;i < adj_list[que_front_index].arr.size();i++) {
                int pos = adj_list[que_front_index].arr[i]->data;
                if(node[pos].visited == false) {
                    node[pos].visited = true;
                    node[pos].parent = &node[que_front_index];
                    que.push(&node[pos]);
                }
            }
            if(que.front()->data == dest) break;
            que.pop();
            states++;
        }
    }

    //DFS
    if(algo == 1) {
        stack<position*> que;
        que.push(&node[source]);
        
        while(!que.empty()) {
            int que_front_index = que.top()->data;
            que.pop();
            states++;
            for(int i = 0;i < adj_list[que_front_index].arr.size();i++) {
                int pos = adj_list[que_front_index].arr[i]->data;
                if(node[pos].visited == false) {
                    node[pos].visited = true;
                    node[pos].parent = &node[que_front_index];
                    que.push(&node[pos]);
                }
            }
            if(que.top()->data == dest) break;
        }
    }
    if(algo == 2) {

    }

    position* path = &node[dest];

    while(path->parent != NULL) {
        int x = path->data / n;
        int y = path->data % n;
        input[x][y] = '0';
        path = path->parent;
        length++;
    }

    cout << states << endl << length << endl;
    for(int i = 0;i < input.size(); i++) cout << input[i] << endl;
}