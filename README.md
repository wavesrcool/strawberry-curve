# strawberry-curve

A GraphQL API in Python for interacting with the elliptic curve $y^2=x^3+7$ over $F_{2^{256}-2^{32}-977}$

### Run
```bash
uvicorn app:app --reload --host '::'
```

### Hello curve!
```bash
curl -L -X POST 'http://localhost:8000/graphql' \
-H 'Content-Type: application/json' \
--data-raw '{"query":"query {\n    helloCurve\n}","variables":{}}'
```

### Tests
```bash
python3 -m unittest
```

