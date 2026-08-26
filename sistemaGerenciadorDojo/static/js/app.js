document.addEventListener("DOMContentLoaded", function () {

    // -----------------------------
    // MENU HAMBÚRGUER
    // -----------------------------

    const btnMenu = document.getElementById("btn-menu");
    const menu = document.getElementById("menu-lateral");

    if (btnMenu && menu) {
        btnMenu.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.classList.toggle("ativo");
        });

        // Fecha ao clicar fora
        document.addEventListener("click", function (e) {
            if (menu.classList.contains("ativo") &&
                !menu.contains(e.target) &&
                e.target !== btnMenu) {
                menu.classList.remove("ativo");
            }
        });
    }


    // -----------------------------
    // DROPDOWN DO USUÁRIO
    // -----------------------------

    const btnUserDropdown = document.getElementById("btn-user-dropdown");
    const userDropdownMenu = document.getElementById("user-dropdown-menu");

    if (btnUserDropdown && userDropdownMenu) {
        btnUserDropdown.addEventListener("click", function (e) {
            e.stopPropagation();
            userDropdownMenu.classList.toggle("aberto");
        });

        document.addEventListener("click", function () {
            userDropdownMenu.classList.remove("aberto");
        });
    }


    // -----------------------------
    // LOGIN
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

            if (email === "mestre@dojo.com" && senha === "1234") {
                window.location.href = "dashboard.html";
            } else {
                erroSenha.textContent = "Email ou senha inválidos";
            }

        });

    }


    // -----------------------------
    // FILTRO DA TABELA DE ALUNOS
    // -----------------------------

    const campoPesquisa = document.getElementById("pesquisa-aluno");
    const filtroModalidade = document.getElementById("filtro-modalidade");

    if (campoPesquisa && filtroModalidade) {

        function filtrarTabela() {

            const texto = campoPesquisa.value.toLowerCase();
            const modalidade = filtroModalidade.value.toLowerCase();
            const linhas = document.querySelectorAll("#lista-alunos tr");

            linhas.forEach(function (linha) {

                const nome = linha.children[0] ? linha.children[0].innerText.toLowerCase() : "";
                const mod = linha.children[1] ? linha.children[1].innerText.toLowerCase() : "";

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

    }

});