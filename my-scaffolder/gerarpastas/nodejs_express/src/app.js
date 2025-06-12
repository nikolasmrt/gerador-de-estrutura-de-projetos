// src/app.js
require('dotenv').config();
const express = require('express');
const app = express();
const port = process.env.PORT || {{ port }};

// Middleware para JSON
app.use(express.json());

// Importar rotas
const mainRoutes = require('./routes/index');

// Usar rotas
app.use('/api', mainRoutes);

// Rota de exemplo
app.get('/', (req, res) => {
  res.send('Bem-vindo à API {{ project_name }}!');
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
  console.log(`Projeto: {{ project_name }}`);
  console.log(`Autor: {{ author }}`);
});