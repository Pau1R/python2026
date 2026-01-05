You are given a single input: a markdown "results" file.

Your job is to return the same markdown file, but with ONLY the following changes.

1) For EACH question block, find the exact placeholder line:
   ## ИИ анализ ![spinner](https://github.githubassets.com/images/spinners/octocat-spinner-32.gif)
   Replace it with an analysis of that question.
   Requirements:
   - Replace that single placeholder line with:
     ## ИИ анализ
     followed immediately by your analysis text on the next lines.
   - Keep the analysis short and specific to the question and the student's answer.

2) If the results file contains at least one question that requires a free-form text answer (not multiple-choice), then locate the line:
   Результат теста:
   and insert exactly one new line immediately below it:
   Обновленный результат: 90/100%

Restrictions:
- Do NOT change any other text, formatting, headings, whitespace, ordering, or scores.
- Do NOT add new sections.
- Only perform the two transformations above.