const express = require('express');
const app = express();
const path = require('path');
const ejs = require('ejs');

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// EJS Setup
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Example route
app.get('/dashboard', (req, res) => {
    // Dummy data for the example
    const user = { name: 'John Doe' };
    const symptoms = [
        { date: '2024-09-13', description: 'Feeling tired and mild nausea' },
        // Add more symptoms
    ];
    const notifications = [
        { message: 'Reminder: Track your symptoms today!' },
        // Add more notifications
    ];
    const chartLabels = ['2024-09-01', '2024-09-02', '2024-09-03']; // Example dates
    const chartData = [10, 20, 15]; // Example data
    
    res.render('dashboard', { user, symptoms, notifications, chartLabels, chartData });
});

// Start server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
