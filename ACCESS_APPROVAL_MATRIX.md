# Access Approval Matrix

Date: 2026-05-16  
Purpose: Show who can approve access based on access sensitivity.

| Access Type | Example | Manager Approval | System Owner Approval | Compliance Approval | Notes |
|---|---|---|---|---|---|
| Standard Role Access | Help Desk standard tools | Required | Not required | Not required | Default role-based access |
| Elevated Functional Access | Team lead reporting tools | Required | Required | Not required | Review least-privilege fit |
| Privileged Admin Access | Local admin, tenant admin | Required | Required | Required | Time-box where possible |
| Temporary Project Access | 30-day cross-team access | Required | Required | Optional | Must include end date |
| Contractor Access | Limited app access | Required | Required | Optional | Must match contract scope |
| Exception Access | Non-standard sensitive access | Required | Required | Required | Must include written justification |

## Matrix Rules

- No privileged access without documented business reason.
- Temporary access must include start and end dates.
- Exception access should be reviewed on a fixed schedule (ex: every 30 days).
