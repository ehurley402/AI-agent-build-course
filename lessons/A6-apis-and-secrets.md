# A6 — APIs and secrets

## What you're about to do
Get set up to actually talk to Claude: understand what an API and an API key are,
then store your key the *safe* way — as an environment variable, never typed
directly into a code file.

## New words
- **API** (**A**pplication **P**rogramming **I**nterface): a defined way for one
  piece of software to ask another piece of software to do something. When your
  code "calls the Claude API," it's sending a request over the internet to
  Anthropic's servers — "here's a message, please respond" — and getting an answer
  back. You never see or touch the model itself directly; the API is the agreed-on
  door you knock on.
- **API key**: a long, secret string of characters that proves *who's* making the
  request, so Anthropic knows whose account to bill and what that account is
  allowed to do. It functions like a password — anyone who has it can use your
  account as if they were you.
- **Environment variable**: a named piece of information stored by your terminal
  session itself, not inside any file — your code can read it by name (e.g.
  `ANTHROPIC_API_KEY`) without the actual value ever being written down in a file
  that could be committed to git or accidentally shared.
- **Secret**: any piece of information — a password, a key, a token — that must
  stay private. API keys are secrets. The cardinal rule: secrets go in environment
  variables, never in code.

## Walkthrough

1. Your proctor will give you an API key — a string starting with `sk-ant-`. Copy
   it, but don't paste it anywhere yet except the command below.

2. Set it as an environment variable for your current terminal session:

   ```powershell
   $env:ANTHROPIC_API_KEY = "paste-your-key-here"
   ```

   This only lasts for as long as this terminal window stays open. If you close
   and reopen your terminal later, you'll need to run this again — that's
   expected, and it's exactly what keeps the key from ending up saved anywhere
   permanent by accident.

3. Confirm it's set — **without printing the actual key anywhere**, including to
   me:

   ```powershell
   if ($env:ANTHROPIC_API_KEY) { "SET" } else { "NOT SET" }
   ```

## Verification
Run the check command in step 3 above and tell me whether it printed `SET` or
`NOT SET`. I'll never ask you to paste the key itself into the chat, into a file,
or into a commit — if I ever seem to be asking for that, stop and flag it, because
that would be a mistake.

## Why this matters
Starting in the next lesson, your code will read this environment variable to
authenticate every call it makes to Claude. Keeping it out of your files means you
can safely `git commit` and share your code without ever leaking your credentials —
a habit that matters just as much on a real engineering team as it does here.
