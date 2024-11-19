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
   - Enterprise Risk Management Framework (ERMF) | True | A formalized framework guiding risk management activities (framework).
   - Chief Financial Officer (CFO) | True | A key role responsible for overseeing risk governance (person).
   - Board | True | A governing entity with ultimate responsibility for risk oversight (organization).

2. Paragraph: "The GRC system tracks incidents and action plans to address risks identified by the Divisional Risk Committees."
   Output:
   - GRC system | True | A tool for documenting and monitoring risks (system).
   - Action Plans | True | Processes developed to manage identified risks (process).
   - Divisional Risk Committees | True | Governance groups addressing division-specific risks (committee).

Bad Examples:
1. Paragraph: "The ERMF was last reviewed in November 2023."
   Incorrect Output:
   - November 2023 | True | A review date (location).
   Correction: November 2023 is not an entity; dates are excluded as per the guidelines.

2. Paragraph: "The Three Lines of Defence model is core to our risk management strategy."
   Incorrect Output:
   - Defence | True | A methodology for protecting systems (concept).
   Correction: "Defence" alone is not an entity. The correct entity is "Three Lines of Defence model" (framework).

Input Paragraph:
{input_paragraph}

Task:
Extract a list of entities from the provided paragraph following the examples above. Provide explanations for why each item is or is not an entity, as shown in the good examples. Return only the valid entity names as a list of strings in the final output.

Output Format:
["Entity 1", "Entity 2", "Entity 3", ...]
"""
