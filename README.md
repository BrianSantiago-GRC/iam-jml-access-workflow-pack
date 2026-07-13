# IAM Joiner-Mover-Leaver Workflow Pack

**A sample identity-lifecycle workflow connecting support tickets, approvals, least privilege, and offboarding evidence.**

## Problem, Action, Result

**Problem:** New hires, role changes, and departures create security and productivity risk when requests, approvals, access changes, and validation are not documented consistently.

**Action:** I designed joiner, mover, and leaver steps, an access-request template, a role/sensitivity approval matrix, an offboarding checklist, and risk notes.

**Result:** The pack provides one reviewable handoff from business request through access fulfillment or removal. It is sample process design, not proof of enterprise IAM architecture or automated provisioning ownership.

## 90-Second Review

1. Follow [`JML_WORKFLOW.md`](JML_WORKFLOW.md).
2. Review the [`access request`](ACCESS_REQUEST_FORM_TEMPLATE.md) and [`approval matrix`](ACCESS_APPROVAL_MATRIX.md).
3. Inspect the [`offboarding checklist`](OFFBOARDING_CHECKLIST.md).
4. Read [`RISK_NOTES.md`](RISK_NOTES.md) for failure modes and controls.

## Support-to-Security Connection

| Support task | Security evidence created |
|---|---|
| Create or change an account | Approved request, role, systems, and effective date |
| Add group or application access | Business owner and sensitivity-based approval |
| Process a role change | Removal of old access before or with new access |
| Offboard a user | Disablement, session/token action, asset return, and completion validation |

## Scope Boundary

The workflow and screenshots are generated portfolio artifacts. They do not come from a live ticketing, HR, Entra, or IAM platform and do not claim enterprise identity-governance ownership.
