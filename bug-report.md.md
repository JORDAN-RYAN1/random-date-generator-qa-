# 🐞 Bug Report – Random Date Generator (CodeBeautify)

---

## ❌ BUG-001 – No Validation for Count = `0`

- **Severity**: Medium
- **Steps**:
  1. Input `0` in "How many dates to generate?"
  2. Click "Generate Random Date"
- **Expected**: Show error message or block input
- **Actual**: No validation; nothing happens
- **Recommendation**: Add minimum value validation (min = 1)

---

## ❌ BUG-002 – Negative Count Allowed

- **Severity**: Medium
- **Steps**:
  1. Enter `-10` as count
  2. Click "Generate"
- **Expected**: Block input or show error
- **Actual**: Attempts to process, no result
- **Recommendation**: Add input constraints for count > 0

---

## ❌ BUG-003 – Malformed Format Accepted

- **Severity**: Low
- **Steps**:
  1. Input `abc123` in the custom format field
  2. Generate dates
- **Expected**: Format should be rejected
- **Actual**: Output malformed or blank
- **Recommendation**: Add format parser or show error

---

## ❗ Feature Suggestions

### ✅ SUGGESTION-001 – Add Copy Confirmation Tooltip

- **Issue**: Clicking “Copy” has no feedback
- **Fix**: Show toast/snackbar: `Copied to clipboard!`

---

### ✅ SUGGESTION-002 – Enforce Format Validation

- **Issue**: Any string is accepted as format
- **Fix**: Whitelist valid placeholders like `YYYY`, `MM`, `DD`

---

### ✅ SUGGESTION-003 – Accessibility Improvements

- Add `aria-label`s for buttons
- Make tool keyboard-friendly (tab index order)
- High contrast mode toggle for visually impaired users

