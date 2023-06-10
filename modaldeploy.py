import modal

# import main from main.py
from gpt_code_ui import main

stub = modal.Stub('smol-talk-v0')

pandas_image = modal.Image.debian_slim().pip_install(
"Flask==2.3.2",
"Flask_Cors==3.0.10",
"ipykernel==6.23.1",
"jupyter_client==8.2.0",
"modal_client==0.49.2348",
"pandas==2.0.2",
"python-dotenv==1.0.0",
"Requests==2.31.0",
"setuptools==65.4.1",
"snakeMQ==1.6",
)


@stub.function(image=pandas_image)
@modal.web_endpoint()
def f(origin: str = 'unknown'):
  # call main function
  if origin:
    print('called from origin: ' + origin)
  main.main();