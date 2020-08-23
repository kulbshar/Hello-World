''' MicroNG'''

import os
import re
import csv
import pandas as pd
import logging
import time

logging.basicConfig(filename='/devel/ksharma/SAS_DEV/data_metrics/code/sm_process_metrics.log', level=logging.DEBUG,
                    format='%(asctime)s:%(message)s:processid:%(process)d')

time.sleep(50)


def createstat(file_path, network, prot, step, counter, currentDict, n=20):

    with open('{}'.format(file_path)) as file:
        for line in (file.readlines()[:250]):
            if line.startswith('PASS HEADER host='):
                hostname = line.split("=")[1]
            if line.startswith('PASS HEADER date='):
                runtime = line.split("=")[1]

    with open('{}'.format(file_path)) as file:
        logging.debug(file_path)
        for line in (file.readlines()[-n:]):
            if "real time" in line:
                if line.split()[2].count(':') == 0:
                    unit = "Seconds"
                    sec = int(line.split()[2].split(".")[0])
                elif line.split()[2].count(':') == 1:
                    unit = "Minutes"
                    sec = int(line.split()[2].split(":")[
                              0])*60 + int(line.split()[2].split(":")[1].split(".")[0])
                elif line.split()[2].count(':') == 2:
                    unit = "Hours"
                    sec = int(line.split()[2].split(":")[0])*60*60 + int(line.split()[2].split(
                        ":")[1])*60 + int(line.split()[2].split(":")[2].split(".")[0])

                print("At Step", counter, step, ":")
                print("          Hostname: ", hostname.strip())
                print("          Runtime: ", runtime.strip())
                print("          Processing time: ", line.split()[2], unit)
                print("          Seconds taken: ", sec)
                print("          Network:", network)
                print("          Protocols:", prot)

                currentDict["network"] = [network]
                currentDict["protocol"] = [prot]
                currentDict["step"] = [step]
                currentDict["hostname"] = [hostname.strip()]
                currentDict["runtime"] = [runtime.strip()]
                currentDict["seconds"] = [sec]

            elif "memory" in line:
                print("          Memory Used", ":", line.split()[1])
                currentDict["memory_used"] = [
                    re.sub(r"\D", "", line.split()[1])]
        b = pd.DataFrame.from_dict(currentDict)
        return b


def loop_protocols(network, protocols, steps, currentDict):

    df_accum = pd.DataFrame(columns=[
                            'network', 'protocol', 'step', 'hostname', 'runtime', 'seconds', 'memory_used'])

    for prot in protocols:
        # path='/trials/LabDataOps/{}/protocols/{}/logs'.format(network, prot)
        path = '/devel/ksharma/LDP-1583/{}/protocols/{}/logs'.format(
            network, prot)
        print()
        logging.debug('Stats for {} {} :'.format(network, prot))
        counter = 0

        for step in steps:
            counter = counter + 1
            name = '{}{}_run_sm_protocol_{}.log'.format(network, prot, step)
            file_path = os.path.join(path, name)
            try:
                df = createstat(file_path, network, prot,
                                step, counter, currentDict)
                df_accum = df_accum.append(
                    df[['network', 'protocol', 'step', 'hostname', 'runtime', 'seconds', 'memory_used']], ignore_index=True)
            except:
                logging.debug('File Error...')
    return df_accum


def main():
    currentDict = {}
    my_data = {}

    network = 'hptn'
    # protocols=['083', '084',  '073', '074', '075', '076', '077', '078', '082']
    protocols = ['083', '084']
    # steps = ['gatherdata', 'findqcs', 'commitqcs', 'makereports']
    steps = ['gatherdata', 'findqcs', 'commitqcs', 'makereports']
    my_data[network] = loop_protocols(network, protocols, steps, currentDict)

    network = 'hvtn'
    # protocols=['702','703','704','705','706', '107','108','115','116',
    #        '117','118','133', '119','120','122','124','127','128',
    #        '123','130', '097','098','100','106','111','112','114',
    #         '505','802','910','137','405']
    protocols = ['702', '910']
    # steps = ['gatherdata', 'findqcs', 'commitqcs','findchrfqcs','commitchrfqcs', 'makereports']
    steps = ['gatherdata', 'findqcs', 'commitqcs', 'makereports']
    my_data[network] = loop_protocols(network, protocols, steps, currentDict)

    network = 'mtn'
    protocols = ['042']
    # steps = ['gatherdata', 'findqcs', 'commitqcs','findchrfqcs','commitchrfqcs', 'makereports']
    steps = ['gatherdata', 'findqcs', 'commitqcs', 'makereports']
    my_data[network] = loop_protocols(network, protocols, steps, currentDict)

    df_final = pd.concat([my_data["hptn"], my_data["hvtn"], my_data["mtn"]])
    logging.debug(df_final)
    df_final.to_excel("/devel/ksharma/SAS_DEV/data_metrics/code/output.xlsx")


if __name__ == '__main__':
    main()

