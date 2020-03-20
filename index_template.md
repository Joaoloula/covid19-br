---
layout: default
---

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<script>
    var R0s = [1.5, 2, 2.5, 3];
    var CFRs = [0.005, 0.01, 0.02, 0.03];
</script>

<div style="text-align:center">
<!-- <input type="checkbox" id="chooseR0"> Reproduction Number (R<sub>0</sub>) <input type="range" min="0" max="3" value="1" id="R0" disabled> -->

<div id="chart" style="width:100%;height:22rem;display:inline-block;"></div><br/>

<div style="display:inline-block; padding-top:10px; padding-bottom:10px; text-align:left; padding-right:20px">
    <input type="checkbox" id="onlydeaths"/> <label for="onlydeaths">Hide states with no recorded deaths</label>
</div>
<div style="display:inline-block; padding-top:10px; padding-bottom:10px; text-align:left;">
    <input type="checkbox" id="chooseR0"> R<sub>0</sub> <input type="range" min="0" max="3" value="1" id="R0" disabled>
    <div id="R0text" style="width:80px; text-align:center; margin-right:20px; display:inline-block; background:lightgray; padding:3px;"></div>
</div>
<div style="display:inline-block; padding-top:10px; padding-bottom:10px; text-align:left;">
    <input type="checkbox" id="chooseCFR"> CFR <input type="range" min="0" max="3" value="1" id="CFR" disabled>
    <div id="CFRtext" style="width:80px; text-align:center; margin-right:20px; display:inline-block; background:lightgray; padding:3px;"></div>
</div>
<br/><i>(hover cursor over graph for numerical values)</i>
</div>

<script>
    document.getElementById("chooseR0").addEventListener('change', (event) => {
        document.getElementById("R0").disabled = !event.target.checked;
        refresh()
    })
    document.getElementById("R0").addEventListener('input', (event) => {refresh()})
    document.getElementById("chooseCFR").addEventListener('change', (event) => {
        document.getElementById("CFR").disabled = !event.target.checked;
        refresh()
    })
    document.getElementById("CFR").addEventListener('input', (event) => {refresh()})
    document.getElementById("onlydeaths").addEventListener('change', (event) => {refresh()})

    var allstats = {{ stats }};
    col = 'blue';
    function refresh(){
        if(document.getElementById("R0").disabled) {
            R0="None"
            document.getElementById("R0text").innerHTML="unknown"
        } else {
            R0=R0s[document.getElementById("R0").value];
            document.getElementById("R0text").innerHTML=R0
        }
        if(document.getElementById("CFR").disabled) {
            CFR="None"
            document.getElementById("CFRtext").innerHTML="unknown"
        } else {
            CFR=CFRs[document.getElementById("CFR").value];
            document.getElementById("CFRtext").innerHTML=CFR*100 + "%"
        }
        
        var stats = allstats[R0 + "," + CFR];
        if(document.getElementById("onlydeaths").checked) {
            _stats = []
            for(var i=0; i<stats.length; i++) {
                if(stats[i][1]['deaths']>0) {
                    _stats.push(stats[i])
                }
            }
            stats = _stats
        }
        console.log("R0=", R0, "CFR=", CFR)
        var data = [
            {
                name: 'Estimated cases',
                x: Array(stats.length).fill(1).map((v, j) => j+1),
                y: Array(stats.length).fill(1).map((v, j) => stats[j][1]['median']),
                marker: {
                    color: col,
                    opacity: 0
                },
                type: 'scatter',
                mode: 'markers',
            },
            {
                name: 'Confirmed cases',
                x: Array(stats.length).fill(1).map((v, j) => j+1),
                y: Array(stats.length).fill(1).map((v, j) => stats[j][1]['positive']),
                type: 'scatter',
                mode: 'markers',
            },
            {
                name: 'Deaths',
                x: Array(stats.length).fill(1).map((v, j) => j+1),
                y: Array(stats.length).fill(1).map((v, j) => stats[j][1]['deaths']),
                type: 'scatter',
                mode: 'markers',
            },
        ];
        shapes = []
        for(var j=0; j<stats.length; j++) {
            if(stats[j][1]['lower50'] != undefined) {
                shapes.push(
                    {layer:'below', type:'line', line:{width:3, color:col}, 
                    x0: j+1, x1: j+1, y0: stats[j][1]['lower50'], y1: stats[j][1]['upper50'] });
                shapes.push(
                    {layer:'below', type:'line', line:{width:1, color:col}, 
                    x0: j+1, x1: j+1, y0: stats[j][1]['lower95'], y1: stats[j][1]['upper95'] });
            }
        }
        layout = {
            hovermode: 'closest',
            title: 'Infections by state <i>({{ date }})</i>',
            xaxis: {
                tickvals: Array(stats.length).fill(1).map((v, j) => j+1),
                ticktext: Array(stats.length).fill(1).map((v, j) => stats[j][0]),
                range: [0, stats.length+1],
                showgrid: false,
                ticklen: 10,
                showline: true,
                showzero: false,
                fixedrange: true
            },
            margin: {t:50, l:50, r:0, b:50},
            yaxis: {
                type: 'log',
                range: [-0.1, 5.2],
                showgrid: false,
                showline: false,
                showzero: false,
                ticklen: 10,
                fixedrange: true
            },
            legend: {
                x: 1,
                xanchor: 'right',
                y: 1
            },
            shapes: shapes
        };
        Plotly.newPlot('chart', data, layout/*,  {staticPlot: true}*/);
    }

    document.getElementById("onlydeaths").checked = window.screen.width<1000;
    refresh();

</script>

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
