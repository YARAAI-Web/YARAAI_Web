rule auto_rule_20250727025001_9443 {
  strings:
    $o0 = "dword_4698B8" wide ascii nocase
    $o1 = "_tmpfname" wide ascii nocase
    $o2 = "Dumping" wide ascii nocase
  condition:
    3 of ($o*)
}