rule auto_rule_20250727021400_5233 {
  strings:
    $o0 = "directive" wide ascii nocase
    $o1 = "dword_4C1310" wide ascii nocase
    $o2 = "dword_4C12CC" wide ascii nocase
  condition:
    3 of ($o*)
}