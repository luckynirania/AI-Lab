#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct node {
	stack<int> poles[3];
	node * parent;
	node() {
		parent = NULL;
	}
};

node* move_gen(node* start) {
	
}

int main() {
	node* initial_state = new node();
	node* final_state = new node();
	int discs = 3;
	
	// initial state
	for(int i = 0;i < discs;i++) initial_state->poles[0].push(i+1);
	
	// final state
	for(int i = 0;i < discs;i++) final_state->poles[2].push(i+1);
}
