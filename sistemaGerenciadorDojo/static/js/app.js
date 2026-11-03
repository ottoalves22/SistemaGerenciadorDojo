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

    // -----------------------------
    // MÁSCARAS DE CAMPOS (Aluno)
    // -----------------------------

    function aplicarMascaraTelefone(campo) {
        campo.setAttribute("placeholder", "(00) 00000-0000");
        campo.setAttribute("maxlength", "15");

        campo.addEventListener("input", function () {
            let v = campo.value.replace(/\D/g, "").slice(0, 11);

            if (v.length === 11) {
                v = v.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
            } else if (v.length === 10) {
                v = v.replace(/(\d{2})(\d{4})(\d{4})/, "($1) $2-$3");
            } else if (v.length > 6) {
                v = v.replace(/(\d{2})(\d{4,5})(\d{0,4})/, "($1) $2-$3");
            } else if (v.length > 2) {
                v = v.replace(/(\d{2})(\d{0,5})/, "($1) $2");
            } else if (v.length > 0) {
                v = v.replace(/(\d{0,2})/, "($1");
            }

            campo.value = v;
        });
    }



    // Documento: máscara varia conforme o tipo selecionado
    function configurarMascaraDocumento(campoDoc, selectTipo) {
        function aplicar() {
            const tipo = selectTipo.value;
            campoDoc.removeEventListener("input", campoDoc._maskHandler);

            if (tipo === "cpf") {
                campoDoc.setAttribute("placeholder", "000.000.000-00");
                campoDoc.setAttribute("maxlength", "14");
                campoDoc._maskHandler = function () {
                    let v = campoDoc.value.replace(/\D/g, "").slice(0, 11);
                    v = v.replace(/(\d{3})(\d)/, "$1.$2")
                        .replace(/(\d{3})(\d)/, "$1.$2")
                        .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
                    campoDoc.value = v;
                };
            } else if (tipo === "rg") {
                campoDoc.setAttribute("placeholder", "00.000.000-0");
                campoDoc.setAttribute("maxlength", "12");
                campoDoc._maskHandler = function () {
                    let v = campoDoc.value.replace(/\D/g, "").slice(0, 9);
                    v = v.replace(/(\d{2})(\d)/, "$1.$2")
                        .replace(/(\d{3})(\d)/, "$1.$2")
                        .replace(/(\d{3})(\d{1})$/, "$1-$2");
                    campoDoc.value = v;
                };
            } else {
                campoDoc.setAttribute("placeholder", "Número do documento");
                campoDoc.removeAttribute("maxlength");
                campoDoc._maskHandler = function () {
                    campoDoc.value = campoDoc.value.toUpperCase();
                };
            }

            campoDoc.addEventListener("input", campoDoc._maskHandler);
        }

        selectTipo.addEventListener("change", aplicar);
        aplicar();
    }

    // Data de Nascimento: dd-mm-aaaa
    function aplicarMascaraDataNascimento(campo) {
        campo.setAttribute("placeholder", "dd-mm-aaaa");
        campo.setAttribute("maxlength", "10");

        // Se já vier preenchido (edição), converte aaaa-mm-dd -> dd-mm-aaaa para exibir
        if (campo.value) {
            const partes = campo.value.split("-");
            if (partes.length === 3 && partes[0].length === 4) {
                const [ano, mes, dia] = partes;
                campo.value = `${dia}-${mes}-${ano}`;
            }
        }

        campo.addEventListener("input", function () {
            let v = campo.value.replace(/\D/g, "").slice(0, 8);
            if (v.length > 4) {
                v = v.replace(/(\d{2})(\d{2})(\d{0,4})/, "$1-$2-$3");
            } else if (v.length > 2) {
                v = v.replace(/(\d{2})(\d{0,2})/, "$1-$2");
            }
            campo.value = v;
        });

        // Converte dd-mm-aaaa -> aaaa-mm-dd antes de enviar o form
        const form = campo.closest("form");
        if (form) {
            form.addEventListener("submit", function () {
                const partes = campo.value.split("-");
                if (partes.length === 3) {
                    const [dia, mes, ano] = partes;
                    campo.value = `${ano}-${mes}-${dia}`;
                }
            });
        }
    }

    const campoTelefone = document.getElementById("id_telefone");
    const campoEmergencia = document.getElementById("id_contato_emergencia");
    const campoDocumento = document.getElementById("id_documento");
    const selectTipoDocumento = document.getElementById("tipo_documento_select");
    const campoDataNascimento = document.getElementById("id_data_nascimento");

    if (campoDataNascimento) aplicarMascaraDataNascimento(campoDataNascimento);
    if (campoTelefone) aplicarMascaraTelefone(campoTelefone);
    if (campoEmergencia) aplicarMascaraTelefone(campoEmergencia);
    if (campoDocumento && selectTipoDocumento) {
        configurarMascaraDocumento(campoDocumento, selectTipoDocumento);
    }

});