let selectedRow;
let userIdLink = document.getElementById("userId");
    userIdLink.style.display = "none";
fetch('/api/quizzes')
  .then(response => response.json())
  .then(data => {
    const quizListBody = document.getElementById('quiz-list-body');
    quizListBody.innerHTML = '';

    data.forEach(quiz => {
      if (quiz.deleted == 0) {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = quiz.id;
        row.appendChild(idCell);

        const nameCell = document.createElement('td');
        nameCell.textContent = quiz.name;
        row.appendChild(nameCell);

        const activeCell = document.createElement('td');
        if (quiz.active == true) {
                  activeCell.textContent = "Aktív";
        } else {
                  activeCell.textContent = "Inaktív";
        }
        row.appendChild(activeCell);

        const created_atCell = document.createElement('td');
        created_atCell.textContent = quiz.created_at;
        const created_atDate = quiz.created_at.split('T')[0];
        created_atCell.textContent = created_atDate;
        row.appendChild(created_atCell);

        const Created_by_idCell = document.createElement('td');
        Created_by_idCell.textContent = quiz.Created_By_id;
        row.appendChild(Created_by_idCell);

        const updated_atCell = document.createElement('td');
        updated_atCell.textContent = quiz.updated_at;
        const updated_atDate = quiz.updated_at.split('T')[0];
        updated_atCell.textContent = updated_atDate;
        row.appendChild(updated_atCell);

        const Updated_By_idCell = document.createElement('td');
        Updated_By_idCell.textContent = quiz.Updated_By_id;
        row.appendChild(Updated_By_idCell);


        row.addEventListener('click', () => {
          selectRow(row);
        });
        quizListBody.appendChild(row);
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

// Id ki kiemelése a selected sorból
function qDelete(event) {
  event.preventDefault();

  let userId = document.querySelector("#userId").value;

  if (selectedRow) {
  const quizId = selectedRow.querySelector('td:first-child').textContent;
  const data = {
    user_id: userId,
    quiz_id: quizId
  };
  console.log(data);
  axios.delete('/api/delete', { data })
    .then(response => {
      document.querySelector("#success").textContent = response.data;
      document.querySelector("#error").textContent = "";
      setTimeout(function () {
        location.reload();
      }, 1500);
    })
    .catch(error => {
      if (error.response) {
        var errorMessage = error.response.data;
        document.querySelector('#error').textContent = errorMessage;
        document.querySelector("#success").textContent = "";
      } else {
        console.log(error);
        document.querySelector('#error').textContent = "Hiba. További információ a konzolban!";
        document.querySelector("#success").textContent = "";
      }
    });
  } else {
    document.querySelector('#error').textContent = "Nincs kvíz kijelölve!";
    document.querySelector("#success").textContent = "";
  }
}


// Törlés gomb
const qdeleteForm = document.querySelector('#qdelete-form');
qdeleteForm.addEventListener('submit', qDelete);