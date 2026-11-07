"""Demonstrate validation, context minimization and explicit publication blocking."""
import json
from pathlib import Path
from .core import validate_task, select_context, evaluate, can_publish


def main():
    root = Path(__file__).resolve().parents[2]
    task = json.loads((root / 'examples' / 'task.json').read_text(encoding='utf8'))
    validate_task(task)
    context = select_context(task)
    draft = {
        'title': 'Who gets to appeal an algorithm?',
        'claims': [{'text':'An automated decision always has an accessible appeal route', 'source_url':None, 'verification':'unverified'}],
        'visuals': [{'id':'journey-map', 'decorative':False, 'alt_text':''}],
        'human_review_complete':False
    }
    report = evaluate(draft)
    result = {'task_context':context, 'evaluation':report, 'can_publish':can_publish(report, approval=None), 'notice':'Demo fixture only: no LLM call or source verification performed.'}
    out=root/'workflows'/'output'/'demo-report.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result,indent=2))
    print(f'Report saved: {out}')

if __name__ == '__main__':
    main()
