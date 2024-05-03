# COH-PIAH
Programa completo - Similaridades entre textos - Caso COH-PIAH parte do curso Introdução à Ciência da Computação com Python oferecido pela Universidade de São Paulo via Cousera.

# Introdução 
Manuel Estandarte é monitor na disciplina Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

# Detecção de autoria
Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.

# Traços linguísticos
Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

Tamanho médio de palavra: Média simples do número de caracteres por palavra.

Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.

Tamanho médio de sentença: Média simples do número de caracteres por sentença.

Complexidade de sentença: Média simples do número de frases por sentença.

Tamanho médio de frase: Média simples do número de caracteres por frase.

# Funcionamento do programa
A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que seu programa deve utilizar são calculados da seguinte forma:

Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.

Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 
4
5
=
0.8
5
4
​
 =0.8

Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 
3
5
=
0.6
5
3
​
 =0.6

Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).

Complexidade de sentença é o número total de frases divido pelo número de sentenças.

Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

Após calcular esses valores para cada texto, você deve compará-los com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, 
𝑎
a e 
𝑏
b, é dado pela fórmula:

𝑆
𝑎
𝑏
=
∑
𝑖
=
1
6
∣
∣
𝑓
𝑖
,
𝑎
−
𝑓
𝑖
,
𝑏
∣
∣
6
S 
ab
​
 = 
6
∑ 
i=1
6
​
 ∣∣f 
i,a
​
 −f 
i,b
​
 ∣∣
​
 

Onde:

𝑆
𝑎
𝑏
S 
ab
​
  é o grau de similaridade entre os textos 
𝑎
a e 
𝑏
b;

𝑓
𝑖
,
𝑎
f 
i,a
​
  é o valor de cada traço linguístico 
𝑖
i no texto 
𝑎
a; e

𝑓
𝑖
,
𝑏
f 
i,b
​
  é o valor de cada traço linguístico 
𝑖
i no texto 
𝑏
b.
