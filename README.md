# Mini Projeto de ADS - Avaliação de Desempenho do Protocolo TCP em condições de congestionamento: cubic x reno

## Rede simulada

![rede](./images/rede.png)

## Métricas

Taxa de transmissão média

## Parâmetros fixados

- Links ethernet 1 Gbps
- Links entre PC e roteador com BER 0
- Janela padrão do TCP
- Tráfego de background somente UDP

## Fatores e níveis

- Algoritmo de congestionamento
    - Cubic
    - Reno
- BER entre os roteadores 1 e 2
    - 1e-5
    - 1e-6
- Delay no link entre roteadores
    - 10ms
    - 100ms
- Tráfego de background
    - 10 Mbps
    - 500 Mbps

## Técnicas utilizadas

Simulação com IMUNES e iperf

## Resultados

| Cenário | Tráfego UDP | BER | Delay | Tx. Média Cubic | Tx. Média Reno |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 10 Mbps | 1/100000 | 10 ms | 4.29 Mbps | 4.6 Mbps |
| 2 | 10 Mbps | 1/100000 | 100 ms | 1.22 Mbps | 1.16 Mbps |
| 3 | 10 Mbps | 1/1000000 | 10 ms | 75.8 Mbps | 53.6 Mbps |
| 4 | 10 Mbps | 1/1000000 | 100 ms | 15.2 Mbps | 13.5 Mbps |
| 5 | 500 Mbps | 1/100000 | 10 ms | 5.08 Mbps | 4.31 Mbps |
| 6 | 500 Mbps | 1/100000 | 100 ms | 2.07 Mbps | 1.07 Mbps |
| 7 | 500 Mbps | 1/1000000 | 10 ms | 49.7 Mbps | 79.1 Mbps |
| 8 | 500 Mbps | 1/1000000 | 100 ms | 12.6 Mbps | 5.51 Mbps |