# import typer
from colorama import Fore, Back, Style
from rich.console import Console
from rich.table import Table
import os
import webbrowser

# app = typer.Typer()

# Defining variables to avoid errors
ans = 0
uc = 'x'
n1 = 0
n2 = 0

os.system("mode con: cols=57 lines=28")
os.system("title The Ultimate Python Calculator by DeveloperKartik")
os.system("title The Ultimate Python Calculator by DeveloperKartik")
os.system("title The Ultimate Python Calculator by DeveloperKartik")
os.system("title The Ultimate Python Calculator by DeveloperKartik")

# Converting temp scales
# @app.command(short_help="Basic Calculations")
def f5():
    print(end="\033c", flush=True)
    print("")
    print("")
    print(Fore.WHITE + Style.BRIGHT + "                    DeveloperKartik's")
    print("     ╭─────────────────────────────────────────────╮")
    print("     │                                             │")
    print("     │   " + Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1" + Fore.WHITE + "   │")
    print("     │                                             │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │  Id  |               Function               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "C" + Fore.WHITE + "]  | Celsius to Farenhiet                 │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "F" + Fore.WHITE + "]  | Farenhiet to Celsius                 │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    tans = input(Fore.WHITE + Style.BRIGHT + "     ╰─ID>")
    print("     │")
    ideg = int(input(Fore.WHITE + Style.BRIGHT + "     ╰─Number>"))
    if tans == 'c' or tans == 'C':
        degree = ideg * 1.8 + 32
        print(" ")
        print(Style.BRIGHT + f'     The Requested result is: {degree}°F')
        print(" ")
        input(Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif tans == 'f' or tans == 'F':
        degree = ideg - 32 / 1.8
        print(Style.BRIGHT + f"     The Requested result is: {degree}°C")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press enter to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()

# checking if a number is odd or even

def f4():
    print(end="\033c", flush=True)
    print(" ")
    print(" ")
    print(Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1")
    print(Style.RESET_ALL)
    print(" ")
    print(" ")
    ooe = int(input(Style.BRIGHT + Fore.MAGENTA + "       Enter number to calculate: "))

    if ooe % 2 == 0:
        print(Style.BRIGHT + "     Number is even")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif ooe % 2 == 1:
        print(Style.BRIGHT + "     Number is odd")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()

# Defining all basic cals like DivMulAddSub.

def f1():
    # print('\n' * os.get_terminal_size().lines)
    print(end="\033c", flush=True)
    print("")
    print("")
    ans = 0
    uc = 0
    # print(" ")
    # print(Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1")
    # print(Style.RESET_ALL)
    # table = Table(title="     Function Table:", style="cyan")
    # # print(Style.BRIGHT + Fore.RED + "     Function Table:")
    # table.add_column("Id", style="red")
    # table.add_column("Function", style="green", justify="center")
    # table.add_column("", style="magenta", justify="center")
    # table.add_row("1", "Addition", "+")
    # table.add_row("2", "Subtraction", "-")
    # table.add_row("3", "Multiplication", "*")
    # table.add_row("4", "Division", "÷")

    # console = Console()
    # console.print(table)
    print(Fore.WHITE + Style.BRIGHT + "                    DeveloperKartik's")
    print("     ╭─────────────────────────────────────────────╮")
    print("     │                                             │")
    print("     │   " + Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1" + Fore.WHITE + "   │")
    print("     │                                             │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │             Basic Calculations              │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "<" + Fore.WHITE + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │  Id  |               Function               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "+" + Fore.WHITE + "]  | Addition                             │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "-" + Fore.WHITE + "]  | Subtraction                          │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "*" + Fore.WHITE + "]  | Multiplication                       │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "/" + Fore.WHITE + "]  | Division                             │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    uc = 0
    uc = input(Fore.WHITE + Style.BRIGHT + "     ╰─ID>")

    if uc == "+" or uc == "-" or uc == "*" or uc == "/" or uc == "<":
        if uc == '+':
            print("     Selected: Addition")
        elif uc == '-':
            print("     Selected: Subtraction")
        elif uc == '*':
            print("     Selected: Multiplication")
        elif uc == '/':
            print("     Selected: Division")
        elif uc == '<':
            print(end="\033c", flush=True)
            maincode()
    else:
        print(" ")
        print(Fore.RED + Style.BRIGHT + "     Invalid Choice")
        print(" ")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()

    print("     │")

    n1 = int(input(Style.BRIGHT + "     ╰─First Number>"))
    print("     │")
    n2 = int(input("     ╰─Second Number>"))
    print(" ")

    if uc == '+':
        ans = n1 + n2
    elif uc == '-':
        ans = n1 - n2
    elif uc == '*':
        ans = n1 * n2
    elif uc == '/':
        ans = n1 / n2

    print(Style.BRIGHT + "     The requested answer is: " + Fore.CYAN + str(ans))
    print(" ")
    input(Style.BRIGHT + Fore.MAGENTA + "       Press Enter ←╯ to rerun")
    # Calling Maincode
    print(end="\033c", flush=True)
    maincode()

# Code For calculating area and perimeter
def f2():
    import math
    print(end="\033c", flush=True)
    print("")
    print("")
    # print(" ")
    # print(" ")
    # print(Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1")
    # print(Style.RESET_ALL)
    # table = Table(title="     Function Table:", style="cyan")
    # # print(Style.BRIGHT + Fore.RED + "     Function Table:")
    # table.add_column("Id", style="red")
    # table.add_column("Function", style="green", justify="center")
    # table.add_row("1", "Sqaure")
    # table.add_row("2", "Rectangle")
    # table.add_row("3", "Circle")
    # table.add_row("4", "Triangle")
    print(Fore.WHITE + Style.BRIGHT + "                    DeveloperKartik's")
    print("     ╭─────────────────────────────────────────────╮")
    print("     │                                             │")
    print("     │   " + Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1" + Fore.WHITE + "   │")
    print("     │                                             │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │               Area Calculator               │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "<" + Fore.WHITE + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │  Id  |               Function               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "1" + Fore.WHITE + "]  | Sqaure                               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "2" + Fore.WHITE + "]  | Rectangle                            │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "3" + Fore.WHITE + "]  | Circle                               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "4" + Fore.WHITE + "]  | Triangle                             │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    uf = input(Fore.WHITE + Style.BRIGHT + "     ╰─ID> ")
    # console = Console()
    # console.print(table)
    # print(" ")
    # defining crv to prevent errors
    crv = int(0)

    if uf == '1':
        sside = int(input(Style.BRIGHT + "     Enter Side: "))
        # Calculates using the "side x 4 and side x side" method.
        peri = sside * 4
        area = sside * sside
        # Prints the result
        print(Style.BRIGHT + f"     The Requested Results are: Area = {area} units Perimeter = {peri} units")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '2':
        rl = int(input(Style.BRIGHT + "     Enter Rect Length:"))
        rb = int(input(Style.BRIGHT + "     Enter Rect Breadth:"))
        # Calculates using the "l + b * 2 and l x b" method.
        area = rl * rb
        peri = 2 * (rl + rb)
        # Prints the result
        print(Style.BRIGHT + f"      The Requested Results are: Area = {area} units Perimeter = {peri} units")
        input(Fore.MAGENTA + Style.BRIGHT + "        Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '3':
        crv = int(input("      Enter radius to calculate: "))
        rans = math.pi * crv * crv
        # Prints the result
        print(Style.BRIGHT + "     The Requested result is: " + Fore.CYAN + str(rans) + " units")
        input(Fore.MAGENTA + Style.BRIGHT + "     Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '4':
        tsa = int(input(Style.BRIGHT + "     First side: "))
        tsb = int(input(Style.BRIGHT + "     Second side: "))
        tsc = int(input(Style.BRIGHT + "     Third side: "))
        # Calculates using the formulas but implemented in python using math.sqrt()
        ts = tsa + tsb + tsc / 2
        aot = math.sqrt(ts*(ts-tsa)*(ts-tsb)*(ts-tsc))

        # Prints the result
        
        print(Style.BRIGHT + "      The Requested result is: " + Fore.CYAN + Back.BLACK +  str(int(aot)))
        print(Style.RESET_ALL)
        input(Fore.MAGENTA + Style.BRIGHT + "       Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '<':
        print(end="\033c", flush=True)
        maincode()

# Code for calcing percent
def f3():
    print(end="\033c", flush=True)
    print(" ")
    print(" ")
    print(Fore.GREEN + Style.BRIGHT + "     The Ultimate Python Calculator")
    print(Style.RESET_ALL)
    print(" ")
    ntcp = input(Style.BRIGHT + "     Number to calculate percent of: ")
    nfrom = input("     Number to calculate percent from: ")
    print(" ")

    result = int(ntcp) / int(nfrom) * 100
    print(Style.BRIGHT + "     The Requested result is: " + str(result))
    input(Fore.MAGENTA + Style.BRIGHT + "     Press Enter ←╯ to go back")
    # Calling Maincode
    print(end="\033c", flush=True)
    maincode()

# Main Code
def maincode():
    os.system("title The Ultimate Python Calculator by DeveloperKartik")
    from colorama import Fore, Back, Style
    import time
    import os
    print(" ")
    print(" ")
    print(Fore.WHITE + Style.BRIGHT + "                    DeveloperKartik's")
    print("     ╭─────────────────────────────────────────────╮")
    print("     │                                             │")
    print("     │   " + Fore.GREEN + Style.BRIGHT + "The  Ultimate  Python  Calculator  v1.1" + Fore.WHITE + "   │")
    print("     │                                             │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │                    Home                     │")
    print("     ├──────────┬──────────┬───────────────────────┤")
    print("     │ [" + Fore.BLUE + "x" + Fore.WHITE + "] Exit │ [" + Fore.BLUE + "?" + Fore.WHITE + "] Help │ [" + Fore.BLUE + "S" + Fore.WHITE + "] 😎 Support        │")
    print("     ├──────┬───┴──────────┴───────────────────────┤")
    print("     │ [" + Fore.BLUE + "/1" + Fore.WHITE + "] | Basic Calculations                   │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "/2" + Fore.WHITE + "] | Calculate area and perimeter of      │")
    print("     │      | various shapes                       │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "/3" + Fore.WHITE + "] | Calculate Percentage of a number     │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "/4" + Fore.WHITE + "] | Check if number is Odd or Even       │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.BLUE + "/5" + Fore.WHITE + "] | Change Temperature Units             │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    uc = 0
    uc = input(Fore.WHITE + Style.BRIGHT + "     ╰─ID>")
    # print(" ")
    # table = Table(title="     Function Table:", style="cyan")
    # table.add_column("Id", style="red", justify="center")
    # table.add_column("Function", style="green")
    # table.add_row("/1", "Basic Calculations")
    # table.add_row("/2", "Calculate area and perimeter of various shapeaas")
    # table.add_row("/3", "Calculate Percentage of a number")
    # table.add_row("/4", "Check if number is Odd or Even")
    # table.add_row("/5", "Change Temperature Units")
    # table.add_row("r", "Re-runs the program")
    # table.add_row("x", "Exit the program")
    # table.add_row("?", "For list of commands")
    # console = Console()
    # console.print(table)

    if uc == '/1':
        f1()
    elif uc == '/2':
        f2()
    elif uc == '/3':
        f3()
    elif uc == '/4':
        f4()
    elif uc == '/5':
        f5()
    elif uc == 'THEBESTWEBSITEEVER':
        print(end="\033c", flush=True)
        # Calling Maincode
        # maincode()
        webbrowser.open('https://softwaretester27.github.io/learnscratch3/Index.html')
        maincode()
    elif uc == '?':
        print(end="\033c", flush=True)
        os.system("mode con: cols=57 lines=33")
        print(" ")
        print("     To use the program enter the id from the ")
        print("     table given below corresponding to the ")
        print("     function you want to perform.")
        # Calling Maincode
        maincode()
        print(" ")
    elif uc == 'x':
        print(end="\033c", flush=True)
        quit()
    elif uc == 'S':
        print(end="\033c", flush=True)
        # Calling Maincode
        # maincode()
        webbrowser.open('https://github.com/SoftwareTester27')
        maincode()
    else:
        secondstoend = 5
        for number in range(5):
            print(end="\033c", flush=True)
            print(f"     Invalid fact '{uc}'. Please Re-run to retry or enter '?' in the first input asked.")
            print(f"     Restarting in {secondstoend} seconds...")
            time.sleep(1)
            secondstoend = secondstoend-1
        
        # Clearing the screen before calling maincode
        print(end="\033c", flush=True)
        # Calling Maincode
        maincode()
# Start the program
print(end="\033c", flush=True)
maincode()