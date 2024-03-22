import subprocess
import os

ALG = ['cubic','reno']
BER = ['1000000','100000']
E2E_DELAY = ['10000','100000'] # 10ms e 100ms
REPETICAO = 8
TEMPO_EXECUCAO = '10'
BANDA_UDP = ['10M','500M']
ID_EXPERIMENTO = 'i1234'
DADOS_CSV = 'data/dados.csv'
CENARIO_IMUNES = 'projeto.imn'

ip_pc1 = '10.0.0.20'
ip_pc2 = '10.0.2.20'
ip_pc3 = '10.0.3.20'
ip_pc4 = '10.0.4.20'

def inicia_imunes():
    if os.path.exists('cliente.csv'):
        os.remove('cliente.csv')
    cmd = f"sudo imunes -b -e {ID_EXPERIMENTO} projeto.imn"
    subprocess.run(cmd, shell=True)
    
def imprime_cabecalho():
    subprocess.run(f'echo -n REPETICAO,PROTOCOLO,BER,DELAY,BANDA UDP,TIMESTAMP,IP PC1,PORTA PC1,IP PC2,PORTA PC2,ID,INTERVALO,TAXA DE TRANSFERENCIA,BANDA TCP >> {DADOS_CSV}', shell=True)

def prepara_cenario():
    init_server_udp = f'sudo himage pc3@{ID_EXPERIMENTO} iperf -s -u &'
    init_server_tcp = f'sudo himage pc1@{ID_EXPERIMENTO} iperf -s &'
    subprocess.run(init_server_udp, shell=True)
    subprocess.run(init_server_tcp, shell=True)
    imprime_cabecalho()
    
def encerra_imunes():
    print('Encerrando simulações já existentes...')
    subprocess.Popen(f'sudo cleanupAll', shell=True).wait()

def inicia_simulacao():
    print('Iniciando simulação...')
    for banda in BANDA_UDP:
        init_cliente_udp = f'sudo himage pc4@{ID_EXPERIMENTO} iperf -c {ip_pc3} -u -t {TEMPO_EXECUCAO} -b {banda} &'
        subprocess.run(init_cliente_udp, shell=True)
        
        for rep in range(REPETICAO):
            for proto in ALG:
                for ber in BER:
                    for e2e in E2E_DELAY:
                            echo = f'echo -n {rep},{proto},{ber},{e2e},{banda}, >> {DADOS_CSV}'
                            subprocess.run(echo, shell=True)
                            
                            vlink = f'sudo vlink -BER {ber} -dly {e2e} router1:router2@{ID_EXPERIMENTO}'
                            subprocess.run(vlink, shell=True)
                            
                            init_cliente_tcp = f'sudo himage pc2@{ID_EXPERIMENTO} iperf -c {ip_pc1} -t {TEMPO_EXECUCAO} -Z {proto} -y C >> {DADOS_CSV}'
                            subprocess.run(init_cliente_tcp, shell=True)
                            
encerra_imunes()
inicia_imunes()
prepara_cenario()
inicia_simulacao()
encerra_imunes()