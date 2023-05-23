import customtkinter
import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "pip", "--upgrade"])

from pip._internal.operations.freeze import freeze


class gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # packages
        self.installed = []
        self.get_installed()

        # customtkinter

        self.geometry("500x300")
        self.title("PIP package installer")
        self.minsize(300, 200)

        self.last_mode = "edit_installed"

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 2), weight=1)

        self.logs = customtkinter.CTkTextbox(master=self, state="disabled", wrap='none')
        self.logs.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

        self.mode = customtkinter.CTkOptionMenu(master=self, values=["Edit installed packages", "Add new packages"])
        self.mode.grid(row=1, column=0, columnspan=3, padx=20, pady=(10, 0), sticky="nesw")

        self.package_name = customtkinter.CTkOptionMenu(master=self, values=self.installed)
        self.package_name.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nesw")

        self.install_button = customtkinter.CTkButton(master=self, text="install", height=30, command=self.install)
        self.install_button.grid(row=2, column=1, padx=(10, 10), pady=10, sticky="nesw")

        self.update_button = customtkinter.CTkButton(master=self, text="update", height=30, command=self.update_package)
        self.update_button.grid(row=2, column=2, padx=(10, 20), pady=10, sticky="nesw")

        self.check_installed()

    def install(self):
        self.logs.configure(state="normal")
        self.update()

        if self.package_name.get().lower() in self.installed:

            self.logs.insert('end', text=f"Starting the uninstallation of {self.package_name.get()}\n")

            try:
                output = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', self.package_name.get(), '-y'],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            except Exception:
                output = subprocess.Popen

        else:
            self.logs.insert('end', text=f"Starting the installation of {self.package_name.get()}\n")
            self.update()

            try:
                output = subprocess.Popen([sys.executable, '-m', 'pip', 'install', self.package_name.get()],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            except Exception:
                output = subprocess.Popen

        while True:
            line = output.stdout.readline()
            if line.decode() == '' and output.poll() is not None:
                break
            self.logs.insert('end', text=f"{line.decode()}")
            self.update()

        self.logs.insert("end", text="\n")
        self.logs.configure(state="disabled")

        self.get_installed()

    def update_package(self):
        self.logs.configure(state="normal")
        self.update()

        self.logs.insert('end', text=f"Starting the update of {self.package_name.get()}\n")
        self.update()

        try:
            output = subprocess.Popen([sys.executable, '-m', 'pip', 'install', '--upgrade', self.package_name.get()],
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except Exception:
            output = subprocess.Popen

        while True:
            line = output.stdout.readline()
            if line.decode() == '' and output.poll() is not None:
                break
            self.logs.insert('end', text=f"{line.decode()}")
            self.update()

        self.logs.insert("end", text="\n")
        self.logs.configure(state="disabled")

        self.get_installed()

    def get_installed(self):
        self.installed = []
        for line in freeze():
            self.installed.append(line.split('==')[0].lower())

    def check_installed(self):
        if self.mode.get() == "Add new packages" and self.last_mode == "edit_installed":
            self.last_mode = "add_new"
            self.package_name = customtkinter.CTkEntry(master=self, placeholder_text="package")
            self.package_name.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nesw")

            self.install_button.configure(text="install")
            self.update_button.configure(state="disabled")
        elif self.mode.get() == "Edit installed packages" and self.last_mode == "add_new":
            self.last_mode = "edit_installed"
            self.package_name = customtkinter.CTkOptionMenu(master=self, values=self.installed)
            self.package_name.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nesw")

        if self.package_name.get() in self.installed:
            self.install_button.configure(text="uninstall")
            self.update_button.configure(state="normal")
        else:
            self.install_button.configure(text="install")
            self.update_button.configure(state="disabled")

        self.after(1000, self.check_installed)


if __name__ == "__main__":
    pip_gui = gui()
    pip_gui.mainloop()
