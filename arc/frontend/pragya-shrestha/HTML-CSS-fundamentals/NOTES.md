## How to Open Links in a New Tab Safely

| Attributes         | What it Does                                       | Why it's Good          |
| ------------------ | -------------------------------------------------- | ---------------------- |
| `target="_blank"`  | Opens the link in a **new tab**                    | Let's people multitask |
| `rel="noopener"`   | Stops new tab from **messing** with your tab       | Keeps you safe         |
| `rel="noreferrer"` | Stops new tab from knowing **where you came from** | Keeps you private      |

```html
<a
  href="https://github.com/pragya-02"
  target="_blank"
  rel="noopener noreferrer"
>
  <img src="github.png" alt="github" />
</a>
```
