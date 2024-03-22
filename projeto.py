import subprocess
from time import sleep

alg = ['cubic','reno']
BER = ['1000000','100000']
e2e_delay = ['10000','100000'] # 10ms e 100ms
repeticao = 8

id_exp = 'i234'
exec_time = '200'
server_exec_time = '50'

ip_pc1 = '10.0.0.20'
ip_pc2 = '10.0.2.20'
ip_pc3 = '10.0.3.20'
ip_pc4 = '10.0.4.20'

bandas = ['2Mbps','5Mbps']

#para cada uma das repeticoes faca
for rep in range(repeticao):
    for proto in alg:
        for ber in BER:
            for banda in bandas:
                for e2e in e2e_delay:
                    
                    # Modifica a BER e o delay do link entre os roteadores
                    vlink = ['sudo', 'vlink', '-BER', ber, '-dly', e2e, 'router1:router2@'+id_exp]

                    # Comando pra rodar o imunes
                    inicia_experimento = ['sudo', 'imunes', '-b', '-e', id_exp, 'projeto.imn']

                    # Tráfego background uDP
                    init_iperf_server_udp = ['sudo', 'himage', 'pc3@'+id_exp, 'iperf', '-s', '-u'] # inicia como server e usa UDP
                    init_iperf_client_udp = ['sudo', 'himage', 'pc4@'+id_exp, 'iperf', '-c', ip_pc3, '-u', '-t', server_exec_time, '-b', banda] # inicia como cliente e usa UDP

                    # Tráfego background TCP
                    init_iperf_server_tcp = ['sudo','himage', 'pc1@'+id_exp, 'iperf', '-s'] # inicia como server e usa TCP
                    init_iperf_client_tcp = f"sudo himage pc2@{id_exp} iperf -c {ip_pc1} -t {exec_time} -e -Z {proto} -y C >> data/cliente.csv" # inicia como cliente e usa TCP

                    print_data = f'sudo echo -n {rep},{proto},{ber},{e2e},{banda}, >> data/cliente.csv'
                    
                    # Inicia o imunes
                    subprocess.Popen(inicia_experimento).wait()

                    # Imprime no arquivo CSV
                    subprocess.Popen(print_data, shell=True,stdout=subprocess.PIPE,text=True)

                    # Modifica BER e delay
                    subprocess.Popen(vlink).wait()

                    # Inicia os servidores
                    subprocess.Popen(init_iperf_server_udp)
                    subprocess.Popen(init_iperf_server_tcp)

                    # Inicia os clientes
                    subprocess.Popen(init_iperf_client_udp)
                    subprocess.Popen(init_iperf_client_tcp, shell=True, stdout=subprocess.PIPE, text=True).wait()

                    # Limpa o experimento
                    subprocess.Popen('cleanupAll').wait()