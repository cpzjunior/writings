# Como impedir que seu MVP vire um Leviatã

_Entre a complexidade que antecipa o futuro e a simplicidade que impede o aprendizado._

**Resumo:** Um MVP não é o menor produto que conseguimos colocar no ar, mas o menor conjunto necessário para testar uma hipótese e aprender algo relevante com o resultado. O risco está tanto em construir demais, antecipando problemas que talvez nunca existam, quanto em construir de menos e comprometer a validade do aprendizado. Por isso, a complexidade precisa ser proporcional ao que sabemos, aos riscos que realmente importam e às perguntas que precisamos responder naquele momento. O MVP pode crescer conforme aprendemos, mas esse crescimento deve ser consequência do conhecimento adquirido, não da tentativa de antecipar o futuro.

------------------------------------------------------------------------

Tenho visto muita gente com boas ideias enfrentar dificuldade para tirá-las do papel. Enderecei parte desse problema em “[Antes de tirar uma ideia do papel, é preciso colocá-la nele](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, mas existe uma dificuldade que começa justamente quando a ideia deixa de ser apenas uma ideia e passa a ser construída: manter o MVP pequeno sem comprometer sua viabilidade.

A intenção inicial costuma ser simples. Construir o suficiente para colocar uma hipótese à prova e aprender com o resultado. O problema é que, à medida que a construção avança, surgem boas razões para ampliar o escopo. Uma funcionalidade parece necessária, uma exceção parece importante, uma decisão arquitetural pode ser generalizada, uma preocupação com escala futura parece prudente. Pouco a pouco, aquilo que deveria servir para testar uma hipótese começa a incorporar respostas para problemas que ainda nem sabemos se teremos.

Para facilitar o cadastro dos usuários, vamos implementar diferentes mecanismos de autenticação, como SSO e OAuth. Como o sistema precisa considerar diferentes níveis, perfis e regras de acesso, precisaremos de um modelo de permissões multidimensional, no estilo de plataformas corporativas como a Salesforce. Como teremos um sistema de assinaturas, vamos construir um ledger baseado em blockchain e um sistema de geolocalização para o antifraude. Para garantir disponibilidade total, adotaremos uma arquitetura multicloud em múltiplas AZs. Para nos antecipar a uma eventual expansão para a América Latina e a Ásia, teremos também suporte a múltiplas localidades e configurações regionais. Quando percebemos, começamos tentando validar uma hipótese de produto e estamos projetando uma plataforma distribuída globalmente para resolver problemas hipotéticos antes mesmo de saber se o produto resolve o problema para o qual foi criado.

É aí que surge a comparação com o Leviatã. Na tradição bíblica, o Leviatã é um monstro associado ao mar e ao caos, uma criatura que escapa ao domínio humano. A comparação é quase literal: o MVP começa como algo pequeno e controlável, mas pode acumular funcionalidades, dependências, regras e exceções até se transformar em um monstro cuja complexidade já não responde facilmente à intenção que deu origem ao produto.

Mas existe uma armadilha no sentido contrário. Na tentativa de manter o MVP sob controle, podemos cortar justamente os elementos necessários para testar a hipótese. O resultado é pequeno, mas já não é suficientemente viável para nos dizer se estamos diante de uma solução adequada.

É nessa tensão, entre construir demais e construir de menos, que começa a discussão sobre o que realmente deve caber dentro de um MVP.

## O MVP não é um produto pequeno

MVP costuma ser entendido como um produto com poucas funcionalidades. É uma definição intuitiva, mas insuficiente. O “mínimo” não está na quantidade de software que conseguimos construir, mas no menor conjunto necessário para colocar uma hipótese relevante à prova de forma suficientemente confiável.

Essa distinção muda a maneira como decidimos o que entra no produto. A pergunta não deveria ser “qual é a menor quantidade de código que conseguimos colocar em produção?”, mas “qual é o menor investimento capaz de nos ensinar algo relevante sobre o produto?”. A segunda pergunta nos obriga a considerar não apenas o que será construído, mas também a qualidade do aprendizado que aquilo será capaz de produzir.

Uma funcionalidade pode ser simples de implementar e ainda assim ser indispensável para testar a hipótese. Outra pode exigir pouco esforço e não acrescentar praticamente nada ao que precisamos descobrir. O esforço de desenvolvimento, portanto, não é um bom indicador isolado de relevância. O que importa é a contribuição daquela parte para o experimento.

É por isso que um MVP pequeno pode ser inadequado. Ao remover uma parte essencial da experiência, podemos colocar algo no ar rapidamente, mas produzir um resultado que não responde à pergunta original. Nesse caso, reduzimos o produto sem necessariamente reduzir a incerteza. Construímos menos, mas aprendemos menos também.

O mesmo raciocínio vale para o excesso. Uma solução pode ser tecnicamente sofisticada e funcionar perfeitamente, mas incorporar capacidades que ainda não são necessárias para testar a tese. O problema, nesse caso, não está necessariamente na qualidade da solução, mas no momento em que escolhemos construí-la. Estamos investindo para responder perguntas que o produto ainda não nos obrigou a fazer.

O tamanho do MVP, portanto, não é uma medida absoluta. Ele precisa ser proporcional ao que queremos descobrir naquele momento.

### Como o Leviatã nasce

O crescimento do MVP raramente acontece por causa de uma grande decisão. Ele costuma nascer da sucessão de pequenas decisões que, tomadas individualmente, parecem perfeitamente defensáveis. Uma integração parece necessária, uma exceção parece simples de acomodar, uma estrutura mais genérica parece evitar retrabalho, uma preocupação com escala parece prudente. Uma configuração adicional parece barata. Uma funcionalidade pedida por um usuário parece importante demais para ser deixada de fora.

É nesse contexto que aparece o conhecido “já que estamos fazendo isso, podemos fazer aquilo também”. A cada decisão, o escopo se desloca um pouco. Como nenhuma mudança parece suficiente para justificar uma interrupção, a soma delas passa despercebida até que o produto já esteja respondendo a problemas que não faziam parte da pergunta original.

O ponto mais traiçoeiro é que o custo de uma decisão raramente termina na sua implementação. Uma nova funcionalidade passa a exigir testes, monitoramento, documentação, suporte e manutenção. Pode introduzir dependências, novos estados, regras de negócio e caminhos de execução que antes não existiam. Também pode restringir decisões futuras, tornando mais caro mudar de direção quando novas informações aparecerem.

Por isso, o custo de uma funcionalidade não é apenas o esforço necessário para colocá-la em produção. É também tudo aquilo que passa a existir depois que ela entra no sistema.

É assim que o escopo pode escapar da intenção original sem que exista um erro evidente para apontar. Cada decisão local pode fazer sentido, enquanto o resultado acumulado deixa de fazer. O Leviatã não nasce necessariamente de uma escolha absurda, mas da soma de escolhas razoáveis que, juntas, produzem uma complexidade que ninguém pretendia construir.

## O problema de tentar resolver o mundo

Existe uma forma particularmente perigosa de antecipação: tentar construir, desde o início, a solução para todos os problemas que o produto talvez tenha no futuro.

Quando a tese ainda é incerta, começamos a imaginar diferentes perfis de usuário, modelos de negócio, grandes volumes de dados, múltiplas integrações, necessidades de internacionalização, diferentes níveis de permissão e cenários de escala. Cada preocupação pode ser legítima isoladamente. O problema aparece quando todas elas passam a influenciar a primeira versão do produto.

É compreensível. Quem constrói sistemas sabe que algumas decisões são difíceis de mudar depois e que determinadas escolhas podem gerar dívida técnica. Também sabe que corrigir uma arquitetura inadequada mais tarde pode ser muito mais caro do que tomar uma boa decisão desde o início. O risco está em transformar essa preocupação legítima em uma tentativa de prever o produto inteiro antes mesmo de sabermos se ele é, de fato, uma solução adequada e viável.

É como assumir o papel de Atlas antes de saber se haverá um mundo para sustentar: carregamos antecipadamente o peso de todos os futuros possíveis, mesmo sem saber quais deles realmente existirão.

Há uma inversão aí. Em vez de a solução evoluir a partir do que aprendemos sobre o problema, começamos a construir uma solução para um futuro hipotético. Passamos a tomar decisões com base em usuários que talvez existam, volumes que talvez sejam alcançados, mercados que talvez sejam explorados e requisitos que talvez nunca apareçam.

Esse futuro tem um custo no presente. E, no estágio inicial, talvez nem saibamos se chegaremos até ele.

A arquitetura precisa lidar com riscos reais, não com todas as possibilidades imagináveis. O mesmo vale para produto. Uma decisão merece investimento proporcional à importância e à probabilidade do problema que pretende resolver. Preparar tudo para uma escala que talvez nunca exista é pagar antecipadamente por um futuro que ainda não foi validado.

## Complexidade também pode ser necessária

Isso não significa que toda complexidade seja um sinal de excesso. Há produtos em que segurança, auditoria, resiliência, observabilidade, controle de acesso ou requisitos operacionais fazem parte da própria solução. Nesses casos, retirar complexidade não significa necessariamente simplificar o produto. Pode significar retirar uma propriedade necessária para que ele funcione corretamente.

Em determinados contextos, simplificar demais o sistema pode ser justamente a decisão irresponsável. Um MVP que movimenta dinheiro, trata dados sensíveis ou participa de processos críticos não pode usar a experimentação como justificativa para ignorar propriedades essenciais do domínio. O fato de estarmos validando uma hipótese não suspende os riscos que já existem.

Também existe uma diferença entre a complexidade percebida pelo usuário e a complexidade necessária no sistema. Uma experiência pode ser simples na superfície e depender de uma infraestrutura bastante sofisticada para funcionar de maneira segura, resiliente e confiável. O objetivo, portanto, não é eliminar complexidade, mas evitar complexidade que não tenha uma razão concreta para existir naquele momento.

Por isso, a pergunta não deveria ser simplesmente “como deixar o sistema mais simples?”, mas “qual complexidade é necessária para este estágio do produto?”. A resposta depende tanto da hipótese que queremos validar quanto dos riscos que não podemos aceitar.

Essa distinção também ajuda a evitar uma falsa oposição entre produto e engenharia. Produto pode estar tentando reduzir o escopo para validar uma hipótese, enquanto engenharia pode estar tentando reduzir um risco técnico relevante ou evitar uma decisão difícil de reverter. As duas preocupações são legítimas. O trabalho de arquitetura está justamente em avaliar esses trade-offs e encontrar uma solução proporcional ao estágio do produto, sem transformar simplicidade ou sofisticação em princípios absolutos.

## Construir menos também pode ser um erro

A reação ao excesso costuma ser o corte. Eliminamos funcionalidades, simplificamos fluxos e reduzimos o escopo até chegar a algo que pareça pequeno o suficiente para ser chamado de MVP. O problema é que reduzir o produto não significa necessariamente aumentar a qualidade do experimento.

Existe uma diferença importante entre reduzir o que será construído e reduzir a capacidade de aprender com aquilo que foi construído. Uma hipótese pode depender de determinados elementos da experiência para ser testada de forma minimamente representativa. Retirar justamente esses elementos pode produzir um resultado aparentemente objetivo, mas que responde a uma pergunta diferente da que pretendíamos fazer.

Podemos, por exemplo, concluir que uma solução não funciona quando, na verdade, testamos uma versão tão simplificada que ela deixou de representar a proposta de valor original. Nesse caso, construímos menos, mas também aprendemos menos.

Por isso, o MVP não serve apenas para colocar alguma coisa em produção. Ele precisa produzir um resultado que seja útil para a próxima decisão. Quanto mais a solução é simplificada, mais importante se torna entender o que foi preservado e o que foi removido. Uma simplificação que elimina justamente o elemento responsável por conectar o problema à solução pode tornar o experimento barato, mas pouco informativo.

Em alguns casos, inclusive, o melhor MVP pode nem ser software. Um protótipo, uma operação manual ou um piloto limitado podem responder à pergunta com menos investimento e menos complexidade. Se conseguimos testar a hipótese sem construir todo o sistema, talvez essa seja a forma mais adequada de começar.

O objetivo não é construir o mínimo possível. É construir apenas o necessário para que o resultado nos diga algo que valha a pena saber.

## O MVP precisa ser diagnosticável

Esse talvez seja um dos critérios mais importantes para decidir o que entra em uma primeira versão: quando o experimento terminar, precisamos conseguir interpretar o que aconteceu.

Um MVP pode falhar por diferentes motivos. A hipótese sobre o problema pode estar errada. A solução pode não ser adequada. A experiência pode não funcionar como esperado. O preço pode estar errado. O canal de aquisição pode não funcionar. A tecnologia pode impor alguma limitação. A operação pode ser inviável. O resultado observado é consequência de uma combinação dessas variáveis, e nem sempre é possível determinar com precisão qual delas foi responsável.

Quanto mais coisas mudamos simultaneamente, mais difícil fica interpretar o resultado. Um produto pode ter sido rejeitado porque a proposta de valor não fazia sentido, porque a experiência era ruim ou simplesmente porque uma limitação da implementação impediu que o usuário percebesse o valor da solução. Sem algum cuidado na composição do MVP, um resultado negativo pode dizer muito pouco sobre a hipótese que pretendíamos testar.

Isso não significa que todo MVP precise ser um experimento controlado ou que seja possível isolar perfeitamente cada variável. Produtos reais raramente oferecem esse nível de controle. Significa apenas que precisamos preservar alguma capacidade de distinguir o que estamos aprendendo. Existe uma diferença entre aceitar a incerteza inerente ao produto e introduzir tanta complexidade no experimento que o próprio resultado se torna difícil de interpretar.

Um MVP, portanto, precisa ser mais do que executável. Precisa ser diagnosticável. Seu resultado deve ser capaz de orientar a próxima decisão, seja para corrigir a solução, reformular a hipótese ou simplesmente abandonar uma direção que não se mostrou promissora.

## O mínimo também se move

Há outro aspecto importante: o MVP não é uma categoria permanente do produto. A tese de um produto pode mudar conforme surgem novas evidências. Uma hipótese inicial pode ser refinada, descartada ou substituída por outra mais sofisticada. As perguntas também mudam. Consequentemente, aquilo que era suficiente para testar uma hipótese em determinado momento pode deixar de ser suficiente para responder à próxima pergunta.

Uma solução simples pode ser adequada para descobrir se determinado problema realmente existe. Depois, pode ser necessário entender se a solução proposta é suficientemente valiosa para ser adotada. Mais adiante, talvez seja preciso avaliar retenção, comportamento em escala, integração com outros sistemas ou algum aspecto operacional que não fazia parte da pergunta inicial.

Nesse processo, o conceito de mínimo se desloca. Uma tese mais sofisticada pode exigir uma solução mais sofisticada. Isso não significa que o MVP fracassou e virou um produto inchado. Pode significar simplesmente que aprendemos o suficiente para fazer perguntas melhores e, portanto, precisamos de uma solução capaz de respondê-las.

A questão está na direção desse movimento. A complexidade deve acompanhar a evolução da tese, e não tentar antecipá-la. O produto pode crescer conforme aumenta o conhecimento sobre o problema, os usuários e a própria solução. O que não faz sentido é construir antecipadamente aquilo que só faria sentido depois de termos aprendido.

O problema não é o MVP crescer. O problema é ele crescer antes de sabermos por que precisa crescer.

## Quando o MVP começa a virar um Leviatã

O sinal mais preocupante talvez não seja o número de funcionalidades, o tamanho do código ou a quantidade de componentes arquiteturais. É quando a complexidade deixa de estar claramente relacionada ao propósito da primeira versão.

Em algum momento, pode se tornar difícil explicar por que determinadas partes do produto existem, quais perguntas elas ajudam a responder ou quais riscos concretos justificaram sua inclusão. Decisões passam a ser tomadas para cenários que ainda não existem, exceções começam a moldar o comportamento principal e uma parcela crescente do esforço passa a ser consumida pela própria complexidade do sistema.

Esse é o ponto em que vale voltar à pergunta que deu origem ao MVP: o que estamos tentando descobrir?

A resposta também impede o movimento contrário. Nem tudo que pode ser removido deveria ser removido. Uma funcionalidade pode ser indispensável para que a hipótese seja testada de maneira válida, mesmo que pareça aumentar o tamanho da primeira versão. O objetivo nunca foi construir o menor sistema possível, mas uma solução proporcional ao que sabemos, ao que ainda precisamos descobrir e aos riscos que realmente importam.

É por isso que o Leviatã não é simplesmente um MVP grande. É o MVP que perdeu o controle sobre a própria complexidade.

Uma primeira versão não precisa ser uma versão reduzida de tudo aquilo que imaginamos construir no futuro. Ela precisa ser uma resposta deliberadamente limitada às perguntas que temos agora. Conforme aprendemos, a tese pode mudar, novas perguntas podem surgir e a solução pode precisar crescer. Nesse caso, o crescimento deixa de ser antecipação e passa a ser consequência do conhecimento adquirido.

O perigo começa quando fazemos o caminho inverso: construímos primeiro e esperamos que o futuro nos dê uma razão para tudo aquilo. Nesse cenário, aquilo que deveria nos ajudar a descobrir o caminho pode acabar criando um caminho que teremos dificuldade de abandonar.
