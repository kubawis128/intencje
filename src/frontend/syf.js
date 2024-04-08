function setup_popUps() {
    let popUps = document.getElementsByClassName("pop-up");
    Array.from(popUps).forEach(pop => {
        pop.addEventListener("click", (event) => {
            if (event.target !== pop) {
                return;
            }
            pop.classList.toggle("hidden");
        })
    })

    document.getElementById("pogrzeb-add").addEventListener("click", () => {
        document.getElementById("pogrzeb-pop").classList.toggle("hidden");
    })

    document.getElementById("parafia-add").addEventListener("click", () => {
        document.getElementById("parafie-pop").classList.toggle("hidden");
    })
}

function setup_add_parafia() {
    var parafia = document.getElementById("parafia");
    parafia.addEventListener("submit", event => {
        event.preventDefault();
        var nazwa = document.getElementById("nazwa").value;

        fetch('/api/parafie/insert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem("token")
            },
            body: JSON.stringify({
                id: 0,
                nazwa: nazwa
            })
        })
            .then(response => response.json())
            .then(data => location.reload(true))
            .catch(error => console.error(error));
    });
}

function setup_add_pogrzeb() {
    var form = document.getElementById("pogrzeb");
    form.addEventListener("submit", event => {
        event.preventDefault();
        var imie = form.querySelector("#imie").value;
        var nazwisko = form.querySelector("#nazwisko").value;
        var data = form.querySelector("#date").value;
        var parafia = parseInt(form.querySelector("#parafia-select").value);

        if (new Date() > new Date(data)) {
            alert("Data pogrzebu musi być w przyszłości")
            return
        }

        fetch('/api/pogrzeby/insert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem("token")
            },
            body: JSON.stringify({
                id: 0,
                imie: imie,
                nazwisko: nazwisko,
                date: data,
                parafia_id: parafia
            })
        })
            .then(response => response.json())
            .then(data => location.reload(true))
            .catch(error => console.error(error));
    });
}

function setup_edit_pogrzeb() {
    var form = document.getElementById("pogrzeb-edit");
    form.addEventListener("submit", event => {
        event.preventDefault();
        var id = form.querySelector("#id_pogrzebu").value;
        var imie = form.querySelector("#imie").value;
        var nazwisko = form.querySelector("#nazwisko").value;
        var data = form.querySelector("#date").value;
        var parafia = parseInt(form.querySelector("#parafia-select").value);
        if (new Date() > new Date(data)) {
            alert("Data pogrzebu musi być w przyszłości")
            return
        }

        fetch('/api/pogrzeby/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem("token")
            },
            body: JSON.stringify({
                id: id,
                imie: imie,
                nazwisko: nazwisko,
                date: data,
                parafia_id: parafia
            })
        })
            .then(response => response.json())
            .then(data => location.reload(true))
            .catch(error => console.error(error));
    });
}

function update_intencje(id) {
    fetch('/api/intencje/get_for?id=' + id, {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem("token")
        }})
        .then(response => response.json())
        .then(data => {
            let table = document.getElementById("intencje-pop").querySelector("#intencje")
            table.querySelector("#tbody").innerHTML = ""
            data.forEach(intencja => {
                let row = table.insertRow();

                row.insertCell(0).innerHTML = intencja.od_kogo;
                row.insertCell(1).innerHTML = intencja.kwota + " zł";

                let del = document.createElement("button");
                del.textContent = "Usuń";
                del.addEventListener("click", () => {
                    fetch('/api/intencje/remove?id=' + intencja.id, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': 'Bearer ' + localStorage.getItem("token")
                        },
                    })
                        .then(response => response.json())
                        .then(data => location.reload(true))
                        .catch(error => console.error(error));
                })

                let row1 = row.insertCell(2)
                row1.appendChild(del)
            });
        })
    
        document.getElementById("intencja-add").addEventListener("click", () => {
            document.getElementById("intencja-add-pop").classList.toggle("hidden");
            document.getElementById("intencja-add-pop").querySelector("#id_pogrzebu").value = id
        })
}

function setup_add_intencje() {
    var intencja = document.getElementById("intencja-add-form");
    intencja.addEventListener("submit", event => {
        event.preventDefault();

        var id = intencja.querySelector("#id_pogrzebu").value;
        var od_kogo = intencja.querySelector("#od_kogo").value;
        var kwota = parseFloat(intencja.querySelector("#kwota").value);

        fetch('/api/intencje/insert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem("token")
            },
            body: JSON.stringify({
                id: 0,
                od_kogo: od_kogo,
                kwota: kwota,
                id_pogrzebu: id
            })
        })
            .then(response => response.json())
            .then(data => location.reload(true))
            .catch(error => console.error(error));
    });
}