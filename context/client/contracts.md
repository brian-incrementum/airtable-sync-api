# Metadata
Base ID: app36dpFPr84hM8TN
Table: Contracts
Table ID: tblu0LdsOvLh3aaHI

# Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "fld0R0HKW1BJmTwH0",
      "name": "Record ID",
      "options": {
        "formula": "RECORD_ID()",
        "isValid": true,
        "referencedFieldIds": [],
        "result": {
          "type": "singleLineText"
        }
      },
      "type": "formula"
    },
    {
      "id": "fldbQ3IOxm7OEHqWH",
      "name": "Agreement Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "id": "fldUNtGWiPdDc7fGm",
      "name": "Agreement Title",
      "type": "singleLineText"
    },
    {
      "id": "fldaeW6ULWgY1KNPU",
      "name": "Services",
      "options": {
        "inverseLinkFieldId": "fldQQigZhh3qe9MZK",
        "isReversed": false,
        "linkedTableId": "tblTYmxXucxldO4Md",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldN33PuAicnJoTCQ",
      "name": "Link to Google Drive",
      "type": "url"
    },
    {
      "id": "fld7UT7Ah7i6ojieh",
      "name": "Brand Services",
      "options": {
        "inverseLinkFieldId": "fldhHNkFxRPjNW0D3",
        "isReversed": false,
        "linkedTableId": "tblLK5hswpid4nH8c",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    }
  ],
  "id": "tblu0LdsOvLh3aaHI",
  "name": "Contracts",
  "primaryFieldId": "fld0R0HKW1BJmTwH0",
  "views": [
    {
      "id": "viwyrRH8QAuQIs4KL",
      "name": "Grid view",
      "type": "grid"
    },
    {
      "id": "viwKr401WVSQpyFQZ",
      "name": "Form",
      "type": "form"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2024-11-14T11:07:18.000Z",
    "fields": {
      "Agreement Date": "2024-07-18",
      "Agreement Title": "MV Sport",
      "Brand Services": [
        "rec4w8O5kcvTqbIuM"
      ],
      "Link to Google Drive": "https://drive.google.com/file/d/1BYXg1ernSgD13sS6-sSqZqQFNRvGP2yA/view?usp=sharing",
      "Record ID": "rec00O7355OSgpV49",
      "Services": [
        "reccdrSxPzewXv5rU"
      ]
    },
    "id": "rec00O7355OSgpV49"
  }
]
