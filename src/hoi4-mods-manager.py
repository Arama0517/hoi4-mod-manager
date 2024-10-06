from sys import exit

from prompt_toolkit.shortcuts import radiolist_dialog

from main import install, start, uninstall, update
from utils import TITLE, clear


def main() -> int:
    options = [
        ('start', '启动客户端'),
        ('install', '安装模组'),
        ('uninstall', '卸载模组'),
        ('update', '更新模组'),
    ]

    while True:
        clear()
        result = radiolist_dialog(
            TITLE, text='请选择一个选项', values=options, ok_text='确定', cancel_text='退出'
        ).run()
        match result:
            case None:
                return 0
            case 'start':
                start.main()
                return 0
            case 'install':
                install.main()
            case 'uninstall':
                uninstall.main()
            case 'update':
                update.main()


if __name__ == '__main__':
    exit(main())
