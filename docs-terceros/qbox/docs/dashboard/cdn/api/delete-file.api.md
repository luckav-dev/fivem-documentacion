> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/dashboard/cdn/api/delete-file.api.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Delete file

**DELETE** `/v1/file/{path}`

Delete file

## Request

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `path` | path | string | yes | URL-encoded storage key path. Example: acme-org%2Fimages%2Fexample.png |
| `authorization` | header | string | yes | API key or Bearer API key. Example: Bearer qbox_live_abc123 |

### Responses

#### 200

Schema (`application/json`):

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "ok"
      ]
    }
  },
  "required": [
    "status"
  ]
}
```

Example `success`:

```json
{
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

Example `missingPath`:

```json
{
  "error": "Missing file path",
  "code": "MISSING_FILE_PATH"
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

Example `missingApiKey`:

```json
{
  "error": "Missing API key",
  "code": "MISSING_API_KEY"
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

Example `deleteNotAllowed`:

```json
{
  "error": "API key is not allowed to delete media",
  "code": "DELETE_NOT_ALLOWED"
}
```

#### 404

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

Example `fileNotFound`:

```json
{
  "error": "File not found",
  "code": "FILE_NOT_FOUND"
}
```

#### 429

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
    "tryAgainIn": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": [
    "error",
    "code"
  ]
}
```

Example `rateLimit`:

```json
{
  "error": "Too many requests",
  "code": "RATE_LIMITED",
  "tryAgainIn": 1000
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
