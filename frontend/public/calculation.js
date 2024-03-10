function calculate(operation) {
    var a = document.getElementById('a').value;
    var b = document.getElementById('b').value;

    console.log(a,b)
    if (a.includes('e') || b.includes('e')) {
        document.getElementById('result').textContent = '';
        document.getElementById('error').textContent = 'Invalid input';
        return;
    }

    // Convert to integers, if empty use 0 value
    a = a === '' ? 0 : parseInt(a);
    b = b === '' ? 0 : parseInt(b);

    var url = 'https://calculationapi.df.r.appspot.com/' + operation;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ a: a, b: b }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('result').textContent = data.error;
            } else {
                document.getElementById('result').textContent = data.result;
            }
        })
        .catch(error => console.error('Error:', error));
}