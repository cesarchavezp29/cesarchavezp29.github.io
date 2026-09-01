# CV and resume sources

LaTeX sources for the three PDFs served from `static/`:

| source | output | served as |
| --- | --- | --- |
| `cv.tex` | `cv.pdf` | `/cv.pdf` (3 pages) |
| `resume.tex` | `resume.pdf` | `/resume.pdf` (1 page) |
| `resume_policy.tex` | `resume_policy.pdf` | `/resume-policy.pdf` (1 page) |

These are the real sources: the text extracted from the PDFs they produce matches the
shipped PDFs exactly. They previously lived only in `D:\Investigacion\_cvbuild`, outside
version control, which made them a single point of failure. That directory is still the
working build folder; this copy is the versioned one.

## Rebuilding

```
pdflatex -interaction=nonstopmode cv.tex
pdflatex -interaction=nonstopmode cv.tex      # twice, for the page refs
```

Then copy the PDF into `static/`, renaming `resume_policy.pdf` to `resume-policy.pdf`
(the served filename uses a hyphen, the LaTeX file an underscore).

## Before committing a rebuild

- Check the page count did not change (cv 3, resume 1, resume_policy 1). A longer entry
  can silently push content onto a new page.
- Check the status wording still matches `content/cv.md` and the paper front matter.
  These PDFs are not generated from site data, so nothing keeps them in sync
  automatically — that is the failure mode to watch for.
