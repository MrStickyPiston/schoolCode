import customtkinter
import sys
import subprocess
from pip._internal.operations.freeze import freeze


class gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # packages
        self.installed = []
        self.get_installed()

        # customtkinter

        self.geometry("500x300")
        self.title("pip package installer")
        self.minsize(300, 200)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.logs = customtkinter.CTkTextbox(master=self, state="disabled")
        self.logs.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        self.package_name = customtkinter.CTkEntry(master=self, placeholder_text="package")
        self.package_name.grid(row=1, column=0, padx=20, pady=20, sticky="nesw")

        self.install_button = customtkinter.CTkButton(master=self, text="install", height=30, command=self.install)
        self.install_button.grid(row=1, column=1, padx=20, pady=20, sticky="nesw")

        self.check_installed()

    def install(self):
        self.logs.configure(state="normal")
        self.update()

        if self.package_name.get().lower() in self.installed:

            self.logs.insert('end', text=f"Starting the uninstallation of {self.package_name.get()}\n")

            try:
                output = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', self.package_name.get(), '-y'],
                                          stdout=subprocess.PIPE)
            except Exception:
                output = subprocess.Popen

            for i in output.stdout.readlines():
                self.logs.insert('end', text=f"{i.decode()}")
                self.update()

        else:
            self.logs.insert('end', text=f"Starting the installation of {self.package_name.get()}\n")
            self.update()

            try:
                output = subprocess.Popen([sys.executable, '-m', 'pip', 'install', self.package_name.get()],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            except Exception:
                output = subprocess.Popen

            for i in output.stdout.readlines():
                self.logs.insert('end', text=f"{i.decode()}")
                self.update()

        self.logs.insert("end", text="\n")
        self.logs.configure(state="disabled")

        self.get_installed()

    def get_installed(self):
        self.installed = []
        for line in freeze():
            self.installed.append(line.split('==')[0].lower())

    def check_installed(self):
        if self.package_name.get() in self.installed:
            self.install_button.configure(text="uninstall")
        else:
            self.install_button.configure(text="install")

        self.after(1000, self.check_installed)


if __name__ == "__main__":
    pip_gui = gui()
    pip_gui.mainloop()
