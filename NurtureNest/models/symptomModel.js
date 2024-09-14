const mongoose = require('mongoose');

const SymptomSchema = new mongoose.Schema({
    date: { type: Date, required: true },
    symptom: { type: String, required: true },
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
});

module.exports = mongoose.model('Symptom', SymptomSchema);
