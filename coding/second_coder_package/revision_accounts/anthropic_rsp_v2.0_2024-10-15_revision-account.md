# Anthropic Responsible Scaling Policy v2.0 (effective October 15, 2024): revision account

Predecessor: v1.0 (September 19, 2023).

## Version-history entry, RSP page
Note: this entry ('Planned ASL-3 Safeguards', 'Planned Capability Assessments', 'Learning from Experience') describes safeguard plans and shortfalls under v1.0; it is not itself a change summary. It is the only entry dated October 15, 2024 on the page.
Source: https://www.anthropic.com/responsible-scaling-policy (live, fetched 2026-09-02; page states 'Last updated Aug 14, 2026'). Heading and text verbatim:

```
## October 15, 2024
## Planned ASL-3 Safeguards
In our Responsible Scaling Policy, reaching certain Capability Thresholds requires us to upgrade our safeguards to the ASL-3 Security Standard or the ASL-3 Deployment Standard. Our RSP contains requirements for meeting these standards, and also says we will publicly release key information related to the evaluation and deployment of our models (not including sensitive details). Below, we give non-binding descriptions of our future ASL-3 safeguard plans. We hope sharing these plans will offer useful insights for organizations working on similar systems, and contribute to conversations about emerging best practices.
## Deployment Safeguards
Our teams are currently developing and building ASL-3 Deployment Safeguards to mitigate catastrophic risks associated with more advanced models. These safeguards are being designed to prevent misuse of capabilities that could enable severe harm, particularly in relation to chemical, biological, radiological, and nuclear (CBRN) technologies. This overview outlines the planned technical architecture and design of these safeguards, with a focus on the technical aspects and safety considerations of this developing system.
Multi-layered defense-in-depth architecture
Our deployment safeguards will employ a defense-in-depth strategy with four main layers, each designed to catch potential misuse that might pass through previous barriers. The four layers will be:
Access controls to tailor safeguards to the deployment context and group of expected users.
Real-time prompt and completion classifiers and completion interventions for immediate online filtering.
Asynchronous monitoring classifiers for a more detailed analysis of the completions for threats.
Post-hoc jailbreak detection with rapid response procedures to quickly address any threats.
Access controls
General access to AI models (e.g. Claude.ai and our API) will use our standard safeguards. However, we recognize that in certain cases, such as safety testing, it may be necessary to tailor these safeguards. To balance security concerns with the need for flexibility, we are developing a tiered access system that allows for nuanced control over safeguard adjustments. At the core of this system will be an enhanced due diligence process under which we will evaluate potential partners based on two key criteria: their overall trustworthiness and the beneficial nature of their use-case. This vetting process will act as a compensating control when a partner’s use-case requires adjusting the standard deployment of our safeguards.
Real-time prompt and completion classifiers
Our online prompt and completion classifiers are machine learning models that will analyze user inputs and AI-generated outputs in real-time. The completion classifiers will use a streaming implementation, whereby the classifier updates the score as tokens are generated, rather than waiting for the entire completion. This approach aims to minimize delays to the end user while maintaining the safety standards.
In order to stay up to date on newly discovered harmful patterns, jailbreaks, and obfuscation techniques, the classifiers will be regularly updated using data from other elements of our deployment safeguards including our asynchronous monitoring system and insights from our incident response protocol, bug bounty program, and internal and external red-teaming efforts.
Asynchronous monitoring classifiers
Asynchronous classification will allow us to perform computationally intensive evaluations to provide a deeper level of scrutiny than the real-time classifiers alone, without impacting user-facing latency.
To allow for flexible monitoring processes, our monitoring system will be organized like a flowchart. One implementation could start with simpler AI models like Claude 3 Haiku to quickly and economically scan content and trigger a detailed analysis with an advanced model like Claude 3.5 Sonnet if anything suspicious is found. This setup will be designed to be adapted and updated easily to respond to new threats by adding new AI models or analysis steps.
Post-hoc jailbreak detection
Our jailbreak rapid response procedures will be designed to identify and mitigate attempts to bypass the sets of safety measures described above.
A new jailbreak could be detected by the asynchronous classifiers or through the bug-bounty program. The rapid-response protocol will involve mitigating the impact of the jailbreak by initiating patching. In an instance where a jailbreak patch is unable to be immediately implemented, we will maintain the capability to adjust the model’s prompting to reinforce safety constraints. For edge cases or situations requiring human judgment, there will be protocols for escalation to human reviewers.
Our process for minimizing jailbreak risks will include rapid retraining, validation, and testing of classifiers against newly discovered patterns and real-world scenarios. The effectiveness of jailbreak detection and response will be enhanced by collaboration and information sharing. To this end, we are developing a rapid response process for sharing threat intelligence with relevant partners.
Ongoing work
By implementing multiple defense layers, from real-time classifiers to asynchronous monitoring and rapid response systems, we hope to create a deployment safeguards infrastructure that is adaptable to various deployment scenarios.
The success of this system will depend on the integration and improvement of individual components. As implementation of these safeguards progresses, new challenges and opportunities for innovation in AI safety are likely to emerge. Ongoing research into areas such as balancing security and model utility, improving scalability and performance, enhancing adversarial robustness, and maintaining cross-platform consistency will be crucial in addressing these challenges.
## Security Safeguards
The following sections outline the key security controls we plan to implement as part of our ASL-3 safeguards. Many of these security measures are already in place and are dedicated to enhancing our existing ASL-2 controls. In presenting this information, we have carefully balanced the need for transparency with the imperative to protect sensitive security details. As such, this overview provides a high-level description of our planned controls, offering insight into our security approach without compromising our defenses against potential threats.
Access management and compartmentalization: Implement multiple clearance levels, data classification, and granular, per-role permission sets to govern employee access to sensitive assets and data including training techniques and hyperparameters. Use multi-tier compartmentalization controls based on asset type to limit blast radius from attacks and reduce insider risk. Educate employees on insider risk and establish a structured insider threat program to incentivize risk reporting.
Researcher tooling security: Enhance usability and security of research tools by preventing unnecessary access and limiting user privileges to only what is essential. Provide robust, user-friendly tooling without direct access to model weights.
Software inventory management: Create a comprehensive software inventory list through automated scanning. Implement strict software inventory management to track all software components used in development and deployment. Regularly monitor inventory to effectively manage risks and maintain a secure environment.
Software supply chain security: Monitor publicly known critical security issues in third-party dependencies. Conduct consistent scanning of all third-party dependencies and maintain a comprehensive vulnerability data repository. Proactively scan all incoming packages to enable download of only secure packages and reduce risk of introducing vulnerabilities.
Artifact integrity and provenance: Leverage frameworks (e.g., SLSA) to improve security controls for software build and deployment. Require packages to have provenance metadata.
Binary authorization for endpoints: Enforce binary authorization on every endpoint to allow only trusted, approved software to run. Follow a strict process for approving any software that needs local installation on machines. Use centrally managed execution policies to prevent unauthorized or malicious code. Limit attacker actions through strict security policies and detailed logging for swift incident detection and response.
Endpoint patching: Use device management software (e.g., Mobile Device Management) to update all devices to the latest, most secure OS and software versions. Monitor for publicly disclosed vulnerabilities in third-party software and quickly deploy patches or mitigate risks. Restrict access for devices that fall behind on critical updates until patches are applied. Implement automated patching processes to close any manual oversight gaps.
Hardware procurement: Source employee endpoints directly from vetted manufacturers for secure chain of custody. Maintain a curated list of approved, recommended hardware and peripherals and provide employees with securely sourced peripherals.
Executive Risk Council: Establish an Executive Risk Council sponsored by executive leadership to oversee security programs. Follow a risk-based approach aligned with ISO 27001 standard. Perform periodic reviews to assess our security program's adherence to obligations deriving appropriately from both internal factors (e.g., adopted industry practices, contractual commitments, internal policies) and appropriate external factors (e.g., regulations and statutes).
Access control for model weights: Implement multi-party authorization and mandatory code review on production code to remove persistent, high-privilege access to model weights. Grant temporary access and only via the smallest set of necessary permissions to reduce risk of weights exfiltration. Require hardware authentication device prompt, justification and employee approval to grant access.
Infrastructure policy: Require all new production infrastructure to be defined in Infrastructure As Code (IaC) before promotion to production environments. Require infrastructure changes be reviewed by the Security team.
Cloud security posture management: Reduce risk of compromise due to cloud misconfiguration by defining and implementing internal standards and best practices. Conduct regular audits of cloud environments and promptly remediate any identified gaps.
Red teaming and penetration testing: Partner with a diverse range of external red team and penetration testing experts. Simulate sophisticated attacks, including insider threat and software supply chain compromise scenarios, to identify vulnerabilities. Build an in-house security team with wide-ranging expertise, including APT defense, insider risk, incident response, and secure design.
Centralized log management and analysis: Centralize storage of major security-centric log sources in a SIEM/SOAR platform. Enable manual and automated analysis, log retention, rule creation and execution for detections and response workflows. Implement orchestration and response playbooks for automated alert investigation. Use a casebook workflow for security analysts to manage incidents.
Access monitoring for critical assets: Conduct manual monitoring of access to model weights and high value IP, including recurring automated detections. Build automated detection across all major log sources for access to critical assets. Leverage additional threat intelligence to continuously improve detections.
Deception technology: Install and monitor honeypots (including fake model weights) for high precision detection of unauthorized system access. Implement deception technology in a realistic way to trick attackers and gain insights into their tactics.
Physical security: Conduct regular Technical Surveillance Countermeasures (TSCM) at physical spaces using advanced detection equipment and techniques. Tailor TSCM sweeps to specific events, threats or incidents that may trigger an inspection. Regularly sweep physical premises for intruders and conduct physical security red-teaming
## Planned Capability Assessments
We plan to publish additional details on our capability assessment methodology in the near future. For information about our past capability assessments, please see our overviews for Claude 3.0 Opus and Claude 3.5 Sonnet .
## Learning from Experience
We have learned a lot in our first year with the previous RSP in effect, and are using this update as an opportunity to reflect on what has worked well and what makes sense to update in the policy. As part of this, we reviewed how well we adhered to the framework and identified a small number of instances where we fell short of meeting the full letter of its requirements. These areas were:
Our most recent evaluations were completed 3 days later than the 3-month interval. This delay allowed our teams to refine their capability elicitation, resulting in higher-quality evaluations. To resolve this issue, the new policy clarifies the ambiguous definition of the evaluation interval, and extends the interval to 6 months to avoid lower-quality, rushed elicitation.
In our most recent evaluations, we updated our autonomy evaluation from the specified placeholder tasks, even though an ambiguity in the previous policy could be interpreted as also requiring a policy update. We believe the updated evaluations provided a stronger assessment of the specified “tasks taking an expert 2-8 hours” benchmark. The updated policy resolves the ambiguity, and in the future we intend to proactively clarify policy ambiguities.
Some of our evaluations lacked some basic elicitation techniques such as best-of-N or chain-of-thought prompting. Our internal Capability Report discloses these limitations, and we believe the risk of substantial under-elicitation is low. We are now systematically tracking these gaps to avoid future under-elicitation.
Our evaluations in one domain were not explicitly designed to establish the 6x scaling buffer mentioned in the previous policy. Since our current techniques aren’t capable of giving confident buffer predictions, we instead relied on empirical observations and rough predictions. We believe this presents minimal risk at present, where capability improvements happen more smoothly with scale, but in the future, quantitative predictions may become necessary. We have updated the new policy to note this situation.
In all cases, we found these instances posed minimal risk to the safety of our models. From our review, we learned two valuable lessons to incorporate into our updated framework: we needed to incorporate more flexibility into our policies, and we needed to improve our process for tracking compliance with the RSP.
Since we first released the RSP a year ago, our goal has been to offer an example of a framework that others might draw inspiration from when crafting their own AI risk governance policies. We hope that proactively sharing our experiences implementing our own policy will help other companies in implementing their own risk management frameworks and contribute to the establishment of best practices across the AI ecosystem.
```

## In-document changelog entry
Source: documents/anthropic_rsp_v2.0_2024-10-15.pdf (section heading 'Changelog', PDF pages 21-22; the entry below occupies PDF page(s) 21-22, printed page number(s) 17-18; the v2.0 changelog headings carry dates only, without version labels). Text verbatim (zero-width characters removed; line breaks as extracted):

```
October 15, 2024
RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI
risks while maintaining our commitment not to train or deploy models unless we have implemented
adequate safeguards. Key improvements include new capability thresholds to indicate when we should
upgrade our safeguards, refined processes for evaluating model capabilities and the adequacy of our
safeguards (inspired by safety case methodologies), and new measures for internal governance and
external input. We describe the most notable changes below.
ASL definition changed: The term “ASL” now refers to groups of technical and operational safeguards
(it previously also referred to models). We also introduced the new concepts of Capability
Thresholds and Required Safeguards. This change allows for more targeted application of
safeguards based on specific capabilities, rather than broad model categories.
ARA threshold now a checkpoint: We replaced our previous autonomous replication and adaption
(ARA) threshold with a “checkpoint” for autonomous AI capabilities. Rather than triggering
higher safety standards automatically, reaching this checkpoint will prompt additional evaluation
of the model’s capabilities and accelerate our preparation of stronger safeguards. We previously
considered these capabilities as a trigger for increased safeguards, motivated by an attempt to
establish some threshold while we developed a better sense of potential threats. We now believe
that these capabilities - at the levels we initially considered - would not necessitate the ASL-3
standard.
AI R&D threshold added: We added a new threshold for AI systems that can significantly advance AI
development. Such capabilities could lead to rapid, unpredictable advances in AI, potentially
outpacing our ability to evaluate and address emerging risks, and may also serve as an early
warning sign for the ability to automate R&D in other domains.
Testing for Capability Thresholds: Rather than using prespecified evaluations, we now require an
affirmative case that models are sufficiently far from Capability Thresholds. Predefined tests may
miss emerging risks or be overly conservative relative to the actual threshold of concern. Our most
accurate tests change frequently enough that it is more practical to use this new approach than to
have our Board of Directors pre-approve evaluations.
Adjusted evaluation cadence: We adjusted the comprehensive assessment cadence to 4x Effective
Compute or six months of accumulated post-training enhancements (this was previously three
months). We found that a three-month cadence forced teams to prioritize conducting frequent
evaluations over more comprehensive testing and improving methodologies.
Less prescriptive evaluation methodology: We have replaced some specifics in our previous testing
methodology (e.g., using 1% of compute for elicitation or creating a 6x buffer), with more general
requirements to (a) match expected efforts of potential adversaries and (b) provide informal
estimates of how further scaling and research developments will impact model capabilities and
performance on the same tasks. We have found that specific methodologies may become outdated
Responsible Scaling Policy, Anthropic
17

[[page 22]]
when new research developments are introduced. Although still an aspirational goal, the science
of evaluations is not currently mature enough to make confident predictions about the precise
buffer we should require between current models and a Capability Threshold.
More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards
requirements to be less prescriptive and more outcome-focused. Rather than detailing specific
operational and technical safeguards, we now specify the overall security or deployment
standards and requirements for meeting them. This is to allow us to adapt our safeguards more
flexibly as our understanding of risks and possible safeguards improves.
Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of
scope for the ASL-3 Security Standard. We also removed the commitment to protect against scaled
attacks and distillation attacks from the ASL-2 Security standard. While distillation remains a
concern for more capable models, models stored under ASL-2 safeguards have not yet reached
potentially harmful Capability Thresholds.
Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment
Standard to allow for different levels of safeguards based on deployment context. For any general
access systems, we still require passing intensive red-teaming. For internal use, safety testing and
deployments to sufficiently trusted users, we will instead require a combination of access controls
and monitoring.
New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard
Reports. We expect that aggregating all the available evidence about model capabilities will
provide decision makers with a more complete picture of the overall level of risk and improve our
ability to solicit feedback on our work.
Internal and external accountability: We have made a number of changes to our previous “procedural
commitments.” These include expanding the duties of the Responsible Scaling Officer; adding
internal critique and external expert input on capability and safeguard assessments; new
procedures related to internal governance; and maintaining a public page for overviews of past
Capability and Safeguard Reports, RSP-related updates, and future plans.
Responsible Scaling Policy, Anthropic
18
```

## Announcement post
Source: https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy (live, fetched 2026-09-02; page shows date 'Oct 15, 2024'). Full post text verbatim (visible text extraction; hyperlink targets for 'here' anchors: [('here', 'https://www.anthropic.com/rsp-updates'), ('here', 'https://www.anthropic.com/rsp-updates'), ('here', 'http://anthropic.com/rsp-updates')]):

```
## Announcing our updated Responsible Scaling Policy
Today we are publishing a significant update to our Responsible Scaling Policy (RSP), the risk governance framework we use to mitigate potential catastrophic risks from frontier AI systems. This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaining our commitment not to train or deploy models unless we have implemented adequate safeguards. Key improvements include new capability thresholds to indicate when we will upgrade our safeguards, refined processes for evaluating model capabilities and the adequacy of our safeguards (inspired by safety case methodologies ), and new measures for internal governance and external input. By learning from our implementation experiences and drawing on risk management practices used in other high-consequence industries, we aim to better prepare for the rapid pace of AI advancement.
## The promise and challenge of advanced AI
As frontier AI models advance, they have the potential to bring about transformative benefits for our society and economy. AI could accelerate scientific discoveries, revolutionize healthcare, enhance our education system, and create entirely new domains for human creativity and innovation. However, frontier AI systems also present new challenges and risks that warrant careful study and effective safeguards.
In September 2023, we released our Responsible Scaling Policy, a framework for managing risks from increasingly capable AI systems. After a year of implementation and learning, we are now sharing a significantly updated version that reflects practical insights and accounts for advancing technological capabilities.
Although this policy focuses on catastrophic risks like the categories listed below, they are not the only risks that we monitor and prepare for. Our Usage Policy sets forth our standards for the use of our products, including rules that prohibit using our models to spread misinformation, incite violence or hateful behavior, or engage in fraudulent or abusive practices. We continually refine our technical measures for enforcing our trust and safety standards at scale. Further, we conduct research to understand the broader societal impacts of our models. Our Responsible Scaling Policy complements our work in these areas, contributing to our understanding of current and potential risks.
## A framework for proportional safeguards
As before, we maintain our core commitment: we will not train or deploy models unless we have implemented safety and security measures that keep risks below acceptable levels. Our RSP is based on the principle of proportional protection: safeguards that scale with potential risks. To do this, we use AI Safety Level Standards (ASL Standards) , graduated sets of safety and security measures that become more stringent as model capabilities increase. Inspired by Biosafety Levels, these begin at ASL-1 for models that have very basic capabilities (for example, chess-playing bots) and progress through ASL-2, ASL-3, and so on.
In our updated policy, we have refined our methodology for assessing specific capabilities (and their associated risks) and implementing proportional safety and security measures. Our updated framework has two key components:
Capability Thresholds: Specific AI abilities that, if reached, would require stronger safeguards than our current baseline.
Required Safeguards: The specific ASL Standards needed to mitigate risks once a Capability Threshold has been reached.
At present, all of our models operate under ASL-2 Standards, which reflect current industry best practices. Our updated policy defines two key Capability Thresholds that would require upgraded safeguards:
Autonomous AI Research and Development: If a model can independently conduct complex AI research tasks typically requiring human expertise—potentially significantly accelerating AI development in an unpredictable way—we require elevated security standards (potentially ASL-4 or higher standards) and additional safety assurances to avoid a situation where development outpaces our ability to address emerging risks.
Chemical, Biological, Radiological, and Nuclear (CBRN) weapons: If a model can meaningfully assist someone with a basic technical background in creating or deploying CBRN weapons, we require enhanced security and deployment safeguards (ASL-3 standards).
ASL-3 safeguards involve enhanced security measures and deployment controls. On the security side, this will include internal access controls and more robust protection of model weights. For deployment risks, we plan to implement a multi-layered approach to prevent misuse, including real-time and asynchronous monitoring, rapid response protocols, and thorough pre-deployment red teaming.
## Implementation and oversight
To contribute to effective implementation of the policy, we have established:
Capability assessments : Routine model evaluations based on our Capability Thresholds to determine whether our current safeguards are still appropriate. (Summaries of past assessments are available here .)
Safeguard assessments: Routine evaluation of the effectiveness of our security and deployment safety measures to assess whether we have met the Required Safeguards bar. (Summaries of these decisions will be available here .)
Documentation and decision-making: Processes for documenting the capability and safeguard assessments, inspired by procedures (such as safety case methodologies ) common in high-reliability industries.
Measures for internal governance and external input: Our assessment methodology will be backed up by internal stress-testing in addition to our existing internal reporting process for safety issues. We are also soliciting external expert feedback on our methodologies. 1
## Learning from experience
We have learned a lot in our first year with the previous RSP in effect, and are using this update as an opportunity to reflect on what has worked well and what makes sense to update in the policy. As part of this, we conducted our first review of how well we adhered to the framework and identified a small number of instances where we fell short of meeting the full letter of its requirements. These included procedural issues such as completing a set of evaluations three days later than scheduled or a lack of clarity on how and where we should note any changes to our placeholder evaluations. We also flagged some evaluations where we may have been able to elicit slightly better model performance through implementing standard techniques (such as chain-of-thought or best-of-N).
In all cases, we found these instances posed minimal risk to the safety of our models. We used the additional three days to refine and improve our evaluations; the different set of evaluations we used provided a more accurate assessment than the placeholder evaluations; and our evaluation methodology still showed we were sufficiently far from the thresholds. From this, we learned two valuable lessons to incorporate into our updated framework: we needed to incorporate more flexibility into our policies, and we needed to improve our process for tracking compliance with the RSP. You can read more here .
Since we first released the RSP a year ago, our goal has been to offer an example of a framework that others might draw inspiration from when crafting their own AI risk governance policies. We hope that proactively sharing our experiences implementing our own policy will help other companies in implementing their own risk management frameworks and contribute to the establishment of best practices across the AI ecosystem.
## Looking ahead
The frontier of AI is advancing rapidly, making it challenging to anticipate what safety measures will be appropriate for future systems. All aspects of our safety program will continue to evolve: our policies, evaluation methodology, safeguards, and our research into potential risks and mitigations.
Additionally, Co-Founder and Chief Science Officer Jared Kaplan will serve as Anthropic’s Responsible Scaling Officer, succeeding Co-Founder and Chief Technology Officer Sam McCandlish who held this role over the last year. Sam oversaw the RSP’s initial implementation and will continue to focus on his duties as Chief Technology Officer. As we work to scale up our efforts on implementing the RSP, we’re also opening a position for a Head of Responsible Scaling. This role will be responsible for coordinating the many teams needed to iterate on and successfully comply with the RSP.
If you would like to contribute to AI risk management at Anthropic, we are hiring ! Many of our teams now contribute to risk management via the RSP, including:
Frontier Red Team (responsible for threat modeling and capability assessments)
Trust & Safety (responsible for developing deployment safeguards)
Security and Compliance (responsible for security safeguards and risk management)
Alignment Science (including sub-teams responsible for developing ASL-3+ safety measures, for misalignment-focused capability evaluations, and for our internal alignment stress-testing program)
RSP Team (responsible for policy drafting, assurance, and cross-company execution)
Read the updated policy at anthropic.com/rsp , and supplementary information at anthropic.com/rsp-updates .
We extend our sincere gratitude to the many external groups that provided invaluable feedback on the development and refinement of our Responsible Scaling Policy.
## Footnotes
1 We have also shared our assessment methodology with both AI Safety Institutes, as well as a selection of independent experts and organizations, for feedback. This does not represent an endorsement from either AI Safety Institute or the independent experts and organizations.
##
```

## Redline
None offered by the provider for v1.0 to v2.0 (checked: RSP page version list, which offers redlines only from v2.2).
