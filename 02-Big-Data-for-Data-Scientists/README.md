# Alguns conceitos para Big Data

## Batch Processing vs Streaming

### Batch Processing
Batch Processing (ou Processamento em Lotes) é um método de processamento de alto volume de dados com o mínimo de interação humana possível.
Neste tipo de processamento, coletamos e armazenamos os dados, e então processamos os mesmos no que chamamos de "*batch window*".

Um exemplo de processamento em lote seria uma transação bancária que só apareceria no histórico da conta alguns dias depois (janela de 
processamento), i.e., o processamento dos dados ocorreu numa janela após os dados serem armazenados. 

Processamento em *batch* nos permite uma melhor governança sobre os recursos computacionais disponíveis e também nos permite priorizar 
tarefas, uma vez que o evento de coletar e armazenar grandes volumes de dados pode ser programado.

### Real-Time Data Streaming
Real-Time Streaming (ou Processamento em tempo real) é um modelo de coleta, armazenamento e processamento de dados que busca executar tais
tarefas à medida em que os dados são disponibilizados. 

Por exemplo, uma transação bancária na qual recebemos instantes após uma notificação sobre a mesma é um exemplo de processamento em "tempo 
real". 

Dados de *streaming* são dados continuamente processados à medida que são gerados, diferente do caso de processamento em batch.

### Batch Processing vs Streaming
**Batch processing** é usado para conjunto de dados não contínuos. São ótimos para gestão de atualizações em bancos de dados, processamento de 
transações etc.

Já processamento de **streaming** é ideal para situações nas quais é necessário que tenhamos acesso aos dados em "tempo real".

Podemos ter ainda casos em que os dois tipos de processamento são necessários. Independente disso, é necessário que tenhamos entendimento de
cada um para que possamos escolher qual usar.
