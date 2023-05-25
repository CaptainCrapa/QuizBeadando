let selectedRow;
let selectedRowUser;
const usernameElement = document.getElementById("username");
const text = usernameElement.textContent;
const split = text.split(" ");
const username = split[2];
let userIdLink = document.getElementById("userId");
    userIdLink.style.display = "none";
fetch('/api/quizzes')
  .then(response => response.json())
  .then(data => {
    const quizListBody = document.getElementById('quiz-list-body');
    quizListBody.innerHTML = '';

    data.forEach(quiz => {
      if (quiz.deleted == 0) {
          if (username == quiz.Created_By_id){
              if (quiz.active == 1){
                    const row = document.createElement('tr');

                    const idCell = document.createElement('td');
                    idCell.textContent = quiz.id;
                    row.appendChild(idCell);

                    const nameCell = document.createElement('td');
                    nameCell.textContent = quiz.name;
                    row.appendChild(nameCell);

                    const created_atCell = document.createElement('td');
                    created_atCell.textContent = quiz.created_at;
                    const created_atDate = quiz.created_at.split('T')[0];
                    created_atCell.textContent = created_atDate;
                    row.appendChild(created_atCell);

                    const Created_by_idCell = document.createElement('td');
                    Created_by_idCell.textContent = quiz.Created_By_id;
                    row.appendChild(Created_by_idCell);

                    row.addEventListener('click', () => {
                    selectRow(row);
                    });
                    quizListBody.appendChild(row);
              }
          }
      }
    });
  })
  .catch(error => {
    console.log(error);
    document.querySelector('#error').textContent = "Hiba történt a kilistázáskor!";
    document.querySelector("#success").textContent = "";
  });

fetch('/api/users_list')
  .then(response => response.json())
  .then(data => {
    const userListBody = document.getElementById('user-list-body');
    userListBody.innerHTML = '';

    data.forEach(user => {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = user.id;
        row.appendChild(idCell);

        const fullnameCell = document.createElement('td');
        fullnameCell.textContent = user.fullname;
        row.appendChild(fullnameCell);

        const usernameCell = document.createElement('td');
        usernameCell.textContent = user.username;
        row.appendChild(usernameCell);

        const emailCell = document.createElement('td');
        emailCell.textContent = user.email;
        row.appendChild(emailCell);

        row.addEventListener('click', () => {
        selectRowUser(row);
        });
        userListBody.appendChild(row);
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
function selectRowUser(row) {
  if (selectedRowUser) {
    selectedRowUser.classList.remove('selected');
  }
  row.classList.add('selected');
  selectedRowUser = row;
}

// Id ki kiemelése a selected sorból
function uInvite(event) {
  event.preventDefault();

  let userId = document.querySelector("#userId").value;

  if (selectedRow) {
      if (selectedRowUser) {
          const quizId = selectedRow.querySelector('td:first-child').textContent;
          const invitedId = selectedRowUser.querySelector('td:first-child').textContent;
          const data = {
              inviter_user_id: userId,
              invited_user_id: invitedId,
              quiz_id: quizId
          };
          console.log(data);
          axios.post('/api/add_user_to_quiz', data)
              .then(response => {
                  document.querySelector("#success").textContent = response.data;
                  document.querySelector("#error").textContent = "";
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
      document.querySelector('#error').textContent = "Nincs felhasználó kijelölve!";
      document.querySelector("#success").textContent = "";
      }
  } else {
      document.querySelector('#error').textContent = "Nincs kvíz kijelölve!";
      document.querySelector("#success").textContent = "";
  }
}


// meghívás gomb
const uinviteForm = document.querySelector('#uinvite-form');
uinviteForm.addEventListener('submit', uInvite);