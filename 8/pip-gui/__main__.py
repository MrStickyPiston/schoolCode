import customtkinter
import sys
import subprocess
from pip._internal.operations.freeze import freeze

installed = []
for line in freeze():
    installed.append(line.split('==')[0].lower())
print(installed)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # packages

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

        self.install_button = customtkinter.CTkButton(master=self, text="(un)install", height=30, command=self.install)
        self.install_button.grid(row=1, column=1, padx=20, pady=20, sticky="nesw")

    def install(self):
        self.logs.configure(state="normal")

        if self.package_name.get().lower() in installed:
            self.logs.insert('end', text=f"Starting the uninstallation of {self.package_name.get()}\n")
            #TODO: uninstallation
        else:
            self.logs.insert('end', text=f"Starting the installation of {self.package_name.get()}\n")
            try:
                output = subprocess.Popen([sys.executable, '-m', 'pip', 'install', self.package_name.get()],
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except Exception:
                output = subprocess.Popen

            for i in output.stdout.readlines():
                self.logs.insert('end', text=f"{i.decode()}")
        self.logs.insert("end", text="\n")
        self.logs.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
