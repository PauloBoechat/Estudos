using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CalculadoraSimples.Models
{
    public class Calculadora
    {
        public void Soma(int x, int y)
        {
            Console.WriteLine($"{x} + {y} = {x + y}");
        }
        public void Subtrair(int x, int y)
        {
            Console.WriteLine($"{x} - {y} = {x - y}");
        }
        public void Multiplicar(int x, int y)
        {
            Console.WriteLine($"{x} x {y} = {x * y}");
        }
        public void Dividir(int x, int y)
        {
            Console.WriteLine($"{x} / {y} = {x / y}");
        }
        public void Potencia(int x, int y)
        {
            Console.WriteLine($"{x} ^ {y} = {Math.Pow(x, y)}");
        }
        public void RaizQuadrada(int x)
        {
            Console.WriteLine($"√{x} = {Math.Sqrt(x)}");
        }
        public void RestoDivisao(int x, int y)
        {
            Console.WriteLine($"{x} % {y} = {x % y}");
        }
        
    }
}
