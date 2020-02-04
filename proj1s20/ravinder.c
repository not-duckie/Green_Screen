#include<stdio.h>
#include<stdlib.h>

void makeCopyArray(int *val1,int n){
	int *val2;
	val2 = (int*) malloc(1000*sizeof(int));
	for(int i =0;i<n;i++){
		val2[i] = val1[i];
	}

	printf("Copied array is\n");
	for(int i=0;i<n;i++){
		printf("%d ",val2[i]); }
}


int* sumCheck(int kay,int *val,int n){
	int tmp=0,sum,*ret;

	ret = (int*) malloc(sizeof(int)*3);
	for(int i=0;i<n;i++){
		tmp++;
		for(int j=tmp;j<n;j++){
			sum = val[i] + val[j];
			if(sum == kay){ 
				 	ret[0] = 1;
		 			ret[1] = i;
					ret[2] = j;	 }
				
			else{ }
		}
	}
	return ret;
}


void sort(int *val,int n){
	int tmp;
	for(int i=0;i< n-1 ;i++){
		for(int j=0;j<n-i-1;j++){
			if(val[j] > val[j+1]){
				tmp = val[j];
				val[j] = val[j+1];
				val[j+1] = tmp;
			}
		}
	}
}

void main(int argc,int *argv[]){
	int *val,*ret,kay,i=0,tmp=0;
	ret = (int*) malloc(2 * sizeof(int));
	val = (int*) malloc(1000 * sizeof(int));

	printf ("Enter in a list of numbers ito be stored in a dynamic array.\n");
	printf ("End the list with the terminal value of -999\n");

	while(1){
		scanf("%d ",&kay);
		if(kay == -999){
			break; }
		else{
			val[i] = kay;	
			i = i+1; }
	}	
	tmp = i;
	
	//makeCopyArray(val,tmp);
	/* this is copy array that will do shit, i have commented it so uncommented to do shit */
	
	sort(val,tmp);


	printf("Enter in a list the numbers to use for searching. \n");
	printf ("End the list with a terminal value of -999\n");
	while(1){
		scanf("%d ",&kay);
		if(kay == -999 ){
			break;}
		else{
		ret = sumCheck(kay,val,tmp);	}
	if(ret[0] == 1){
		printf("found the elements that add upto the target = %d at val[%d]= %d and val[%d] = %d \n",kay,ret[1],val[ret[1]],ret[2],val[ret[2]]);}	
	else{ printf("Not found the elements that add upto the target\n");}
	}



}
