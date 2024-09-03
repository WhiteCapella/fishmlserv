from fishmlserv.model.manager import get_model_path, prediction
import typer
import fire


def ppping():
  print("pong")

def model_path():
  fire.Fire(get_model_path)

def pp():
  fire.Fire(prediction)

def ppp():
  typer.run(prediction)
