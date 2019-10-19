#include <iostream>
#include <limits.h>

using namespace std;
#define V 9
void printPath(int parent[], int j) 
{ 
      
    // Base Case : If j is source 
    if (parent[j] == - 1) 
        return; 
  
    printPath(parent, parent[j]); 
  
//    printf("%d ", j);
	cout<<j;
} 
int mind(int dist[],bool visi[])
{
    int min =INT_MAX,min_index;
    for (int v=0;v<V;v++)
        if(visi[v]==false && dist[v]<=min)
            min=dist[v],min_index=v;
    return min_index;
}
int printsol(int dist[],int parent[])
{
	int src=0;
    for (int i=0;i<V;i++)
    {    
	    cout<<src<<i<<" "<<dist[i]<<"\t"<<src<<endl;
	    printPath(parent,i);
	}
      return 0;
}
void diji(int graph[V][V],int src)
{
    int dist[V];
    bool visi[V];
    int parent[V];
    for (int i=0;i<V;i++)
        dist[i]=INT_MAX,visi[i]=false,parent[0]=-1;
    dist[src]=0;
    for(int count=0;count<V-1;count++)
    {
        int u=mind(dist,visi);
        visi[u]=true;
        for(int v=0;v<V;v++)
            if(!visi[v] && graph[u][v] && dist[u]!=INT_MAX && dist[u]+graph[u][v]<dist[v])
	    {
		    dist[v]=dist[u]+graph[u][v];
		    parent[v]=u;
	    }
    }
    printsol(dist,parent);
}


int main()
{
    int aa,bb;

int graph[V][V] = { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
{ 4, 0, 8, 0, 0, 0, 0, 11, 0 },
{ 0, 8, 0, 7, 0, 4, 0, 0, 2 },
{ 0, 0, 7, 0, 9, 14, 0, 0, 0 },
{ 0, 0, 0, 9, 0, 10, 0, 0, 0 },
{ 0, 0, 4, 14, 10, 0, 2, 0, 0 },
{ 0, 0, 0, 0, 0, 2, 0, 1, 6 },
{ 8, 11, 0, 0, 0, 0, 1, 0, 7 },
{ 0, 0, 2, 0, 0, 0, 6, 7, 0 } };

diji(graph, 0);
int o;
cin>>o;
return 0;
} 
