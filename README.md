# ornellas_dojo
Oss!

# update 1/10/2026: 
 - Alteração do campo CPF virou campo Documento, para contemplar RG e outros documentos (temos alunos de vários países)
 - Adição de campo contrato, para armazenar arquivos, por enquanto no volume do container web mesmo.
 - #TODO: Criar script de pg_dump para backup de dados de alunos e considerar um banco de dados dedicado em produção
 - #TODO: TROCAR armazenamento de arquivos em Oracle Cloud Object Storage (e atualizar o código de upload)
 - #TODO: Criar recuperação de arquivo na tela do aluno (criar codigo de "download" do arquivo)


# update2 01/10/2026
 - Adição do esqueleto da funcionalidade de whatsapp (Eles precisam MUITO de um lembrete de pagamento acessível)
 - #TODO: Criar token da meta e verificar o uso de um VoIP pra não ter de comprar outro chip de telefone

# update3 08/10/2026
- Adição das máscaras de formatação de dados para formulários afim de facilitar o uso do formulário e também garantir consistência de tipo de dado no bd
- Adição do campo de seleção de tipo de documento já que aceitamos mais de um tipo. A máscara de formatação acompanha o tipo de documento selecionado 
- Teste de funcionalidade do campo de arquivos para que seja possível baixar seu conteúdo prévio. (conceito em revisão, nenhum teste subiu para main)
- #TODO: revisar e definir nova funcionalidade 