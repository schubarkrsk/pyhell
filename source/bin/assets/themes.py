import os
import sys

ASCII_LOGO = "                            ,-.\n" \
             "       ___,---.__          /'|`\\          __,---,___\n" \
             "    ,-'    \\`    `-.____,-'  |  `-.____,-'    //    `-.\n" \
             "  ,'        |           ~'\\     /`~           |        `.\n" \
             " /      ___//              `. ,'          ,  , \\___      \\\n" \
             "|    ,-'   `-.__   _         |        ,    __,-'   `-.    |\n" \
             "|   /          /\\_  `   .    |    ,      _/\\          \\   |\n" \
             "\\  |           \\ \\`-.___ \\   |   / ___,-'/ /           |  /\n" \
             " \\  \\           | `._   `\\\\  |  //'   _,' |           /  /\n" \
             "  `-.\\         /'  _ `---'' , . ``---' _  `\\         /,-'\n" \
             "     ``       /     \\    ,='/ \\`=.    /     \\       ''\n" \
             "             |__   /|\\_,--.,-.--,--._/|\\   __|\n" \
             "             /  `./  \\\\`\\ |  |  | /,//' \\,'  \\\n" \
             "PyHell      /   /     ||--+--|--+-/-|     \\   \\\n" \
             "           |   |     /'\\_\\_\\ | /_/_/`\\     |   |\n" \
             "            \\   \\__, \\_     `~'     _/ .__/   /\n" \
             "             `-._,-'   `-._______,-'   `-._,-'\n"


def change_color(color="4F"):
    """

    :param color: HEX code XY, where X - bg color, Y - font color
                     0 = Черный 8 = Серый
                     1 = Синий 9 = Светло-синий
                     2 = Зеленый A = Светло-зеленый
                     3 = Голубой B = Светло-голубой
                     4 = Красный C = Светло-красный
                     5 = Лиловый D = Светло-лиловый
                     6 = Желтый E = Светло-желтый
                     7 = Белый F = Ярко-белый

    :return:
    """
    if sys.platform == "win32":
        str_col = f"color {color}"
        os.system(str_col)


def clear_console():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
