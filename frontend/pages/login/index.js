if (localStorage.getItem('token') !== null && localStorage.getItem('id_user') !== null) {
    window.location.href = '/home';
  }

  
  document.getElementById('login').addEventListener('click', async function(event) {
        event.preventDefault();
        const email = document.getElementById('email')?.value;
        let password = document.getElementById('password')?.value;

        if (!email || !password || email === '' || password === '') {
          Swal.fire({
            title: "Aviso!",
            text: "Preencha todos os campos!",
            icon: "warning",
          });
            return;
        }

        password = btoa(password);

        const loginData = {
            email: email,
            password: password
        };

        await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginData)
        })
        .then(response => response.json())
        .then(data => {
          if (!data.status) {
            Swal.fire({
              title: "Aviso!",
              text: data.message,
              icon: "error",
            });
          } else {
            localStorage.setItem('token', data.token);
            localStorage.setItem('id_user', data.id);
            Swal.fire({
              title: "Sucesso!",
              text: data.message,
              icon: "success",
            });
            window.location.href = '/home';
          }
        })
        .catch(error => {
            console.log('Error:', error);
        });
    });