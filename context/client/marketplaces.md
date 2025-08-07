# Metadata
Base ID: app36dpFPr84hM8TN
Table: Marketplaces
Table ID: tblsjMd2w00cu5qV8

# Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "fldyBepNs2ppVCOhM",
      "name": "Name",
      "type": "singleLineText"
    },
    {
      "id": "fldgCsoZXiYosTVMj",
      "name": "Brand Services",
      "options": {
        "inverseLinkFieldId": "fldEpdYsfnKozmEbH",
        "isReversed": false,
        "linkedTableId": "tblLK5hswpid4nH8c",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    }
  ],
  "id": "tblsjMd2w00cu5qV8",
  "name": "Marketplaces",
  "primaryFieldId": "fldyBepNs2ppVCOhM",
  "views": [
    {
      "id": "viwCfdNW3H6lO931U",
      "name": "Grid view",
      "type": "grid"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2024-11-11T15:52:47.000Z",
    "fields": {
      "Brand Services": [
        "recvP5T82x3SwLcET",
        "recUHCzy086aVndiK",
        "recfcJ857gMsIAfTN"
      ],
      "Name": "IT"
    },
    "id": "rec2l4Oqr6uJVZ8V6"
  }
]