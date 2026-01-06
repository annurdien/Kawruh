# Contributing to Kawruh

## The Rules
1. **Valid Sources Only**: Do not invent new meanings. Use sources like *Baoesastra*, *Serat Wedhatama*, or established oral tradition.
2. **JSON Format**: Ensure your JSON is valid. Trailing commas will fail the build.
3. **English & Indonesian**: The `philosophy` or `meaning` field should preferably be in English or Indonesian to maximize accessibility.
4. **IDs**: Generate a unique ID for your entry (e.g., check the last ID `kb_050` and make yours `kb_051`).

## How to Submit
1. Fork the repo.
2. Create a branch: `git checkout -b add-guru-philosophy`.
3. Add your data to the relevant `.json` file.
4. Run validation: `python3 scripts/validate.py`.
5. Push and PR.