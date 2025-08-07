# Metadata
Base ID: app36dpFPr84hM8TN
Table: Console Login Emails
Table ID: tblk7kVfDShzc5S4j
# Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "fldLNpi6SeZ8qcPOj",
      "name": "Name",
      "type": "singleLineText"
    },
    {
      "id": "fld5rZOFh2kmJzzAi",
      "name": "Email",
      "type": "email"
    },
    {
      "id": "fldZEWzeyo9kDWtEX",
      "name": "Brand Services",
      "options": {
        "inverseLinkFieldId": "fldukWM85bwG1Ua0x",
        "isReversed": false,
        "linkedTableId": "tblLK5hswpid4nH8c",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldlObpqR6RHS3NdA",
      "name": "Google Voice",
      "type": "phoneNumber"
    }
  ],
  "id": "tblk7kVfDShzc5S4j",
  "name": "Console Login Emails",
  "primaryFieldId": "fldLNpi6SeZ8qcPOj",
  "views": [
    {
      "id": "viwBGGqvayDoSX8Y0",
      "name": "Grid view",
      "type": "grid"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2024-11-22T14:52:32.000Z",
    "fields": {
      "Brand Services": [
        "rec1Yl2QjQhwSGNlp"
      ],
      "Name": "omnitopia.walmart@incrementumclients.com"
    },
    "id": "rec0GjpjI7wDC6HKo"
  }
]