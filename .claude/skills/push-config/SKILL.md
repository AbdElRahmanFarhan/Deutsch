---
name: push-config
description: Copy settings from config/<area>.toml into the Deutsch dashboard, replacing that area's live values. Use when the learner types /push-config or says they edited a config file.
---

# Push a settings file to the dashboard

1. Areas: the arguments (e.g. `/push-config schedule tutor`), or every `config/*.toml` changed in
   `git diff` if none are given. Show the learner which areas will be replaced and wait for a yes:
   this overwrites what they set in the dashboard for those areas.
2. `python3 scripts/build_seed.py <areas...>` writes `build/seed/config__<area>.json`.
3. Read each `config/<area>` document to get its `version`, then one `ArtifactData` `batch` of `set`
   writes with `file_path` and `if_version`.
4. Commit the TOML change. Say which areas were updated.
