using System.ComponentModel;
using Projeto1.Models;
using System;

List<string> listaString = new List<string>();

listaString.Add("SP");
listaString.Add("BA");
listaString.Add("MG");

Console.WriteLine("Percorrendo com FOR");
for (int contador = 0; contador < listaString.Count; contador++)
{
    Console.WriteLine($"Posição N{contador} - {listaString[contador]}");
}

Console.WriteLine("Percorrendo com FOREACH");
int contadorForeach = 0;
foreach (string item in listaString)
{
    Console.WriteLine($"Posição N{contadorForeach} - {item}");
}










//Console.WriteLine();

//Console.WriteLine("Percorrendo Array com o FOREACH");
//int contadorForeach = 0;
//foreach (int valor in arrayInteiros)
//{
//    Console.WriteLine($"Posição N{contadorForeach} - {valor}"); 
//}




//int numero = 5;
//int controle = 0;

//while (true)// pode fazer while (controle < 10)
//{
//    Console.WriteLine($"{numero} x {controle} = {numero * controle}");
//    controle++;
//    if (controle > 10)
//    {
//        break;
//    }
//}






//Console.WriteLine("Sistema de taboadas");

//Console.Write("Digite o número para fazer a tabuada: ");
//int numero = Convert.ToInt32(Console.ReadLine());

//for (int i = 1; i <= 10; i++)
//{
    //Console.WriteLine($"{numero} x {i} = {numero * i}");
//}




//Calculadora calc = new Calculadora();
//calc.Somar(2,5);
//calc.Subtrair(10, 50);
//calc.Multiplicar(15, 45);
//calc.Dividir(10, 2);
//calc.Potencia(3, 3);
//calc.Seno(30);
//calc.Coseno(30);
//calc.Tangente(30);