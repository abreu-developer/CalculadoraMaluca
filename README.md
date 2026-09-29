# CalculadoraMaluca

O projeto possui três calculadoras, cada uma responsável por uma operação específica:

Calculator 1
Responsável por realizar um cálculo básico a partir de um número recebido na requisição. Possui validação dos dados de entrada e tratamento de erros.

Calculator 2
Recebe uma lista de números e calcula o desvio padrão utilizando um driver baseado em NumPy.

Calculator 3
Recebe uma lista de números e realiza o cálculo da variância e da multiplicação dos valores. Antes de retornar o resultado, realiza uma validação para verificar a relação entre os valores calculados.


Arquitetura
As calculadoras utilizam uma separação de responsabilidades baseada em:

Calculators: responsáveis pelas regras de negócio.
Drivers: responsáveis pela implementação dos cálculos matemáticos.
Factories: responsáveis pela criação e configuração das calculadoras.
Routes: responsáveis por receber as requisições HTTP e retornar as respostas.
Error Controller: responsável pelo tratamento centralizado das exceções.
