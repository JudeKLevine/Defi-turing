#include ‹stdio.h>
#include ‹stdlib.h>
#include ‹math.h>

int main()
{
	int max = 0;
  
	for(int a = 0; a < 3600; a++)
  {
		for(int b = 0; b < 3600; b++)
    {
			for(int c = 0; c < 3600; c++)
      {
				if(a * a == b * b + c * c && a + b + c == 3600)
        {
					int t = a * b * c;
					if(t > max){max = t;}
				}
			}
		}
	}
	printf("%d \n",t);
}
