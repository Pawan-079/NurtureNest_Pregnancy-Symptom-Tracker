const express = require('express');
const Symptom = require('../models/symptomModel');
const auth = require('../middleware/auth');
const router = express.Router();

// Track symptoms (Protected Route)
router.post('/', auth, async (req, res) => {
    const { date, symptom } = req.body;
    try {
        const newSymptom = new Symptom({ date, symptom, userId: req.userId });
        await newSymptom.save();
        res.status(201).json({ message: "Symptom tracked successfully!" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;
