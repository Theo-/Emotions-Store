#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>

int logIn(char *name);
int isLoggedIn(char *name);

int main(void) {
	printf("Content-Type: text/html;charset=us-ascii\n");
//printf("lol2");
//	char *data = strdup("UserName=theos&password=22");
	char *data = getenv("QUERY_STRING");
	char password[100];  
//printf("lol1");
	char *passwordIndex = strstr(data, "&");

	sscanf(passwordIndex, "&password=%s", password);
//printf("lol");	
	char username[passwordIndex-data-8];
	int number = passwordIndex-data-9;
	strncpy(username, data+9, passwordIndex-data-9);
	username[number] = '\0';
	
	//printf("\n\n");
	//printf("username=%s and ",username);
	//printf("password=%s", password);  
	
	// We read if we find the username
	int found = 0;
	
//	printf("Creating");
	FILE *file = fopen("Members.csv", "r");
	char usernameBuffer[50];
	char passwordBuffer[50];
//	printf("Opened");
	if(file == NULL) {
		printf("\n\nError");
		exit(0);	
	}

	char c = 0;
	int comp = 0;
	int p = 0;

//	printf("Starting loop");
	while ((c = fgetc(file)) != EOF)
    	{
	//printf("u = %s & p = %s \n", usernameBuffer, passwordBuffer);
		if(c == ',') {
			comp++;
			p = 0;
			continue;
		}
		if((c == '\n')) {
			if(strcmp(usernameBuffer, username) == 0 && strcmp(passwordBuffer, password) == 0) {
				found = 1;
				break;	
			}
			
			strncpy(usernameBuffer, "", 49);
			strncpy(passwordBuffer, "", 49);
			
			comp = 0;
			p = 0;
			continue;	
		}
		if(comp == 0) {
        		usernameBuffer[p] = c;
			usernameBuffer[p+1] = '\0';
		} 
		if(comp == 1) {
			passwordBuffer[p] = c;
			passwordBuffer[p+1] = '\0';
		}
    		p++;
	}

	if(found == 0) {
		printf("\n\n");
		printf("<html><body>Wrong username or password please <a href='login.html'>Try again</a></body></html>");
	} else {
		if(isLoggedIn(username) == 0) {
//printf("Logged in");
			logIn(username);
		}
		printf("Location: catalogue.py?name=%s", username);	
	}
	fclose(file);

	printf("\n\n");

	return 0;
}

int isLoggedIn(char *name) {
	FILE *file = fopen("loggedin.csv", "r");
	if(file == NULL) {
		printf("No loggedin.csv found");
		exit(0);
	}

	char c;
	int p = 0;
	char buffer[50];
//	printf("Looking for %s", name);	

	while((c = fgetc(file)) != EOF) {
//printf("c= %c buffer = %s\n",c, buffer);
		if(c == ',' || c == '\n') {
//			printf("%s = %s", buffer, name);
			if(strcmp(buffer, name) == 0) {
//printf("Logged in");
				return 1;	

			}		

			p = 0;
			continue;
		}

		buffer[p] = c;
		buffer[p+1] = '\0';
		p++;
	}

	return 0;
}

int logIn(char *name) {
	char command[100];
	sprintf(command, "echo \"%s,\" >> loggedin.csv", name); 
	//printf("\n%s\n", command);
	system(command);
	return 1;
}
