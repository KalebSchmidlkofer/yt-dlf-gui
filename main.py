import tkinter
import tkinter.messagebox
import customtkinter
from typing import Optional
from pydantic import BaseModel, ValidationError
import yaml, sys, os

class AppConfig(BaseModel):
  host: str
  port: int
  username: str
  password: str
if sys.platform == "linux":
  # conf_path=os.path.join(os.path.join('~', '.config', 'ytdlf-app', 'config.yaml'))
  conf_path=os.path.join(os.path.join('config.yaml'))
if sys.platform == "win32"

def load_config(file_path: str) -> AppConfig:
    
  fileexist=True
  if not os.path.exists(file_path):
    fileexist=False
  with open(file_path, 'a') as file:
    if not fileexist:
      con=AppConfig(host='localhost', port=5000, username='username', password='password')
      conn=yaml.dump(con.model_dump(mode='yaml'))
      file.write(conn)
    yaml_data = yaml.safe_load(file)
    try:
      return AppConfig(**yaml_data)
    except ValidationError as e:
      raise ValueError(f"Invalid configuration: {e}")


try:
  config = load_config(conf_path)
except ValueError as e:
  print('An Error Occured in this config')
  print(e)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
  def init(self):
    super().init()

    self.title('Youtube Downloader')
    self.geometry(f"{1100}x{500}")
    

if __name__ == "__main__":
  app=App()
  app.mainloop()