async function submitEssay(){
    const topic = document.getElementById("topic").value;
    const essay = document.getElementById("essay").value;

    try {
        const response = await fetch("/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                topic: topic,
                essay: essay
            })
        });

        const data = await response.json();
        console.log(data); 

    } catch (error) {
        console.error("Error:", error);
    }
}