# Metadata
Base ID: app36dpFPr84hM8TN
Table: Services
Table ID: tblTYmxXucxldO4Md

# Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "flduT2zeh2MTCYbWq",
      "name": "Name",
      "type": "singleLineText"
    },
    {
      "id": "fldRT1WF3lKa6Pem4",
      "name": "Description",
      "type": "multilineText"
    },
    {
      "id": "fldLjBKsgtJdSQwb7",
      "name": "Account Services Details",
      "options": {
        "inverseLinkFieldId": "fldownYUeGYVkiQwM",
        "isReversed": false,
        "linkedTableId": "tblLK5hswpid4nH8c",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldQQigZhh3qe9MZK",
      "name": "Contracts",
      "options": {
        "inverseLinkFieldId": "fldaeW6ULWgY1KNPU",
        "isReversed": false,
        "linkedTableId": "tblu0LdsOvLh3aaHI",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fld3cHgnad3vYziNJ",
      "name": "Client Meetings",
      "options": {
        "inverseLinkFieldId": "fldozzJpad2T4Rmng",
        "isReversed": false,
        "linkedTableId": "tblV3ZIKJfdYcUuSG",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    }
  ],
  "id": "tblTYmxXucxldO4Md",
  "name": "Services",
  "primaryFieldId": "flduT2zeh2MTCYbWq",
  "views": [
    {
      "id": "viw9qRLy6ccTSFQ66",
      "name": "Grid view",
      "type": "grid"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2025-06-04T13:44:44.000Z",
    "fields": {
      "Client Meetings": [
        "recmKmkwvzXbMMCdt"
      ],
      "Name": "Walmart DSP"
    },
    "id": "recDLSBXY9xhVUahr"
  }
]