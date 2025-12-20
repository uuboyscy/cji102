# Tibame CJI102 Notes

## Lecture Notes
- [Tibame 20251109 pyetl morning](docs/Tibame_20251109_pyetl_morning.md)
- [Tibame 20251109 pyetl afternoon](docs/Tibame_20251109_pyetl_afternoon.md)
- [Tibame 20251130 pyetl](docs/Tibame_20251130_pyetl.md)
- [Tibame 20251206 pyetl morning](docs/Tibame_20251206_pyetl_morning.md)
- [Tibame 20251206 pyetl afternoon](docs/Tibame_20251206_pyetl_afternoon.md)
- [Tibame 20251220 flask](https://notebooklm.google.com/notebook/40b108db-7d31-4aa1-9d65-7b80feeeff75)

## Quick Notes (YYYY/MM/DD)
### note_20251109.md
#### selector
```
. -> class
# -> id
```
- example
  ```
  <div class="r-list-container action-bar-margin bbs-screen">
    -> div.r-list-container.action-bar-margin.bbs-screen
  ```

#### Web crawler steps
1. Open `developer tools -> Network` to see what HTTP method to use
2. See payload to see what data to be attached
   - Query string parameters
   - form data
3. Switch to `Element` to locate HTML structure
4. Coding
