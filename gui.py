import toga
from toga.style.pack import Pack, ROW, CENTER, COLUMN
import notify2
import os
import tools

# n = notify2.Notification("Summary",
#                          "Some body text",
#                          "notification-message-im"   # Icon name
#                         )
# n.show()
#
#
#
# def button_handler(widget):
#     print("hello")
#
# def SureChangePassword():
#

path = os.path.dirname(os.path.abspath(__file__))
class CryptoCutGUI(toga.App):
    def startup(self):
        def ApplySet():
            pass
        def Random1(self):
            self.password_input.label=tools.RandomGenerator(1)
        def Random2():
            self.password_input.label=tools.RandomGenerator(2)
        def Random3():
            self.password_input.label=tools.RandomGenerator(3)
        DonateIcon = os.path.join(path, "Files", "Cash.png")
        GithubIcon = os.path.join(path, "Files", "Github.png")
        InfoIcon = os.path.join(path, "Files", "Info.png")
        self.icon=os.path.join(path, "Files", "Logo.ico")
        self.cmd0 = toga.Command(
            ApplySet,
            label='Donate',
            tooltip='Donate to Us',
            icon=DonateIcon,
        )
        self.cmd1 = toga.Command(
            ApplySet,
            label='About Us',
            tooltip='Software info and cast',
            icon=InfoIcon,
        )
        self.cmd2 = toga.Command(
            ApplySet,
            label='Github',
            tooltip='Open Github ',
            shortcut='k',
            icon=GithubIcon
        )
        #INIT OBJECTS
        self.main_window = toga.MainWindow(title=(self.name + " - Setting"),size=(400,390))
        self.password_input = toga.PasswordInput()
        self.label_password = toga.Label(" Enter passphrase:")
        self.button_random_low = toga.Button('Random (Fast)',on_press=Random1())
        self.button_random_med = toga.Button('Random (Good)')
        self.button_random_high = toga.Button('Random (Seure)')
        self.button_apply = toga.Button('Apply')
        self.box = toga.Box()
        self.switch_notification = toga.Switch("")
        self.switch_paste = toga.Switch("")
        self.switch_startup = toga.Switch("")
        self.switch_active = toga.Switch("")
        self.label_notification = toga.Label('Show notification when its successfully worked')
        self.label_paste = toga.Label("Paste on highlighted text (or just copy to clipboard)")
        self.label_startup = toga.Label("start automatically after restart")
        self.label_active = toga.Label("make program active and ready to sevice")
        self.box_switchs = toga.Box()
        self.box_switch_labels = toga.Box()
        self.box_switchs_and_labels_all = toga.Box()
        self.box_encrypt_type_all = toga.Box()
        self.box_encrypt_password = toga.Box()
        self.box_random_button = toga.Box()
        self.select_method = toga.Selection(items=['method1' , 'method2' , 'method3'])
        self.label_select_encrypt = toga.Label("Choose encryption method")
        self.motherbox = toga.Box()

        #UPDATE THEMES
        self.switch_active.style.update(padding=0.5)
        self.switch_startup.style.update(padding=0.5)
        self.switch_paste.style.update(padding=0.5)
        self.switch_notification.style.update(padding=0.5)
        self.label_active.style.update(padding=50)
        self.label_startup.style.update(padding=5)
        self.label_paste.style.update(padding=5)
        self.label_notification.style.update(padding=5)
        self.button_apply.style.update(flex = 1,padding_top=10)
        self.box_switchs.style.update(direction="column")
        self.box_switch_labels.style.update(direction="column")
        self.box_encrypt_type_all.style.update(direction="column")
        self.box_encrypt_password.style.update(direction="column")
        self.box_switchs_and_labels_all.style.update(direction="row")
        self.label_notification.style.update(padding=4,font_size=40,width=330)
        self.label_paste.style.update(padding=4,font_size=40,width=334)
        self.label_startup.style.update(padding=4,font_size=40,width=334)
        self.label_active.style.update(padding=4,font_size=40,width=334)
        self.box.style.update(direction="column",padding=3,padding_top=80)
        self.select_method.style.update(height=30,width=398)
        self.label_select_encrypt.style.update(padding=2)
        self.label_password.style.update(width=70,padding_top=4)
        self.password_input.style.update(width=395,padding=2)
        self.button_random_low.style.update(width=120,padding=6)
        self.button_random_med.style.update(width=120,padding=6)
        self.button_random_high.style.update(width=120,padding=6)
        self.button_apply.style.update(width=396)

        #BUILD IN BOX
        self.box_switchs.add(self.switch_active)
        self.box_switchs.add(self.switch_paste)
        self.box_switchs.add(self.switch_notification)
        self.box_switchs.add(self.switch_startup)
        self.box_switch_labels.add(self.label_active)
        self.box_switch_labels.add(self.label_paste)
        self.box_switch_labels.add(self.label_notification)
        self.box_switch_labels.add(self.label_startup)
        self.box_switchs_and_labels_all.add(self.box_switch_labels)
        self.box_switchs_and_labels_all.add(self.box_switchs)
        self.box_encrypt_type_all.add(self.label_select_encrypt)
        self.box_encrypt_type_all.add(self.select_method)
        self.box_encrypt_password.add(self.label_password)
        self.box_encrypt_password.add(self.password_input)
        self.box_random_button.add(self.button_random_low)
        self.box_random_button.add(self.button_random_med)
        self.box_random_button.add(self.button_random_high)

        self.box.add(self.box_switchs_and_labels_all)
        self.box.add(self.box_encrypt_type_all)
        self.box.add(self.box_encrypt_password)
        self.box.add(self.box_random_button)
        self.box.add(self.button_apply)

        self.motherbox.add(self.box)

        #LAST STEPS
        self.commands.add(self.cmd1, self.cmd2, self.cmd0)
        self.main_window.toolbar.add(self.cmd1, self.cmd2, self.cmd0)
        self.main_window.content = self.motherbox
        self.main_window.show()


def main():
    return CryptoCutGUI('CryptoCut', 'com.plurality.cryptocut', icon=os.path.join(path, "Files", "Logo.ico"))

if __name__ == '__main__':
    main().main_loop()
