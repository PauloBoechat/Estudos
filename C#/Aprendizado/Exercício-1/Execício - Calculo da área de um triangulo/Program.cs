using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Execício___Calculo_da_área_de_um_triangulo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Criando variaveis
            double a = 0;
            double h= 0;
            double b = 0;
            string entrada = "";

            Console.WriteLine("Calculo area triangulo");//Titulo
            Console.Write("Digite o valor do base:");//Pergunta
            entrada = Console.ReadLine();//Coleta dos dados
            b = Convert.ToDouble(entrada);//Conversão

            Console.Write("Digite o valor do altura:");
            entrada = Console.ReadLine();
            h = Convert.ToDouble(entrada);

            a = ((b * h) / 2);//Executando calculo
            Console.WriteLine("A area do triangulo é {0}", a);//printando

            Console.ReadKey();


        }
    }
}
