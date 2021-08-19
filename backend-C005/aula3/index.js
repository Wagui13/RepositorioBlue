const express = require('express');
const { get } = require('http');
const app = express();

app.use(express.json());

const port = 3000;

const sims = [
    "sim", 
    "yes",
    "si",
    "oui",
    "hai"
]

// READ
app.get('/', (req, res) => {
    res.send("Opa");
})

app.get('/sims', (req, res) => {
    res.send(sims);
})

app.get('/sims/:id', (req, res) => {
    const id = req.params.id -1;
    const sim = sims[id];
    
    if(!sim) {
        res.send('não tem sim');
    }
    res.send(sim);
})

// CREATE
app.post('/sims', (req, res) => {
    const sim = req.body.sim;
    const id = sims.length;
    
    sims.push(sim);

    res.send(`Filme add sucesso: ${sim} e o id é ${id + 1}`)
})

// UPDATE
app.put('/sims/:id', (req, res) => {
    const id = req.params.id -1;
    const simAntes = sims[id];
    const sim = req.body.sim;
    sims[id] = sim;
    
    res.send(`100% atualizado é ruim de aturar, enfim seu ${simAntes} virou ${sim}`)  
})

// DELETE
app.delete('/sims/:id', (req, res) => {
    const id = req.params.id -1;
    const simAntes = sims[id];
    
    if(!simAntes) {
        res.send('ta errado, tenta de novo')
    }
    delete sims[id];
    
    res.send(`seu ${simAntes} foi deletado man`);
})

app.delete('/sims-splice/:id', (req, res) => {
    const id = req.params.id -1;
    sims.splice(id,1);
    
    res.send('agora apagou memo, sem o null')
})

app.listen(port, function() {
    console.info(`App rodano no http://localhost:${port}/`);
});