rule auto_rule_20250727021716_2525 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "_abstract_cw" wide ascii nocase
    $o2 = "dword_4570DC" wide ascii nocase
  condition:
    3 of ($o*)
}