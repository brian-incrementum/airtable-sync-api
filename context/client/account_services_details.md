# Metadata
Base ID: app36dpFPr84hM8TN
Table: Account Services Detail
Table ID: tblLK5hswpid4nH8c

# Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "fldaMCswS6dljF8Ak",
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
      "id": "fldEcmeSQYCDGt2OF",
      "name": "Account",
      "options": {
        "inverseLinkFieldId": "fldXT8HDr1kDM87XY",
        "isReversed": false,
        "linkedTableId": "tblLb0ek0O4HiB3OY",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldownYUeGYVkiQwM",
      "name": "Service",
      "options": {
        "inverseLinkFieldId": "fldLjBKsgtJdSQwb7",
        "isReversed": false,
        "linkedTableId": "tblTYmxXucxldO4Md",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fld7Vscdxs7t1kHl1",
      "name": "Account Manager",
      "options": {
        "inverseLinkFieldId": "fldK8Zu8eEZLfjgdv",
        "isReversed": false,
        "linkedTableId": "tbl2t9Ylc9kM7cfUG",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldVcJHfLm6rVSOgf",
      "name": "Storefront Name",
      "type": "singleLineText"
    },
    {
      "id": "fldV5WbyUJl7XJEev",
      "name": "Service Start Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "id": "fldz6pA1cDLD5Emu5",
      "name": "Service Cancel Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "description": "Required for Amazon Ads\n",
      "id": "fldEpdYsfnKozmEbH",
      "name": "Marketplaces",
      "options": {
        "inverseLinkFieldId": "fldgCsoZXiYosTVMj",
        "isReversed": false,
        "linkedTableId": "tblsjMd2w00cu5qV8",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldl6TJWNs81pz7d7",
      "name": "Pricing Terms",
      "type": "multilineText"
    },
    {
      "id": "fldX5LRS89khD2JIx",
      "name": "Renewal Type",
      "options": {
        "choices": [
          {
            "color": "blueLight2",
            "id": "selpQdOdkVfDtr0dO",
            "name": "monthly"
          },
          {
            "color": "cyanLight2",
            "id": "self4oPARmnCRhV05",
            "name": "yearly"
          },
          {
            "color": "tealLight2",
            "id": "selktGf9BTsKwrXZE",
            "name": "quarterly"
          },
          {
            "color": "greenLight2",
            "id": "sel9FbpRLfAhIDi6P",
            "name": "project"
          },
          {
            "color": "yellowLight2",
            "id": "selqI8jvwqgi7R0qD",
            "name": "other"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fld7hpFGBwkfYSwDD",
      "name": "Cancellation Reason",
      "type": "multilineText"
    },
    {
      "id": "fldhHNkFxRPjNW0D3",
      "name": "Agreement",
      "options": {
        "inverseLinkFieldId": "fld7UT7Ah7i6ojieh",
        "isReversed": false,
        "linkedTableId": "tblu0LdsOvLh3aaHI",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fld9AToyU9L7jcVsl",
      "name": "Software Tools",
      "options": {
        "inverseLinkFieldId": "fld33JzfGUVVbJiwE",
        "isReversed": false,
        "linkedTableId": "tblTWlmmBcZWImDM6",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldDBq0DMsDPXBRa5",
      "name": "Yearly Renewal Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "id": "fld5kZLY9fS7YZ6j0",
      "name": "Minimum Fee",
      "options": {
        "precision": 2,
        "symbol": "$"
      },
      "type": "currency"
    },
    {
      "id": "fldukWM85bwG1Ua0x",
      "name": "Console Login Emails",
      "options": {
        "inverseLinkFieldId": "fldZEWzeyo9kDWtEX",
        "isReversed": false,
        "linkedTableId": "tblk7kVfDShzc5S4j",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldcAUUaZcZDmXR3w",
      "name": "Ad Console Name",
      "type": "singleLineText"
    },
    {
      "id": "fld1zJLpO19rvnbf9",
      "name": "Seller Type",
      "options": {
        "choices": [
          {
            "color": "blueLight2",
            "id": "selxr34tR6R27lZbH",
            "name": "1P"
          },
          {
            "color": "cyanLight2",
            "id": "sel9GxG0cTl2hrE49",
            "name": "3P"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fldjm8HXC6heh0PFa",
      "name": "Data Owl",
      "options": {
        "color": "greenBright",
        "icon": "check"
      },
      "type": "checkbox"
    },
    {
      "id": "fldYbakfR3ACpsvfE",
      "name": "Data Owl Title",
      "type": "singleLineText"
    },
    {
      "id": "fldRAH6OPlYXxwuor",
      "name": "Partner Network",
      "options": {
        "color": "greenBright",
        "icon": "check"
      },
      "type": "checkbox"
    },
    {
      "id": "fldiNwM4OFG9M306R",
      "name": "Last Billing Period Ad Spend",
      "options": {
        "precision": 2,
        "symbol": "$"
      },
      "type": "currency"
    },
    {
      "id": "fldNeG1xZqk6UvxuZ",
      "name": "Billing Day",
      "options": {
        "precision": 0
      },
      "type": "number"
    },
    {
      "id": "fldjy3prp7yYvQlmO",
      "name": "ClickUp Onboarding Link",
      "type": "url"
    },
    {
      "id": "fldrGDvW834wWJfMZ",
      "name": "Slack Channel ID",
      "type": "singleLineText"
    },
    {
      "id": "fld9xvdJOMWrC4Pwv",
      "name": "Main Contact Slack ID",
      "type": "singleLineText"
    },
    {
      "id": "fldkMekpG3oNq98xY",
      "name": "Last Modified",
      "options": {
        "isValid": true,
        "referencedFieldIds": [],
        "result": {
          "options": {
            "dateFormat": {
              "format": "l",
              "name": "local"
            },
            "timeFormat": {
              "format": "h:mma",
              "name": "12hour"
            },
            "timeZone": "America/Chicago"
          },
          "type": "dateTime"
        }
      },
      "type": "lastModifiedTime"
    }
  ],
  "id": "tblLK5hswpid4nH8c",
  "name": "Account Services Detail",
  "primaryFieldId": "fldaMCswS6dljF8Ak",
  "views": [
    {
      "id": "viw2DgAa1HiRU4vyS",
      "name": "AA Active Clients",
      "type": "grid"
    },
    {
      "id": "viwGrezt6srSIaNM5",
      "name": "Seller Ops Active Clients",
      "type": "grid"
    },
    {
      "id": "viw4QyufDfEY0ints",
      "name": "Walmart Active Clients",
      "type": "grid"
    },
    {
      "id": "viwvWCwyVUg1jyq5w",
      "name": "AA Active Clients Billing",
      "type": "grid"
    },
    {
      "id": "viwMpLk213m8FkqjT",
      "name": "BM Active Clients",
      "type": "grid"
    },
    {
      "id": "viwpbFfGCltqm8Xoy",
      "name": "ALL View for Agent",
      "type": "grid"
    },
    {
      "id": "viwjE9rltALfTF0EL",
      "name": "Service Filter",
      "type": "grid"
    },
    {
      "id": "viwvvwVrJWqQhVljp",
      "name": "Active: Do not touch",
      "type": "grid"
    },
    {
      "id": "viwFPctvbIjKEJv4U",
      "name": "Onboarding",
      "type": "grid"
    },
    {
      "id": "viwOYIOSGedIWxJNr",
      "name": "Cancelled",
      "type": "grid"
    },
    {
      "id": "viwHy1LbUPEHh1oHF",
      "name": "Tracking service status",
      "type": "grid"
    },
    {
      "id": "viw9rGyvcncX1Dypr",
      "name": "Client slack channel",
      "type": "grid"
    },
    {
      "id": "viwGsDwJlyyOTZBTp",
      "name": "Ad manager field missing",
      "type": "grid"
    },
    {
      "id": "viwBlOM3tO0VBwYRc",
      "name": "Ad managers",
      "type": "grid"
    },
    {
      "id": "viwEdpkjJq2vvhkE5",
      "name": "ClickUp ID",
      "type": "grid"
    },
    {
      "id": "viwFm80ubaIteynTx",
      "name": "Private Test View",
      "type": "grid"
    },
    {
      "id": "viwNzg7MsPuErbRfd",
      "name": "Data Owl Sync",
      "type": "grid"
    },
    {
      "id": "viwuzx9whWm8i5Kra",
      "name": "Missing pricing terms",
      "type": "grid"
    },
    {
      "id": "viwHotL2N4Rwwfi3A",
      "name": "Missing minimum fee",
      "type": "grid"
    },
    {
      "id": "viwpdOU9Vv4tWFoBb",
      "name": "Missing last billing adspend",
      "type": "grid"
    },
    {
      "id": "viwBPiTbYrjNlhqDN",
      "name": "Form",
      "type": "form"
    },
    {
      "id": "viwy5jcguQrchWMI3",
      "name": "Brian's Grid",
      "type": "grid"
    },
    {
      "id": "viwh9PHni3ZEkZGD9",
      "name": "Saras Analytics",
      "type": "grid"
    },
    {
      "id": "viw7qm8bC0Pa6cYux",
      "name": "Self Serve",
      "type": "grid"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2024-11-14T11:00:56.000Z",
    "fields": {
      "Account": [
        "rece7h13EjbqsMDmr"
      ],
      "Account Manager": [
        "recte6igwNd4uOdDr"
      ],
      "Ad Console Name": "Biostime",
      "Agreement": [
        "recLvIG9prdKwdD9x"
      ],
      "Console Login Emails": [
        "recSbma3a6f3KKYW7"
      ],
      "Contract Date": [
        "2024-09-03"
      ],
      "Contract Lookup": [
        "https://drive.google.com/file/d/1HPyXqLtxUSVq5QfWW6dexCfzIOdFiixt/view?usp=sharing"
      ],
      "Last Modified": "2025-07-15T18:32:04.000Z",
      "Marketplaces": [
        "recx5VTrLL5fPp4bS"
      ],
      "Minimum Fee": 750,
      "Pricing Terms": "$1500 combined with Swisse Wellness",
      "Record ID": "rec04g6g6qyC6rBcg",
      "Renewal Type": "yearly",
      "Seller Type": "3P",
      "Service": [
        "reccdrSxPzewXv5rU"
      ],
      "Service Start Date": "2024-09-16",
      "Service Status": "Active",
      "Storefront Name": "Biostime",
      "Yearly Renewal Date": "2025-09-03"
    },
    "id": "rec04g6g6qyC6rBcg"
  }
]