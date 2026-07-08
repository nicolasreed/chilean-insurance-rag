# Development Journal

One entry per work session. Newest first. Append-only.

## 11-07-2026 / M0
- **Done:** repo created, uv environment configured (Python 3.12), GitHub Models PAT set up, smoke test working end-to-end against the API.
- **Broke / learned:** first time using the OpenAI SDK, hit a few small issues along the way (e.g. forgot to quote the env var name in `os.environ[GITHUB_MODELS_TOKEN]`, causing a `NameError`). Nothing broke the milestone, but it's clear I'm still learning the SDK's basics.
- **Open:** go deeper into the OpenAI SDK before building on it in M1: how calls are structured, what else the client supports, understanding the library beyond just the code that already works.
- **Next:** start M1, select the manifest norms and build the downloader.