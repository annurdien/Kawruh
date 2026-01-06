# JSON Schemas for Kawruh

This directory contains JSON Schema definitions for validating the data files in the Kawruh repository.

## Schema Files

- `kerata_basa.schema.json` - Validates etymological philosophy entries
- `paribasan.schema.json` - Validates proverb entries  
- `sanepa.schema.json` - Validates paradoxical expression entries
- `neptu.schema.json` - Validates numerology data entries

## Usage

### Python (jsonschema)
```python
import json
import jsonschema

# Load schema and data
with open('schemas/paribasan.schema.json') as schema_file:
    schema = json.load(schema_file)
    
with open('data/paribasan.json') as data_file:
    data = json.load(data_file)

# Validate
jsonschema.validate(instance=data, schema=schema)
print("✅ Valid!")
```

### Node.js (ajv)
```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

const schema = require('./schemas/kerata_basa.schema.json');
const data = require('./data/kerata_basa.json');

const validate = ajv.compile(schema);
const valid = validate(data);

if (valid) {
  console.log('✅ Valid!');
} else {
  console.log('❌ Invalid:', validate.errors);
}
```

### Command Line (jsonschema)
```bash
# Install jsonschema CLI
pip install jsonschema

# Validate
jsonschema -i data/paribasan.json schemas/paribasan.schema.json
```

## Schema Standards

All schemas follow [JSON Schema Draft 7](https://json-schema.org/draft-07/schema) specification.

## Validation in CI/CD

These schemas are automatically validated in GitHub Actions on every push and pull request. See `.github/workflows/validate.yml` for details.
