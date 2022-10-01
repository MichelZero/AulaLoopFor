/* 
 Autores:
 Michel 

 Data: 01/10/2022

 */

/* 
C / C++ (loop)
Quando você souber exatamente quantas vezes deseja percorrer um bloco de código, use o forloop em vez de um whileloop: 
*/

/* 
 Sintaxe
 for (instrução 1; instrução 2; instrução 3) {
 bloco de instruções executado no loop
 }

 A instrução 1 é executada (uma vez) antes da execução do bloco de código.

A instrução 2 define a condição para executar o bloco de código.

A instrução 3 é executada (todas as vezes) após a execução do bloco de código.

 */

//#include <iostream>
using namespace std;

int main() {
  for (int i = 0; i < 5; i++) {
    cout << i << "\n";
  }
  return 0;
}

// imprime 0 .. 4