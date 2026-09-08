# OpenAI Preparedness Framework, Version 2 (15 April 2025): revision account

Predecessor: Preparedness Framework (Beta), 18 December 2023. Two provider accounts exist and are copied verbatim below. No version-history web page, redline PDF or other account was found (checked: openai.com/safety/preparedness and openai.com/preparedness via Wayback; the v2 PDF; the announcement post; METR /fsp list per recon).

## 1. In-document changelog: Appendix A 'Change log'
Source: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf , original 15 April 2025 file, Wayback capture 20250415191354 (https://web.archive.org/web/20250415191354id_/https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf). Section heading: 'A Change log' (Appendix A). PDF pages 15-16 (printed page numbers 14-15). Items 1-11 are on PDF page 15 (printed 14); item 12 is on PDF page 16 (printed 15). The text below is identical in the silently re-uploaded file (Wayback 20250611025204 onward). Line breaks follow the PDF extraction.

```
## A
## Change log

In this version of the Preparedness Framework, we make a number of updates, designed to reflect what
we’ve learned and update our safety and governance process for the next generations of highly capable
models. Key changes include that we:

1. Clarify the relationship among capabilities, risks and safeguards. In our updated framework, we
make clear that we use a holistic process to decide which areas of frontier AI capability to track,
and to define threshold levels of those capabilities that are associated with meaningful increases in
risk of severe harm. We describe how we develop and maintain threat models that identify these
severe risks, and how we evaluate model capabilities and build and test safeguards that sufficiently
minimize the associated risks. We make clear that safeguards can take a variety of forms, and that
reducing risk generally does not require reducing capability.

2. Define how High and Critical capability thresholds relate to underlying risks. High capability
thresholds mean capabilities that significantly increase existing risk vectors for severe harm under
the relevant threat model. Critical capability thresholds mean capabilities that present a meaningful
risk of a qualitatively new threat vector for severe harm with no ready precedent under the relevant
threat model. Also, we are removing terms “low” and “medium” from the Framework, because
those levels were not operationally involved in the execution of our Preparedness work.

3. Give specific criteria for which capabilities we track. We track capabilities that create risks meeting
five criteria – they are plausible, measurable, severe, net new, and instantaneous or irremediable.

4. Update the Tracked Categories of frontier capability accordingly, focusing on biological and
chemical capability, cybersecurity, and AI self-improvement. Going forward we will handle risks
related to persuasion outside the Preparedness Framework, including via our Model Spec and
policy prohibitions on the use of our tools for political campaigning or lobbying, and our ongoing
investigations of misuse of our products (including detecting and disrupting influence operations).
We are moving Nuclear and Radiological capabilities into Research Categories.

5. Introduce Research Categories, areas of capability that do not meet the criteria to be Tracked
Categories, but where we believe additional work is needed now. For these areas, in collaboration
with external experts, we commit to further developing the associated threat models and advancing
the science of capability measurement for the area, including by investing in the development of
rigorous capability evaluations. These include Long-range Autonomy, Sandbagging, Autonomous
Replication and Adaptation, Undermining Safeguards, and Nuclear and Radiological.

6. Provide more detail on our capability elicitation approach, making clear that we will consider a
range of techniques in order to test a model version that approximates the high end of expected elici-
tation by threat actors attempting to misuse the model. We also define “scalable evaluations,” which
are automated, and distinguish these from “deep dive” evaluations that may include consultation
with human experts and are designed in part to validate the scalable evaluations.

7. Provide risk-specific safeguard guidelines. This information gives more detail on how we expect
to safely develop and deploy models advanced enough to pose severe risks in tracked capability
areas. As we move toward increasingly capable models, we are planning for safeguards that will be
tailored to the specific risks they are intended to address.

8. Establish Capabilities Reports and Safeguards Reports, the key artifacts we use to support
informed decision-making under the Preparedness Framework in the context of systems that are
capable enough to pose severe risks.

9. Clarify approach to establishing safeguard efficacy, moving beyond the flawed approach of re-
running capability evaluations on the safeguarded model and towards a more thorough assessment
of each safeguard and its efficacy (Section 4.1).

10. Deprioritize safety drills, as we are shifting our attention to a more durable approach of continu-
ously red-teaming and assessing the effectiveness of our safeguards.

11. Clarify our focus on marginal risk, including the context of other systems available on the market,
and outline our approach for maintaining responsible safeguards and reinforcing responsible
practices across the industry if another actor releases a system we would assess as having High or
Critical capability.

14


[[page 16]]

12. Clarify the governance process. Our Safety Advisory Group oversees the effective design, imple-
mentation, and adherence to the Preparedness Framework, in partnership with safety leaders in
the company. For covered launches, SAG assesses residual risk in tracked areas, net of safeguards,
and makes expert recommendations on safeguard adequacy and deployment decision-making to
OpenAI leadership.
```

## 2. Announcement post: 'Our updated Preparedness Framework'
Source: https://openai.com/index/updating-our-preparedness-framework/ , dated April 15, 2025; read via Wayback capture 20250416173732 (https://web.archive.org/web/20250416173732id_/https://openai.com/index/updating-our-preparedness-framework/). openai.com returns HTTP 403 to this sandbox so the live page was not read. Full post text verbatim (html_to_text() extraction; site navigation header lines and the footer tags '2025 / Ethics & Safety / Framework / Author' are omitted; the strings '(opens in a new window)' are the page's own link labels; on the page the three paragraphs beginning 'Tracked Categories:', 'Research Categories:' and 'Persuasion risks' are nested bullets inside the 'Sharper capability categories' item, and the extraction rendered them inside that item's text, so they appear once below within that item):

April 15, 2025
## Our updated Preparedness Framework
Sharing our updated framework for measuring and protecting against severe harm from frontier AI capabilities.
We’re releasing an update to our Preparedness Framework, our process for tracking and preparing for advanced AI capabilities that could introduce new risks of severe harm. As our models continue to get more capable ⁠ , safety will increasingly depend on having the right real-world safeguards in place.
This update introduces a sharper focus on the specific risks that matter most, stronger requirements for what it means to “sufficiently minimize” those risks in practice, and clearer operational guidance on how we evaluate, govern, and disclose our safeguards. Additionally, we introduce future-facing research categories that allow us to remain at the forefront of understanding emerging capabilities to keep pace with where the technology is headed. We will continue investing deeply in this process by making our preparedness work more actionable, rigorous, and transparent as the technology advances.
We’ve learned a great deal from our own testing, insights from external experts, and lessons from the field. This update reflects that progress. In line with our core safety principles ⁠ , it makes targeted improvements that include:
Clear criteria for prioritizing high-risk capabilities. We use a structured risk assessment process to evaluate whether a frontier capability could lead to severe harm and we assign it to a category based on defined criteria. We track capabilities that meet five key criteria that make it a priority for us to prepare in advance: the risk should be plausible, measurable, severe, net new, and instantaneous or irremediable. We measure progress on these capabilities, and build safeguards against the risks that these capabilities create.
Sharper capability categories. We've updated our categorization of capabilities to apply these criteria and reflect our current understanding. Tracked Categories: These are established areas where we have mature evaluations and ongoing safeguards. They are Biological and Chemical capabilities, Cybersecurity capabilities, and AI Self-improvement capabilities. We continue to believe some of the most transformative benefits from AI will come from its use in science, engineering, and research - including from capabilities in our Tracked Categories. Investing early in both measurement and safeguards for these dual-use categories will enable us to safely unlock the benefits we anticipate from their use. Research Categories: We’re introducing a set of Research Categories of capability, which are areas that could pose risks of severe harm, that do not yet meet our criteria to be Tracked Categories. We’re working to develop threat models and advanced capability evaluations for these. Current focus areas include Long-range Autonomy, Sandbagging (intentionally underperforming), Autonomous Replication and Adaptation, Undermining Safeguards, and Nuclear and Radiological. Persuasion risks will be handled outside the Preparedness Framework, including via our Model Spec, restricting the use of our tools for political campaigning or lobbying, and our ongoing investigations into misuse of our products (including detecting and disrupting influence operations ⁠ (opens in a new window) ).
Clarified capability levels. We’ve streamlined levels to two clear thresholds that map to specific operational commitments: High capability, which could amplify existing pathways to severe harm, and Critical capability, which could introduce unprecedented new pathways to severe harm. Covered systems that reach High capability must have safeguards that sufficiently minimize the associated risk of severe harm before they are deployed. Systems that reach Critical capability also require safeguards that sufficiently minimize associated risks during development. The Safety Advisory Group (SAG), a cross-functional team of internal safety leaders, reviews whether safeguards sufficiently minimize severe risk and makes targeted recommendations, ranging from approving deployment to requesting further evaluation or stronger protections. Their guidance goes to OpenAI Leadership for final decisions, with an ongoing commitment to reassess safeguards if new evidence emerges.
Scalable evaluations to support more frequent testing. Advances in reasoning allow us to improve models more frequently and sometimes without major new training runs. This means evaluations must be able to scale, too. We’ve built a growing suite of automated evaluations that can keep up with this faster cadence, while also continuing to do expert-led “deep dives” to ensure the scalable evaluations are measuring the right things.
Responding to shifts in the frontier landscape. If another frontier AI developer releases a high-risk system without comparable safeguards, we may adjust our requirements. However, we would first rigorously confirm that the risk landscape has actually changed, publicly acknowledge that we are making an adjustment, assess that the adjustment does not meaningfully increase the overall risk of severe harm, and still keep safeguards at a level more protective.
Defined Safeguards Reports. We’ve focused on producing Capabilities Reports (formerly known as the “Preparedness Scorecard”), which assess whether a model has crossed a threshold that poses risks. We’re now adding more detail about how we’ll design strong safeguards and verify their effectiveness in dedicated Safeguards Reports, consistent with our principle of defense in depth ⁠ , which will guide deployment decisions. SAG reviews both reports, assesses residual risk, and makes recommendations to OpenAI Leadership on whether it’s safe enough to deploy.
We’ll continue to publish our Preparedness findings with each frontier model release, just as we’ve done for GPT‑4o ⁠ , OpenAI o1 ⁠ , Operator ⁠ , o3‑mini ⁠ , deep research ⁠ , and GPT‑4.5 ⁠ , and share new benchmarks to support broader safety efforts across the field.
We’re deeply grateful to internal teams, external researchers and industry peers who’ve contributed invaluable insights to this latest update. The Preparedness Framework remains a living document, and we expect to continue updating it as we learn more.
