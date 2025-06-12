// src/routes/index.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ message: 'Bem-vindo à API principal!' });
});

module.exports = router;