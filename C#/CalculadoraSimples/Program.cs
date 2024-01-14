using System;
using CalculadoraSimples.Models;

class Program
{
    static void Main()
    {
        Console.WriteLine("Calculadora Simples");

        Console.WriteLine("Soma - 1");
        Console.WriteLine("Subtração - 2");
        Console.WriteLine("Multiplicação - 3");
        Console.WriteLine("Divisão - 4");
        //Console.WriteLine("Potência - 5");
        //Console.WriteLine("Raiz Quadrada - 6");
        //Console.WriteLine("Resto da Divisão - 7");
        //Console.WriteLine("Escolha uma das opções acima: ");

        Console.Write("Escolha uma das opções acima: ");
        string escolha = Console.ReadLine();

        if (escolha == "1")
        {
            Console.WriteLine("Soma");

            Console.Write("Digite o primeiro valor: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.Write("Digite o segundo valor: ");
            int y = Convert.ToInt32(Console.ReadLine());

            Calculadora calculadora = new Calculadora();
            calculadora.Soma(x, y);
        }
        else if (escolha == "2")
        {
            Console.WriteLine("Subtração");

            Console.Write("Digite o primeiro valor: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.Write("Digite o segundo valor: ");
            int y = Convert.ToInt32(Console.ReadLine());

            Calculadora calculadora = new Calculadora();
            calculadora.Subtrair(x, y);
        }
        else if (escolha == "3")
        {
            Console.WriteLine("Multiplicação");

            Console.Write("Digite o primeiro valor: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.Write("Digite o segundo valor: ");
            int y = Convert.ToInt32(Console.ReadLine());

            Calculadora calculadora = new Calculadora();
            calculadora.Multiplicar(x, y);
        }
        else if (escolha == "4")
        {
            Console.WriteLine("Divisão");

            Console.Write("Digite o primeiro valor: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.Write("Digite o segundo valor: ");
            int y = Convert.ToInt32(Console.ReadLine());

            Calculadora calculadora = new Calculadora();
            calculadora.Dividir(x, y);
        }
        else {
            Console.WriteLine("Sua opção não existe");
        }

    }
}