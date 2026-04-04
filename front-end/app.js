document.addEventListener("DOMContentLoaded", function () {

    const btnMenu = document.getElementById("btn-menu");
    const menu = document.getElementById("menu-lateral");

    if (btnMenu) {
        btnMenu.addEventListener("click", function () {
            menu.classList.toggle("ativo");
        });
    }


    // -----------------------------
    // LOGIN SIMULADO
    // -----------------------------

    const formLogin = document.getElementById("form-login");

    if (formLogin) {

        formLogin.addEventListener("submit", function (e) {

            e.preventDefault();

            const email = document.getElementById("email").value;
            const senha = document.getElementById("senha").value;

            const erroEmail = document.getElementById("erro-email");
            const erroSenha = document.getElementById("erro-senha");

            erroEmail.textContent = "";
            erroSenha.textContent = "";

            let valido = true;

            if (email === "") {
                erroEmail.textContent = "Informe o email";
                valido = false;
            }
            if (senha === "") {
                erroSenha.textContent = "Informe a senha";
                valido = false;
            }
            if (!valido) return;

            // LOGIN SIMULADO
            if (email === "mestre@dojo.com" && senha === "1234") {
                window.location.href = "dashboard.html";
            } else {
                erroSenha.textContent = "Email ou senha inválidos";
            }

        });

    }



    // -----------------------------
    // LISTA DE ALUNOS
    // -----------------------------

    const lista = document.getElementById("lista-alunos");

    if (lista) {

        const nomes = [
            "João Silva",
            "Maria Souza",
            "Pedro Santos"
        ];

        const modalidades = [
            "Jiu Jitsu",
            "Muay Thai",
            "Boxe"
        ];
        
        const status = [
            "Ativo",
            "Ativo",
            "Inativo"
        ];

        const faixa = [
            "Branca",
            "Amarela",
            "Azul"
        ];

        let html = "";

        for (let i = 0; i < nomes.length; i++) {

            html += `
                <tr>

                <td data-label="Nome">${nomes[i]}</td>

                <td data-label="Modalidade">${modalidades[i]}</td>

                <td data-label="Status">${status[i]}</td>

                <td data-label="Status">${faixa[i]}</td>

                <td data-label="Ações">

                <button class="btn-editar">Editar</button>
                <button class="btn-excluir">Excluir</button>

                </td>

                </tr>
                `;

        }

        lista.innerHTML = html;

    }

    const campoPesquisa = document.getElementById("pesquisa-aluno");
    const filtroModalidade = document.getElementById("filtro-modalidade");

    function filtrarTabela() {

        const texto = campoPesquisa.value.toLowerCase();
        const modalidade = filtroModalidade.value.toLowerCase();

        const linhas = document.querySelectorAll("#lista-alunos tr");

        linhas.forEach(function (linha) {

            const nome = linha.children[0].innerText.toLowerCase();
            const mod = linha.children[1].innerText.toLowerCase();

            let mostrar = true;

            if (texto && !nome.includes(texto) && !mod.includes(texto)) {
                mostrar = false;
            }

            if (modalidade && mod !== modalidade) {
                mostrar = false;
            }

            linha.style.display = mostrar ? "" : "none";

        });

    }

    campoPesquisa.addEventListener("keyup", filtrarTabela);
    filtroModalidade.addEventListener("change", filtrarTabela);

    if (btnNovo) {
        btnNovo.addEventListener('click', () => {
            alert('Abrir formulário de cadastro');
        });
    }

});