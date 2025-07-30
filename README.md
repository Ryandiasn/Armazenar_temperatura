# 🌤️ Coletor de Dados Meteorológicos - São Paulo

Um programa simples em Python que coleta dados de temperatura e umidade de São Paulo usando web scraping no Google e salva os dados em uma planilha Excel.

## 📋 Funcionalidades

- 🌡️ Coleta temperatura atual
- 💧 Coleta umidade do ar
- 📊 Salva dados automaticamente no Excel
- 🖥️ Interface gráfica simples
- ⏰ Registra data e hora da coleta

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Selenium** - Automação web
- **OpenPyXL** - Manipulação de planilhas Excel
- **Tkinter** - Interface gráfica
- **ChromeDriver** - Controle do navegador

## 📦 Instalação

### 1. Instalar Python
Baixe e instale Python 3.x do site oficial: https://python.org

### 2. Instalar dependências
```bash
pip install selenium openpyxl
```

### 3. Baixar ChromeDriver
1. Acesse: https://chromedriver.chromium.org/
2. Baixe a versão compatível com seu Chrome
3. Extraia o arquivo `chromedriver.exe`
4. Coloque na mesma pasta do script Python

### 4. Verificar versão do Chrome
- Abra o Chrome
- Digite: `chrome://version/`
- Anote a versão para baixar o ChromeDriver correto

## 🚀 Como Usar

### Execução Básica
1. Execute o arquivo Python:
```bash
python coletor_tempo.py
```

2. Uma janela será aberta com o botão "Buscar previsão"

3. Clique no botão para coletar os dados

4. Os dados serão salvos no arquivo `ProjetoTempo.xlsx`

### Primeira Execução
- Na primeira vez, o programa criará automaticamente:
  - Arquivo `ProjetoTempo.xlsx`
  - Cabeçalhos: Temperatura, Umidade, Hora, Data

### Execuções Seguintes
- Os novos dados serão adicionados às linhas existentes
- Histórico completo será mantido na planilha

## 📁 Estrutura dos Arquivos

```
projeto/
├── coletor_tempo.py     # Código principal
├── chromedriver.exe     # Driver do Chrome (Windows)
└── ProjetoTempo.xlsx    # Planilha gerada automaticamente
```

## 📊 Formato da Planilha

| Temperatura (°C) | Umidade (%) | Hora     | Data       |
|------------------|-------------|----------|------------|
| 23               | 65%         | 14:30:25 | 30-07-2025 |
| 25               | 60%         | 15:45:10 | 30-07-2025 |

## ⚠️ Possíveis Problemas

### ChromeDriver não encontrado
```
WebDriverException: 'chromedriver' executable needs to be in PATH
```
**Solução**: Baixar ChromeDriver e colocar na pasta do projeto

### Versão incompatível
```
SessionNotCreatedException: session not created
```
**Solução**: Verificar se ChromeDriver é compatível com sua versão do Chrome

### Elementos não encontrados
```
NoSuchElementException: Unable to locate element
```
**Solução**: Google pode ter mudado a estrutura. Verificar se está funcionando manualmente

### Problemas de conexão
```
TimeoutException
```
**Solução**: Verificar conexão com internet

## 🔧 Personalização

### Alterar cidade
No arquivo `coletor_tempo.py`, linha 15:
```python
navegador.find_element(By.NAME, 'q').send_keys('Temperatura SUA_CIDADE_AQUI', Keys.ENTER)
```

### Alterar nome da planilha
No arquivo `coletor_tempo.py`, linha 26:
```python
arquivo = 'SEU_NOME_AQUI.xlsx'
```

### Alterar formato da data
No arquivo `coletor_tempo.py`, linhas 37-38:
```python
data_atual = datetime.now().strftime('%d/%m/%Y')  # Formato brasileiro
hora_atual = datetime.now().strftime('%H:%M')     # Sem segundos
```

## 🐛 Solução de Problemas

### 1. Chrome abre mas não faz nada
- Verificar se ChromeDriver está na pasta correta
- Tentar executar como administrador

### 2. Erro "automation controlled"
- O código já inclui configurações para evitar detecção
- Se persistir, pode ser bloqueio temporário do Google

### 3. Planilha não abre automaticamente
- Verificar se Excel está instalado
- Abrir manualmente o arquivo `ProjetoTempo.xlsx`

### 4. Dados não aparecem
- Verificar conexão com internet
- Testar busca manual no Google: "Temperatura taboão da serra"

## 📝 Exemplo de Uso

```python
# Executar o programa
python coletor_tempo.py

# Saída no terminal:
# A temperatura atual de Taboão da Serra é 23°C e a umidade é 65%
# Dados armazenados na planilha com sucesso.
```

## 📋 Requisitos do Sistema

- **Sistema Operacional**: Windows, macOS ou Linux
- **Python**: 3.6 ou superior
- **Navegador**: Google Chrome instalado
- **Internet**: Conexão ativa necessária
- **Espaço**: ~50MB para dependências

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

## 🤝 Contribuição

Para melhorias:
1. Faça um fork do projeto
2. Crie suas modificações
3. Teste localmente
4. Envie suas sugestões

---

**Desenvolvido para coleta automatizada de dados meteorológicos** 🌡️📊
