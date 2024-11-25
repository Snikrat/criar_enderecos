Verificar a Política de Execução Atual
No powershell
Get-ExecutionPolicy

Alterar Temporariamente a Política de Execução
Para permitir scripts durante esta sessão do PowerShell:
No powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Alternativa: Alterar a Política de Execução Permanentemente:
powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Criar ambiente virtual
python -m venv venv

Ativar o ambiente virtual:
powershell
.\venv\Scripts\activate

Para desativar:
deactivate