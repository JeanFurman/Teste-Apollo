# Questão 1

Faça uma API que liste 50 pacotes do python a sua escolha, pacotes 
estes que serão recuperados por uma API externa e armazenados em um CSV

## Endpoints

```bash
/pacotes/
```
Retorna todos os pacotes armazenados ordenados pelo nome.

```bash
/pacotes/?ordem=versao
```

Retorna todos os pacotes armazenados ordenados pela versão.

```bash
/pacotes/?ordem=data
```

Retorna todos os pacotes armazenados ordenados pela data.

```bash
/pacotes/nome/{nome}
```

Retorna o pacote com o nome inserido nos colchetes.

```bash
/pacotes/versao/{versao}
```

Retorna os pacotes com a versao inserida nos colchetes.

# Questão 2

Apenas execute o arquivo 'calculo_porcentagem' normalmente.
