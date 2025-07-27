rule auto_rule_20250726152302_3575 {
  strings:
    $o0 = "dword_6403145C" wide ascii nocase
  condition:
    all of them
}