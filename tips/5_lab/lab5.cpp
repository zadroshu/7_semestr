// lab5.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
#include <stdio.h>
#include <math.h>


void printMatrix(int row, int col, int* matrix) {
	for (int y = 0; y < row; y++) {
		printf("| ");
		for (int x = 0; x < col; x++) {
			printf("%d ", matrix[y * col + x]);
		}
		printf("|\n");
	}
}

void transpaner(int row, int col, int* matrix, int* matrixT) {
	for (int x = 0; x < col; x++) {
		for (int y = 0; y < row; y++) {
			matrixT[x * row + y] = matrix[y * col + x];
		}
	}
}

void generateOnesesMatrix(int row, int* matrix) {
	for (int y = 0; y < row; y++) {
		for (int x = 0; x < row; x++) {
			if (x == y) {
				matrix[y * row + x] = 1;
			}
			else {
				matrix[y * row + x] = 0;
			}
		}
	}
}

void generateTestMatrix(int row, int col, int* matrix, int* matrixTest) {
	// Transpaner
	int *matrixT = new int[col*row];
	transpaner(row, col, matrix, matrixT);

	// Oneses
	int *matrixO = new int[col * row];
	generateOnesesMatrix(col, matrixO);

	// Generate
	for (int y = 0; y < col; y++) {
		for (int x = 0; x < row; x++) {
			matrixTest[y * (col + row) + x] = matrixT[y * row + x];
		}
		for (int x = 0; x < col; x++) {
			matrixTest[y * (col + row) + row + x] = matrixO[y * col + x];
		}
	}
}

int pow_(int a, int step) {
	int result = 1;
	while (step > 0) {
		result *= a;
		step -= 1;
	}
	return result;
}

int invert(int data) {
	if (data == 1) { return 0; }
	return 1;
}

void findError(int row, int col, int* matrixH, int* b, int* error) {

	//int matrixHT[row * col * 2];
	//transpaner(col, row * 2, matrixH, matrixHT);
	//printMatrix(row * 2, col, matrixHT);


	int sumE;
	int index = 0;
	for (int e = 0; e < col; e++) {
		sumE = 0;
		for (int x = 0; x < row + col; x++) {
			sumE += matrixH[(row + col) * e + x] * b[x];
			while (sumE > 1) {
				sumE -= 2;
			}
			//printf("%d * %d + ", b[x], matrixH[row * e + x]);
		}
		index += pow_(2, col - e - 1) * sumE;
		//printf("\n%d\n", (int)(pow_(2, col - e - 1)));
		printf("%d", sumE);
	}


	printf(" = %d\n", index);

	// Fix
	if (index > 0) {
		b[col + row - index] = invert(b[col + row - index]);
	}

}


#define ROW 3
#define COL 3

int main(int argc, char* argv[]) {

	int matrixG[ROW * COL] = {
		0, 1, 1,
		1, 0, 1,
		1, 1, 0,
	};

	int matrixH[ROW * COL + COL * COL];

	printMatrix(ROW, COL, matrixG);
	printf("\n");
	generateTestMatrix(ROW, COL, matrixG, matrixH);
	printf("\n");
	printMatrix(COL, ROW + COL, matrixH);
	printf("\n\n");

	int b[COL * ROW] = {
		1, 1, 0, 1, 1, 0
	};
	int error[COL];
	findError(ROW, COL, matrixH, b, error);


	printf("\nFixed code:\n");
	for (int i = 0; i < COL + ROW; i++) {
		printf("%d", b[i]);
	}



	printf("\n");
	return 0;
}