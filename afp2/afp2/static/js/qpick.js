let selectedRow;
fetch('/api/quiz_picker')
  .then(response => response.json())
  .then(data => {
    const quizListBody = document.getElementById('quiz-list-body');
    quizListBody.innerHTML = '';

    data.forEach(pick => {
      if (pick.deleted == 0) {
          if (pick.active == 1) {
            const row = document.createElement('tr');

            const idCell = document.createElement('td');
            idCell.textContent = pick.id;
            row.appendChild(idCell);

            const nameCell = document.createElement('td');
            nameCell.textContent = pick.name;
            row.appendChild(nameCell);

            const Created_by_idCell = document.createElement('td');
            Created_by_idCell.textContent = pick.Created_By_id;
            row.appendChild(Created_by_idCell);


            row.addEventListener('click', () => {
              selectRow(row);
            });
            quizListBody.appendChild(row);
          }
      }
    });
  })
  .catch(error => {
    console.log(error);
    document.querySelector('#error').textContent = "Hiba történt a kilistázáskor!";
    document.querySelector("#success").textContent = "";
  });

// Sor kijelölésének a függvénye
function selectRow(row) {
  if (selectedRow) {
    selectedRow.classList.remove('selected');
  }
  row.classList.add('selected');
  selectedRow = row;
}

function qPick(event) {
  event.preventDefault();

  if (selectedRow) {
          window.location.href = '/api/qquiz';
  } else {
      document.querySelector('#error').textContent = "Nincs kvíz kijelölve!";
      document.querySelector("#success").textContent = "";
  }
}


// Törlés gomb
const qpickForm = document.querySelector('#qpick-form');
qpickForm.addEventListener('submit', qPick);