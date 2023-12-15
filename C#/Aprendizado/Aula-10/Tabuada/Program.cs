using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tabuada
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string entrada = "";
            int n = 0;

            Console.WriteLine("Tabuada"); //Titulo da aplicação
            Console.Write("Digite o número da tabuada:"); //Pergunta
            entrada = Console.ReadLine(); //Coleta de dados
            n = Convert.ToInt32(entrada); //Conversão
            Console.WriteLine("1x{0} = {1}", n, n * 1); //execução
            Console.WriteLine("2x{0} = {1}", n, n * 2); //execução
            Console.WriteLine("3x{0} = {1}", n, n * 3); //execução
            Console.WriteLine("4x{0} = {1}", n, n * 4); //execução
            Console.WriteLine("5x{0} = {1}", n, n * 5); //execução
            Console.WriteLine("6x{0} = {1}", n, n * 6); //execução
            Console.WriteLine("7x{0} = {1}", n, n * 7); //execução
            Console.WriteLine("8x{0} = {1}", n, n * 8); //execução
            Console.WriteLine("9x{0} = {1}", n, n * 9); //execução
            Console.WriteLine("10x{0} = {1}", n, n * 10); //execução
            //Não pode converter na hora de coletar os dados, só depois :(

            Console.ReadKey();
        }
    }
}
