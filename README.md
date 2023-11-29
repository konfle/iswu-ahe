# iswu-ahe

## Database


#### secret.yaml

```
apiVersion: v1
kind: Secret
metadata:
  name: postgres-credentials
type: Opaque
data:
  POSTGRES_USER: <base64_encoded_username>
  POSTGRES_PASSWORD: <base64_encoded_password>

```

Command to encode base64 string <br>
```
echo -n 'string_to_encode' | base64
```