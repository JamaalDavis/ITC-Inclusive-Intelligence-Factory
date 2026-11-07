import unittest
from itc_factory.core import validate_task, select_context, evaluate, can_publish

TASK = {'task_id':'1','topic':'access','audience':'designers','deliverable':'article','approval_required':True,'permissions':['draft']}

class FactoryTests(unittest.TestCase):
    def test_valid_task(self):
        self.assertTrue(validate_task(TASK))
    def test_approval_cannot_be_disabled(self):
        with self.assertRaises(ValueError):
            validate_task({**TASK,'approval_required':False})
    def test_context_excludes_private_extraneous_data(self):
        ctx=select_context({**TASK,'private_person_data':'secret'})
        self.assertNotIn('private_person_data',ctx)
        self.assertNotIn('permissions',ctx)
    def test_unverified_claim_blocks(self):
        result=evaluate({'claims':[{'text':'X','source_url':'https://example.com','verification':'unverified'}], 'human_review_complete':True})
        self.assertFalse(result['passed'])
    def test_missing_alt_blocks(self):
        result=evaluate({'claims':[{'text':'X','source_url':'https://example.com','verification':'human_verified'}], 'visuals':[{'id':'x'}], 'human_review_complete':True})
        self.assertFalse(result['passed'])
    def test_human_approval_required(self):
        report={'passed':True}
        self.assertFalse(can_publish(report,None))
        self.assertFalse(can_publish(report,{'approved':True}))
        self.assertTrue(can_publish(report,{'approved':True,'reviewer_id':'r1','reviewed_at':'2026-11-07T12:00:00Z'}))
    def test_review_failure_blocks(self):
        self.assertFalse(can_publish({'passed':False},{'approved':True,'reviewer_id':'r1','reviewed_at':'2026-11-07'}))

if __name__=='__main__':unittest.main()
