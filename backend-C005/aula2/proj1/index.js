const express = require('express');
const app = express();

const port = 3000;

const filmes = [
    'Blade Runner',
    'Scarface',
    'Psicose', 
    'Estomago'
];

app.get('/',(req, res) => {
    res.send("Olá humano, lista de filme aqui");
})

app.get('/filmes',(req, res) => {
    res.send(filmes);
})

app.get('/filmes/:id',(req, res) => {
    const id = req.params.id -1;
    const filme = filmes[id];
    res.send(filme);
})

app.listen(port, () => {
    console.info(`App ta rodano em: http://localhost:${port}/`)
})