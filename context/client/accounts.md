# Metadata
Base ID: app36dpFPr84hM8TN
Table: Accounts
Table ID: tblLb0ek0O4HiB3OY

# Schema (fields i want to keep)
{
  "fields": [
    {
      "description": "Use the brand name, unless an account has multiple brands.  If they do use the storefront name",
      "id": "fldMBaLFkS0KKudvW",
      "name": "Name",
      "type": "singleLineText"
    },
    {
      "id": "fldCmFlVAKoxnUwoa",
      "name": "Companies",
      "options": {
        "inverseLinkFieldId": "fldV7fqTr5pjCALLY",
        "isReversed": false,
        "linkedTableId": "tbl35cnxFSmMnBQYL",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldgcQt3ppH2I4xJ4",
      "name": "Sub Account Hubspot ID",
      "type": "singleLineText"
    },
    {
      "id": "fldXT8HDr1kDM87XY",
      "name": "Brand Services Record",
      "options": {
        "inverseLinkFieldId": "fldEcmeSQYCDGt2OF",
        "isReversed": false,
        "linkedTableId": "tblLK5hswpid4nH8c",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldx1p8avPSzqtRkv",
      "name": "Stripe_ID",
      "type": "singleLineText"
    },
    {
      "id": "fldUbeHknNE79aUF1",
      "name": "Client Meetings",
      "options": {
        "inverseLinkFieldId": "fldbPlcIdkGhcyEuK",
        "isReversed": false,
        "linkedTableId": "tblV3ZIKJfdYcUuSG",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    }
  ],
  "id": "tblLb0ek0O4HiB3OY",
  "name": "Accounts",
  "primaryFieldId": "fldMBaLFkS0KKudvW",
  "views": [
    {
      "id": "viweqUx4fDYj8Eo1w",
      "name": "All View",
      "type": "grid"
    },
    {
      "id": "viwR4TpIXyrFReBnq",
      "name": "Active",
      "type": "grid"
    },
    {
      "id": "viw72wEDYyic14hr5",
      "name": "Slack channels reference",
      "type": "grid"
    },
    {
      "id": "viwBhlknx0wP1a43D",
      "name": "Cancelled",
      "type": "grid"
    },
    {
      "id": "viwEGeiSa4CFIQtFA",
      "name": "Form",
      "type": "form"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2025-07-02T15:48:18.000Z",
    "fields": {
      "Active Services": [
        "reccQKTDSYeOYv47x",
        "rechAllEOZ7Uo0qcF"
      ],
      "Brand Services Record": [
        "recxn1qk3SNSRQ3Qq",
        "recczam3FgzjgQqsC"
      ],
      "Client Meetings": [
        "reci8PiLYVb9o5ANb",
        "recN5Kxu7B6C1NdiA"
      ],
      "Companies": [
        "recbBUzbnrk5tnEUX"
      ],
      "Merged Hubspot ID": [
        "35655600744"
      ],
      "Name": "Drops of Nature",
      "Parent Hubspot ID": [
        "35655600744"
      ],
      "Service Count": 2,
      "Service Start Dates": [
        "2025-07-07",
        "2025-07-14"
      ]
    },
    "id": "rec0DOeDJiJ4A4p2r"
  }
]