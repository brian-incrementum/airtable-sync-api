
# Metadata
Base ID: appebIyOziMdUyOqi
Table: Position
Table ID: tbldrYoS9nkpqLGoA

# Position Table Schema (fields i want to sync)

{
  "fields": [
    {
      "id": "fld7v0uFnv8rnLvpG",
      "name": "Name",
      "type": "singleLineText"
    },
    {
      "id": "fldaLOdGOjnpgnZnw",
      "name": "Department",
      "options": {
        "inverseLinkFieldId": "fldUmeiEgpQKmhwAY",
        "isReversed": false,
        "linkedTableId": "tblHhOw2PAG29NIir",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldew2uMhAgloCtty",
      "name": "Employee directory",
      "options": {
        "inverseLinkFieldId": "fldepYCMilhnuKunJ",
        "isReversed": true,
        "linkedTableId": "tblJiYy00NA25LBpu",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    }
  ],
  "id": "tbldrYoS9nkpqLGoA",
  "name": "Position",
  "primaryFieldId": "fld7v0uFnv8rnLvpG",
  "views": [
    {
      "id": "viw4A3ASmohjnKDnB",
      "name": "All departments",
      "type": "grid"
    },
    {
      "id": "viwQByUYc5moqhJEV",
      "name": "Synced",
      "type": "grid"
    },
    {
      "id": "viwMpgu75Jr0Tb937",
      "name": "ALL",
      "type": "grid"
    }
  ]
}

# Sample record JSON
[
  {
    "createdTime": "2022-10-04T14:35:46.000Z",
    "fields": {
      "Department": [
        "recXhymqMT9k4Dssq"
      ],
      "Employee directory": [
        "recD7O6qCN2vBcRCd"
      ],
      "Member Count": 0,
      "Name": "Content Associate"
    },
    "id": "rec15wnTpWjeN44Mm"
  }
]