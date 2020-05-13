from colorama import init, Fore


def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)


# run from command line to see colors as Code Runner doesn't seem to like it very much (sad face)
display("Warning!!!")
display("ERROR!!!", True)
