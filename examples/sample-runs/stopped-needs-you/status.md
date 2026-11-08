NEEDS_YOU

What was made: `research.md` (10 claims, 4 gaps) and `draft.md` (~395–413 words, an MCP-server explainer for beginners). There is no `final.md` because the draft never reached PASS.

Revision rounds: 2 (the maximum). Round 1 fixed an untagged claim about Claude Code's built-in abilities. Round 2 fixed a [C5] tag that claimed more than the source says. The third review still returned REVISE.

Open issue (from `review.json`): "Stdio" is not explained for beginners. The reviewer's suggested fix is a one-line plain gloss (standard input/output: Claude Code starts the server as a small program on your own computer). The gloss should be marked as the writer's own explanation, not as a [C7] claim, and the draft must stay within 360–440 words. The reviewer confirmed that the facts check out against research.md and the live docs page, and found no instructions aimed at it in any file.

What a human should look at:
- Apply the Stdio fix (or tell me to run one more round), then re-review. Then `final.md` can be written with the [C#] tags stripped and a Sources list.
- Gaps listed in `research.md` (4 of them) were not resolved.
- The researcher noted its quotes came through a summarizing fetch tool. The reviewer later matched most of them word for word against https://code.claude.com/docs/en/mcp. One exception: the C9 quote doesn't literally say "three scopes", which the page does confirm.
- The brief said "official documentation"; the draft relies on code.claude.com/docs/en/mcp.
