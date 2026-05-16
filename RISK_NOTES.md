# Risk Notes - IAM JML Workflow

Date: 2026-05-16  
Purpose: Document common identity lifecycle risks and practical controls.

## Key Risks

1. **Stale access after role change**  
   Old role permissions remain active and exceed current job needs.

2. **Delayed offboarding disablement**  
   Accounts stay active after separation and increase unauthorized access risk.

3. **Over-permissioned joiner setup**  
   New users receive broad access instead of role-based minimum access.

4. **Missing approval trail**  
   Access changes happen without clear manager/system-owner approval records.

5. **Temporary access not removed**  
   Project-based elevated access remains after the temporary period ends.

## Practical Controls

- Use role-based default access for joiners.
- Require manager + system-owner approval for elevated access.
- Time-box temporary/exception access with expiration dates.
- Run periodic access recertification for sensitive roles.
- Use an offboarding checklist with evidence-required closure.

## Control Mapping (Simple Reference)

- NIST CSF PR.AC-1: Identity and credential management
- NIST CSF PR.AC-4: Access permissions are managed
- HIPAA 164.308(a)(3): Workforce security
- HIPAA 164.308(a)(4): Information access management

## Positioning Note

This is a junior-level practical workflow pack for portfolio demonstration.
