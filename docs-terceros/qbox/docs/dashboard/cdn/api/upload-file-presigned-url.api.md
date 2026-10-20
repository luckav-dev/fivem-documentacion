> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/dashboard/cdn/api/upload-file-presigned-url.api.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Upload file (Presigned URL)

**POST** `/v1/file/presigned-url/{token}`

Upload file (Presigned URL)

## Request

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `token` | path | string | yes | URL-encoded presigned upload token. Example: eyJ2IjoxLCJleHAiOjE3NDAwMDAwMDAsIm9yZ0lkIjoiYWJjIn0.signature |

### Request body

```json
{
  "title": "Body",
  "body": {
    "required": true,
    "content": {
      "multipart/form-data": {
        "schema": {
          "type": "object",
          "properties": {
            "file": {
              "type": "string",
              "format": "binary",
              "description": "File to upload"
            },
            "filename": {
              "type": "string",
              "description": "Custom filename (example: logo.png). If omitted, a random name is generated."
            },
            "path": {
              "type": "string",
              "description": "Storage folder path within the API key folder (example: super)."
            }
          },
          "required": [
            "file"
          ]
        }
      }
    }
  }
}
```

### Responses

#### 200

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Storage object ID (full storage key)"
        },
        "url": {
          "type": "string",
          "format": "uri"
        }
      },
      "required": [
        "id",
        "url"
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "ok"
      ]
    }
  },
  "required": [
    "data",
    "status"
  ]
}
```

Example `success`:

```json
{
  "data": {
    "url": "https://r2.qbox.re/acme-org/images/example.png"
  },
  "status": "ok"
}
```

#### 400

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string",
      "description": "Human-readable error message. Example: Missing API key"
    },
    "code": {
      "type": "string",
      "description": "Machine-readable error code. Example: MISSING_API_KEY"
    }
  },
  "required": [
    "error",
    "code"
  ]
}
```

Example `malformedToken`:

```json
{
  "error": "Malformed presigned upload token",
  "code": "MALFORMED_PRESIGNED_UPLOAD_TOKEN"
}
```

#### 401

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string",
      "description": "Human-readable error message. Example: Missing API key"
    },
    "code": {
      "type": "string",
      "description": "Machine-readable error code. Example: MISSING_API_KEY"
    }
  },
  "required": [
    "error",
    "code"
  ]
}
```

Example `invalidToken`:

```json
{
  "error": "Invalid or expired presigned upload token",
  "code": "INVALID_PRESIGNED_UPLOAD_TOKEN"
}
```

#### 403

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string",
      "description": "Human-readable error message. Example: Missing API key"
    },
    "code": {
      "type": "string",
      "description": "Machine-readable error code. Example: MISSING_API_KEY"
    }
  },
  "required": [
    "error",
    "code"
  ]
}
```

Example `mediaTypeNotAllowed`:

```json
{
  "error": "Presigned upload is not allowed for media type image/webp",
  "code": "MEDIA_TYPE_NOT_ALLOWED"
}
```

#### 413

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    },
    "code": {
      "type": "string"
    },
    "usageBytes": {
      "type": "integer",
      "minimum": 0
    },
    "uploadBytes": {
      "type": "integer",
      "minimum": 0
    },
    "limitBytes": {
      "type": "integer",
      "minimum": 0
    },
    "remainingBytes": {
      "type": "integer",
      "minimum": 0
    },
    "plan": {
      "type": "string"
    }
  },
  "required": [
    "error",
    "code"
  ]
}
```

Example `storageLimit`:

```json
{
  "error": "Organization storage limit exceeded",
  "code": "ORG_STORAGE_LIMIT_EXCEEDED",
  "usageBytes": 2147483648,
  "uploadBytes": 7340032,
  "limitBytes": 2147483648,
  "remainingBytes": 0,
  "plan": "free"
}
```

#### 500

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string",
      "description": "Human-readable error message. Example: Missing API key"
    },
    "code": {
      "type": "string",
      "description": "Machine-readable error code. Example: MISSING_API_KEY"
    }
  },
  "required": [
    "error",
    "code"
  ]
}
```

Example `storageNotConfigured`:

```json
{
  "error": "R2 storage is not configured",
  "code": "STORAGE_NOT_CONFIGURED"
}
```
