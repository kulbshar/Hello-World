''' MicroNG'''

import os
import re
import csv
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createstat(file_path, network, prot, step, counter, currentDict, n=20):

    with open('{}'.format(file_path)) as file:
        for line in (file.readlines()[:250]):
            if line.startswith('PASS HEADER host='):
                hostname = line.split("=")[1]
            if line.startswith('PASS HEADER date='):
                runtime = line.split("=")[1]

    with open('{}'.format(file_path)) as file:
        print(file_path)
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

                currentDict["network"] = (network)
                currentDict["protocol"] = (prot)
                currentDict["step"] = (step)
                currentDict["hostname"] = (hostname.strip())
                currentDict["runtime"] = (runtime.strip())
                currentDict["seconds"] = (sec)

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
        print('Stats for {} {} :'.format(network, prot))
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
                print('File Error...')
    return df_accum


def data_visualize(dataset):
    if dataset.empty:
        print('DataFrame is empty!')
    else:
        dataset["minutes"] = dataset["seconds"]/60
        dataset["memory_used_mb"] = dataset["memory_used"].astype('int')/1000

        # Horizontal Bar
        df_pivot_barh = dataset.pivot_table(
            index='network', values=['protocol'], aggfunc=lambda x: len(x.unique()))
        yint = range(math.floor(min(df_pivot_barh['protocol'])), math.ceil(
            max(df_pivot_barh['protocol']))+1)
        df_pivot_barh.plot(kind='barh', xticks=yint)
        plt.title("Number of Protocols per Network")
        plt.xlabel("Network")
        plt.ylabel("Number of Protocol")
        plt.tight_layout()
        plt.show()

        df_pivot = dataset.pivot_table(
            index='network', columns='protocol', values='minutes', aggfunc={'minutes': np.sum})
        df_pivot.plot(kind='bar')
        plt.title("process time by each Network & Protocol")
        plt.xlabel("Network'")
        plt.ylabel("Process Time in minutes'")
        plt.tight_layout()
        plt.show()

        df_pivot_1 = dataset.pivot_table(
            index='network', columns='protocol', values='memory_used_mb', aggfunc={'memory_used_mb': np.sum})
        df_pivot_1.plot(kind='bar')
        plt.title("Memory used by each Network & Protocol")
        plt.xlabel("Network'")
        plt.ylabel("Memory used in mb'")
        plt.tight_layout()
        plt.show()

        df_pivot_2 = dataset.pivot_table(
            index='network', values='memory_used_mb', aggfunc={'memory_used_mb': np.sum})
        df_pivot_2.plot.pie(y='memory_used_mb', figsize=(
            5, 5), autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        plt.title("Memory used by each Network")
        plt.show()

        df_pivot_min = dataset.pivot_table(
            index='network', values='minutes', aggfunc={'minutes': np.sum})
        df_pivot_min.plot.pie(y='minutes', figsize=(
            5, 5), autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        plt.title("Process Time by each Network")
        plt.show()

        df_pivot_3 = dataset.pivot_table(index='network', values=[
                                         'memory_used_mb', 'minutes'], aggfunc={'memory_used_mb': np.sum, 'minutes': np.sum})
        df_pivot_3.plot.pie(subplots=True, figsize=(10, 5), autopct='%1.0f%%')
        plt.title("Memory used(in MB) & Process Time(in Secs) by each Network")
        plt.show()


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

    df_metrics = pd.concat([my_data["hptn"], my_data["hvtn"], my_data["mtn"]])
    df_metrics.reset_index(inplace=True)
    # print(df_metrics)
    df_metrics.to_excel("/devel/ksharma/SAS_DEV/data_metrics/code/output.xlsx")

    data_visualize(df_metrics)


if __name__ == '__main__':
    main()

