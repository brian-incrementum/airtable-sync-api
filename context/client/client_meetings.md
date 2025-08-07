# Metadata
Base ID: app36dpFPr84hM8TN
Table: Client Meetings
Table ID: tblV3ZIKJfdYcUuSG

# Schema (fields i want to keep)
{
  "fields": [
    {
      "id": "fldvYdL9fBRLIERkl",
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
      "id": "fldLC5R3sM0szwvE3",
      "name": "Submitter",
      "options": {
        "inverseLinkFieldId": "fldg1S5dbKgkS7GS6",
        "isReversed": false,
        "linkedTableId": "tbl2t9Ylc9kM7cfUG",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldbPlcIdkGhcyEuK",
      "name": "Accounts",
      "options": {
        "inverseLinkFieldId": "fldUbeHknNE79aUF1",
        "isReversed": false,
        "linkedTableId": "tblLb0ek0O4HiB3OY",
        "prefersSingleRecordLink": true
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldRCnsurkaUIaUz7",
      "name": "Meeting Date",
      "options": {
        "dateFormat": {
          "format": "l",
          "name": "local"
        }
      },
      "type": "date"
    },
    {
      "id": "fldozzJpad2T4Rmng",
      "name": "Services",
      "options": {
        "inverseLinkFieldId": "fld3cHgnad3vYziNJ",
        "isReversed": false,
        "linkedTableId": "tblTYmxXucxldO4Md",
        "prefersSingleRecordLink": false
      },
      "type": "multipleRecordLinks"
    },
    {
      "id": "fldwxr20pCevWopgJ",
      "name": "Meeting Type",
      "options": {
        "choices": [
          {
            "color": "blueLight2",
            "id": "selKlaP2QM0Y5VQSL",
            "name": "Onboarding"
          },
          {
            "color": "cyanLight2",
            "id": "selESC4dJ2d8uWV8A",
            "name": "Performance"
          },
          {
            "color": "tealLight2",
            "id": "sel36EjbCMcYOiVDN",
            "name": "Other"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fldM85zFGikMVR8mQ",
      "name": "Transcript",
      "type": "multilineText"
    },
    {
      "id": "fldvdRHjcM3dKNs8u",
      "name": "Follow Up Message",
      "type": "richText"
    },
    {
      "id": "fld4PA9mLkfk0BWLr",
      "name": "Meeting Analysis",
      "type": "richText"
    },
    {
      "id": "fldBYu00pFi21krSU",
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
    },
    {
      "id": "fldNxeqocbeTKcmRS",
      "name": "Sentiment",
      "options": {
        "choices": [
          {
            "color": "greenBright",
            "id": "selG8VnCMhXqFodvq",
            "name": "Positive"
          },
          {
            "color": "blueLight2",
            "id": "selCnUHGu5paYl9PT",
            "name": "Negative"
          },
          {
            "color": "blueLight2",
            "id": "selsW6zoSGfvTbvYq",
            "name": "Neutral"
          },
          {
            "color": "blueLight2",
            "id": "selu3g0K2AtLxvmsF",
            "name": "Neutral-Positive"
          },
          {
            "color": "blueLight2",
            "id": "selBGiFkHeJHOkrRE",
            "name": "Very Positive"
          },
          {
            "color": "blueLight2",
            "id": "selglrDPNnQFALZyZ",
            "name": "Neutral to Positive"
          },
          {
            "color": "blueLight2",
            "id": "selV36ptuaKq8mSbE",
            "name": "Neutral-Negative"
          },
          {
            "color": "blueLight2",
            "id": "selSnmfgHVOPEk0QL",
            "name": "Not Applicable"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fldGIaiYt6g2kz3ir",
      "name": "Sentiment Explained",
      "type": "multilineText"
    },
    {
      "id": "fld3bcPrcSzGWd1iU",
      "name": "Risk Level",
      "options": {
        "choices": [
          {
            "color": "yellowBright",
            "id": "selHKzKOvlbAOrHNH",
            "name": "Medium"
          },
          {
            "color": "blueLight2",
            "id": "selfwd9mnBbIlmh6q",
            "name": "Low"
          },
          {
            "color": "blueLight2",
            "id": "selm6PwLkwOytclVV",
            "name": "High"
          },
          {
            "color": "blueLight2",
            "id": "sel71uBgUOzvxja3r",
            "name": "Medium-Low"
          },
          {
            "color": "blueLight2",
            "id": "sels315qUJtYvxsgg",
            "name": "Medium-High"
          },
          {
            "color": "blueLight2",
            "id": "selj4YwQDrE1vJUcJ",
            "name": "Not Applicable"
          },
          {
            "color": "blueLight2",
            "id": "selGLdo3UVmKvJkvn",
            "name": "Low-Medium"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fldPxMcmealEfeyhj",
      "name": "Risk Explained",
      "type": "multilineText"
    },
    {
      "id": "fldD4kDHh2GbTIiwm",
      "name": "Predicted Intentions",
      "options": {
        "choices": [
          {
            "color": "greenBright",
            "id": "selGpigey1ZAslCkx",
            "name": "Continue service"
          },
          {
            "color": "blueLight2",
            "id": "seleB9LyMUmaEe6zB",
            "name": "Considering alternatives"
          },
          {
            "color": "blueLight2",
            "id": "selLuPzZP95ICdtOz",
            "name": "Continue service with expanded investment"
          },
          {
            "color": "blueLight2",
            "id": "selpMvg3jszbJiqx7",
            "name": "Continue service with conditions"
          },
          {
            "color": "blueLight2",
            "id": "selsHN6XqD4x4JDsJ",
            "name": "Not Applicable - Internal Training"
          },
          {
            "color": "blueLight2",
            "id": "selMs4meVHGfdfRpo",
            "name": "Likely to terminate"
          },
          {
            "color": "blueLight2",
            "id": "sel1TmwCdJCKPywlD",
            "name": "Continue service with potential scope adjustments"
          },
          {
            "color": "blueLight2",
            "id": "selxko8jKmrbTV9Jd",
            "name": "Likely to terminate with possibility of return"
          }
        ]
      },
      "type": "singleSelect"
    },
    {
      "id": "fldG8ptayPD0PUvyJ",
      "name": "Share Link",
      "type": "url"
    },
    {
      "id": "fldwiy7DGJRDUlYho",
      "name": "Services_Text",
      "options": {
        "formula": "{fldozzJpad2T4Rmng}",
        "isValid": true,
        "referencedFieldIds": [
          "fldozzJpad2T4Rmng"
        ],
        "result": {
          "type": "singleLineText"
        }
      },
      "type": "formula"
    },
    {
      "id": "fldtkKz7mkCjRJPEK",
      "name": "Created",
      "options": {
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
      "type": "createdTime"
    }
  ],
  "id": "tblV3ZIKJfdYcUuSG",
  "name": "Client Meetings",
  "primaryFieldId": "fldvYdL9fBRLIERkl",
  "views": [
    {
      "id": "viwvWae5ofKIRQEan",
      "name": "All",
      "type": "grid"
    },
    {
      "id": "viwAXboUCsQ8feEKo",
      "name": "All copy",
      "type": "grid"
    },
    {
      "id": "viwdydBXEWqsmfMbk",
      "name": "Temp",
      "type": "grid"
    },
    {
      "id": "viw5JRg3yCASQYOPr",
      "name": "Concerns",
      "type": "grid"
    },
    {
      "id": "viwQ9YZSW05pKvEBi",
      "name": "Process to Hubspot",
      "type": "grid"
    }
  ]
}
# Sample record JSON
[
  {
    "createdTime": "2025-04-03T16:12:18.000Z",
    "fields": {
      "Account_Text": "Naturtint USA",
      "Accounts": [
        "rec2OlZ6sGMWXmq0h"
      ],
      "Created": "2025-04-03T16:12:18.000Z",
      "Follow Up Message": "# Meeting Summary: Naturtint x Incrementum Digital\n**Date: April 03, 2023**\n\nDear Daniel,\n\nThank you for today's productive meeting. Here's a comprehensive summary of our discussion and next steps:\n\n## Performance Overview\n- Year-to-date performance shows an 18% increase in business growth\n- Current BSR (Best Sellers Rank) maintaining strong at 6\n- Market share and VSR (Vendor Sell-Through Rate) remain stable and meeting targets\n\n## Strategic Initiatives\n### Promotional Strategy\n- Resuming branded telepromotions post-Spring Sale\n- Implementing 20% off promotion targeting:\n- Brand Card Abandoners (78,000 potential customers)\n- High-potential new customers (45,000 audience size)\n- Additional cart abandoners and wishlist saves from last 60 days\n\n### New Product Launch Update\n- Currently addressing Amazon's sealing requirements\n- Two warehouse samples sent for evaluation in Ohio\n- Estimated timeline: Approximately one month for completion\n- We'll prepare for product setup once sealing process is finalized\n\n## Next Steps\n1. Our team will continue monitoring performance metrics while maintaining current budget efficiency\n2. We'll proceed with the planned promotional campaigns once Spring Sale concludes\n3. You'll keep us updated on the product sealing process for the new launch\n\nPlease let us know if you need any clarification or have additional questions. We're here to support your continued growth on Amazon.\n\nBest regards,\nThe Incrementum Digital Team\n",
      "Last Modified": "2025-04-03T16:13:46.000Z",
      "Meeting Analysis": "Attendees:\n- Daniel Hodous (Client - Naturtint USA)\n- Ahmed Sandeer (Incrementum Digital)\n- Usama Shahid (Incrementum Digital)\n\nMain Topics Discussed:\n1. Budget management and performance metrics\n2. Current VSR and market share performance\n3. Amazon SAS4 representative relationship\n4. Brand Card Abandoners targeting strategy\n5. Business performance (18% growth YoY)\n6. New product launch delays due to sealing requirements\n\nKey Decisions:\n1. Continue with 20% off promotions for targeted audiences\n2. Resume branded telepromotions after Spring Sale\n3. Maintain current strategy given positive performance metrics\n\nAction Items:\n1. Email introduction of Incrementum team to Amazon SAS4 rep\n2. Implement promotions for Brand Card Abandoners (78K audience)\n3. Target potential new customers (45K audience)\n4. Wait for update on new product sealing (ETA: 1 month)\n\nFollow-up Required:\n1. Monitor new product sealing process\n2. Implementation of promotional campaigns post-Spring Sale\n",
      "Meeting Date": "2025-04-03",
      "Meeting Type": "Performance",
      "Merged Hubspot ID (from Accounts)": [
        "18001521511"
      ],
      "Predicted Intentions": "Continue service",
      "Record ID": "rec00Gjq0WRPTzqii",
      "Risk Explained": "No significant concerns raised about service quality. Budget limitations are discussed pragmatically rather than as complaints. Client appears stable and committed to the relationship with clear future planning.",
      "Risk Level": "Low",
      "Sentiment": "Positive",
      "Sentiment Explained": "Client demonstrates strong trust in the agency, explicitly stating preference over Amazon representatives. Shows satisfaction with performance (18% growth), actively engages in strategic planning, and maintains collaborative communication throughout.",
      "Services": [
        "reccQKTDSYeOYv47x"
      ],
      "Services_Text": "Amazon Advertising",
      "Share Link": "https://fathom.video/calls/266773134?tab=summary",
      "Slack ID (from Submitter)": [
        "U04GJ2Z6GQL"
      ],
      "Submitter": [
        "reckTROfD2svxj6ic"
      ],
      "Team (Submitter)": [
        "Team Haider"
      ],
      "Transcript": "Naturtint x Incrementum Digital - April 03\nVIEW RECORDING - 14 mins (No highlights): https://fathom.video/share/_t4xrxbiuGzj9mE1PmyTci1p5u5VG8ut\n\n---\n\n0:00 - Daniel Hodous (Naturtint USA)\n  you can distribute the same results in home. you\n\n1:18 - Ahmed Sandeer\n  But we are looking into it, just want to bring this to new light, we are here to just make sure anything that is aligned with our goals, our strategy, know we have a limitation, budget limitation within our budget, that just you know we see okay this is going to convert, well this is going to be efficient and you know in anything that is  And anything that is just, you know, increasing budgets. We know a lot of campaigns. We know good performing targets going out of budget, but yeah, we have to remain in our tax costs and everything.  As we are not losing our VSR, we are fine.\n\n9:15 - Daniel Hodous (Naturtint USA)\n  We're not losing market share, we are fine.\n\n9:18 - Ahmed Sandeer\n  So just wanted to give you this information that we are, and just taking any suggestions that is risky, like, okay, it's profitable in the long term or helpful for us in our goals.  take those suggestions and others. I think we're on the same page. I like having a wrap. I'm glad that we found these people.  They're great for answering questions, they're great for troubleshooting, but yeah, they're all incentivized to get their contacts to spend more money because they work for Amazon, and that's how they make money.  So when it comes to actually strategizing, I trust you guys a lot more than I trust anyone in Amazon.\n  ACTION ITEM: Email intro Incrementum team to Amazon SAS4 rep for deals/advice - WATCH: https://fathom.video/share/_t4xrxbiuGzj9mE1PmyTci1p5u5VG8ut?timestamp=617.9999  They just won't. They just won't. But yeah, it's good there there. Anything will be like, okay, any information that we can not access.  They provide definitely will get their help on the side. And you mentioned this, the other wrap, your SaaS4 app.  Maybe you can share any email, you know, introducing us. Maybe we can ask some question regarding the deals and, you know, some of those advice I want to get from him.  Yes, she sends a lot of information, a lot of charts, a lot of things that are not accessible to anybody other than her, things that we can access is solar central.\n\n11:03 - Daniel Hodous (Naturtint USA)\n  So, yeah, I think I'll start with the other sessions. Yeah. On the instance, maybe even with that extra sale last year.  Yes, exactly.\n\n11:22 - Ahmed Sandeer\n  We did have this this year. So again, we're still doing better. So yeah, hopefully, yeah, it looks like we are in the right track and we make sure we keep this momentum going and we have a good higher year this year.  And moving on, so we discussed, first, we were not, you know, branded telepromotions were not active and we discussed, we will do that after the spring sale.  So, we will continue. with this, with this promotion that we were doing with the 20% off, with the Brand Card Abendenters and high potential new customers.  And just let's see quickly how much Brand Card Abendenters we have for the last 90 days. 77,000 audience size, almost 78,000 audience size we have.  We can target these audience. Card Abendenters and 33,000 potential new customers and 12,000. This also comes under potential new customers who have added to cart or save list, save for later on the wishlist in the last 60 days, but haven't purchased, but did not purchase in the last one year.  So yeah, definitely these two segments, almost like 45,000 audience size for new customers and Also, this also brings in new customers as well, brand partners.\n\n11:04 - Daniel Hodous (Naturtint USA)\n  Yeah, that Cardaben is used to really well for us, but you definitely want to get all three of these audiences, often in the 20% off and see what happens, and then they've all been working for us.  Yeah, exactly.\n\n11:21 - Ahmed Sandeer\n  yeah, we were waiting for Spring Summer Sales to end, Spring Sales to end, so now we will turn this back on.  We are back with our response, we won't sure, we will continue to do that. Also we are putting our BSR, making sure we are not losing our ranks, so we have six right now.\n\n11:55 - Daniel Hodous (Naturtint USA)\n  Oh, that's great.\n\n11:57 - Ahmed Sandeer\n  So, yeah, this is also, yeah, please.\n\n12:02 - Daniel Hodous (Naturtint USA)\n  and everything is fine and yeah about can you guys hear me yeah I was looking at the business report we are up by 18 percent this year yeah we just awesome yeah that's great and any update Daniel's about the new products so I think I told you that they didn't they came in without the seals in Amazon requires it so we're working trying to find a warehouse close by to us in Ohio that will steal them for us we've sent some samples to two different warehouses we're waiting to hear back  Once they, once we get that set up, we will have to send them all reports, have them seal it, have to send them all back to us, so it's going to take a while.  I think I'm going take a while. At least a month. Okay, so a month. Okay, yeah, that's what I was going to ask.  Okay, awesome. Okay, let's go take some time.\n\n13:21 - Ahmed Sandeer\n  Okay, awesome, Let us know if let us know.\n\n13:34 - Daniel Hodous (Naturtint USA)\n  Yeah, absolutely. I'm going to charge you guys when we're ready to set those up, those products up. Sure, sure.\n\n13:43 - Usama Shahid (Incrementum Digital)\n  Sure, sure.\n\n13:45 - Ahmed Sandeer\n  Okay, Daniel, thank you. Thank you for your time. All right, thank you guys.\n\n13:49 - Daniel Hodous (Naturtint USA)\n  Everything's looking great. appreciate it. Thank you.\n\n13:52 - Ahmed Sandeer\n  Let us know if anything"
    },
    "id": "rec00Gjq0WRPTzqii"
  }
]