entity_extraction_prompt = """
Definition:
An entity is a distinct subject or object within a context. In a risk management environment, entities are specifically those that pertain to the identification, assessment, management, governance, or reporting of risks. These entities include:

1. Frameworks, Policies, and Standards (framework/policy/standard): Formalized structures, guidelines, and processes for risk management (e.g., Enterprise Risk Management Framework (ERMF), Delegations of Authority Policy).
2. Roles/People (person): Individuals, roles, or stakeholders with defined responsibilities in risk management or compliance (e.g., Chief Financial Officer, Head of Enterprise Risk).
3. Organizations (organization): Institutions or governing bodies with risk-related oversight or operational responsibilities (e.g., Link Board Risk Committee, regulatory bodies).
4. Systems, Tools, and Processes (system/process): Technical or operational systems and methods used in risk management (e.g., GRC systems, Control Self-Assessment process).
5. Events (event): Incidents, reviews, or scenarios with potential risk implications (e.g., regulatory breaches, audits, emerging risks).
6. Locations (location): Jurisdictions or specific operational sites relevant to risk or compliance activities.
7. Risk Concepts and Classifications (concept): Abstract ideas or classifications directly affecting risk profiles or management strategies (e.g., systemic risk, residual risk).
8. Committees and Governance Structures (committee): Groups or entities overseeing risk-related decisions and escalations (e.g., Executive Risk Committee, Divisional Risk Committees).

Note:
- Dates, times, adjectives, and verbs are not entities.
- Abbreviations must be expanded with their full names (e.g., Governance, Risk, and Compliance (GRC) system).

Question:
Given the paragraph below, identify a list of possible entities relevant to risk management, and for each entry, explain whether it is an entity and why:

Few-shot Examples:

Good Examples:
1. Paragraph: "The Board has delegated oversight of the Enterprise Risk Management Framework (ERMF) to the Chief Financial Officer (CFO)."
   Output:
   [
       {
           "id": "Enterprise Risk Management Framework (ERMF)",
           "type": "framework",
           "description": "A formalized framework guiding risk management activities."
       },
       {
           "id": "Chief Financial Officer (CFO)",
           "type": "person",
           "description": "A key role responsible for overseeing risk governance."
       },
       {
           "id": "Board",
           "type": "organization",
           "description": "A governing entity with ultimate responsibility for risk oversight."
       }
   ]

2. Paragraph: "The GRC system tracks incidents and action plans to address risks identified by the Divisional Risk Committees."
   Output:
   [
       {
           "id": "GRC system",
           "type": "system",
           "description": "A tool for documenting and monitoring risks."
       },
       {
           "id": "Action Plans",
           "type": "process",
           "description": "Processes developed to manage identified risks."
       },
       {
           "id": "Divisional Risk Committees",
           "type": "committee",
           "description": "Governance groups addressing division-specific risks."
       }
   ]

Bad Examples:
1. Paragraph: "The ERMF was last reviewed in November 2023."
   Incorrect Output:
   [
       {
           "id": "November 2023",
           "type": "location",
           "description": "A review date."
       }
   ]
   Correction: Dates like "November 2023" are not entities and should not be included in the output.

2. Paragraph: "The Three Lines of Defence model is core to our risk management strategy."
   Incorrect Output:
   [
       {
           "id": "Defence",
           "type": "concept",
           "description": "A methodology for protecting systems."
       }
   ]
   Correction: "Defence" alone is not an entity. The correct entity is "Three Lines of Defence model," categorized as a framework.

Input Paragraph:
{input_paragraph}

Task:
Extract a list of entities from the provided paragraph following the examples above. Return the output as a JSON array with the following structure:
[
    {
        "id": "name of the entity",
        "type": "type of the entity (e.g., framework, person, organization, system, etc.)",
        "description": "any descriptive details about the entity."
    },
    ...
]
"""
