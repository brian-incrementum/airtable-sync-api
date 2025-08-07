# Metadata

Base ID: app36dpFPr84hM8TN
Table: Companies
Table ID: tbl35cnxFSmMnBQYL
Description: No description available


Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "fldY9w7spPLw4CPAs",
      "name": "Company Name",
      "type": "singleLineText"
    },
    {
      "id": "fldV7fqTr5pjCALLY",
      "name": "Linked Accounts",
      "options": {
        "inverseLinkFieldId": "fldCmFlVAKoxnUwoa",
        "isReversed": false,
        "linkedTableId": "tblLb0ek0O4HiB3OY",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldqBUZ4F5Tv8VX7F",
      "name": "Hubspot ID",
      "type": "singleLineText"
    },
    {
      "id": "fldLHqQqKnsGJXmn4",
      "name": "Active Brands",
      "options": {
        "fieldIdInLinkedTable": "fldMBaLFkS0KKudvW",
        "isValid": true,
        "recordLinkFieldId": "fldV7fqTr5pjCALLY",
        "result": {
          "type": "singleLineText"
        }
      },
      "type": "multipleLookupValues"
    }
  ],
  "id": "tbl35cnxFSmMnBQYL",
  "name": "Companies",
  "primaryFieldId": "fldY9w7spPLw4CPAs",
  "views": [
    {
      "id": "viwU9lhc8TGQ9VDKc",
      "name": "All ",
      "type": "grid"
    },
    {
      "id": "viwxsPU1GT5mPvJRp",
      "name": "Active",
      "type": "grid"
    },
    {
      "id": "viwtW1T9YxeBYJKie",
      "name": "Form",
      "type": "form"
    }
  ]
}


# Sample record JSON
[
  {
    "createdTime": "2024-11-14T16:19:21.000Z",
    "fields": {
      "Active Brands": [
        "National Naturopathic"
      ],
      "Active Services": 1,
      "Company Name": "13314201 Canada Inc.",
      "Hubspot Company Link": "https://app.hubspot.com/contacts/20305264/company/6851145617",
      "Hubspot ID": "6851145617",
      "Linked Accounts": [
        "reczalkTaN8wkyr2f"
      ]
    },
    "id": "rec037mRqh3Cs1KSn"
  }
]