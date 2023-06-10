# smol talk

hosted code interpreter with anthropic claude 100k

## install

note to self:

- having gpt-code-ui pip installed interferes with the project. need to uninstall it
- `make build`
- create a python virtual env (`mkvirtualenv myvirtualenv --python=/usr/bin/python3.10`)
- `pip install -e .`
- THEN run `python gpt_code_ui/main.py`



## frontend live reloading

is not worked out yet

- terminal 1: `cd frontend && npm run dev`
- terminal 2: `WEB_PORT=5173 python gpt_code_ui/main.py` 

## modal deploy

```bash
pip install modal-client # if not already installed

pip install pipreqs
pipreqs .

# update the modalreploy.py file with deps

modal deploy modal.py 
```


## acknowledgements

this is a fork of https://github.com/ricklamers/gpt-code-ui/tree/main