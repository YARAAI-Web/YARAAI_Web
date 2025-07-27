rule auto_rule_20250726184552_0079 {
  strings:
    $o0 = "dword_1001E8D8" wide ascii nocase
    $o1 = "QBFxiTVxcRxD1TL4MVq2iyZrf5vZ9TWvBAJiiCJfVBca1Ty8MVGiiyO" wide ascii nocase
    $o2 = "dword_1001E998" wide ascii nocase
    $o3 = "QAFw3WRy0WBtfjaU5UKz2xPB41GkNxGXRRpF4S3kfRBR0BzmRUavNwLjiKC" wide ascii nocase
  condition:
    4 of ($o*)
}