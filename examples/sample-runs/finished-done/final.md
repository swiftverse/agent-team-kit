Claude Code can only hold so much at once. That space is the context window: everything Claude knows about your session (one ongoing conversation), including your instructions, the files it reads, and its own replies.

When the window nears its limit, Claude Code compacts automatically, so a full window doesn't end your session. Compacting means swapping the long conversation for a structured summary. Exactly when this happens depends on your model (the Claude AI version you use) and setup.

The catch: the summary keeps your requests and key code snippets (short pieces of code), but detailed instructions from early on may be lost. Put rules you always need in CLAUDE.md, a file of standing instructions for your project, in your project's top folder. That file is reloaded from your computer's saved files afterward. You can also type the command /compact yourself and choose what the summary keeps.

## Sources
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/how-claude-code-works.md
