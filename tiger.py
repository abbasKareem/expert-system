

info = {
    "has hair": False,
    "has ears": False,
    "has hoves": False,
    "has strips lines": False,
    "eat meet": False,
    "has long legs": False,
    "has long neck": False,
    "can jump between trees": False,
    "walks on two feet": False
}


def confirm_user_input(x):
    if x in info:
        user_input = input(f"is your animal {x}?: ")
        user_input = user_input.lower()
        if user_input == "y":
            info[x] = True


def tiger():
    confirm_user_input("has hair")
    confirm_user_input("has ears")
    confirm_user_input("eat meet")

    if info['has hair'] == True and info['has ears'] == True and info['eat meet'] == True:
        print("your animal is Tiger! and it [ has hair, has ears, eat meet ] ")
        exit(0)


def zebra():
    confirm_user_input("has hoves")
    confirm_user_input("has strips lines")
    if info['has hair'] == True \
            and info['has ears'] == True \
            and info['has hoves'] == True \
            and info["has strips lines"] == True:
        print("your animal is Zebra! and it [ has hair, has ears, has hoves, has strips lines ]")
        exit(0)


def giraffe():
    confirm_user_input("has long legs")
    confirm_user_input("has long neck")
    if info['has hair'] == True \
            and info['has ears'] == True \
            and info['has hoves'] == True \
            and info['has long legs'] == True \
            and info['has long neck'] == True:
        print("your animal is griffe! and it [ has hair, has ears, has hoves, has long legs, has long neck ]")
        exit(0)


def monkey():
    confirm_user_input("walks on two feet")
    confirm_user_input("can jump between trees")
    if info['has hair'] == True \
            and info['has ears'] == True \
            and info['can jump between trees'] == True \
            and info['walks on two feet'] == True:
        print("your animal is monkey! and it [ has hair, has ears, can jumps between trees, walks on two feet]")
        exit(0)
