from fastapi import FastAPI

app = FastAPI()

@app.post("/{path_params}")
async def get_server_status(data: dict, q_param1: str, path_params: str):
  print(data)
  print(q_param1)
  print(path_params)
  return "All well"
