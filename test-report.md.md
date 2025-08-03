# 🧪 Test Report: Random Date Generator (CodeBeautify)

## 🌐 Test Target

- **URL**: https://codebeautify.org/generate-random-date
- **Tool**: Random Date Generator
- **Tested On**: Chrome (v115+), Windows 10, Mobile Emulator (Galaxy S9)

---

## ✅ Summary

| Total Test Cases | Passed | Failed | Notes |
|------------------|--------|--------|-------|
| 10               | 7      | 3      | See bug report |

---

## 🔍 Test Cases

### TC01 – Basic Date Generation

- **Input**: Count = `10`
- **Expected**: 10 valid dates generated
- **Actual**: ✅ As expected

---

### TC02 – Valid Custom Format: `YYYY-MM-DD`

- **Input**: Format = `YYYY-MM-DD`
- **Expected**: All dates appear in correct format
- **Actual**: ✅ As expected

---

### TC03 – Invalid Input (Count = `0`)

- **Input**: Count = `0`
- **Expected**: Show validation error or block
- **Actual**: ❌ Dates still attempted to generate (nothing happens)
- **Bug ID**: `BUG-001`

---

### TC04 – Negative Input (Count = `-10`)

- **Input**: Count = `-10`
- **Expected**: Show error
- **Actual**: ❌ UI accepts and tries to generate
- **Bug ID**: `BUG-002`

---

### TC05 – Same Start and End Date

- **Input**: Start = `2025-08-03`, End = `2025-08-03`
- **Expected**: All generated dates = `2025-08-03`
- **Actual**: ✅ As expected

---

### TC06 – Copy to Clipboard

- **Action**: Click copy icon after generating dates
- **Expected**: Dates copied + success feedback
- **Actual**: ✅ Copies, ❌ but no feedback shown

---

### TC07 – File Download

- **Action**: Click download button
- **Expected**: CSV file downloaded with correct dates
- **Actual**: ✅ Works fine, correct format

---

### TC08 – Custom Format: Malformed Input (`abc123`)

- **Input**: Format = `abc123`
- **Expected**: Validation error or ignore
- **Actual**: ❌ Accepts input, output format breaks
- **Bug ID**: `BUG-003`

---

### TC09 – High Load (1000 Dates)

- **Input**: Count = `1000`
- **Expected**: No crash, all dates valid
- **Actual**: ✅ Takes ~2–3 seconds, all valid

---

### TC10 – Mobile Responsiveness

- **Device**: Galaxy S9 emulator
- **Expected**: Responsive layout, no cutoffs
- **Actual**: ✅ Fully responsive

