# covid19-br

- Webpage: https://joaoloula.github.io/covid19-br/

Uma das maiores dificuldades na luta contra o coronavírus é a falta de dados confiáveis. A incidência do vírus é difícil de estimar: no Brasil, por exemplo, faltam testes, e o governo anunciou que testará somente os casos graves—ao contrário das diretrizes da OMS—o que faz com que o número de casos confirmados seja uma considerável subestimacão do número real. Como então podemos estimar o número de pessoas infectadas?

O paper [_Inferring the number of COVID-19 cases from recently reported deaths_](https://www.medrxiv.org/content/10.1101/2020.03.10.20033761v1.full.pdf) [1], de Jombart e colegas, é um tratamento tão detalhado dessa pergunta quanto você pode querer ler (de fato, talvez seja um tratamento mais detalhado do que você queira ler.) A ideia é que o dado mais confiável que temos é o número de mortes: se aliarmos a ele as nossas melhores estimativas de algumas constantes epidemiológicas, podemos reconstruir os passos do vírus e chegar a uma boa aproximacão do número de infectados no momento atual.

Para a simulacão acima, usamos o modelo já mencionado de [1], com o método de simulacão descrito em [6], dados do ministério da saúde [7], a estimativa do período de incubacão dada em [2], do intervalo serial dada em [3], e intervalos para a taxa de fatalidade e o número de reproducão baseados nos valores de [4, 5].

Citacões:

[1] [Jombart, T., van Zandvoort, K., Russell, T., Jarvis, C., Gimma, A., Abbott, S., ... & Pearson, C. (2020). Inferring the number of COVID-19 cases from recently reported deaths. medRxiv.](https://www.medrxiv.org/content/10.1101/2020.03.10.20033761v1.full.pdf)

[2] [Linton, N. M., Kobayashi, T., Yang, Y., Hayashi, K., Akhmetzhanov, A. R., Jung, S. M., ... & Nishiura, H. (2020). Incubation period and other epidemiological characteristics of 2019 novel coronavirus infections with right truncation: a statistical analysis of publicly available case data. Journal of Clinical Medicine, 9(2), 538.](https://www.mdpi.com/2077-0383/9/2/538)

[3] [Nishiura, H., Linton, N. M., & Akhmetzhanov, A. R. (2020). Serial interval of novel coronavirus (COVID-19) infections. International Journal of Infectious Diseases.](https://www.medrxiv.org/content/medrxiv/early/2020/02/17/2020.02.03.20019497.full.pdf)

[4] [Wilson, N., Kvalsvig, A., Barnard, L. T., & Baker, M. (2020). Estimating the Case Fatality Risk of COVID-19 using Cases from Outside China. medRxiv.](https://www.medrxiv.org/content/10.1101/2020.02.15.20023499v1)

[5] [Midas-network. COVID-19 parameter estimates. (2020)](https://github.com/midas-network/COVID-19) 

[6] [Covid19-US. (2020)](<https://github.com/covid19-us/covid19-us.github.io>)

[7] [Notificação de casos de doença pelo coronavírus 2019 (COVID-19).](http://plataforma.saude.gov.br/novocoronavirus/)

Esse site usa como modelo o [Covid19-US. (2020)](<https://github.com/covid19-us/covid19-us.github.io>), créditos a Luke Hewitt.

Contato: jloula@mit.edu
