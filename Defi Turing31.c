#include ‹stdio.h>
#include ‹stdlib.h>

int main(){
	int sum =0;
	for(int a=0;a‹=200;a++){
		for(int b=0;b‹=100;b++){
			for(int c=0;c‹=50;c++){
				for(int d=0;d‹=20;d++){
					for(int e=0;e‹=10;e++){
						for(int f=0;f‹=5;f++){
							for(int g=0;g‹=2;g++){
								if(1000==5*a+10*b+20*c+50*d+100*e+200*f+500*g){
									sum += 1;
							}
						}
					}
				}
			}	
		}
	}
}
printf("%d\n",sum);
}
// 104560
