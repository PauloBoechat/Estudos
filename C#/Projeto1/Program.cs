using Projeto1.Models;

int quantidadeSys = 10;

Console.WriteLine("Sistema de Vendas E-Commerce");
Console.Write("Digite a quantidade de produtos que você vai comprar: ");
int quantidadeUser = Convert.ToInt32(Console.ReadLine());

if (quantidadeUser == 0)
{
    Console.WriteLine("Você não comprou nada!");
}
else if (quantidadeUser <= quantidadeSys)
{
    Console.WriteLine("Compra efetuada com sucesso!");
}
else
{
    Console.WriteLine($"Desculpe, mas não temos mais do que {quantidadeSys} no nosso estoque.");
}
Console.ReadKey();
