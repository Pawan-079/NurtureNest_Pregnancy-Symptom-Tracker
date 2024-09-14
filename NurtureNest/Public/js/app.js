document.getElementById("symptom-form").addEventListener("submit", function(e) {
    e.preventDefault();
    const date = document.getElementById("date").value;
    const symptom = document.getElementById("symptom").value;

    const symptomData = {
        date: date,
        symptom: symptom
    };

    fetch('/track-symptoms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(symptomData)
    }).then(response => response.json())
      .then(data => {
          alert("Symptoms tracked successfully!");
          document.getElementById("symptom-form").reset();
      })
      .catch(error => console.error('Error:', error));
});

// Fetch baby development updates from an external API (or backend)
fetch('/baby-updates')
    .then(response => response.json())
    .then(data => {
        const babyDiv = document.getElementById("baby-updates");
        babyDiv.innerHTML = `<p>Baby Development: ${data.message}</p>`;
    });
