#!/bin/bash
# Apply branch protection to main. Run once after the repository is public
# (GitHub Free allows branch protection only on public repositories).
# Needs: gh with the repo scope.
set -euo pipefail
R=scsnake/taipei-2026-guide
gh api -X PUT repos/$R/branches/main/protection --input - <<'JSON'
{"required_status_checks":{"strict":false,"checks":[{"context":"check"}]},
 "enforce_admins":true,
 "required_pull_request_reviews":{"required_approving_review_count":0,"dismiss_stale_reviews":false,"require_code_owner_reviews":false},
 "restrictions":null,"allow_force_pushes":false,"allow_deletions":false,
 "required_linear_history":false,"required_conversation_resolution":false}
JSON
gh api -X POST repos/$R/branches/main/protection/required_signatures >/dev/null
gh api repos/$R/branches/main/protection --jq '{pull_requests:(.required_pull_request_reviews!=null), signed:.required_signatures.enabled, force_push:.allow_force_pushes.enabled, delete:.allow_deletions.enabled, checks:[.required_status_checks.checks[].context], admins_too:.enforce_admins.enabled}'
