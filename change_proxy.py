# Trial
import time

import pywinauto

def update_proxy():
    with open("proxy.txt", 'r') as f:
        lines = f.readlines()
    with open("proxy.txt", 'w') as f:
        f.writelines(lines[1:])
    new_proxy = lines[0]
    if new_proxy is None:
        raise Exception("Proxy")
    change_proxy(new_proxy)

def change_proxy(proxy):
    app_proxier_trial = pywinauto.application.Application().start(
        "C:\\Program Files (x86)\\Proxifier\\Proxifier.exe"
    )
    try:
        time.sleep(2)
        w_handle = pywinauto.findwindows.find_windows(title=u'Proxifier Trial', class_name='#32770')[0]
        window = app_proxier_trial.window_(handle=w_handle)
        ctrl = window['Button']
        ctrl.ClickInput()
    except Exception:
        pass
    time.sleep(2)

    app_proxier = pywinauto.application.Application().start(
        "C:\\Program Files (x86)\\Proxifier\\Proxifier.exe"
    )

    time.sleep(2)
    pywinauto.mouse.click(coords=(801, 150))
    time.sleep(2)

    w_handle = pywinauto.findwindows.find_windows(title=u'Proxy Servers', class_name='#32770')[0]
    window_servers = app_proxier.window_(handle=w_handle)
    ctrl_server = window_servers['Button2']
    ctrl_server.Click()
    # time.sleep(2)
    # ctrl = window['Edit']
    # ctrl.Click()
    w_handle = pywinauto.findwindows.find_windows(title=u'Proxy Server', class_name='#32770')[0]
    window_server = app_proxier.window_(handle=w_handle)
    ctrl_server = window_server['Edit']
    ctrl_server.Click()
    time.sleep(0.2)
    ctrl_server.set_text(proxy)
    ctrl_server = window_server['OK']
    ctrl_server.Click()
    time.sleep(0.2)

    ctrl_servers = window_servers['OK']
    ctrl_servers.Click()
    app_proxier.kill()