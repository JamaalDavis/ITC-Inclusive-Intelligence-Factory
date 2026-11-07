"""Deterministic checks for a non-production editorial workflow."""
from dataclasses import dataclass

REQUIRED = {"task_id", "topic", "audience", "deliverable", "approval_required"}
DELIVERABLES = {"article", "carousel", "research_brief"}


def validate_task(task):
    if not isinstance(task, dict):
        raise ValueError("task must be an object")
    missing = REQUIRED - task.keys()
    if missing:
        raise ValueError("missing task fields: " + ", ".join(sorted(missing)))
    for key in ("task_id", "topic", "audience"):
        if not isinstance(task[key], str) or not task[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    if task["deliverable"] not in DELIVERABLES:
        raise ValueError("unsupported deliverable")
    if task["approval_required"] is not True:
        raise ValueError("human approval is required")
    if "permissions" in task and (not isinstance(task["permissions"], list) or any(not isinstance(p, str) for p in task["permissions"])):
        raise ValueError("permissions must be a list of strings")
    for key in ("source_urls", "accessibility_requirements"):
        if key in task and (not isinstance(task[key], list) or any(not isinstance(s, str) for s in task[key])):
            raise ValueError(f"{key} must be a list of strings")
    return True


def select_context(task):
    validate_task(task)
    # Explicit allowlist; do not include arbitrary task fields, chat histories or private profile.
    return {key:task[key] for key in ("task_id", "topic", "audience", "deliverable", "accessibility_requirements", "source_urls") if key in task}


def evaluate(draft):
    findings = []
    if not draft.get("claims"):
        findings.append("No claim inventory to verify")
    for claim in draft.get("claims", []):
        if not claim.get("source_url") or claim.get("verification") != "human_verified":
            findings.append(f"Unverified claim: {claim.get('text', '<untitled>')}")
    for visual in draft.get("visuals", []):
        if not visual.get("decorative") and not visual.get("alt_text", "").strip():
            findings.append(f"Missing alt text: {visual.get('id', '<unnamed>')}")
    if not draft.get("human_review_complete"):
        findings.append("Human review incomplete")
    return {"passed": not findings, "findings": findings}


def can_publish(report, approval):
    # Illustrative check, not an identity/authorization system.
    return (report.get("passed") is True and
            isinstance(approval, dict) and
            approval.get("approved") is True and
            bool(approval.get("reviewer_id")) and
            bool(approval.get("reviewed_at")))
