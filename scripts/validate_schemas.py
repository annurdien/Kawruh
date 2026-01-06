#!/usr/bin/env python3
"""Validate JSON data files against their schemas."""

import json
import sys
import os
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("⚠️  jsonschema not installed. Install with: pip install jsonschema")
    sys.exit(1)

def validate_all_schemas():
    """Validate all data files against their corresponding schemas."""
    schemas_dir = Path("schemas")
    data_dir = Path("data")
    
    if not schemas_dir.exists():
        print("ℹ️  No schemas directory found, skipping validation")
        return True
    
    has_error = False
    validated_count = 0
    
    for schema_file in schemas_dir.glob("*.schema.json"):
        data_file = data_dir / f"{schema_file.stem.replace('.schema', '')}.json"
        
        if not data_file.exists():
            continue
            
        try:
            with open(schema_file) as sf:
                schema = json.load(sf)
            
            with open(data_file) as df:
                data = json.load(df)
            
            jsonschema.validate(instance=data, schema=schema)
            print(f"✅ {data_file.name} validates against schema")
            validated_count += 1
            
        except jsonschema.ValidationError as e:
            print(f"❌ Validation error in {data_file.name}:")
            print(f"   {e.message}")
            has_error = True
        except Exception as e:
            print(f"❌ Error validating {data_file.name}: {e}")
            has_error = True
    
    if validated_count == 0:
        print("⚠️  No data files validated")
    
    return not has_error

if __name__ == "__main__":
    if validate_all_schemas():
        print("🎉 All schema validations passed!")
        sys.exit(0)
    else:
        sys.exit(1)
