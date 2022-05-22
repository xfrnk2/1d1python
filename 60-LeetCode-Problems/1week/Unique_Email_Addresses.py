from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d: dict = dict()

        for email in emails:

            email_id, email_site = email.split("@")
            cleared_id = ""

            for c in email_id:

                if c == ".":
                    continue

                if c == "+":
                    break

                cleared_id += c

            res = cleared_id + "@" + email_site

            d[res] = d.get(res, 0) + 1
        ans = len(d.keys())
        return ans
