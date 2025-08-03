# QA Test Report: Random Date Generator (CodeBeautify.org)

## 🧪 Overview

This repository contains a QA test evaluation of the [Random Date Generator](https://codebeautify.org/generate-random-date) hosted on CodeBeautify.org.  
The purpose of this assessment is to evaluate the behavior, reliability, and usability of the date generation feature under various input conditions.

This evaluation was conducted as part of a QA/Testing challenge and includes:
- Manual test cases
- Bug reports
- UI/UX observations
- Suggestions for improvement

---

## ✅ Scope of Testing

Only the **Random Date Generator** tool at [https://codebeautify.org/generate-random-date](https://codebeautify.org/generate-random-date) is in scope.  
Other site tools are out of scope.

---

## 🧾 Deliverables

| File              | Description                                                              |
|-------------------|---------------------------------------------------------------------------|
| `test-report.md`  | Contains 10+ test cases with steps, expected vs actual results           |
| `bug-report.md`   | Documents at least one verified defect or enhancement suggestion         |
| `README.md`       | This summary and usage documentation                                      |

---

## 🧪 Testing Types Performed

- ✅ Functional Testing  
- ✅ Boundary & Edge Case Testing  
- ✅ Input Validation (Positive/Negative)  
- ✅ Format & Range Testing  
- ✅ UX Review (Copy/download behavior)  
- ✅ Responsive Layout (Chrome/Desktop + Mobile)  
- ⚠️ Performance (basic — 1000 dates tested)

---

## 🧪 Sample Test Case (from `test-report.md`)

| Test Case ID | Description                                |
|--------------|--------------------------------------------|
| **TC03**     | **Input Validation — Zero or Negative Count** |
| **Steps**: Input `0` or `-10` in "How many dates to generate?" and click `Generate Random Date` |
| **Expected Result**: Tool should either block the input or show a validation error |
| **Actual Result**: It attempts to generate dates (no error shown) |
| **Status**: ❌ Failed — No input validation |
| **Severity**: Medium |
| **Bug ID**: `BUG-001` in `bug-report.md` |

---

## 🐞 Bug Summary

- ❌ **No validation for invalid date count inputs** (`0`, `-1`, `abc`)
- ❌ **No alert or message on malformed date format input**
- ❌ **Allowing same Start and End date shows unexpected formatting sometimes**
- ❌ **No clipboard confirmation when copying**
- ✅ Download button works as expected (CSV)

> See `bug-report.md` for details

---

## 💡 Suggestions for Improvement

- Add input validation (min = 1) for count field
- Add confirmation tooltip/toast after clicking "Copy"
- Auto-adjust end date to always be after start date
- Add export options: JSON, XML
- Improve accessibility (tab index, screen reader support)

---

## 📎 How to Use This Repo

If you're reviewing this repo as part of a QA assessment:

```bash
📂 random-date-generator-qa/
├── README.md
├── test-report.md
└── bug-report.md
