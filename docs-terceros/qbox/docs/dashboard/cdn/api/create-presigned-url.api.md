> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/dashboard/cdn/api/create-presigned-url.api.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Create Presigned URL

**GET** `/v1/file/presigned-url`

Create Presigned URL

## Request

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `authorization` | header | string | yes | API key or Bearer API key. Example: Bearer qbox_live_abc123 |

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
        "presignedUrl": {
          "type": "string",
          "format": "uri"
        },
        "expiresIn": {
          "type": "integer",
          "minimum": 1
        }
      },
      "required": [
        "presignedUrl",
        "expiresIn"
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
    "presignedUrl": "https://api.qbox.re/v1/file/presigned-url/eyJ2IjoxLCJleHAiOjE3NDAwMDAwMDAsIm9yZ0lkIjoiYWJjIn0.signature",
    "expiresIn": 300
  },
  "status": "ok"
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

Example `invalidMetadata`:

```json
{
  "error": "API key metadata is missing organization context",
  "code": "INVALID_KEY_METADATA"
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

Example `missingPresignedSecret`:

```json
{
  "error": "Presigned URL secret is not configured",
  "code": "PRESIGNED_URL_SECRET_NOT_CONFIGURED"
}
```
