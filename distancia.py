#include <stdio.h>

from ast import main
from os import name


int main() 
{
    chr name[50]; // Definindo uma string para armazenar o nome do motorista
    float distancia, velocidade, tempo;

    printf("Digite o nome do motorista: ");
    scanf("%s", nome); // Lendo o nome do motorista

    printf("Digite a distância a percorrer em km: ");
    scanf("%f", &distancia);

    printf("Digite a velocidade média em km/h: ");
    scanf("%f", &velocidade);

    tempo = distancia / velocidade;

    printf("O motorista %s levará %.2f horas para fazer o percurso.\n", nome, tempo);

    return 0;
}