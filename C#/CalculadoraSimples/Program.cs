using System;
using CalculadoraSimples.Models;

class Program
{
    static void Main()
    {
        Console.WriteLine();
        Console.WriteLine("-=-=-=-=-=Calculadora Simples=-=-=-=-=-");
        while (true)
        {
            Console.WriteLine();

            Console.WriteLine("Soma - 1");
            Console.WriteLine("Subtração - 2");
            Console.WriteLine("Multiplicação - 3");
            Console.WriteLine("Divisão - 4");
            Console.WriteLine("Potência - 5");
            Console.WriteLine("Raiz Quadrada - 6");
            Console.WriteLine("Resto da Divisão - 7");

            Console.WriteLine();

            Console.Write("Escolha uma das opções acima: ");
            string escolha = Console.ReadLine();
            Console.WriteLine();

            if (escolha == "1")
            {
                Console.WriteLine("=-Soma-=");
                Console.WriteLine();

                Console.Write("Digite o primeiro valor: ");
                int x = Convert.ToInt32(Console.ReadLine());

                Console.Write("Digite o segundo valor: ");
                int y = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine();
                Calculadora calculadora = new Calculadora();
                calculadora.Soma(x, y);

            }
            else if (escolha == "2")
            {
                Console.WriteLine("=-Subtração-=");
                Console.WriteLine();

                Console.Write("Digite o primeiro valor: ");
                int x = Convert.ToInt32(Console.ReadLine());

                Console.Write("Digite o segundo valor: ");
                int y = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine();
                Calculadora calculadora = new Calculadora();
                calculadora.Subtrair(x, y);

            }
            else if (escolha == "3")
            {
                Console.WriteLine("=-Multiplicação-=");
                Console.WriteLine();

                Console.Write("Digite o primeiro valor: ");
                int x = Convert.ToInt32(Console.ReadLine());

                Console.Write("Digite o segundo valor: ");
                int y = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine();
                Calculadora calculadora = new Calculadora();
                calculadora.Multiplicar(x, y);
            }
            else if (escolha == "4")
            {
                Console.WriteLine("=-Divisão-=");
                Console.WriteLine();

                Console.Write("Digite o primeiro valor: ");
                int x = Convert.ToInt32(Console.ReadLine());

                Console.Write("Digite o segundo valor: ");
                int y = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine();
                Calculadora calculadora = new Calculadora();
                calculadora.Dividir(x, y);
            }
            else if (escolha == "5")
            {
                Console.WriteLine("=-Potência-=");
                Console.WriteLine();

                Console.Write("Digite o primeiro valor: ");
                int x = Convert.ToInt32(Console.ReadLine());

                Console.Write("Digite o segundo valor: ");
                int y = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine();
                Calculadora calculadora = new Calculadora();
                calculadora.Potencia(x, y);
            }
            else if (escolha == "6")
            {
                Console.WriteLine("=-Raiz Quadrada-=");
                Console.WriteLine();

                Console.Write("Digite o número a ser calculado: ");
                int x = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine();
                Calculadora calculadora = new Calculadora();
                calculadora.RaizQuadrada(x);
            }
            else
            {
                Console.WriteLine("Sua opção não existe");
                Console.WriteLine();
                continue;
            }

            Console.Write("Deseja efetuar outro calculo? (S/N) --> ");
            string saida = Console.ReadLine();

            if saida == "S" || "s"
            {
                continue;
            }
            else
            {
                break;
            }
        }

    }
}