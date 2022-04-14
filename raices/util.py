
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

START = 0
ROOT_NOT_FOUND_YET = 1
ROOT_FOUND = 2

err_with___pn__pn_1 = 0
err_with___pn__pn_1_over_pn = 1
err_with___f_of_pn = 2



def imprimir_tabla(table_code, p_n = 0, n_iteracion = 0, err = 9999) :

    if table_code == START :
        print(f"\n {bcolors.HEADER} [========================================//========================================] {bcolors.ENDC}\n")
        print(f" {bcolors.OKBLUE}N° iteracion{bcolors.ENDC}    |    {bcolors.OKBLUE}Valor actual de p_n{bcolors.ENDC}    |    {bcolors.OKBLUE}Valor actual de error estimado{bcolors.ENDC} ")

    elif table_code == ROOT_NOT_FOUND_YET:
        print(f"     {n_iteracion}                 {p_n}                 {err} ")
        
    elif table_code == ROOT_FOUND:
        print(f"     {bcolors.OKGREEN}{n_iteracion}{bcolors.ENDC}                 {bcolors.OKGREEN}{p_n}{bcolors.ENDC}                 {bcolors.OKGREEN}{err}{bcolors.ENDC} \n")
        print(f" {bcolors.HEADER} [========================================//========================================] {bcolors.ENDC}\n")


#Iteración funcional p_n = g(p_n-1) para todo n>=1  con:  g(x) = x - @(x)*f(x) ;   y   |p_n - p_n-1| <= tolerancia.
#Notar que se requiere la g, NO la f a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar que la g ES FUNCIÓN ADMISIBLE (SEGUN SEA QUE ESTA FUNCION SE USE CON PUNTO_FIJO O CON NR)
def iteracion_funcional(g, tolerancia, semilla, n_recursion = 1, prev_p_n = 0):

    if n_recursion == 1:
        imprimir_tabla(START)
        prev_p_n = semilla  #PREV_P_N NO PUEDE USARSE CON VALOR CERO!!!!
    
    p_n = g(prev_p_n)
    err = abs(p_n - prev_p_n)

    if err <= tolerancia :
        imprimir_tabla(ROOT_FOUND, p_n, n_recursion, err)
        p_n
    else:
        imprimir_tabla(ROOT_NOT_FOUND_YET, p_n, n_recursion, err)
        iteracion_funcional(g, tolerancia, semilla, n_recursion+1, p_n)