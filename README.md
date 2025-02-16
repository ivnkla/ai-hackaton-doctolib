# ai-hackaton-doctolib

## Requirements

- Python 3+
- A Scaleway account

After cloning the repo to your space :

```rb
git clone "https://github.com/ivnkla/ai-hackaton-doctolib.git"
```

Run the following to add the necessary librairies to your environment :

```rb
pip install -r requirements.txt
```

Also, considering sentitive API leak, you have to own your scaleway key and then run the following :

```rb
echo API_KEY=<your Scaleway key here> >> .env.example
mv .env.example .env
```

## Usage

After launching Docker run this command:

```rb
make 
make re
```

Then, open on your browser on : 

```
http://127.0.0.1:8000
```

## Example

See a demo :
![Demo](./demo.gif)

## Structure
```markdown
├── Dockerfile
├── Makefile
├── README.md
├── api.py
├── prompt.txt
├── requirements.txt
├── server.py
└── static
    ├── index.html
    ├── script.js
    └── style.css
```

## Motivation

Well, we have noiticed a ... to pitch 

## Authors

- [@scartriche](https://github.com/scartriche)        - Clement Morice    - ECE Paris
- [@ArthurDelf](https://github.com/ArthurDelf)        - Arthur Delfosse   - ECE Paris
- [@gfranque42](https://github.com/gfranque42)        - Guillaume Franque - 42 Paris
- [@replace_stan](https://github.com/replace_lucas)   - Stanislas Barrage - 42 Paris
- [@replace_lucas](https://github.com/replace_lucas)  - Lucas Lorang      - ECE Paris
- [@ivnkla](https://github.com/ivnkla)                - Kalvin Pichon     - Université Grenoble

## Acknowledgments

We are grateful to :
- Antonin and ... from Scaleway who helped us with their solution and various subjects
- The Tech team which helped us on various subjects