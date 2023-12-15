using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entrada_de_Dados
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Programa que efetua leitura de dados do usuário"); //WriteLine faz a escrita do título
            Console.WriteLine("Olá qual o seu nome?"); //WriteLine faz a escrita da pergunta
            Console.Write("Digite seu nome:"); //Write faz a caixa de texto sem pular uma linha
            string nome = Console.ReadLine(); //ReadLine faz a leitura do valor e manda para a variavel por meio de *Tipo+Variavel* = Console.ReadLine()
            Console.WriteLine("bem vindo(a) as aulas de programação "+nome); //Aqui o uso da variavel no parenteses com o sinal de +  insere no texto o valor dela
            Console.WriteLine("Bem vindo(a) as aulas de programação {0}", nome); //O {n} com o , variavel(n) infinitamente
            Console.ReadKey(); //Para não terminar o aplicativo assim que aparecer o texto anterior o readkey espera receber alguma tecla
        }
    }
}
