# ai-hackaton-doctolib
# safe-pg-migrations

ActiveRecord migrations for Postgres made safe.

![safe-pg-migrations](./logo.png)

## Requirements

- Python 3+

After cloning the repo to your space :

```rb
git clone "https://github.com/ivnkla/ai-hackaton-doctolib.git"
```

Run the following to add the necessary librairies to your environment :

```rb
pip install -r requirements.txt
```

## Usage

Run this command:

```rb
python main.py
```

or 

```rb
python3 main.py
```

## Example

Consider the following migration:

```rb
class AddPatientRefToAppointments < ActiveRecord::Migration[6.0]
  def change
    add_reference :appointments, :patient
  end
end
```

## Structure
```rb
├── README.md
├── __pycache__
│   ├── api.cpython-313.pyc
│   ├── chat.cpython-313.pyc
│   └── timeout.cpython-313.pyc
├── api.py
├── chat.py
├── main.py
├── prompt.txt
└── timeout.py
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
- Antonin and ... from Scaleway ...
- The Tech team which ...