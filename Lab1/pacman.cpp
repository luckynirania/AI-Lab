#include <iostream>
#include <string>
#include <vector>
#include <queue> 

using namespace std;
struct node{
    int data;
    int depth;
    bool visited;
    node() {
        visited = false;
        depth = 0;
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

void dfs(node* u,adj* adj_list,int dest,int &states) {
    u->visited = true;
    for(int i = 0;i < adj_list[u->data].arr.size();i++) {
        if(adj_list[u->data].arr[i]->visited == false && (u->data != dest)) {
            states++;
            adj_list[u->data].arr[i]->depth = u->depth + 1;
            dfs(adj_list[u->data].arr[i], adj_list,dest,states);
        }
    }
}

int main() {
    int algo;
    // cin >> algo;
    algo = 0;
    vector<string> input;
    string temp;
    while(getline(cin, temp) && temp != ""){
        input.push_back(temp);
    }
    int m = input.size();
    int n = input[0].length();     // each "input[i]"" is a string containing "+--+--+--+" or "|  +  |  "
    // cout << m << " " << n << endl;
    adj adj_list[99999];   // adj_list[3] contains sets of pointer to a "node" which are reachable from node "3"
    node graph[99999];    // graph is set of actual nodes......note that adj_list contains pointer to these graph
    input[0][0] = ' ';
    for(int i = 0;i < m - 1;i++) {
        // cout << input[i] << endl;
        for(int j = 0;j < n - 1;j++) {
            if(input[i][j] == ' ') {
                adj temp;
                if(input[i+1][j] == ' ' or input[i+1][j] == '*') {
                    node *tmp = &graph[n*(i+1) + j];
                    tmp->data = n*(i+1) + j;
                    temp.arr.push_back(tmp);
                }
                if((i - 1 >= 0) && (input[i-1][j] == ' ' or input[i-1][j] == '*' )) {
                    node* tmp = &graph[n*(i-1) + j];
                    tmp->data = n*(i-1) + j;
                    temp.arr.push_back(tmp);
                }
                if(input[i][j+1] == ' ' or input[i][j+1] == '*') {
                    node* tmp = &graph[n*i + (j+1)];
                    tmp->data = n*i + (j+1);
                    temp.arr.push_back(tmp);
                }
                if((j - 1 >= 0) && (input[i][j-1] == ' ' or input[i][j-1] == '*' )) {
                    node* tmp = &graph[n*i + (j-1)];
                    tmp->data = n*i + (j-1);
                    temp.arr.push_back(tmp);
                }
                adj_list[n*i + j] = temp;
            }
        }
    }
    // for(int i = 0;i < n*m;i++) {
    //     cout << i << "\t";
    //     adj_list[i].disp();
    // }
    int source = 0;
    int dest = n*(m - 1) - 1;

    // implement bfs
    if(algo == 0) {
        int states = 1  ;
        vector<node*> path;
        queue<node*> que;

        node* tmp = &graph[source];
        path.push_back(tmp);
        graph[source].visited = true;
        for(int i = 0;i < adj_list[source].arr.size();i++) {
            states++;
            que.push(adj_list[source].arr[i]);
            adj_list[source].arr[i]->visited = true;
            adj_list[source].arr[i]->depth = graph[source].depth + 1;
        }

        while(!que.empty() && (que.front()->data != dest)) { 
            for(int i = 0;i < adj_list[que.front()->data].arr.size();i++) {
                if(adj_list[que.front()->data].arr[i]->visited == false) {
                    que.push(adj_list[que.front()->data].arr[i]);
                    adj_list[que.front()->data].arr[i]->visited = true;
                    adj_list[que.front()->data].arr[i]->depth = que.front()->depth + 1;
                }
            }
            states++;
            que.pop();
        }

        // backtracking / path retracing (shortest obviously)
        int number = dest;
        int x,y;
        while(input[1][1] != '0') {
            x = number / n;
            y = number % n;
            input[x][y] = '0'; 
            int dep = graph[number].depth - 1;
            for(int i = 0;i < 4;i++) {
                if(graph[number - 1].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number - 1].arr.size();j++) {
                        if(adj_list[number - 1].arr[j]->data == number) {
                            present = true;
                            number = number - 1;
                            break;
                        }
                    }
                }
                if(graph[number + 1].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number + 1].arr.size();j++) {
                        if(adj_list[number + 1].arr[j]->data == number) {
                            present = true;
                            number = number + 1;
                            break;
                        }
                    }
                }
                if(graph[number - n].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number - n].arr.size();j++) {
                        if(adj_list[number - n].arr[j]->data == number) {
                            present = true;
                            number = number - n;
                            break;
                        }
                    }
                }
                if(graph[number + n].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number + n].arr.size();j++) {
                        if(adj_list[number + n].arr[j]->data == number) {
                            present = true;
                            number = number + n;
                            break;
                        }
                    }
                }
            }
        }
        cout << "states explored\t" << states << endl;
        cout << "length of path\t" << graph[dest].depth + 1 << endl; // + 1 bcoz counting from 0
    }
    else if(algo == 1) {
        int states = 0;
        for(int i = source;i <= dest;i++) {
            graph[i].visited = false;
            graph[i].depth = 0;
        }
        for(int i = source;i <= dest;i++) dfs(&graph[i],adj_list,dest,states);
        
        
        // backtracking / path retracing (shortest obviously)
        int number = dest;
        int x,y;
        while(input[1][1] != '0') {
            x = number / n;
            y = number % n;
            input[x][y] = '0'; 
            int dep = graph[number].depth - 1;
            for(int i = 0;i < 4;i++) {
                if(graph[number - 1].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number - 1].arr.size();j++) {
                        if(adj_list[number - 1].arr[j]->data == number) {
                            present = true;
                            number = number - 1;
                            break;
                        }
                    }
                }
                if(graph[number + 1].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number + 1].arr.size();j++) {
                        if(adj_list[number + 1].arr[j]->data == number) {
                            present = true;
                            number = number + 1;
                            break;
                        }
                    }
                }
                if(graph[number - n].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number - n].arr.size();j++) {
                        if(adj_list[number - n].arr[j]->data == number) {
                            present = true;
                            number = number - n;
                            break;
                        }
                    }
                }
                if(graph[number + n].depth == dep) {
                    bool present = false;
                    for(int j = 0;j < adj_list[number + n].arr.size();j++) {
                        if(adj_list[number + n].arr[j]->data == number) {
                            present = true;
                            number = number + n;
                            break;
                        }
                    }
                }
            }
        }
        cout << "states explored\t" << states << endl;
        cout << "length of path\t" << graph[dest].depth + 4 << endl; // + 4 beacuse 0,0 0,1 and * position is not counted and also counting from 0
        
    }
    input[0][0] = '0';
    input[1][0] = '0';
    for(int i = 0;i < input.size();i++) {
        cout << input[i] << endl;
    }


    return 0;
}