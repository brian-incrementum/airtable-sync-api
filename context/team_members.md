
Meta data
Base ID: appebIyOziMdUyOqi
Table: Team directory
Table ID: tblJiYy00NA25LBpu

# Table Schema i want to sync
{
  "fields": [
    {
      "id": "fldDqSK2XMDVjGypp",
      "name": "Full Name",
      "type": "singleLineText"
    },
    {
      "id": "fldIfOKWYyD0dMwhA",
      "name": "Department",
      "options": {
        "inverseLinkFieldId": "fldImSCWXNCY7Evnp",
        "isReversed": false,
        "linkedTableId": "tblHhOw2PAG29NIir",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldGOU2RoUKEEnqk9",
      "name": "Manager",
      "options": {
        "isReversed": false,
        "linkedTableId": "tblJiYy00NA25LBpu",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldKBebJcCygM4c1N",
      "name": "Photo",
      "options": {
        "isReversed": true
      },
      "type": "multipleAttachments"
    },
    {
      "id": "fld5gTSsIGdsHozRQ",
      "name": "Status",
      "options": {
        "choices": [
          {
            "color": "greenLight2",
            "id": "selh8ybW76QJlGKCT",
            "name": "Employee"
          },
          {
            "color": "blueLight2",
            "id": "selh60iwm4mDaFvwU",
            "name": "Contractor"
          },
          {
            "color": "grayLight2",
            "id": "seldhNMVJT3PE5U4w",
            "name": "On leave"
          },
          {
            "color": "tealLight2",
            "id": "sel7jZonCEYeDb7Xd",
            "name": "Dismissed"
          },
          {
            "color": "yellowLight2",
            "id": "selibxigVgVq2V875",
            "name": "Project"
          },
          {
            "color": "blueLight2",
            "id": "selesqijOM09JetSX",
            "name": "Onboarding"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fldepYCMilhnuKunJ",
      "name": "Position",
      "options": {
        "inverseLinkFieldId": "fldew2uMhAgloCtty",
        "isReversed": false,
        "linkedTableId": "tbldrYoS9nkpqLGoA",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldKpTC0RAD76KKrw",
      "name": "Company email",
      "type": "singleLineText"
    },
    {
      "id": "fldMsKJP0LCYjPBks",
      "name": "Phone",
      "type": "phoneNumber"
    },
    {
      "id": "fldMqUzWTEG5bFHtA",
      "name": "Start date",
      "options": {
        "dateFormat": {
          "format": "M/D/YYYY",
          "name": "us"
        }
      },
      "type": "date"
    },
    {
      "id": "fldGewjtHaULKBSAG",
      "name": "Last Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "id": "fldMfUCY2NAZcCGvm",
      "name": "DOB",
      "options": {
        "dateFormat": {
          "format": "M/D/YYYY",
          "name": "us"
        }
      },
      "type": "date"
    },
    {
      "id": "fld3nNbtr1MFT90nw",
      "name": "Personal Email",
      "type": "singleLineText"
    },
    {
      "id": "fldGAemCq8EHX08Nu",
      "name": "Country",
      "type": "singleLineText"
    },
    {
      "id": "fld6HKythwBG4Fe5R",
      "name": "Slack ID",
      "type": "singleLineText"
    },
    {
      "id": "fldwK70zNDfTgoHvJ",
      "name": "Click Up ID",
      "type": "singleLineText"
    },
    {
      "id": "fldOJ0GfnpDWF7afx",
      "name": "Record ID",
      "options": {
        "formula": "RECORD_ID()\n",
        "isValid": true,
        "referencedFieldIds": [],
        "result": {
          "type": "singleLineText"
        }
      },
      "type": "formula"
    },
    {
      "id": "fldaGxhIqEM9sll04",
      "name": "HS User ID",
      "type": "singleLineText"
    },
    {
      "id": "fldjhhbEAj6vPglD8",
      "name": "Government ID",
      "type": "url"
    },
    {
      "id": "fldtqSim3A4bSBjKO",
      "name": "ID Expiration Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "id": "fldj4bDEy9ByeHZMa",
      "name": "Active Lastpass",
      "options": {
        "color": "greenBright",
        "icon": "check"
      },
      "type": "checkbox"
    },
    {
      "id": "fldulIGo1wV73PF8p",
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
            "timeZone": "client"
          },
          "type": "dateTime"
        }
      },
      "type": "lastModifiedTime"
    }
  ],
  "id": "tblJiYy00NA25LBpu",
  "name": "Team directory",
  "primaryFieldId": "fldDqSK2XMDVjGypp",
  "views": [
    {
      "id": "viwOYgPXCCfJ6SGs3",
      "name": "Team Directory Form",
      "type": "form"
    },
    {
      "id": "viw1Ct5HeKYID3hS3",
      "name": "Active",
      "type": "grid"
    },
    {
      "id": "viwDUNRVAATSH0fSb",
      "name": "Temp",
      "type": "grid"
    },
    {
      "id": "viwyeOzS3EI36HJlx",
      "name": "Grouped by department",
      "type": "grid"
    },
    {
      "id": "viwkujc7OgODdzrQY",
      "name": "Team grouped by dept - shared",
      "type": "grid"
    },
    {
      "id": "viwWNtdKIxi57ENrz",
      "name": "Headshots - Shared",
      "type": "gallery"
    },
    {
      "id": "viwskkL9fTqNZX4UL",
      "name": "Team members - Shared",
      "type": "grid"
    },
    {
      "id": "viw4HwBecO1Ic9Z1b",
      "name": "Dismissed",
      "type": "grid"
    },
    {
      "id": "viwmSI8FjsfaJ7BdL",
      "name": "Dismissed copy",
      "type": "grid"
    },
    {
      "id": "viwLlQSZsrn6hR54P",
      "name": "Advertising Analyst",
      "type": "grid"
    },
    {
      "id": "viwIjgDsNEgKRJb2D",
      "name": "Shared w/ Client Onboarding",
      "type": "grid"
    },
    {
      "id": "viwz61ipdEf5IJoxU",
      "name": "ALL",
      "type": "grid"
    },
    {
      "id": "viwapPK1XKm6bJi08",
      "name": "Synced - DO NOT TOUCH",
      "type": "grid"
    },
    {
      "id": "viwDHV8yOKn7QWgtz",
      "name": "Amazon advertising - DO NOT TOUCH",
      "type": "grid"
    },
    {
      "id": "viwNoLLUgb5asbb7Y",
      "name": "Group by Manager (Advertising) (DNT)",
      "type": "grid"
    },
    {
      "id": "viwl3kSW4bBSu82Rr",
      "name": "Group by Manager (Advertising) (DNT) copy",
      "type": "grid"
    },
    {
      "id": "viw9ZfgyiQszD4Hey",
      "name": "PH TEAM",
      "type": "grid"
    },
    {
      "id": "viwd6RDKedKZr4z4g",
      "name": "Started This Month",
      "type": "grid"
    },
    {
      "id": "viwmxy0AKxsVhruw7",
      "name": "Sales Team",
      "type": "grid"
    },
    {
      "id": "viwEady0fzIuDSNSe",
      "name": "Group by Country",
      "type": "grid"
    },
    {
      "id": "viwi5D0JEDyikcCUM",
      "name": "Group by Manager (DNT)",
      "type": "grid"
    },
    {
      "id": "viwJhAdWTVZxEkNrb",
      "name": "Amazon advertising - DO NOT TOUCH copy",
      "type": "grid"
    },
    {
      "id": "viwLeimizNNOWFVnd",
      "name": "Saras Analytics",
      "type": "grid"
    },
    {
      "id": "viw930AC4SY4AE6Ce",
      "name": "Missing Slack ID",
      "type": "grid"
    },
    {
      "id": "viwPZmF5J0B7E2T7T",
      "name": "ClickUp ID",
      "type": "grid"
    },
    {
      "id": "viwZ6MsN2PMF7BWpa",
      "name": "Missing Company Audit",
      "type": "grid"
    },
    {
      "id": "viw3go8WplLvRXr5w",
      "name": "Hubspot IDs",
      "type": "grid"
    },
    {
      "id": "viww6DhSAKvBT9xja",
      "name": "Gov't ID tracker",
      "type": "grid"
    },
    {
      "id": "viwF3rhi38zhsa9RJ",
      "name": "Lastpass users",
      "type": "grid"
    },
    {
      "id": "viwiXVIB13cSA8x7B",
      "name": "Brian's Grid",
      "type": "grid"
    },
    {
      "id": "viwz2DfZBu5IyVNAa",
      "name": "Ops view",
      "type": "grid"
    },
    {
      "id": "viwQYI9obOhzYoxeO",
      "name": "Andu's Team",
      "type": "grid"
    },
    {
      "id": "viwCgKOPlxGxgK4cZ",
      "name": "Slack Profile Update",
      "type": "grid"
    },
    {
      "id": "viwoUGbTjCUgipcQ5",
      "name": "Ratio of Strategist to Analysts",
      "type": "grid"
    },
    {
      "id": "viwFlZLtVOXKJZoOI",
      "name": "By Team",
      "type": "grid"
    },
    {
      "id": "viwjEKIIx3vXRHZQo",
      "name": "Temp-Fathom Count",
      "type": "grid"
    }
  ]
}

# Record example: 
[
  {
    "createdTime": "2023-06-13T14:29:29.000Z",
    "fields": {
      "Country": "NJ",
      "DOB": "1989-01-21",
      "Employee Tenure in Days": 4,
      "Fillout Sync": "https://forms.incrementumdigital.com/TeamDirectory?id=rec0JwqpzhCMLUcXS",
      "Full Name": "Anto Dragomir",
      "Last Date": "2020-12-01",
      "Last Modified": "2024-02-02T12:55:51.000Z",
      "Personal Email": "dragomir_anto@yahoo.com",
      "Phone": "(347) 698-8028",
      "Photo": [
        {
          "filename": "TQBV3NS4B-U01D38YN0Q6-bd7f51b9f3e6-512.png",
          "height": 512,
          "id": "att4oqjNHdvMagIpf",
          "size": 415133,
          "thumbnails": {
            "full": {
              "height": 3000,
              "url": "https://v5.airtableusercontent.com/v3/u/43/43/1754438400000/rMNzFts0_wx1Qw2HHloCmg/F2WEBTXogyB35yGHpbFVcGoOKBCn-w7h3q9Nd_J_cEyt2GZ4GlIHVwBqQVexclSo8fwkGYXfW8DRScjidu1wsGQSmYSEUiprO1kKCEDNRY9NWGtQYnhLwcHK7sXlWWwl-1QATbcOFAI8Sk9pm9DX2A/MNv8qO5QziO21Nty3wzOE4eCxElWlCEJUtW9M5CJSt0",
              "width": 3000
            },
            "large": {
              "height": 512,
              "url": "https://v5.airtableusercontent.com/v3/u/43/43/1754438400000/cZCyMXMXOZApIToyHv2yaA/MVFqORnNryCvVcg3IFy-x8H06RM6opPjlEjJXjHaZ8ZvyMXj3bSHUDlfHPJGUmDCnIFFKHd-BMnKpOmdcDq4md6xj0dyFAlwWLZwTiYdUXfzxEfbuezkwFJuG6SgdAo1_VabfwHImrkWqmiS0A1DKQ/bR2XKRSbMxVGf9fZz7YoVwFPNGrPL00YE2GszDBDycw",
              "width": 512
            },
            "small": {
              "height": 36,
              "url": "https://v5.airtableusercontent.com/v3/u/43/43/1754438400000/gYh8h1buEOJrBhNcecvKLA/RdzuY2XfyGfQFhAsB_wlhorbETib8KSYUj8tSyqItSXE3V26aMRRP1lLEemvHGPqJTyrMEeCi_IRaJ1hfvHZpytoUA0arSv4256ZOxy0HXNwrjnloHRYYkt8VtG9uggdfyXX6UGayoacOzGq9KuDzA/PsKe0RLWTLgVn2Sprtx13R2hDDk8d-AHW3cl7fncLlQ",
              "width": 36
            }
          },
          "type": "image/png",
          "url": "https://v5.airtableusercontent.com/v3/u/43/43/1754438400000/WBqJWdSjbvcoAhY0Tc9dIQ/fOn28NgVyeHkdgMzj757J9DhZ9Dkk1cHTCwDq49iGbyCjAdxQPLMkm2XCdkCWdXJ-qv2YFqxyOWs9X69sKGwdmSk9RcZSSLTUN8hoGAePE8IAWaAik3p95C8AgAZ0slQfrODN_aoi7vWi273DffMoJoCzZDIEtBAN5VjGibMFLk_BwyCaogJ8geFSfHMemtr/BD70L6bkfJ3-feqgP9BYCpZmLHo2pH3z9lar0kBqZBI",
          "width": 512
        }
      ],
      "Record ID": "rec0JwqpzhCMLUcXS",
      "Soft employee detail link": "https://incrementumportal.softr.app/team-directory-detail?recordId=rec0JwqpzhCMLUcXS",
      "Start date": "2020-10-25",
      "Status": "Dismissed",
      "TF Submission": "https://incrementum-digital.typeform.com/to/HiXCKG74#fname=Anto&airtableid=rec0JwqpzhCMLUcXS"
    },
    "id": "rec0JwqpzhCMLUcXS"
  }
]