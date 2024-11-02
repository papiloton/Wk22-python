import shutil

shutil.copy('projects/chart.yaml', 'projects/chart_bk.yaml')

def chartModif(chart_version):
    with open("projects/chart.yaml", 'r') as f:
        content = f.readlines()
        
    with open("projects/test.yaml" , 'w')  as f1:
        for line in content:
            if 'version' in line:
                f1.write(f'version: {chart_version}\n')
            else:
                f1.write(line)
     
chartModif('3.0')  