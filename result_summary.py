import os

TRAINING_PATH = "./traffic_light_images/training/"
OUT_PATH = "./traffic_light_images/out/"

RED = "red"
YELLOW = "yellow"
GREEN = "green"

def get_file_color(file_name):
    prefix = ''
    if (file_name.startswith(GREEN)):
        prefix = GREEN
    elif (file_name.startswith(RED)):
        prefix = RED
    elif (file_name.startswith(YELLOW)):
        prefix = YELLOW
    else:
        return None
    
    return file_name[0:len(prefix)]

def calc_total_training_set():
    all_files = os.listdir(TRAINING_PATH)
    total_green = 0
    total_yellow = 0
    total_red = 0
    
    for file_name in all_files:
        file_color = get_file_color(file_name)
        if (file_color == GREEN):
            total_green += 1
        elif (file_color == RED):
            total_red += 1
        elif (file_color == YELLOW):
            total_yellow += 1
        else:
            print(f"WARNING: ignoring file {file_name}")
    
    return total_green, total_red, total_yellow

def main():
    total_green, total_red, total_yellow = calc_total_training_set()
    total = total_green + total_red + total_yellow
    
    tgg = 0  # total_verde_verde
    trg = 0 # total_red_green
    tyg = 0 # total_yellow_green
    for file_name in os.listdir(OUT_PATH + "/GREEN"):
        file_color = get_file_color(file_name)
        if (file_color == GREEN):
            tgg += 1
        elif (file_color == RED):
            trg += 1
        elif (file_color == YELLOW):
            tyg += 1
        else:
            print(f"WARNING: ignoring file {file_name}")
    
    trr = 0 # total_red_red
    tgr = 0 # total_green_red
    tyr = 0 # total_yellow_red
    for file_name in os.listdir(OUT_PATH + "/RED"):
        file_color = get_file_color(file_name)
        if (file_color == RED):
            trr += 1
        elif (file_color == GREEN):
            tgr += 1
        elif (file_color == YELLOW):
            tyr += 1
        else:
            print(f"WARNING: ignoring file {file_name}")

    tyy = 0 # total_yellow_yellow
    tgy = 0 # total_green_yellow
    tri = 0 # total_red_i(y)ellow (try é palavra reservada)
    for file_name in os.listdir(OUT_PATH + "/YELLOW"):
        file_color = get_file_color(file_name)
        if (file_color == YELLOW):
            tyy += 1
        elif (file_color == RED):
            tri += 1
        elif (file_color == GREEN):
            tgy += 1
        else:
            print(f"WARNING: ignoring file {file_name}")

    total_acertos = tgg + trr + tyy
    total_erros = total - total_acertos
    print(f"Total de imagens analisadas: {total}")
    print(f"Total de acertos: {total_acertos} ({float((total_acertos/total) * 100):.2f}%)")
    print(f"Total de erros: {total_erros} ({float((total_erros/total) * 100):.2f}%)")

    print()

    print("Relação resposta certa / palpite:", end="")
    print(
f"""
| ------  | VERDE | VERMELHO | AMARELO |
|VERDE    |  {tgg:3d}  |    {tgr:3d}   |   {tgy:3d}   |
|VERMELHO |  {trg:3d}  |    {trr:3d}   |   {tri:3d}   |
|AMARELO  |  {tyg:3d}  |    {tyr:3d}   |   {tyy:3d}   |
""")
    # % total de acertos
    # % total de acertos green
    # % total de acertos red
    # % total de acertos yellow
    
    #        | green | red | yellow 
    # green  |  100  |     |
    # red    |  n%   |     |
    # yellow |  x%   |     |
    #


if __name__ == "__main__":
    main()
