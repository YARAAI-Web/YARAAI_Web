rule auto_rule_20250726174432_5122 {
  strings:
    $o0 = "dword_4C1630" wide ascii nocase
    $o1 = "dword_4C20D8" wide ascii nocase
    $o2 = "dword_4C1684" wide ascii nocase
  condition:
    3 of ($o*)
}