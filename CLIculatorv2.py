# import typer
from colorama import Fore, Back, Style
import colorama
from rich.console import Console
from rich.traceback import install
import webbrowser
from rich.panel import Panel
import os
import time
import sys
import re
import codecs
install()

# Try to set the encoding for stdout to UTF-8
try:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())
except Exception:
    pass # Fallback if already wrapped or not applicable

console = Console()

# Defining variables to avoid errors
ans = 0
uc = 'x'
n1 = 0
n2 = 0
csb = [(70, 180, 240), (70, 180, 240)]

os.system("mode con: cols=132 lines=40")
os.system('title " CLIculatorv2 "')

colorama.init()

def rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def pgl(lines, colors, delay=0.06):
    if len(colors) < 2:
        raise ValueError("Need at least 2 colors")

    total_lines = len(lines)
    segments = len(colors) - 1

    for i, line in enumerate(lines):
        pos = i / max(total_lines - 1, 1)
        seg = min(int(pos * segments), segments - 1)

        start = colors[seg]
        end = colors[seg + 1]

        local_pos = (pos - seg / segments) * segments

        r = int(start[0] + (end[0] - start[0]) * local_pos)
        g = int(start[1] + (end[1] - start[1]) * local_pos)
        b = int(start[2] + (end[2] - start[2]) * local_pos)

        sys.stdout.write(rgb(r, g, b, line) + "\n")
        sys.stdout.flush()      # 👈 THIS is the magic
        time.sleep(delay)

title_lines = [
    "     ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────┐",
    "     │                                                                                                               │",
    "     │     ______     __         __     ______     __  __     __         ______     ______   ______     ______       │",
    "     │    /\  ___\   /\ \       /\ \   /\  ___\   /\ \/\ \   /\ \       /\  __ \   /\__  _\ /\  __ \   /\  == \      │",
    "     │    \ \ \____  \ \ \____  \ \ \  \ \ \____  \ \ \_\ \  \ \ \____  \ \  __ \  \/_/\ \/ \ \ \/\ \  \ \  __<      │",
    "     │     \ \_____\  \ \_____\  \ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\    │",
    "     │      \/_____/   \/_____/   \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/ v2 │",
    "     │                                                                                                               │",
    "     │    By [DeveloperKartik]                                                                                       │",
    "  ┌──┤                                                                                                               ├──┐",
    "  │  └───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │",
    "  │                                                                                                                     │",
    "  └─────────────────┬──────────────────────────────────────────────┬─────────────────────────────────────────────┬──────┘"
]

import re

ucresult = ""

def format_bodmas_expression():
    expr = input(Fore.LIGHTRED_EX + "                    ├─►").replace(" ", "")
    
    if '(' in expr or ')' in expr:
        return evaluate_expression(expr)

    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expr)
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    def to_bracketed(tokens):
        def higher_precedence(op1, op2):
            return precedence[op1] >= precedence[op2]

        output = []
        ops = []

        def pop_and_build():
            if len(output) < 2:
                print("")
                print("                    String Error: not enough operands.")
                print("")
                return
            op = ops.pop()
            b = output.pop()
            a = output.pop()
            output.append(f"({a} {op} {b})")

        for token in tokens:
            if token in precedence:
                while ops and higher_precedence(ops[-1], token):
                    pop_and_build()
                ops.append(token)
            else:
                output.append(token)

        while ops:
            pop_and_build()

        if output:
            return output[0]
        else:
            return None

    ucresult = to_bracketed(tokens)

    if ucresult is None:
        print("Error: Failed to create a bracketed expression.")
        return None
    return evaluate_expression(ucresult)

def evaluate_expression(expr):
    if not isinstance(expr, str):
        # print("Error: expression must be a string.")
        return None
    try:
        ucresult = eval(expr)
        print("                    │")
        print("                    └─Result is►", ucresult)
        print("")
        return ucresult
    except Exception as e:
        print("                    └─Error during evaluation► \n", e)
        return None

colors = [(0, 120, 212), (50, 150, 230), (70, 180, 240)]

def f5():
    print(end="\033c", flush=True)
    print(" ")
    # gradient_title(title_lines, [(107, 7, 247), (247, 7, 203), (255, 0, 102)])
    pgl(title_lines, colors, delay=0.05)
    print("     ")
    print("     ")
    print(Fore.LIGHTRED_EX +"     ┌──────┬──────────────────────────────────────╮")
    print("     │  Id  |               Function               │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "C" + Fore.LIGHTRED_EX + "]  | Celsius to Farenhiet                 │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "F" + Fore.LIGHTRED_EX + "]  | Farenhiet to Celsius                 │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    tans = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─ID►")
    print("     │")
    ideg = int(input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─Number►"))
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
    pgl(title_lines, colors, delay=0.05)
    print("     ")
    print(Fore.LIGHTRED_EX +"     ┌─────────────────────────────────────────────╮")
    print("     │                 Odd or Even                 │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├─────────────────────────────────────────────╯")
    print("     │")
    ooe = int(input(Style.BRIGHT +"     ╰─Number to calculate► "))

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
    ans = 0
    uc = 0
    # gradient_title(title_lines, [(107, 7, 247), (247, 7, 203), (255, 0, 102)])
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    pgl(title_lines, colors, delay=0.05)

    linesoff1 = [
        "                    │                                     Basic Calculations                                       │",
        "                    ├──────────────────────────────────────────────┼───────────────────────────────────────────────┤",
        "                    ├─[+] Addition                                 ├─[<] Go Back",
        "                    │                                              │",
        "                    ├─[-] Subtraction                              └─[x] Exit    ❌",
        "                    │",
        "                    ├─[*] Multiplication",
        "                    │",
        "                    ├─[/] Division",
        "                    │"
    ]
    pgl(linesoff1, csb, delay=0.05)
    # uc = input(Fore.LIGHTRED_EX + Style.BRIGHT + "                    └─►")
    ucresult = format_bodmas_expression()

    evaluate_expression(ucresult)

    # if uc == "+" or uc == "-" or uc == "*" or uc == "/" or uc == "<":
    #     if uc == '+':
    #         print("     Selected: Addition")
    #     elif uc == '-':
    #         print("     Selected: Subtraction")
    #     elif uc == '*':
    #         print("     Selected: Multiplication")
    #     elif uc == '/':
    #         print("     Selected: Division")
    #     elif uc == '<':
    #         print(end="\033c", flush=True)
    #         maincode()
    # else:
    #     print(" ")
    #     print(Fore.RED + Style.BRIGHT + "     Invalid Choice")
    #     print(" ")
    #     input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
    #     # Calling Maincode
    #     print(end="\033c", flush=True)
    #     maincode()
    
    # print("     │")

    # n1 = input(Style.BRIGHT + "     ╰─First Number►")

    # if n1 == "":
    #     n1 = 0
    #     print("     No input detected, using 0 as default.")
    # n1 = int(n1)

    # print("     │")

    # n2 = input("     ╰─Second Number►")
    # if n2 == "":
    #     n2 = 0
    #     print("     No input detected, using 0 as default.")

    # n2 = int(n2)
    # print(" ")

    # if uc == '+':
    #     ans = n1 + n2
    # elif uc == '-':
    #     ans = n1 - n2
    # elif uc == '*':
    #     ans = n1 * n2
    # elif uc == '/':
    #     ans = n1 / n2

    # print(Style.BRIGHT + "     The requested answer is: " + Fore.CYAN + str(ans))
    print(" ")
    fiff1 = input(Style.BRIGHT + Fore.LIGHTGREEN_EX + "                    Press 'Enter ◄─┘' to enter again or press '<' to go back ► ")
    if fiff1 == '<':
        print(end="\033c", flush=True)
        maincode()
    elif fiff1 == '':
        print(end="\033c", flush=True)
        f1()

# Code For calculating area and perimeter
def f2():
    import math
    print(end="\033c", flush=True)
    pgl(title_lines, colors, delay=0.05)
    print(Fore.LIGHTRED_EX +"     ┌─────────────────────────────────────────────╮")
    print("     │               Area Calculator               │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │  Id  |               Function               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "1" + Fore.LIGHTRED_EX + "]  | Sqaure                               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "2" + Fore.LIGHTRED_EX + "]  | Rectangle                            │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "3" + Fore.LIGHTRED_EX + "]  | Circle                               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "4" + Fore.LIGHTRED_EX + "]  | Triangle                             │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    uf = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─ID► ")
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
    print("     ")
    print("     ")
    linesoff1 = [
        "     ┌─────────────────────────────────────────────╮",
        "     │            Percentage Calculator            │",
        "     ├──────────┬──────────┬───────────────────────┤",
        "     │ [x] Exit │ [?] Help │ [S] Support           │",
        "     ├──────────┴──────────┴───────────────────────╯",
        "     │",
    ]
    pgl(title_lines, colors, delay=0.05)
    pgl(linesoff1, csb, delay=0.05)

    ntcp = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─► ___ is what percent of ")
    if ntcp == "x":
        quit()

    print(end="\033c", flush=True)

    print(" ")
    pgl(title_lines, colors, delay=0.05)                                                                                                   
    print(Fore.LIGHTRED_EX +"     ")
    print("     ")
    print("     ┌─────────────────────────────────────────────╮")
    print("     │            Percentage Calculator            │")
    print("     ├──────────┬──────────┬───────────────────────┤")
    print("     │ [x] Exit │ [?] Help │ [S] Support           │")
    print("     ├──────────┴──────────┴───────────────────────╯")
    print("     │")

    ul = f"     ╰─► {ntcp} is what percent of "
    nfrom = input(ul)

    print(end="\033c", flush=True)

    print(" ")
    pgl(title_lines, colors, delay=0.05)                                                                                                     
    print(Fore.LIGHTRED_EX +"     ")
    print("     ")
    print("     ┌─────────────────────────────────────────────╮")
    print("     │            Percentage Calculator            │")
    print("     ├──────────┬──────────┬───────────────────────┤")
    print("     │ [x] Exit │ [?] Help │ [S] Support           │")
    print("     ├──────────┴──────────┴───────────────────────╯")
    print("     │")
    print(f"     ├─► {ntcp} is what percent of {nfrom}")
    print(" ")

    result = (int(ntcp) / int(nfrom)) * 100

    print(Style.BRIGHT + f"     {ntcp} is {result} percent of {nfrom}")
    input(Fore.LIGHTGREEN_EX + Style.BRIGHT + "     Press Enter ←╯ to go back")

    # Calling Maincode
    print(end="\033c", flush=True)
    maincode()

# Main Code
def maincode():

    print("")
    print("")
    print("")
    print("")

    linesoff1 = [
        "                    │                                             Home                                           │",
        "                    ├──────────────────────────────────────────────┼─────────────────────────────────────────────┘",
        "                    ├─[1] Basic Calculations                       ├─[x] Exit    ❌",
        "                    │                                              │",
        "                    ├─[2] Calculate area and perimeter of shapes   ├─[?] Help    ❓",
        "                    │                                              │",
        "                    ├─[3] Calculate Percentage of a number         └─[S] Support 🤍",
        "                    │",
        "                    ├─[4] Check if number is Odd or Even",
        "                    │",
        "                    ├─[5] Change Temperature Units",
        "                    │"
    ]
    pgl(title_lines, colors, delay=0.05)
    pgl(linesoff1, csb, delay=0.05)
    uc = 0
    uc = input("                    └─►")

    match uc:
        case '1':
            f1()
        case '2':
            f2()
        case '3':
            f3()
        case '4':
            f4()
        case '5':
            f5()
        case 'THE-BEST-WEBSITE-EVER':
            print(end="\033c", flush=True)
            # Calling Maincode
            # maincode()
            webbrowser.open('https://softwaretester27.github.io/learnscratch3/Index.html')
            maincode()
        case 'THE-WORST-WEBSITE-EVER':
            print(end="\033c", flush=True)
            # Calling Maincode
            # maincode()
            webbrowser.open('https://apple.com')
            maincode()
        case '?':
            print(end="\033c", flush=True)
            os.system("mode con: cols=134 lines=40")
            print(" ")
            print("     To use the program enter the id from the ")
            print("     table given below corresponding to the ")
            print("     function you want to perform.")
            # Calling Maincode
            maincode()
            print(" ")
        case 'x':
            quit()
        case 'S':
            print(end="\033c", flush=True)
            # Calling Maincode
            # maincode()
            webbrowser.open('https://github.com/SoftwareTester27')
            maincode()
        case _:
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

if __name__ == "__main__":
    try:
        maincode()
    except Exception as e:
        import traceback
        traceback.print_exc()
    finally:
        input("Press Enter to exit...") 
        time.sleep(1000)
