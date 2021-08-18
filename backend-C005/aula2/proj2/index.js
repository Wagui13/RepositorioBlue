const express = require('express');
const app = express();

const port = 3000;

const juegos = [
    '1 - Super Mario Hermanos',
    '2 - El Deos del la Guierra',
    '3 - La Suembra del los Colossos', 
    '4 - Gran Robo Auto',
    '5 - Necessidad del la velocidad',
    '6 - No Hablo Puercaria Niuma'
]

function randomMinMax(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

// home
app.get('/',(req, res) => {
    res.send('Tem uma lista de jogos ai, dá uma olhada no "/juegos"\n'+
    'Ou escolha um só, colocando o numero do filme lá na url, exemplo: "/juegos/1"\n'+
    'Ooou veja um juego aleatório no "/juegos/random"');
})

// todos os juegos
app.get('/juegos',(req, res) => { 
    res.send(juegos);
})

// juego aleatorio
app.get('/juegos/random',(req, res) => {
    const qtd = juegos.length;
    const aleatorio = randomMinMax(1, qtd);
    
    res.send(juegos[aleatorio]);
})

// escolha um juego
app.get('/juegos/:id',(req, res) => {
    const id = req.params.id -1;
    
    if(id >= juegos.length || id < 0) {
        res.send(`Tá errado isso ai irmão, tenta de novo, voce tem de 1 a ${juegos.length}`); 
    } else {
        res.send(juegos[id]); 
    }

})


app.listen(port, () => {
    console.info(`O App está rodando em: http://localhost:${port}/`)
})