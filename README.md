# Kawruh ꦏꦮꦿꦸꦃ

![Data License](https://img.shields.io/badge/Data%20License-CC0-green)
![Code License](https://img.shields.io/badge/Code%20License-MIT-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![PRs](https://img.shields.io/badge/PRs-welcome-orange)

**Kawruh** (Javanese: *Knowledge*) is an open-source database of Javanese philosophy, metaphysics, and linguistic logic. 

It preserves concepts like *Kerata Basa* (etymological philosophy), *Sanepa* (sarcasm/paradox), and *Paribasan* (social laws) in a machine-readable format (JSON) for developers, data scientists, and cultural preservationists.

## 📂 Data Structure

All data is stored in the `data/` directory.

| File | Content | Logic |
| :--- | :--- | :--- |
| `kerata_basa.json` | **Jarwo Dosok** | Etymological dissection of words to find philosophical meaning. |
| `sanepa.json` | **Paradoxes** | Irony and sarcasm constants (e.g., *Pait Madu* = Very Sweet). |
| `paribasan.json` | **Axioms** | Social rules and consequences (Karma, Law, Economy). |
| `neptu.json` | **Numerology** | Constants for *Weton* calculations (Days & Markets). |

## 🚀 Usage

You can use the raw JSON files directly or use the included scripts to generate SQL.

### Raw JSON
```javascript
const paribasan = require('./data/paribasan.json');
console.log(paribasan.find(p => p.category === 'Karma'));
```

### Export to SQL
```bash
python3 scripts/export_sql.py
# output: kawruh_dump.sql
```

### 🤝 Contribution
We value quality over quantity.
1. **No duplicates**: Check existing data before adding.
2. **Strict Schema**: Follow the JSON structure strictly.
3. **Valid Philosophy**: Do not add random slang. Only established philosophical terms.

### 📜 Philosophy
Ngèlmu iku kalakoné kanthi laku. 
Knowledge is only acquired through practice (implementation).

