# Documentação - Automatização de Preenchimento de Formulário Web com Python e Selenium

## Visão Geral
Este projeto demonstra como automatizar o preenchimento de um formulário web usando Python e Selenium. A automação é útil para tarefas repetitivas de entrada de dados em formulários online, economizando tempo e minimizando erros manuais.

### Funcionalidades Principais
- Abre um navegador web.
- Acessa um formulário web específico usando a URL fornecida.
- Preenche campos do formulário com dados fictícios.
- Submete o formulário (se houver um botão de envio).
- Fecha o navegador após a conclusão.

## Pré-requisitos
- Python 3.x instalado no seu sistema. Você pode baixar Python em [python.org](https://www.python.org/downloads/).
- Bibliotecas Python necessárias: `selenium`, `webdriver-manager`. Instale as bibliotecas executando o seguinte comando:
- ChromeDriver configurado corretamente. Você pode baixar o ChromeDriver em [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) e garantir que ele esteja no seu PATH de ambiente ou configurado no código.

## Instalação e Configuração
1. **Clonar o Repositório**:

2. **Instalar Dependências**:

3. **Configurar o ChromeDriver**:
Certifique-se de que o ChromeDriver está configurado corretamente. Você pode configurá-lo no código do script ou adicioná-lo ao seu PATH de ambiente.

## Uso
1. **Editar o Script**:
- Abra o arquivo `automacao_formulario.py` no seu editor de código preferido.
- Personalize o preenchimento dos campos do formulário editando os IDs conforme necessário. Exemplo:
  ```python
  campo_nome = driver.find_element_by_id("id-do-campo-de-nome")
  campo_nome.send_keys("João da Silva")
  ```

2. **Executar o Script**:
- Salve suas alterações e execute o script:
  ```
  python automacao_formulario.py
  ```

3. **Observações**:
- O script abrirá um navegador, preencherá o formulário com os dados fictícios configurados e submeterá o formulário (se houver um botão de envio).
- Após a conclusão, o navegador será fechado automaticamente.
