async function submitEssay(event) {

    event.preventDefault();

    console.log("submit clicked");

    const topic = document.getElementById("topic").value;
    const essay = document.getElementById("essay").value;
    const apiKey = document.getElementById("api").value;
    const cefr = document.getElementById("target").value;

    console.log(topic)
    console.log(essay)
    console.log(cefr)

    const response = await fetch("/submit", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            topic: topic,
            essay: essay,
            api_key: apiKey,
            cefr: cefr
        })

    });

    

    const data = await response.json();

    console.log(data);
}